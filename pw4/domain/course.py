import numpy as np
import math

class Courses: 
    def __init__(self, Id, Name):
        self.id = Id
        self.name = Name
            
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def set_id(self,Id):
        self.id = Id

    def set_name(self,Name):
        self.name = Name
