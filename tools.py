#Convert action index to text
def action_int_to_text(actionInt):
    actions = {
        1: "fold",
        2: "call",
        3: "raise"
    }
    return actions.get(actionInt)

#Converts cards to full text. Ex: "Ac4d" to "Ace of Clubs, 4 of Diamonds"
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

    return full_card_names

