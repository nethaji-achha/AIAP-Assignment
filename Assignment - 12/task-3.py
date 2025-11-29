best_profit = -1
best_A = 0
best_B = 0

# brute-force search with step size 0.01 for accuracy
for i in range(0, 501):  # A from 0 to 5
    for j in range(0, 501):  # B from 0 to 5
        A = i / 100
        B = j / 100

        # Check constraints
        if A + B <= 5 and 3*A + 2*B <= 12:
            profit = 6*A + 5*B
            if profit > best_profit:
                best_profit = profit
                best_A = A
                best_B = B

print("Optimal A =", best_A)
print("Optimal B =", best_B)
print("Maximum Profit =", best_profit)