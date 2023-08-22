import sys
from inputs import Flop, preFlop, Turn, River
from text import textForAI, get_player_position_as_text
from chatgpt import get_chatgpt_response

#This is the main looping function for the game.
def play_game():

    print("**********************************************")
    print("**** Welcome to Burny's ChatGPT Poker Bot ****")
    print("**********************************************")
    print("Please enter pre-game information")
    print("---------------------------------")


    #Takes user inputs of information that does not change between rounds
    selectGameState = int(input("Please select a game state to start in.\n1: Pre-Flop\n2: Flop\n3: Turn\n4: River\n"))
    smallBlindAmount = float(input("Please input the small blind amount: "))
    bigBlindAmount = float(input("Please input the small blind amount: "))
    numPlayers = int(input("Enter how many players are at your table: "))
    playerPosition = int(input("Please enter player position: \n 1: BTN \n 2: SB \n 3: BB \n 4: UTG \n 5: MP \n 6: CO \n"))
    communityCards = ""
    handNeeded = True
    isRebetRound = False

    #Goes through each stage of betting and asks for information for each round.
    while True:
        
        if handNeeded == True:
            hand = input("Please enter your hand, Ex. 'Ac4d'\n")
            handNeeded = False

        if selectGameState == 1:
            print("Pre-Flop Starting...")
            print("Player Position: " + get_player_position_as_text(playerPosition))
            print("*********************************\n")
            preFlopString = preFlop(smallBlindAmount, bigBlindAmount, hand, playerPosition, numPlayers)
            print("*********************************")
            get_chatgpt_response(preFlopString)
        elif selectGameState == 2:
            print("\nFlop Starting...")
            print("*********************************")
            if isRebetRound == False:
                communityCards += input("Please enter the 3 community cards: ")
            flopString = Flop(hand, playerPosition, communityCards, numPlayers)
            print("*********************************")
            get_chatgpt_response(flopString)
        elif selectGameState == 3:
            print("Turn Starting...")
            print("*********************************")
            if isRebetRound == False:
                communityCards += input("Please enter the 1 new community card: ")
            turnString = Turn(hand, playerPosition, communityCards, numPlayers)
            print("*********************************")
            get_chatgpt_response(turnString)
        elif selectGameState == 4:
            print("River Starting...")
            print("*********************************")
            if isRebetRound == False:
                communityCards += input("Please enter the 1 new community card: ")
            riverString = River(hand, playerPosition, communityCards, numPlayers)
            print("*********************************")
            get_chatgpt_response(riverString)


        if input("did you fold? y/n: ") == "y":
            selectGameState = 5
            handNeeded = True

        if input("Is round over? y/n: ") == "y":
            selectGameState += 1
        else:
            isRebetRound = True



        if selectGameState > 4:
            finished = input("Would you like to play another round? y/n: ")
            if finished == "y":
                handNeeded = True
                selectGameState = 1
                playerPosition -= 1
                if playerPosition == 0:
                    playerPosition = numPlayers
            else:
                print("Thanks for playing!")
                sys.exit()



play_game()
    