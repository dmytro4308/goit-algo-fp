items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected = {}
    remaining = budget

    for name, info in sorted_items:
        if info['cost'] <= remaining:
            selected[name] = 1
            total_calories += info['calories']
            remaining -= info['cost']

    return total_calories, selected

def dynamic_programming(items, budget):
    n = len(items)
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    dp = [0] * (budget + 1)
    path = [{} for _ in range(budget + 1)]

    for i in range(n):
        for b in range(budget, costs[i] - 1, -1):
            if dp[b - costs[i]] + calories[i] > dp[b]:
                dp[b] = dp[b - costs[i]] + calories[i]
                path[b] = path[b - costs[i]].copy()
                path[b][names[i]] = path[b].get(names[i], 0) + 1

    return dp[budget], path[budget]

# Run and compare both algorithms
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Total Calories:", greedy_result[0])
print("Selected Items:", greedy_result[1])
print("\nDynamic Programming:")
print("Total Calories:", dp_result[0])
print("Selected Items:", dp_result[1])

# Greedy Algorithm:
# Total Calories: 870
# Selected Items: {'cola': 1, 'potato': 1, 'pepsi': 1, 'hot-dog': 1}

# Dynamic Programming:
# Total Calories: 970
# Selected Items: {'pizza': 1, 'pepsi': 1, 'cola': 1, 'potato': 1}