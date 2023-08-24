import sys
from chatgpt import create_question
from table import PokerTable
from tools import action_int_to_text, convert_card_codes
from player import Player


#*********************************************************************************
#*********************************************************************************
#************************************ Burny's ************************************
#*********************************** Poker Bot ***********************************
#*********************************************************************************
#*********************************************************************************

action_input_choices = "Select an Action. 1: Fold 2: Call 3: Raise\n"

def playGame():
    #initial setup information
    small_blind = int(input("Please enter the small blind value: "))
    big_blind = int(input("Please enter the big blind value: "))
    buy_in = int(input("Please enter the buy-in amount: $"))
    num_players = int(input("Please enter the number of players playing: "))
    starting_pos = int(input("Please enter your starting position: "))
    print("*******************************************************")

    #Initialize Table
    table = PokerTable(small_blind, big_blind)

    #Creates a list of player obects
    playerList = list()
    x = 1
    while x < num_players + 1:
        if x == starting_pos:
            playerList.append(Player(buy_in, x, True, "", f"Hero"))
        else:
            playerList.append(Player(buy_in, x, False, "", f"Player {x}"))
        x += 1
    
    #Adds all players to the table
    for player in playerList:
        table.add_player(player)
    
    print("**********************************************************")
    #Action functions


    #PREFLOP ROUND
    #--------------------------------------------------------------------------
    table.set_round("pre-flop")
    #Set default call amount (BB)
    table.set_call_amount(big_blind)
    #Set default pot (SB + BB)
    table.add_to_pot(small_blind + big_blind)
    #Set round starting conditions
    is_round_over = False
    #Which positions starts this round
    starting_pos = 2
    #Force bets for small and big blind
    table.players[0].stack_size -= small_blind
    table.players[0].bet_amount += small_blind
    table.players[0].round_bet_amount += small_blind
    table.players[1].stack_size -= big_blind
    table.players[1].bet_amount += big_blind
    table.players[1].round_bet_amount += big_blind

    
    

    #Get Hero's hand
    hand = input("Please enter your hand: ")
    
    for player in table.players:
        if player.name == "Hero":
            player.give_hand(hand)

        #This loops until the round is over
        while is_round_over == False:

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status != "folded":
                    print(table.players[index].name + "'s Turn (" + table.players[index].position + ")")
                    print("Round Pot: " + str(table.round_pot))
                    print("Total Pot: " + str(table.pot))
                    print("Amount to call: $" + str(table.amount_needed_to_call(index)))
                    if table.players[index].name == "Hero":
                        print(create_question(table, index, table.players[index].hand))
                    if table.amount_needed_to_call(index) == 0:
                        action = int(input("Please select an action:\n1: Check\n2: Raise\n"))
                        if action == 1:
                            table.check(index)
                        elif action == 2:
                            amount_to_raise = int(input("Raise to: $"))
                            
                            table.raise_bet(index, amount_to_raise)
                    else:
                        action = int(input("Please select an action:\n1: Fold\n2: Call\n3: Raise\n"))
                        if action == 1:
                            table.fold(index)
                        elif action == 2:
                            table.call(index)
                        elif action == 3:
                            amount_to_raise = int(input("Raise to: $"))
                            table.raise_bet(index, amount_to_raise)
                        print(table.players[index].bet_amount)
                else:
                    print(table.players[index].position + " has folded")
            
            is_round_over = True

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status == "folded" or (table.players[index].round_bet_amount == table.call_amount):
                    pass
                else:
                    is_round_over = False
                    print(table.players[index].name + " has not called the same amount")

    print("**********************************************")        
    print(table)
    print("**********************************************")

    starting_pos = 0

    #FLOP ROUND
    #--------------------------------------------------------------------------
    table.set_round("flop")
    table.player_round_reset()
    table.table_round_reset()
    
    #Get the three community cards
    community_cards = input("Enter the three community cards: ")
    table.deal_community_cards(convert_card_codes(community_cards))

    is_round_over = False

    while is_round_over == False:

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status != "folded":
                    print(table.players[index].name + "'s Turn (" + table.players[index].position + ")")
                    print("Round Pot: " + str(table.round_pot))
                    print("Total Pot: " + str(table.pot))
                    print("Amount to call: $" + str(table.amount_needed_to_call(index)))
                    if table.amount_needed_to_call(index) == 0:
                        action = int(input("Please select an action:\n1: Check\n2: Raise\n"))
                        if action == 1:
                            table.check(index)
                        elif action == 2:
                            amount_to_raise = int(input("Raise to: $"))
                            
                            table.raise_bet(index, amount_to_raise)
                    else:
                        action = int(input("Please select an action:\n1: Fold\n2: Call\n3: Raise\n"))
                        if action == 1:
                            table.fold(index)
                        elif action == 2:
                            table.call(index)
                        elif action == 3:
                            amount_to_raise = int(input("Raise to: $"))
                            table.raise_bet(index, amount_to_raise)
                        print(table.players[index].bet_amount)
                else:
                    print(table.players[index].position + " has folded")
            
            is_round_over = True

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status == "folded" or (table.players[index].round_bet_amount == table.call_amount):
                    pass
                else:
                    is_round_over = False
                    print(table.players[index].name + " has not called the same amount")
    
    print("**********************************************")        
    print(table)
    print("**********************************************")

    starting_pos = 0

    #TURN ROUND
    #--------------------------------------------------------------------------
    table.set_round("turn")
    table.player_round_reset()
    table.table_round_reset()
    
    #Get the new community card
    community_cards = input("Enter the new community card: ")
    table.deal_community_cards(convert_card_codes(community_cards))

    is_round_over = False

    while is_round_over == False:

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status != "folded":
                    print(table.players[index].name + "'s Turn (" + table.players[index].position + ")")
                    print("Round Pot: " + str(table.round_pot))
                    print("Total Pot: " + str(table.pot))
                    print("Amount to call: $" + str(table.amount_needed_to_call(index)))
                    if table.amount_needed_to_call(index) == 0:
                        action = int(input("Please select an action:\n1: Check\n2: Raise\n"))
                        if action == 1:
                            table.check(index)
                        elif action == 2:
                            amount_to_raise = int(input("Raise to: $"))
                            
                            table.raise_bet(index, amount_to_raise)
                    else:
                        action = int(input("Please select an action:\n1: Fold\n2: Call\n3: Raise\n"))
                        if action == 1:
                            table.fold(index)
                        elif action == 2:
                            table.call(index)
                        elif action == 3:
                            amount_to_raise = int(input("Raise to: $"))
                            table.raise_bet(index, amount_to_raise)
                        print(table.players[index].bet_amount)
                else:
                    print(table.players[index].position + " has folded")
            
            is_round_over = True

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status == "folded" or (table.players[index].round_bet_amount == table.call_amount):
                    pass
                else:
                    is_round_over = False
                    print(table.players[index].name + " has not called the same amount")

    print("**********************************************")        
    print(table)
    print("**********************************************")

    starting_pos = 0

    #RIVER ROUND
    #--------------------------------------------------------------------------
    table.set_round("river")
    table.player_round_reset()
    table.table_round_reset()
    
    #Get the new community card
    community_cards = input("Enter the new community card: ")
    table.deal_community_cards(convert_card_codes(community_cards))

    is_round_over = False

    while is_round_over == False:

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status != "folded":
                    print(table.players[index].name + "'s Turn (" + table.players[index].position + ")")
                    print("Round Pot: " + str(table.round_pot))
                    print("Total Pot: " + str(table.pot))
                    print("Amount to call: $" + str(table.amount_needed_to_call(index)))
                    if table.amount_needed_to_call(index) == 0:
                        action = int(input("Please select an action:\n1: Check\n2: Raise\n"))
                        if action == 1:
                            table.check(index)
                        elif action == 2:
                            amount_to_raise = int(input("Raise to: $"))
                            
                            table.raise_bet(index, amount_to_raise)
                    else:
                        action = int(input("Please select an action:\n1: Fold\n2: Call\n3: Raise\n"))
                        if action == 1:
                            table.fold(index)
                        elif action == 2:
                            table.call(index)
                        elif action == 3:
                            amount_to_raise = int(input("Raise to: $"))
                            table.raise_bet(index, amount_to_raise)
                        print(table.players[index].bet_amount)
                else:
                    print(table.players[index].position + " has folded")
            
            is_round_over = True

            for i in range(len(table.players)):
                index = (starting_pos + i) % len(table.players)
                if table.players[index].status == "folded" or (table.players[index].round_bet_amount == table.call_amount):
                    pass
                else:
                    is_round_over = False
                    print(table.players[index].name + " has not called the same amount")

    print("**********************************************")        
    print(table)
    print("**********************************************")

playGame()