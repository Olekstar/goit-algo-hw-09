import time
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    tracker = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                tracker[i] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = tracker[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

test_amounts = [100000, 500000, 1000000]

# Записуємо час виконання для жадібного алгоритму
greedy_times = []
for amount in test_amounts:
    start_time = time.time()
    find_coins_greedy(amount)
    greedy_times.append(time.time() - start_time)

# Записуємо час виконання для алгоритму динамічного програмування
dp_times = []
for amount in test_amounts:
    start_time = time.time()
    find_min_coins(amount)
    dp_times.append(time.time() - start_time)

# Тестуємо функції на прикладі суми 113
greedy_result = find_coins_greedy(113)
dp_result = find_min_coins(113)

# Виведення результатів жадібного алгоритму
print("Результати жадібного алгоритму для суми 113:")
for denom, count in greedy_result.items():
    print(f"- Номінал монети {denom}: кількість {count}")

# Виведення результатів алгоритму динамічного програмування
print("\nРезультати алгоритму динамічного програмування для суми 113:")
for denom, count in dp_result.items():
    print(f"- Номінал монети {denom}: кількість {count}")

# Виведення порівняння часу виконання
print("\nЧас виконання алгоритмів на великих сумах:")
for i, amount in enumerate(test_amounts):
    print(f"Сума {amount}:")
    print(f"- Жадібний алгоритм: {greedy_times[i]:.6f} секунд")
    print(f"- Алгоритм динамічного програмування: {dp_times[i]:.6f} секунд")

