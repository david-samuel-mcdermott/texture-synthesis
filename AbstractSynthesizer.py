from abc import ABC


class AbstractSynthesizer(ABC):
	
	@abstractmethod
	def __init__(self, textonNeighborhoodDiameter):
	"""
	This is the abstract class constructor
	
	Args:
		textonNeighborhoodDiameter: This is the diameter for the texton neighborhood in pixels
	"""
		self.textonNeighborhoodDiameter = textonNeighborhoodDiameter
	
	@abstractmethod
	def generateTexture(self, inputData, outputSize):
	"""
	This is the main method for the synthesizer
	
	Args:
		inputData: An array-like-object of two dimensions with a single value for greyscale or a tuple for RGB/RGBA data
		outputSize: A tuple dictating the size of the output image in (X, Y)
		
	Returns:
		An array-like-object of two dimensions in the same colorspace as the input data and the dimensions of the specified size
	"""
		return None
		
	