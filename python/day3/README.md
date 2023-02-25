### Day 3: Rucksack Reorganization

Time Complexity: O( (n/2) ** 2 )

## The Algorithm
```
let total_priority = 0
foreach rucksack in rucksacks:
    let intersection = get_intersection(rucksack)
    let priority = get_priority(intersection)
    total_priority += priority
return total_priority
```

Each rucksack has two equally sized compartments, and we can assume the elf evenly distributed items into the compartments. Therefore, we can assume that the number of items in each rucksack, i.e the length of each list, to be even.


## Calculating the Priority Score
In order to get the priority score for a given character, I could have manually created a dictionary keeping track of the priority of values from a-Z. If this program needed to be as fast as possible, this would be the way to do it, since a dictionary with 52 keys is within the realm of reason for a python program (from a code elegance standpoint).


Since that is not very fun, I decided to use the ASCII table to help me build the dictionary. The `chr()` function was helpful here. 
