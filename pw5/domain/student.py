import numpy as np
import math

class Student:
    #array = []
    def __init__(self, ID, Name, Dob):
        self.IDs = ID
        self.names = Name
        self.dob = Dob
        self.mark = []
    
    def get_ids(self):
        return self.IDs

    def get_names(self):
        return self.names

    def get_dob(self):
        return self.dob

    def set_id(self, Id):
        self.IDs = Id
    
    def set_name(self, Name):
        self.names = Name

    def set_dob(self, Dob):
        self.dob = Dob
    
    def get_mark(self, courID, Mark): 
        tpm_cour = {"ID": courID, "Mark": Mark}
        self.mark.append(tpm_cour)
        print(self.mark)

    def show_cour_mark(self, courID):
        for i in range(self.mark.__len__()):
            print(self.mark[i])
