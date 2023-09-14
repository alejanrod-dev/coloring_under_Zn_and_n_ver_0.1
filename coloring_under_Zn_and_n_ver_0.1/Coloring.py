#coloring class .ver 0.1
#Alejandro Rodriguez, Isreal Wilbur, Alexis Gonzales
#9/12

import math

class Coloring():

    #####################
    # general functions #
    #####################

    # Initializie function
    def __init__(self, structure, col_list, size) -> None:

        #true/1 = Z_n
        #false/0 = [n]
        self.structure = structure

        #example input [1,2,3]
        self.custom_coloring = col_list

        #empty
        self.colored_list = []

        #size that we want our colored_list to be
        self.n = size

        #if user wants a Z_n structure
        if self.structure == 1:

            #build Z_n list as normal
            for x in range(0,self.n):
                for i in range(len(self.custom_coloring)):
                    if x % len(self.custom_coloring) == i:
                        self.colored_list.append(self.custom_coloring[i])
                        continue

        # user wants a [n] strucure
        else:

            #build [n] list by adding zero to the front of the list [0,coloring...]
            self.colored_list.append(0)
            for x in range(0,self.n):
                for i in range(len(self.custom_coloring)):
                    if x % len(self.custom_coloring) == i:
                        self.colored_list.append(self.custom_coloring[i])
                        continue

    #prints out the colored list
    def print_coloring(self):

        #if Z_n
        if self.structure == 1:
            print("Z_",self.n,"=",self.colored_list)

        #else [n]
        else:
            print("[", self.n,"]","=",self.colored_list[1:])


    pass
