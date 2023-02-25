def main():
    with open("python/day1/data.txt") as f:
        lines = list(f.readlines())
        totals = []
        current_total = 0
        current_max = None
        for line in lines:
            if line == "\n": # line break means new elf
                if (current_max is None) or (current_total > current_max):
                    current_max = current_total
                totals.append(current_total)
                current_total = 0
            else:
                current_total += int(line.strip("\n"))
    return current_max


if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")
