Tic_Tac_Toe_List = [[None, None, None], [None, None, None], [None, None, None]]
##Printing the board
def print_board(tttl):
    #pass
    i = 0
    for item in tttl[0]:
        
        if item == None:
            print(" ", end = '')
        else:
            print(item, end = '')
        if i != 2:
            print("|", end = '')
        else:
            print()
        i+=1
    print("-+-+-")
    i = 0
    for item in tttl[1]:
        
        if item == None:
            print(" ", end = '')
        else:
            print(item, end = '')
        if i != 2:
            print("|", end = '')
        else:
            print()
        i+=1
    print("-+-+-")
    i = 0
    for item in tttl[2]:
        
        if item == None:
            print(" ", end = '')
        else:
            print(item, end = '')
        if i != 2:
            print("|", end = '')
        else:
            print()
        i+=1

##Setting up the game!
P1Won = False
P2Won = False
full = False
turn = -1 #turn number
playerOneCharacter = input("What would you like your tic tac toe character to be? If nothing is typed, it will be X.\n")
if playerOneCharacter == '':
    playerOneCharacter = "X"
else:
    playerOneCharacter = playerOneCharacter[0]
playerTwoCharacter = playerOneCharacter
while playerTwoCharacter == playerOneCharacter:
    playerTwoCharacter = input("What would you like your tic tac toe character to be? If nothing is typed, it will be O.\n")
    if playerTwoCharacter == '':
        playerTwoCharacter = "O"
    else:
        
        playerTwoCharacter = playerTwoCharacter[0]
        


#Starting the game!
while True:
    turn +=1
    #end!
    if full or P1Won or P2Won:
        if full:
            status_code = "_full_"
        elif P1Won:
            status_code = "P1_won"
        else:
            status_code = "P2_won"
        break
    print("""Game Board:


""")
    print_board(Tic_Tac_Toe_List)
    print("\n" * 5)
    print(Tic_Tac_Toe_List)
    if turn%2 == 0:
        ##Player One goes!
        valid = False
        while not valid:
            P1Place = input("""Where would you, Player One, like to go? Type in row number and then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    """)
            P1Place_parse = P1Place.split()
            if len(P1Place_parse) != 2:
                # must be of length 2
                P1Place = input("""Invalid! Type in a row number then column number, seperated by a space.For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)
    """)
                continue
            else:
                if P1Place_parse[0] not in ["0", "1", "2"] and P1Place_parse[1] not in ["0", "1", "2"]:
                    #o#
                    P1Place = input("""Invalid row number and column number! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)""")
                    continue
                elif P1Place_parse[0] not in ["0", "1", "2"] and P1Place_parse[1] in ["0", "1", "2"]:
                    P1Place = input("""Invalid row number! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)""")
                    continue
                elif P1Place_parse[0] in ["0", "1", "2"] and P1Place_parse[1] not in ["0", "1", "2"]:
                    P1Place = input("""Invalid column number! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)""")
                else:
                    # I need to check if the space is already occupied!
                    if Tic_Tac_Toe_List[int(P1Place_parse[0])][int(P1Place_parse[1])] != None:
                        P1Place = input("""Oh noes! The space you are trying to mark is already occupied! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)
    """)
                    else:
                        Tic_Tac_Toe_List[int(P1Place_parse[0])][int(P1Place_parse[1])] = playerOneCharacter
                        break

    
            
    else:
        ##Player Two goes!
        valid = False
        while not valid:
            P2Place = input("""Where would you, Player Two, like to go? Type in row number and then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    """)
            P2Place_parse = P2Place.split()
            print(P2Place_parse)
            if len(P2Place_parse) != 2:
                # must be of length 2
                P2Place = input("""Invalid! Type in a row number then column number, seperated by a space.For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)
    """)
                
            else:
                if P2Place_parse[0] not in ["0", "1", "2"] and P2Place_parse[1] not in ["0", "1", "2"]:
                    #o#
                    P2Place = input("""Invalid row number and column number! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 1 BTW)""")
                    
                elif P2Place_parse[0] not in ["0", "1", "2"]:
                    P2Place = input("""Invalid row number! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 2 BTW)""")
                    
                elif P2Place_parse[1] not in ["0", "1", "2"]:
                    P2Place = input("""Invalid column number! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 2 BTW)""")
                else:
                    # I need to check if the space is already occupied!
                    if Tic_Tac_Toe_List[int(P2Place_parse[0])][int(P2Place_parse[1])] != None:
                        P2Place = input("""Oh noes! The space you are trying to mark is already occupied! Type in a row number then column number, seperated by a space.
    For example, 0 1 would be
     |H| 
    -+-+-
     | |
    -+-+-
     | |
    (where H is the place you would like to go)
    (You are Player 2 BTW)
    
    """)
                    else:
                        Tic_Tac_Toe_List[int(P2Place_parse[0])][int(P2Place_parse[1])] = playerTwoCharacter
                        break
                      
    ##now win condition time
    ##full?
    TTTL = Tic_Tac_Toe_List
    f0 = 0
    f1 = 0
    f2 = 0
    #full detection at the end
    
    
    ##win detection
    ##first we do P1
    
    P1C = playerOneCharacter
    P2C = playerTwoCharacter

    for x in range(3):
        if TTTL[x][0] == P1C and TTTL[x][1] == P1C and TTTL[x][2] == P1C:
            #top row
            P1Won = True
            break
    for x in range(3):
        if TTTL[0][x] == P1C and TTTL[1][x] == P1C and TTTL[2][x] == P1C:
            #top row
            P1Won = True
            break
    if TTTL[0][0] == P1C and TTTL[1][1] == P1C and TTTL[2][2] == P1C:
        #top-left to bottom right diagonal
        P1Won= True
    elif TTTL[2][0] == P1C and TTTL[1][1] == P1C and TTTL[0][2] == P1C:
        #other diagonal
        P1Won = True
    else:
        #Player One didn't win!

        for x in range(3):
            if TTTL[x][0] == P2C and TTTL[x][1] == P2C and TTTL[x][2] == P2C:
                #top row
                P2Won = True
        for x in range(3):
            if TTTL[0][x] == P2C and TTTL[1][x] == P2C and TTTL[2][x] == P2C:
                #top row
                P2Won = True
                break
        if TTTL[0][0] == P2C and TTTL[1][1] == P2C and TTTL[2][2] == P2C:
            #top-left to bottom right diagonal
            P2Won= True
        elif TTTL[2][0] == P1C and TTTL[1][1] == P1C and TTTL[0][2] == P1C:
            #other diagonal
            P2Won = True
        else:
            for item in Tic_Tac_Toe_List[0]:
                if item != None:
                    f0 += 1
            for item in Tic_Tac_Toe_List[1]:
                if item != None:
                    f1 += 1
            for item in Tic_Tac_Toe_List[2]:
                if item != None:
                    f2 += 1
            if f0 == 3 and f1 == 3 and f2 == 3:
                full = True
            if full:
                continue
            if not (full or P1Won or P2Won):
                print("Neither player has won, and the board isn't full yet. Let's keep going!")




##GAME_OVER!

print("Game over! :D :D :D")
##if full or P1Won or P2Won:
##        if full:
##            status_code = "_full_"
##        elif P1Won:
##            status_code = "P1_won"
##        else:
##            status_code = "P2_won"
##        break
if status_code == "_full_":
    print("The board is full! It was a tie. Final position:")
    
elif status_code == "P1_won":
    print("Good job to Player One! Player one has won! Final position:")
else:
    print("Good Job to Player Two! Player Two has won! Final position:")
print_board(TTTL)

#oh my gosh this is more than 10,000 characters






        

