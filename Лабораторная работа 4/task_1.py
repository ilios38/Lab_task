import json

def task():
    with open("input.json", "r") as file:
        data = json.load(file)

    total_sum = sum(entry["score"] * entry["weight"] for entry in data)

    result = round(total_sum, 3)

    return result

print(task())