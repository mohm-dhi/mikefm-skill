import numpy as np
from shapely.geometry import Point
from mikeio import Dfs0

class PointObservation:
    
    name = None
    filename = None
    dfs = None
    x = None
    y = None
    z = None
    item_number = None
    
    def __init__(self, filename, x, y, z=None, item=0, name=None):
        self.filename = filename
        self.dfs = Dfs0(filename)
        self.x = x
        self.y = y
        self.z = z

        if name is None:
            name = filename
        self.name = name

    def __repr__(self):
        out = f"PointObservation: {self.name}"
        return out

    @property
    def geo(self) -> Point:
        if self.z is None:
            return Point(self.x, self.y)
        else:
            return Point(self.x, self.y, self.z)
        
