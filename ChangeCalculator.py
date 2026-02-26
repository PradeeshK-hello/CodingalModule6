def change_combinations(amount, options):
    result = []
    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(combo.copy())
            return
        if remaining < 0:
            return
        for i in range(start, len(options)):
            combo.append(options[i])
            backtrack(remaining - options[i], combo, i)
            combo.pop()
    backtrack(amount, [], 0)
    return result
amount = int(round(float(input("Enter the amount: ")) * 100))
denominations = [10000, 5000, 1000, 500, 200, 100, 50, 20, 10, 5]
combinations = change_combinations(amount, denominations)
for c in combinations:
    final = [f"{cents/100:.2f}" for cents in c]
    print(final)