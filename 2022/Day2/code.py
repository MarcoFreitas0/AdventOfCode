# Points Mapping
game_map = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissor",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissor",
}

# Define Elf wins
elf_wins = {
    "Rock": "Scissor",
    "Scissor": "Paper",
    "Paper": "Rock"
}

me_wins = {v: k for k,v in elf_wins.items()}

bet_points = {
    "Rock": 1,
    "Paper": 2,
    "Scissor": 3
}

win_points = {
    "Loss": 0,
    "Draw": 3,
    "Win": 6
}


def winner(elf, me):
    
    if elf == me:
        return "Draw"
    elif me == elf_wins[elf]:
        return "Loss"
    else:
        return "Win"
    
def point_calc(game):
    elf, me = game

    return bet_points[me] + win_points[winner(elf, me)]


file_path = 'input.txt'

with open(file_path, "r") as f:
    text = f.read().strip()

hashed_games = list(map(lambda x: x.split(" "),text.split("\n")))

games = [tuple([game_map[bet] for bet in game]) for game in hashed_games]

points_per_game = list(map(point_calc, games))

print(f'Answer 1: Total points in the game is {sum(points_per_game)}')

# Part 2 Update

game_map_2 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissor",
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win",
}

games_2 = [tuple([game_map_2[bet] for bet in game]) for game in hashed_games]

def play(elf, result):
    
    if result == 'Draw':
        return elf
    elif result == 'Loss':
        return elf_wins[elf]
    else:
        return me_wins[elf]

def point_calc_2(game):
    elf, result = game

    return bet_points[play(elf,result)] + win_points[result]

points_per_game_2 = list(map(point_calc_2, games_2))

print(f'Answer 2: Total points in the game is {sum(points_per_game_2)}')