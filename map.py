import numpy as np

class Map:
    def __init__(self, width=10, height=10):
        self._width = width
        self._height = height
        
        # USING NUMPY TO MAKE ARRAY FOR MAP
        self.grid = np.arange(100)
        self.grid.shape = (self.width,self.height)


    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height


    # CODE NOT USED YET
    # def isonmap(self, pwidth, pheight):
    #     if pwidth >= 0 and pwidth < self.width and pheight >= 0 and pheight < self.height:
    #         return True
    #     return False


