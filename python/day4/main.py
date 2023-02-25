import typing as typ

def get_range(range_as_str: str) -> typ.List[int]:
    as_list: str = range_as_str.split("-")
    start, end = int(as_list[0]), int(as_list[1])
    return list(range(start, end + 1))
    
def completely_contains(range_1: typ.List[int], range_2: typ.List[int]) -> bool:
    range_1_start: int = range_1[0]
    range_1_end: int = range_1[-1]

    range_2_start: int = range_2[0]
    range_2_end: int = range_2[-1]

    if (range_1_start >= range_2_start) and (range_1_end <= range_2_end):
        return True
    elif (range_2_start >= range_1_start) and (range_2_end <= range_1_end):
        return True
    else:
        return False

def do_draw(range_1: typ.List[int], range_2: typ.List[int]):
    def get_range_str(r: typ.List[int], m: int) -> str:
        r_start: int = r[0]
        r_end: int = r[-1]
        return f"{r_start}-{r_end}  |  " + "." * (r_start - 1) + f"{''.join(str(x) for x in r)}" + "." * (m - r_end)
    
    max_val: int = max(range_1[-1], range_2[-1])

    print(get_range_str(range_1, max_val))
    print(get_range_str(range_2, max_val))
    print("\n")


def main(draw: bool = False):
    with open("python/day4/data.txt", "r", encoding="UTF-8") as file:
        completely_contains_count: int = 0
        for line in file.readlines():
            ranges: typ.List[str] = line.strip("\n").split(",")
            range_1: typ.List[int] = get_range(ranges[0])
            range_2: typ.List[int] = get_range(ranges[1])

            if completely_contains(range_1, range_2):
                completely_contains_count += 1

            if draw:
                do_draw(range_1, range_2)
            
    return completely_contains_count

if __name__ == "__main__":
    result: int = main(draw=True)
    print(f"Result = {result}")