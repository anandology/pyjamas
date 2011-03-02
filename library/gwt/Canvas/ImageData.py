# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:56:31 2010

@author: Alexander Tsepkov
"""

"""
This class wraps around ImageData HTML5 Canvas object and allows easier 
per-pixel access
"""
class ImageData:
    def __init__(self, imagedata):
        self.width = imagedata.width
        self.height = imagedata.height
        self.data = imagedata.data
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getPixel(self, x, y):
        offset = (y*self.width + x)*4
        return self.data[offset:offset+4]
    
    """
    rgba must be an array of 4 integers ranging from 0 to 255
    """
    def setPixel(self, x, y, rgba):
        offset = (y*self.width + x)*4
        self.data[offset:offset+4] = rgba