from abc import ABC, ABCMeta, abstractmethod
import typing
from typing import List, Union, Tuple
import numpy as np

class AbstractSynthesizer(ABC):
	"""
	The abstract synthesizer defines the interface for texture synthesis implementations
	"""
	
	@abstractmethod
	def __init__(self, textonNeighborhoodDiameter : int):
		"""
		This is the abstract class constructor
		
		Args:
			textonNeighborhoodDiameter: This is the diameter for the texton neighborhood in pixels
		"""
		self.textonNeighborhoodDiameter = textonNeighborhoodDiameter
	
	@abstractmethod
	def generateTexture(self, inputData: Union[List, np.ndarray] , outputSize: Tuple[int, int]) -> Union[List, np.ndarray]:
		"""
		This is the main method for the synthesizer
		
		Args:
			inputData: An array-like-object of two dimensions with a single value for greyscale or a tuple for RGB/RGBA data
			outputSize: A tuple dictating the size of the output image in (X, Y)
			
		Returns:
			An array-like-object of two dimensions in the same colorspace as the input data and the dimensions of the specified size
		"""
		return None
		
	@abstractmethod
	def getDescription(self) -> str:
		"""
		This method gives the description for the texture synthesis algorithm
		
		Returns:
			A string describing the algorithm and its assumptions
		"""
		return "Abstract Base Class for Texture Synthesis"