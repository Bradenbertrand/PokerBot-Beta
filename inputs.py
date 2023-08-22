from text import textForAI

#These functions allow the user to input information for each betting round.
#It then uses the textForAI function to return the paragraph that is to be sent to ChatGPT.
#There is probably 1000 different and better ways to do this. I am not a programmer. I am silly little boy.


#preFlop specific information
def preFlop(smallBlindAmount, bigBlindAmount, hand, playerPosition, numPlayers):
    didPlayersRaise = False
    numPlayersRaised = 0
    callAmount = bigBlindAmount
    potAmount = input("Please enter the pot value: ")
    numPlayersFolded = input("Please enter how many players have folded: ")
    numPlayersCalled = input("Please enter how many players have called: ")
    if input("Did anyone raise? Enter y/n: ") == "y":
        didPlayersRaise = True
        numPlayersRaised = input("How many players raised?: ")
        raiseAmount = input("What did the last player raise it to?: ")
        callAmount = raiseAmount
    else:
        raiseAmount = 0
    return textForAI(smallBlindAmount, bigBlindAmount, playerPosition, hand, "Preflop", "", potAmount, callAmount, numPlayers, numPlayersFolded, numPlayersCalled, didPlayersRaise, numPlayersRaised, raiseAmount)

#Flop specific information
def Flop(hand, playerPosition, communityCards, numPlayers):
    didPlayersRaise = False
    numPlayersRaised = 0
    callAmount = input("Please enter the amount to call: ")
    potAmount = input("Please enter the pot value: ")
    numPlayersFolded = input("Please enter how many players have folded: ")
    numPlayersCalled = input("Please enter how many players have called: ")
    if input("Did anyone raise? Enter y/n: ") == "y":
        didPlayersRaise = True
        numPlayersRaised = input("How many players raised?: ")
        raiseAmount = input("What did the last player raise it to?: ")
        callAmount = raiseAmount
    else:
        raiseAmount = 0
    
    return textForAI("", "", playerPosition, hand, "Flop", communityCards, potAmount, callAmount, numPlayers, numPlayersFolded, numPlayersCalled, didPlayersRaise, numPlayersRaised, raiseAmount)

#Turn specific information
def Turn(hand, playerPosition, communityCards, numPlayers):
    didPlayersRaise = False
    numPlayersRaised = 0
    callAmount = input("Please enter the amount to call: ")
    potAmount = input("Please enter the pot value: ")
    numPlayersFolded = input("Please enter how many players have folded: ")
    numPlayersCalled = input("Please enter how many players have called: ")
    if input("Did anyone raise? Enter y/n: ") == "y":
        didPlayersRaise = True
        numPlayersRaised = input("How many players raised?: ")
        raiseAmount = input("What did the last player raise it to?: ")
        callAmount = raiseAmount
    else:
        raiseAmount = 0
    
    return textForAI("", "", playerPosition, hand, "Turn", communityCards, potAmount, callAmount, numPlayers, numPlayersFolded, numPlayersCalled, didPlayersRaise, numPlayersRaised, raiseAmount)

#River specific information
def River(hand, playerPosition, communityCards, numPlayers):
    didPlayersRaise = False
    numPlayersRaised = 0
    callAmount = input("Please enter the amount to call: ")
    potAmount = input("Please enter the pot value: ")
    numPlayersFolded = input("Please enter how many players have folded: ")
    numPlayersCalled = input("Please enter how many players have you called: ")
    if input("Did anyone raise? Enter y/n: ") == "y":
        didPlayersRaise = True
        numPlayersRaised = input("How many players raised?: ")
        raiseAmount = input("What did the last player raise it to?: ")
        callAmount = raiseAmount
    else:
        raiseAmount = 0
    
    return textForAI("", "", playerPosition, hand, "River", communityCards, potAmount, callAmount, numPlayers
    , numPlayersFolded, numPlayersCalled, didPlayersRaise, numPlayersRaised, raiseAmount)
