#initializes the game
def start_game():
    x = input("Would you like to start a new game [y/n]? ")
    if x == 'y':
        print("Starting game!")
        params = game_setup()
        return current_game = Game(params[0], params[1], params[2])

    elif x == 'n':
        print("Goodbye.")

    else:
        print("Invalid input, please try again.")
        start()

#START THE GAME
game = start()
player_setup()
game.table = Table(game)
#START THE GAME

#sets rules for game
def game_setup():
    start_chips = input("Starting chip amount: ")
    num_players = input("How many players? ")
    big_blind = input("Big blind? ")
    return [start_chips, num_players, big_blind]

#adds players to game
def player_setup():
    for player in range(game.num_players):
        name = input("Player{0} name: ".format(player))
        Player(game, name)
