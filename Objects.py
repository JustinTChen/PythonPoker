from datascience import *
import numpy as np
from Deck import *

class Game:
"""
Defines game-specific rules, where each new game is an instance
"""
    table = None
    def __init__(self, start_chips, num_players, big_blind):
        self.total, self.start_chips = start_chips * num_players, start_chips
        self.big_blind_val, self.small_blind_val = big_blind, big_blind / 2
        self.min_bet = big_blind
        self.players = []

class Player(Game):
"""
A player class where:
    - Each player is an instance
    - chips
    - hand
    - raise/bet/check/fold
    - big/small blind
"""
    big_blind, small_blind = False, False
    def __init__(self, game, name):
        self.game_ID, self.name = game, name
        self.chips = game.start_chips
        game.players.append(self)

    def skip(self, table):
        return None

    def turn(self, round):
        assert self.chips > 0, "{0} is out of chips".format(player.name)
        print("Current Pot: ${0}".format(round.pot))
        ################################################################
        def options(round):
            action = input("Would you like to raise an amount, call $" + str(round.call_amount) + ", check, or fold? ")
            if 'raise' in action.lower():
            	amount = input("How much would you like to raise the pot? ")
            	try:
            		if int(amount) > round.call_amount and int(amount) <= self.chips:
            			print("You bet $" + amount + "!" )
            			#self.raise(int(amount))             Commented out these function calls until we build bet, call, fold, raise.
            		elif int(amount) > self.chips:
            			print("You're broke! Try again.")
            			options(round)
            		else:
            			print("Invalid amount. Try again.")
            			options(round)
            	except ValueError:
            		print("Invalid amount.")
            		options(round)
            elif 'check' in action.lower():
            	print("You checked!")
            	#self.check()
            elif 'call' in action.lower():
            	print("You called $" + str(round.call_amount) "!")
            	#self.call(round.call_amount)
            elif 'fold' in action.lower():
                print("You folded!")
                self.fold()
            else:
            	print("Invalid response. Try again.")
        ################################################################
        if big_blind == True:
            round.pot += self.big_blind_val
            self.chips -= self.big_blind_val
            self.big_blind = False
        elif small_blind == True:
            round.pot += self.small_blind_val
            self.chips -= self.small_blind_val
            self.small_blind, self.big_blind = False, True
            options(round)
        else:
            #check if it is next small big_blind
            #depending on input, complete the action
            try:
                if next(round.order).small_blind == True:   #How tf idk man somehow need to rotate the turn order
                    self.small_blind = True                 #Big blind, for simplicity, should go first
            except:                                         #Small blind goes last, but need to reassign big and small blinds
                self.small_blind = True
            options(round)
        print("Pot is now ${0}".format(round.pot))

class Table(Game):
"""
A table class where:
    - keeps track of num_players
    - order
    - dealer/dealing
    - pool/split pots
    - payout
    - remove player from game if broke
"""
    players, current_round = [], None
    def __init__(self, game): #when names are entered, need to convert to str
        self.game = game
        for player in game.players:
            player.table = self
            self.players.append(player) #table player list keeps track of who is still in the game
        #assign big blind, small big_blind
        self.players[len(self.players) - 1].small_blind = True
        self.players[len(self.players) - 2].big_blind = True

    def start_round(self):
        self.current_round = Round(self.game, self)
        self.current_round.play_round()

class Round(Table):
    pot = 0
    call_amount = 0

    def __init__(self, game, table):
        self.game, self.table = game, table
        self.deck = Deck().shuffle()
        self.call_amount += game.big_blind_val + game.small_blind_val

    def order(self):    #Use iterator to keep track of and check order (creates copy of player list)
        self.order = iter(self.table.players)
        return self.order

    def deal(self, player):
        player.hand = self.deck.shuffle(2, with_replacement=False)
                

    def play_round(self):
        for player in order():
            try #TURN
            except AssertionError:
                self.players.remove(player)
            #for each player, let them play a turn. Give them pot amount to start with. Then ask for action.
