def max_calories(calories, top=1):
    from collections import Counter
    calories_per_elf = Counter()
    elf = 1
    for cal in calories.split('\n'):
        if not cal:
            elf += 1
            continue
        calories_per_elf[elf] += int(cal)
    return sum(x[1] for x in calories_per_elf.most_common()[0:top])
