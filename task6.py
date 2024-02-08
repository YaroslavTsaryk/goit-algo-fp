items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(budjet):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"], reverse=True)
    res = []
    calories = 0
    for it in sorted_items:
        if it[1]["cost"] <= budjet:
            res.append(it)
            budjet -= it[1]["cost"]
            calories += it[1]["calories"]
    return calories, res


budjet = int(input("Enter budjet (ex 100):"))

print("Greedy solution")
answer = greedy_algorithm(budjet)
print(f"Calories: {answer[0]}")
print(f"Ingredients: {answer[1]}")


def dynamic_programming(budjet):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["cost"])
    # print(sorted_items)
    K = [[(0, []) for i in range(budjet + 1)] for c in range(len(sorted_items) + 1)]

    for i in range(len(sorted_items) + 1):
        for b in range(budjet + 1):
            if i == 0 or b == 0:
                K[i][b] = (0, [])
            elif sorted_items[i - 1][1]["cost"] <= b:
                val1 = (
                    sorted_items[i - 1][1]["calories"]
                    + K[i - 1][b - sorted_items[i - 1][1]["cost"]][0]
                )
                val2 = K[i - 1][b][0]
                # K[i][b] = max(sorted_items[i - 1][1]['calories'] + K[i - 1][b - sorted_items[i - 1][1]['cost']], K[i - 1][b])
                if val1 >= val2:
                    # foods=[sorted_items[i - 1],K[i - 1][b - sorted_items[i - 1][1]['cost']][1]]
                    foods = K[i - 1][b - sorted_items[i - 1][1]["cost"]][1] + [
                        sorted_items[i - 1]
                    ]
                    K[i][b] = (val1, foods)
                else:
                    K[i][b] = K[i - 1][b]
            else:
                K[i][b] = K[i - 1][b]

    return K[len(sorted_items)][budjet]


print("Dynamic programming solution")
answer = dynamic_programming(budjet)
print(f"Calories: {answer[0]}")
print(f"Ingredients: {answer[1]}")
