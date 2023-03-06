import typing as typ


def get_elf_totals() -> typ.List[int]:
    with open("python/day1/data.txt") as f:
        lines: typ.List[str] = list(f.readlines())
        totals: typ.List[int] = []
        current_total: int = 0
        for line in lines:
            if line == "\n": # line break means new elf
                totals.append(current_total)
                current_total = 0
            else:
                current_total += int(line.strip("\n"))
    return sorted(totals)


def part_1() -> int:
    totals: typ.List[int] = get_elf_totals()
    return totals[-1]


def part_2() -> int:
    totals = get_elf_totals()
    return sum(totals[len(totals) - 3:])
    

if __name__ == "__main__":
    result_1: int = part_1()
    result_2: int = part_2()
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")
