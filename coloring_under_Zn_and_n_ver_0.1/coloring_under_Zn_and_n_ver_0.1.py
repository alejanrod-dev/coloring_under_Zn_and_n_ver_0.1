#coloring under Z_n and [n] . ver 0.1
#Alejandro Rodriguez, Isreal Wilbur, Alexis Gonzales
#9/12

import Coloring

#############
# main loop #
#############
while True:

    #prompt user
    print("are we in Z_n or [n]?")
    print("1) for Z_n")
    print("2) for [n]")

    choice = int(input("choice: "))


    #######
    # Z_n #
    #######
    if(choice == 1):
        print("Z_n")

        print("Input your custom coloring; ex 123 will repeat 123123123...")
        custom_coloring = input("coloring:")

        #turn string into a list
        custom_coloring_list = []

        #this list takes string "123" -> [1,2,3]
        for x in range(len(custom_coloring)):
            custom_coloring_list.append(int(custom_coloring[x]))

        #prints [1,2,3]
        #print("Coloring = ",custom_coloring_list)

        #now we can initizlize our class with (boolean, [1,2,3], 28)
        #example

        #strucure is already True = Z_n
        x = Coloring.Coloring(True,custom_coloring_list,6)
        x.print_coloring()

    #######
    # [n] #
    #######
    elif (choice == 2):
        print("[n]")

        print("Input your custom coloring; ex 123 will repeat 123123123...")
        custom_coloring = input("coloring:")

        #turn string into a list
        custom_coloring_list = []

        #this list takes string "123" -> [1,2,3]
        for x in range(len(custom_coloring)):
            custom_coloring_list.append(int(custom_coloring[x]))

        #prints [1,2,3]
        #print("Coloring = ",custom_coloring_list)

        #now we can initizlize our class with (boolean, [1,2,3], 28)
        #example

        #strucure is already False = Z_n
        x = Coloring.Coloring(False,custom_coloring_list,6)
        x.print_coloring()

    #######
    # END #
    #######
    else:
        break




