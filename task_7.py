import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(trials=100_000):
    # Initialize a dictionary to store count of each possible dice sum (2 to 12)
    results = {sum_: 0 for sum_ in range(2, 13)}

    # Simulate dice rolls
    for _ in range(trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    # Convert counts to percentage probabilities
    percentages = {k: (v / trials) * 100 for k, v in results.items()}

    return percentages

# Run simulation
percentages = monte_carlo_dice_simulation(trials=10_000_000)

# Print table of results
print("Sum\tProbability (%)")
for k in sorted(percentages.keys()):
    print(f"{k}\t{percentages[k]:.2f}")



