import typing as typ

ranges_type = typ.List[typ.Tuple[typ.List[int], typ.List[int]]]

    
def do_draw(range_1: typ.List[int], range_2: typ.List[int]) -> None:
    def get_range_str(r: typ.List[int], m: int) -> str:
        r_start: int = r[0]
        r_end: int = r[-1]
        return f"{r_start}-{r_end}  |  " + "." * (r_start - 1) + f"{''.join(str(x) for x in r)}" + "." * (m - r_end)
    
    max_val: int = max(range_1[-1], range_2[-1])

    print(get_range_str(range_1, max_val))
    print(get_range_str(range_2, max_val))
    print("\n")


def completely_contains(range_1: typ.List[int], range_2: typ.List[int]) -> bool:
    range_1_start: int = range_1[0]
    range_1_end: int = range_1[-1]

    range_2_start: int = range_2[0]
    range_2_end: int = range_2[-1]

    return (
        (range_1_start >= range_2_start) and (range_1_end <= range_2_end) 
        or (range_2_start >= range_1_start) and (range_2_end <= range_1_end)
    )
    

def overlaps(range_1: typ.List[int], range_2: typ.List[int]) -> bool:
    range_1_start: int = range_1[0]
    range_1_end: int = range_1[-1]

    range_2_start: int = range_2[0]
    range_2_end: int = range_2[-1]

    return not (
        (range_1_end < range_2_start) 
        or (range_2_end < range_1_start)
    )


def get_ranges() -> ranges_type:
    
    def get_range(range_as_str: str) -> typ.List[int]:
        as_list: str = range_as_str.split("-")
        start, end = int(as_list[0]), int(as_list[1])
        return list(range(start, end + 1))
    
    ranges: ranges_type = []
    with open("python/day4/data.txt", "r", encoding="UTF-8") as file:
        lines = [line.strip("\n").split(",") for line in file.readlines()]
        for line in lines:
            range_1: typ.List[int] = get_range(line[0])
            range_2: typ.List[int] = get_range(line[1])
            ranges.append((range_1, range_2))

    return ranges


def part_1(draw: bool = False):
    range_groups: ranges_type = get_ranges()
    count: int = 0
    for range_group in range_groups:
        range_1: typ.List[int] = range_group[0]
        range_2: typ.List[int] = range_group[1]
        
        if completely_contains(range_1, range_2):
            count += 1

        if draw:
            do_draw(range_1, range_2)

    return count

def part_2(draw: bool = False):
    range_groups: ranges_type = get_ranges()
    count: int = 0
    for range_group in range_groups:
        range_1: typ.List[int] = range_group[0]
        range_2: typ.List[int] = range_group[1]
        
        if overlaps(range_1, range_2):
            count += 1

        if draw:
            do_draw(range_1, range_2)

    return count


if __name__ == "__main__":
    result_1: int = part_1(draw=False) # draw is broken
    result_2: int = part_2(draw=False) # draw is broken
    print(f"Result 1 = {result_1}")
    print(f"Result 2 = {result_2}")