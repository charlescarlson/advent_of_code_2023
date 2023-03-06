import typing as typ

with open("python/day3/data.txt", 'r', encoding="UTF-8") as f:
    LINES = [line.strip("\n") for line in f.readlines()]

def get_priority_score(intersection: str) -> int:

    # https://www.ascii-code.com/
    LOWERCASE_ASCII_START_INDEX = 97
    UPPERCASE_ASCII_START_INDEX = 65
    
    def get_score_from_ascii(
        ascii_start: int, 
        offset: typ.Optional[int] = 0
    ) -> typ.Dict[str, int]:
        return {
            chr(ascii_start + i): offset + i + 1
            for i in range(26)
        }
    
    priority_score_map = {
        **get_score_from_ascii(LOWERCASE_ASCII_START_INDEX),
        **get_score_from_ascii(UPPERCASE_ASCII_START_INDEX, offset=26)
    }
        
    return priority_score_map[intersection]


def part_1() -> int:
    total = 0
    for line in LINES:
        halfway = int(len(line) / 2)
        arr1 = set(line[:halfway])
        arr2 = set(line[halfway:])

        intersection = arr1.intersection(arr2)
        total += get_priority_score(intersection.pop())
    return total


def part_2():
    total = 0
    while len(LINES) > 0:
        elf_1: typ.Set[str] = set(LINES.pop())
        elf_2: typ.Set[str] = set(LINES.pop())
        elf_3: typ.Set[str] = set(LINES.pop())

        intersection_1_2 = elf_1.intersection(elf_2)
        intersection_1_2__3 = intersection_1_2.intersection(elf_3)

        total += get_priority_score(intersection_1_2__3.pop())
    return total
        

if __name__ == "__main__":
    result_1 = part_1()
    result_2 = part_2()
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")