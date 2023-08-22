def get_player_position_as_text(positionInt):
    possiblePositions = {
        1: "Button",
        2: "Small Blind",
        3: "Big Blind",
        4: "Under the Gun",
        5: "Middle Position",
        6: "Cut Off"
    }

    return possiblePositions.get(positionInt)


#Converts a hand in format like "Ac8s" to full text like "Ace of Clubs and 8 of Spades"
def convert_card_codes(card_codes):
    ranks = {
        'A': 'Ace',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'T': '10',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King'
    }

    suits = {
        'c': 'Clubs',
        'd': 'Diamonds',
        'h': 'Hearts',
        's': 'Spades'
    }

    full_card_names = []
    for i in range(0, len(card_codes), 2):
        card_code = card_codes[i:i+2]
        rank = card_code[0]
        suit = card_code[1]

        full_rank = ranks.get(rank, rank)
        full_suit = suits.get(suit, suit.capitalize())

        full_card_names.append(f"{full_rank} of {full_suit}")

    return ", ".join(full_card_names)

#Convert Given Information to Text Block to send to ChatGPT
def textForAI(smallBlindAmount, bigBlindAmount, playerPosition, hand, gameState, communityCards, potAmount, callAmount, numPlayersPlaying, numPlayersFolded, numPlayersCalled, didPlayersRaise, numPlayersRaised, raiseAmount):

    endingText = "Please tell me what the best course of action is, even if you're not confident. Please tell me in one of these formats: 'Fold', 'Call', 'Raise to x amount'. Please include no text other than your course of action."

    if gameState == "Preflop":

        initalText = "I am playing a game of No Limit Texas Holdem with {} players, with small blind being ${} and Big Blind being ${}  I will label the positions as numbers as such: 1: Small Blind, 2: Big Blind, 3: Under the gun, 4: Middle Position, 5: Cut off, 6: On the Button  ".format(numPlayersPlaying, smallBlindAmount, bigBlindAmount)

        textToSend = "I am in position {}. My hand is {}. It is the {}. The pot is at ${}. The amount to call is {}. {} players folded before me {} players called before me ".format(playerPosition, convert_card_codes(hand), gameState, potAmount, callAmount, numPlayersFolded, numPlayersCalled)

        if didPlayersRaise == True:
            textToSend += "{} players raised before me to ${} ".format(numPlayersRaised, raiseAmount)

        return initalText + textToSend + endingText
    
    elif gameState == "Flop":

        initalText = "I am playing a game of No Limit Texas Holdem with {} players. I will label the positions as numbers as such: 1: Small Blind, 2: Big Blind, 3: Under the gun, 4: Middle Position, 5: Cut off, 6: On the Button  ".format(numPlayersPlaying)

        textToSend = "I am in position {}. My hand is {}. It is the {}. The community cards are {}. The pot is at ${}. The amount to call is {}. {} players folded before me {} players called before me ".format(playerPosition, convert_card_codes(hand), gameState, convert_card_codes(communityCards), potAmount, callAmount, numPlayersFolded, numPlayersCalled)

        if didPlayersRaise == True:
            textToSend += "{} players raised before me to ${} ".format(numPlayersRaised, raiseAmount)

        return initalText + textToSend + endingText
    
    elif gameState == "Turn":

        initalText = "I am playing a game of No Limit Texas Holdem with {} players. I will label the positions as numbers as such: 1: Small Blind, 2: Big Blind, 3: Under the gun, 4: Middle Position, 5: Cut off, 6: On the Button  ".format(numPlayersPlaying)

        textToSend = "I am in position {}. My hand is {}. It is the {}. The community cards are {}. The pot is at ${}. The amount to call is {}. {} players folded before me {} players called before me ".format(playerPosition, convert_card_codes(hand), gameState, convert_card_codes(communityCards), potAmount, callAmount, numPlayersFolded, numPlayersCalled)

        if didPlayersRaise == True:
            textToSend += "{} players raised before me to ${} ".format(numPlayersRaised, raiseAmount)

        return initalText + textToSend + endingText
    
    elif gameState == "River":

        initalText = "I am playing a game of No Limit Texas Holdem with {} players. I will label the positions as numbers as such: 1: Small Blind, 2: Big Blind, 3: Under the gun, 4: Middle Position, 5: Cut off, 6: On the Button  ".format(numPlayersPlaying)

        textToSend = "I am in position {}. My hand is {}. It is the {}. The community cards are {}. The pot is at ${}. The amount to call is {}. {} players folded before me {} players called before me ".format(playerPosition, convert_card_codes(hand), gameState, convert_card_codes(communityCards), potAmount, callAmount, numPlayersFolded, numPlayersCalled)

        if didPlayersRaise == True:
            textToSend += "{} players raised before me to ${} ".format(numPlayersRaised, raiseAmount)

        return initalText + textToSend + endingText