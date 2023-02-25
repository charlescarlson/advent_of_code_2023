import typing as typ

ROCK: str = "ROCK"
PAPER: str = "PAPER"
SCISSORS: str = "SCISSORS"

A: str = "A"
B: str = "B"
C: str = "C"
X: str = "X"
Y: str = "Y"
Z: str = "Z"

WIN: str = "win"
LOSE: str = "lose"
DRAW: str = "draw"

W: int = 6
L: int = 0
D: int  = 3

WIN_LOSE_PERMUTATIONS: typ.Dict[typ.Tuple[str, str], int] = {

    # oponent, you
    (ROCK, ROCK): D, 
    (ROCK, PAPER): W,
    (ROCK, SCISSORS): L,
    
    (PAPER, ROCK): L,
    (PAPER, PAPER): D,
    (PAPER, SCISSORS): W,
    
    (SCISSORS, ROCK): W,
    (SCISSORS, PAPER): L,
    (SCISSORS, SCISSORS): D,
}

REVERSE_LOOKUP: typ.Dict[typ.Tuple[str, str], str] = {
    # opponent, outcome
    (ROCK, WIN): PAPER,
    (ROCK, LOSE): SCISSORS,
    (ROCK, DRAW): ROCK,

    (PAPER, WIN): SCISSORS,
    (PAPER, LOSE): ROCK,
    (PAPER, DRAW): PAPER,

    (SCISSORS, WIN): ROCK,
    (SCISSORS, LOSE): PAPER,
    (SCISSORS, DRAW): SCISSORS,
}

MOVE_SCORE: typ.Dict[str, int] = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

def translate_second_column_part_1(letter: str) -> str:
    if letter == X:
        return A
    elif letter == Y:
        return B
    elif letter == Z:
        return C
    else:
        raise ValueError("Must be X, Y, or Z")
    
def translate_second_column_part_2(letter: str) -> str:
    if letter == X:
        return LOSE
    elif letter == Y:
        return DRAW
    elif letter == Z:
        return WIN
    else:
        raise ValueError("Must be X, Y, or Z")

def get_move_from_letter(letter: str) -> str:
    if letter == A:
        return ROCK
    elif letter == B:
        return PAPER
    elif letter == C:
        return SCISSORS
    else:
        raise ValueError("Must be A, B, or C")


def game(line: str, part: int) -> typ.Tuple[str, str]:
    stripped: str = line.strip("\n")
    split: str = stripped.split(" ")

    opponent_move: str = get_move_from_letter(split[0])
    if part == 1:
        your_move: str = get_move_from_letter(translate_second_column_part_1(split[1]))
    else:
        intended_outcome: str = translate_second_column_part_2(split[1])
        your_move = REVERSE_LOOKUP[(opponent_move, intended_outcome)]
    
    return (opponent_move, your_move)


def calculate_score(game: typ.Tuple[str, str], debug: bool = False) -> int:
    move_score: int = MOVE_SCORE[game[1]]
    win_lose_draw_result: int = WIN_LOSE_PERMUTATIONS[game]

    score: int = win_lose_draw_result + move_score
    if debug:
        print(f"Game: {game}, score: {score}")
    return score


def part_1() -> int:
    with open("python/day2/data.txt") as file:
        lines: typ.List[str] = file.readlines()
        total_score: int = 0
        for line in lines:
            total_score += calculate_score(game(line, part=1), debug=True)
    return total_score

def part_2() -> int:
    with open("python/day2/data.txt") as file:
        lines: typ.List[str] = file.readlines()
        total_score: int = 0
        for line in lines:
            total_score += calculate_score(game(line, part=2), debug=True)
    return total_score


if __name__ == "__main__":
    result_1: int = part_1()
    result_2: int = part_2()
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")