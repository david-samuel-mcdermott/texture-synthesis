import typing
from typing import List, Union, Tuple

class Pixel:
    
    def __init__(self, a:float = 0.0, r: float = 0.0, g: float = 0.0, b: float = 0.0, filled: bool = False):
        """
        Create an ARGB pixel with default of fully transparent black and marked as not filled
        Alpha is used as greyscale value for getGreyscale
        """
        self.a = float(a)
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
        self.filled = bool(filled)
        
    def setFilled(self,filled: bool = True):
        self.filled = filled
        
    def isFilled(self) -> bool:
        return self.filled
    
    def setR(self, r: float):
        self.r = r
       
    def setG(self, g: float):
        self.g = g
        
    def setB(self, b: float):
        self.b = b
        
    def setA(self, a: float):
        self.a = a
        
    def cp(self, pixel):
        self.a = pixel.a
        self.r = pixel.r
        self.g = pixel.g
        self.b = pixel.b
        self.filled = True
    
    def getRGBA(self) -> Tuple[float, float, float, float]:
        return (self.r, self.g, self.b, self.a)
    
    def getRGB(self) -> Tuple[float, float, float]:
        return (self.r, self.g, self.b)
    
    def getGreyscale(self) -> float:
        return self.a
        
    