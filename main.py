#!/usr/bin/env python3
import collections
import re
import sys

#Check for Anaconda before proceeding; this guarantees packages not to be missing
if 'conda' not in sys.version:
	print("Anaconda is recommended to use dependencies; please make sure that numpy, matplotlib, and Pillow are available")

#import nonstandard packages
import matplotlib.image as mpimage
import matplotlib.pyplot as plt
import numpy as np

#import custom classes
from algorithms import AbstractSynthesizer
from algorithms import EfrosLeungSynthesizer

algorithms = collections.defaultdict(lambda: EfrosLeungSynthesizer.EfrosLeungSynthesizer(3))
#TODO: algorithms add


#look for help in arguments
if "-h" in sys.argv or "--help" in sys.argv:
	print("Usage: <input texture file name> <texton neighborhood diameter> <output size>")
	print("Optional Postfix Flag: -method=<texture synthesis algorithm>")
	print("Available algorithms:")
	print("Default:", algorithms[""].getDescription())
	for key, value in algorithms.items():
		print(key, ':', value.getDescription())
	sys.exit()

#If wrong number of arguments, you need help
if len(sys.argv) < 3:
	print("Usage: <input texture file name> <texton neighborhood diameter> <output size>")
	sys.exit()
	
#Parse commandline arguments
inputFileName = sys.argv[1]
textonNeighborhoodDiameter = sys.argv[2]
outputSize = sys.argv [3]

algorithms = collections.defaultdict(lambda: EfrosLeungSynthesizer.EfrosLeungSynthesizer(textonNeighborhoodDiameter))
#TODO: algorithms add

	
#Can I run the synthesis?
quitFlag = False

#Check for malformed command line arguments
#Try load image, if FNF or invlid format, alert
try: 
	imageData = mpimage.imread(inputFileName)
	if imageData is None:
		raise ValueError("Failed to load image data")
except:
	print("Input File Name (arg #1) must be a valid image file name")
	#If your image doesn't load, you may need Pillow to handle format
	try:
		from PIL import Image
	except:
		print("Pillow not available, install pillow for non PNG images")
	quitFlat = True

#Try parse input as number
try:
	textonNeighborhoodDiameter = int(textonNeighborhoodDiameter)
	if textonNeighborhoodDiameter % 2 == 0:
		raise ValueError("Texton Neighborhood Diameter must be odd")
except:
	print("Texton Neighboorhood Diameter (arg #2) must be an odd integer")
	quitFlag = True

#Try parse input as x,y size	
try:
	outputSize = (int(outputSize), int(outputSzie))
except:
	match = re.match(r"(\d+)[xX](\d+)", outputSize)
	if match:
		x = int(match.group(1))
		y = int(match.group(2))
		outputSize = (x, y)
	else:
		print("Output Size (arg #3) must be an integer or a string matched by r\"\\d+[xX}\\d+\"")
		quitFlag = True
	
#If we fail to handle conditions, then bail out
if quitFlag:
	print("Provided Arguments", "inputFileName", inputFileName, "texton", textonNeighborhoodDiameter, "outputSize", outputSize)
	sys.exit()


if len(sys.argv) == 5:
	algorithmName = re.match(r"match=(\w+)", sys.argv[3]).group(1)
else:
	algorithmName = ""
	
if algorithmName not in algorithms and algorithmName != "":
	print("Given algorithm not found, using default algorithm")
	
algorithm = algorithms[algorithmName]
#Validate that the algorithm is a valid synthesizer
if not isinstance(algorithm, AbstractSynthesizer.AbstractSynthesizer):
	print("Something has gone horribly wrong with the algorithm selection, aborting")
	sys.exit()
	
#Generate the new texture
print("Generating imamge")
newImage = algorithm.generateTexture(imageData, outputSize)

ext = inputFileName.split('.')[-1]
#Special case for no file extension
if ext == inputFileName:
	ext = ""
	
#Save the image
print("Saving generated image to", "output"+ext)
plt.imsave("output"+ext, newImage)
print("Done!")