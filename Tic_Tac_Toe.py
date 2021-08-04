# To clear the window
from os import system  
# Method to explain the game to make the user understand how to play it.
def explanation():
# Make the general table of the game with numbers to make it easy for players's choices.
    for i in range(1,16):
        if i == 6 or i == 11:
            print("- - - - - - - - - - - - - - - - - - - - - - - -") 
            print("                |                |               ")
        elif i == 3:
            print("       1        |        2       |        3       ")
        elif i == 8:
            print("       4        |        5       |        6       ")
        elif i == 13:
            print("       7        |        8       |        9       ")
        else:
            print("                |                |               ")
    # The explanation :             
    print("Explanation:-\n  -Tic_Tac_Toe is a game aimes to collect 3 similar symbols in row (X_or_O).")
    print("  -Player1 always plays with symbol(X)_in Green and Player2 always plays with symbol(O)_in Yellow.")
    print("  -As you see, you can put your symbol according to the above numbers from 1 --> 9, As in phone dial.\n")
    print("NOTE : You can exit the game any time by pressing (Ctrl+C)_or_(Ctrl+Z, then Enter).")
    print("* Without further ado, let's play :)\n")
    input("Press any key to Continue!")
    system("cls")
########################################################################################################################
########################################################################################################################
# Method shows how the game works from players'choices to the results (wins, loses, tie game)
def the_game(): 
    # name of players :
    player_1 = input("Name of the Player_1 : ")      
    player_2 = input("Name of the Player_2 : ")  
    # make the first letter capital in both of them
    player_1 = player_1[0].upper() + player_1[1:]
    player_2 = player_2[0].upper() + player_2[1:]
    print()
    # in case of similar names we make the first --> (name)_1 and the second --> (name)_2
    if player_1 == player_2:
        player_1 = "(" + player_1 + ")" + "_1"
        player_2 = "(" + player_2 + ")" + "_2"
    # Greeting them and give each of them a symbol (X for player_1), (O for player_2)
    print("Welcome ",player_1,", You will play with (X).",sep="")   
    print("Welcome ",player_2,", You will play with (O).\n",sep="")   
    input("Press any key to Continue!")
    system("cls")
    # list of numbers that players can choose from it
    nums = ["1","2","3","4","5","6","7","8","9"]  
    # Colors to the text : Green(X), Red(O)
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
    green = Fore.GREEN  # for X
    c_x = green + "X"   # colored X with green 
    yellow = Fore.YELLOW       # for O
    c_o = yellow + "O"   # colored O with green
    # put the numbers of the list in the table to make a link between them 
    # and print the table to start the game 
    for i in range(1,16):
        if i == 6 or i == 11:
            print("- - - - - - - - - - - - - - - - - - - - - - - -") 
            print("                |                |               ")
        elif i == 3:
            print("      ",nums[0],"         |        ",nums[1],"       |        ",nums[2],"       ",sep="")
        elif i == 8:
            print("      ",nums[3],"         |        ",nums[4],"       |        ",nums[5],"       ",sep="")
        elif i == 13:
            print("      ",nums[6],"         |        ",nums[7],"       |        ",nums[8],"       ",sep="")
        else:
            print("                |                |               ") 
    print()
    #-------------------------------------------------------------------------------------------------------------
    print(player_1,"will play First!!\n") 
    # the summation of turns for both players is 9 (always player1 plays 5 times, always player2 plays 4 times)
    # So, it will be 5 iterations for player 1 and 4 iterations for player 2
    for x in range(1,6): 
        # The First player :              
        is_number = False
        while not is_number : # keep working if player_1 doesn't enter an integer number 
            # recive the input from the player_1
            num = input(player_1+"'s turn = ")  
            # check if player_1's input is an integer number 
            if num.isnumeric() == True:   # case of true input
                is_number_in_list = False
                while not is_number_in_list: # keep working if player_1 doesn't enter a number belongs to the list 
                    # check if player_1's input belongs to the given list of numbers 
                    if num in nums:   # case of true (number in the list) 
                        # we determine the index of the input in the list to replace it with (X)
                        # So, we can decrease the choices in the next turn
                        indx = nums.index(num)   
                        # The choices of player_1 as it put in the list, it also put in the table
                        # to make it easy to interact with the game
                        nums[indx] = c_x        
                        system("cls")
                        for i in range(1,16):
                            if i == 6 or i == 11:
                                print("- - - - - - - - - - - - - - - - - - - - - - - -") 
                                print("                |                |               ")
                            elif i == 3:
                                print("      ",nums[0],"         |        ",nums[1],"       |        ",nums[2],"       ",sep="")
                            elif i == 8:
                                print("      ",nums[3],"         |        ",nums[4],"       |        ",nums[5],"       ",sep="")
                            elif i == 13:
                                print("      ",nums[6],"         |        ",nums[7],"       |        ",nums[8],"       ",sep="")
                            else:
                                print("                |                |               ") 
                        # cases that player_1 wins and player_2 loses  
                        # wins ---> horizontally, vertically, crosses 
                        if (nums[0]==c_x and nums[1]==c_x and nums[2]==c_x) or (nums[3]==c_x and nums[4]==c_x and nums[5]==c_x) or (nums[6]==c_x and nums[7]==c_x and nums[8]==c_x) or (nums[0]==c_x and nums[3]==c_x and nums[6]==c_x) or (nums[1]==c_x and nums[4]==c_x and nums[7]==c_x) or (nums[2]==c_x and nums[5]==c_x and nums[8]==c_x) or (nums[0]==c_x and nums[4]==c_x and nums[8]==c_x) or (nums[2]==c_x and nums[4]==c_x and nums[6]==c_x):
                            print("Winner!!, Winner!!, Winner!!")
                            print(player_1,"win the game!")
                            print("Good jop, ",player_1," ___ Hard luck, ",player_2,"\n",sep="")
                            # play_again option 
                            expected_input = False
                            while not expected_input:   # keep working if the user enter unecpected input
                                check_y_or_n = input("Do you want to play agin?!\n(y for Yes) and (n for No)---> ")
                                check_y_or_n = check_y_or_n.lower()
                                if check_y_or_n == "n":     # if the choice is no ---> exit the game 
                                    exit()
                                elif check_y_or_n == "y":    # if the choice is yes ---> repeate the game
                                    system("cls")
                                    the_game() 
                                else:       # if the choice not yes or no re-check the input of the user
                                    system("cls")
                                    print("Please, Check your input (y for Yes) and (n for No)\n")
                                    expected_input = False
                        is_number_in_list = True   
                        is_number = True           
                    else:  # case of false (number is not in the list)--->(not from 1-->9) or (Choosen before)
                        print("Please, choose an appropriate number.")
                        print("It is maybe happen if you insert an chosen number or choose number not from 1 --> 9\n")
                        is_number_in_list = True        # no meaning in logic, but to make the code work :)
                        is_number = False               # no meaning in logic, but to make the code work :)
            else:
                print("Please, Enter an integer number!, like 1,2,3,....,9\n")   # case of false input 
                is_number = False
        # in case of tie game 
        # if the game still working until the last iteration this mean that no one win or lose 
        # So, it will be a tie game. 
        if x == 5:
            print("WOW!, No one lose :)\nGame is tie.\n")
            # play_again option 
            expected_input = False
            while not expected_input:   # keep working if the user enter unecpected input
                check_y_or_n = input("Do you want to play agin?!\n(y for Yes) and (n for No)---> ")
                check_y_or_n = check_y_or_n.lower()
                if check_y_or_n == "n":   # if the choice is no ---> exit the game 
                    exit()
                elif check_y_or_n == "y":   # if the choice is yes ---> repeate the game  
                    system("cls")
                    the_game() 
                else:     # if the choice not yes or no re-check the input of the user
                    system("cls")
                    print("Please, Check your input (y for Yes) and (n for No)\n")
                    expected_input = False
    #-------------------------------------------------------------------------------------------------------------
        # The Second player :
        # prevent the fifth iteration from the player_2
        if x == 5:
            break   
        else:
            is_number = False   
            while not is_number :     # keep working if player_2 doesn't enter an integer number
                # recive the input from the player_2
                num = input(player_2+"'s turn = ")   
                # check if player_2's input is an integer number 
                if num.isnumeric() == True:   # case of true input
                    is_number_in_list = False
                    while not is_number_in_list: # keep working if player_2 doesn't enter a number belongs to the list 
                        # check if player_2's input belongs to the given list of numbers 
                        if num in nums:   # case of true (number in the list) 
                            # we determine the index of the input in the list to replace it with (O)
                            # So, we can decrease the choices in the next turn
                            indx = nums.index(num)
                            # The choices of player_2 as it put in the list, it also put in the table
                            # to make it easy to interact with the game
                            nums[indx] = c_o  
                            system("cls")
                            for i in range(1,16):
                                if i == 6 or i == 11:
                                    print("- - - - - - - - - - - - - - - - - - - - - - - -") 
                                    print("                |                |               ")
                                elif i == 3:
                                    print("      ",nums[0],"         |        ",nums[1],"       |        ",nums[2],"       ",sep="")
                                elif i == 8:
                                    print("      ",nums[3],"         |        ",nums[4],"       |        ",nums[5],"       ",sep="")
                                elif i == 13:
                                    print("      ",nums[6],"         |        ",nums[7],"       |        ",nums[8],"       ",sep="")
                                else:
                                    print("                |                |               ")
                            # cases that player_2 wins and player_1 loses  
                            # wins ---> horizontally, vertically, crosses  
                            if (nums[0]==c_o and nums[1]==c_o and nums[2]==c_o) or (nums[3]==c_o and nums[4]==c_o and nums[5]==c_o) or (nums[6]==c_o and nums[7]==c_o and nums[8]==c_o) or (nums[0]==c_o and nums[3]==c_o and nums[6]==c_o) or (nums[1]==c_o and nums[4]==c_o and nums[7]==c_o) or (nums[2]==c_o and nums[5]==c_o and nums[8]==c_o) or (nums[0]==c_o and nums[4]==c_o and nums[8]==c_o) or (nums[2]==c_o and nums[4]==c_o and nums[6]==c_o):
                                print("Winner!!, Winner!!, Winner!!")
                                print(player_2,"win the game!")
                                print("Good jop, ",player_2," ___ Hard luck, ",player_1,"\n",sep="")
                                # play_again option 
                                expected_input = False
                                while not expected_input: # keep working if the user enter unecpected input 
                                    check_y_or_n = input("Do you want to play agin?!\n(y for Yes) and (n for No)---> ")
                                    check_y_or_n = check_y_or_n.lower()
                                    if check_y_or_n == "n":    # if the choice is no ---> exit the game
                                        exit()
                                    elif check_y_or_n == "y":    # if the choice is yes ---> repeate the game
                                        system("cls")
                                        the_game() 
                                    else:               # if the choice not yes or no re-check the input of the user
                                        system("cls")
                                        print("Please, Check your input (y for Yes) and (n for No)\n")
                                        expected_input = False
                            is_number_in_list = True   
                            is_number = True                        
                        else:  # case of false (number is not in the list)--->(not from 1-->9) or (Choosen before)
                            print("Please, choose an appropriate number.")
                            print("It is maybe happen if you insert an chosen number or choose number not from 1 --> 9\n")
                            is_number_in_list = True        # no meaning in logic, but to make the code work :)
                            is_number = False               # no meaning in logic, but to make the code work :)
                else:
                    print("Please, Enter an integer number!, like 1,2,3,....,9\n")   # case of false input 
                    is_number = False
########################################################################################################################
########################################################################################################################
# The executed code :    
try:                 
    print("Welcome in Tic_Tac_Toe Game!\n")
    choice = False 
    while not choice:   # keep working if the user make a wrong choice 
        direct_indirect_playing = input("Do you want to :-\n1:play Tic_Tac_toe Game directly\n2:see the explanation first\n\n(1 for first choice) and (2 for second choice)---> ")
        # in case of right choice
        if direct_indirect_playing == "1":  # in case of direct playing
            system("cls")
            the_game()
            choice = True
        elif direct_indirect_playing == "2": # in case of indirect playing
            system("cls")
            explanation()
            the_game() 
            choice = True
        # in case of wrong choice
        else:
            system("cls")
            print("Please, Check your input (1 for first choice) and (2 for second choice)\n")
            choice = False 
except:    
    print("Exiting!")    