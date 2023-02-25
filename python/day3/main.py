import typing as typ

def get_intersection(arr: typ.List[str]) -> str:
    halfway = int(len(arr) / 2)
    arr1 = arr[:halfway]
    arr2 = arr[halfway:]

    # O((n/2)**2)
    for elem in arr1:
        if elem in arr2:
            return elem


def build_priority_score_maping():

    # https://www.ascii-code.com/
    LOWERCASE_ASCII_START_INDEX = 97
    UPPERCASE_ASCII_START_INDEX = 65
    
    def get_score_from_ascii(ascii_start: int, offset: typ.Optional[int] = 0) -> typ.Dict[str, int]:
        return {
            chr(ascii_start + i): offset + i + 1
            for i in range(26)
        }
        
    return {
        **get_score_from_ascii(LOWERCASE_ASCII_START_INDEX),
        **get_score_from_ascii(UPPERCASE_ASCII_START_INDEX, offset=26)
    }


def get_priority_score(intersection: str) -> int:
    priority_score_mappings = build_priority_score_maping()

    return priority_score_mappings[intersection]


def main() -> int:
    with open("python/day3/data.txt", 'r', encoding="UTF-8") as f:
        total = 0
        for line in f.readlines():
            intersection = get_intersection(line.strip("\n"))
            total += get_priority_score(intersection)
    return total
        

if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")