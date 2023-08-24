class Player:
    def __init__(self, stack_size, position, is_hero, hand, name):
        self.stack_size = stack_size
        self.position = position
        self.status = "active"  # Can be "active", "folded", "called", or "raised"
        self.bet_amount = 0
        self.round_bet_amount = 0
        self.is_hero = is_hero
        self.hand = hand
        self.test_string = ""
        self.name = name


    def check(self):
            self.status = "checked"

    def call(self, amount):
        self.status = "called"
        self.stack_size -= amount
        self.bet_amount += amount
        self.round_bet_amount += amount

    def fold(self):
            self.status = "folded"

    def raise_bet(self, amount):
        self.status = "raised to " + str(amount)
        self.stack_size -= amount
        self.bet_amount += amount
        self.round_bet_amount += amount
    
    def give_hand(self, hand):
        self.hand = hand

    def round_reset(self):
        if self.status != "folded":
            self.status = "active"
            self.round_bet_amount = 0
    
    def __str__(self):
        return f"Player {self.name} | Position: {self.position} | Status: {self.status} | Stack: {self.stack_size}"