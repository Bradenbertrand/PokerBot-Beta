class PokerTable:
    def __init__(self, smallBlind, bigBlind):
        self.players = []
        self.community_cards = []
        self.round_pot = 0
        self.pot = 0
        self.positions = ["SB", "BB", "UTG", "MP", "CO", "BTN"]
        self.round = ""
        self.position_index = 0
        self.call_amount = 0

    def add_player(self, player):
        if len(self.players) < 6:
            player.position = self.positions[len(self.players)]
            self.players.append(player)
            if player.is_hero == True:
                print(f"Hero has joined the table in position {player.position}.")
            else:
                print(f"{player.name} has joined the table in position {player.position}.")
        else:
            print("Table is full. Cannot add more players.")

    def deal_community_cards(self, cards):
        self.community_cards.extend(cards)
        print("Community cards:", self.community_cards)

    def reset_table(self):
        self.community_cards = []
        self.pot = 0
        for player in self.players:
            player.status = "active"
            player.bet_amount = 0
            player.round_bet_amount = 0
        self.position_index = 0

    def next_round(self):
        self.position_index = (self.position_index + 1) % len(self.positions)

    def set_round(self, round):
        self.round = round

    def set_call_amount(self, amount):
        self.call_amount = amount

    def add_to_pot(self, amount):
        self.pot += amount
        self.round_pot += amount

    def reset_round_pot(self, amount):
        self.round_pot = 0

    def amount_needed_to_call(self, player_index):
        return self.call_amount - self.players[player_index].round_bet_amount

    def call(self, player_index):
        amount_needed = self.amount_needed_to_call(player_index)
        self.add_to_pot(amount_needed)
        self.players[player_index].call(amount_needed)
    
    def fold(self, player_index):
        self.players[player_index].fold()

    def raise_bet(self, player_index, amount):
        self.add_to_pot(amount)
        self.call_amount = amount
        self.players[player_index].raise_bet(amount)
    
    def check(self, player_index):
        self.players[player_index].check()
        
    def player_round_reset(self):
        for player in self.players:
            player.round_reset()
    
    def table_round_reset(self):
        self.round_pot = 0
        self.call_amount = 0

    def __str__(self):
        player_info = "\n".join(str(player) for player in self.players)
        return f"Poker Table:\n{player_info}\nCommunity cards: {self.community_cards}\nPot: {self.pot}\nCurrent Position: {self.positions[self.position_index]}"