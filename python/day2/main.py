import typing as typ

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

A = "A"
B = "B"
C = "C"
X = "X"
Y = "Y"
Z = "Z"

WIN = 6
LOSE = 0
DRAW = 3

WIN_LOSE_PERMUTATIONS = {

    # oponent, you
    (ROCK, ROCK): DRAW, 
    (ROCK, PAPER): WIN,
    (ROCK, SCISSORS): LOSE,
    
    (PAPER, ROCK): LOSE,
    (PAPER, PAPER): DRAW,
    (PAPER, SCISSORS): WIN,
    
    (SCISSORS, ROCK): WIN,
    (SCISSORS, PAPER): LOSE,
    (SCISSORS, SCISSORS): DRAW,
}

MOVE_SCORE = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

def translate_second_column(letter: str):
    if letter == X:
        return A
    elif letter == Y:
        return B
    elif letter == Z:
        return C
    else:
        raise ValueError("Must be X, Y, or Z")

def get_move_from_letter(letter: str):
    if letter == A:
        return ROCK
    elif letter == B:
        return PAPER
    elif letter == C:
        return SCISSORS
    else:
        raise ValueError("Must be A, B, or C")


def game(line: str):
    stripped = line.strip("\n")
    split = stripped.split(" ")

    opponent_move = get_move_from_letter(split[0])
    your_move = get_move_from_letter(translate_second_column(split[1]))
    
    return (opponent_move, your_move)


def calculate_score(game: typ.Tuple[str, str]):
    move_score = MOVE_SCORE[game[1]]
    win_lose_draw_result = WIN_LOSE_PERMUTATIONS[game]

    score = win_lose_draw_result + move_score
    print(f"Game: {game}, score: {score}")
    return score


def main():
    with open("python/day2/data.txt") as file:
        lines = file.readlines()
        total_score = 0
        for line in lines:
            total_score += calculate_score(game(line))
    return total_score


if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")