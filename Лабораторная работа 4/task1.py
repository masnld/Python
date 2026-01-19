
import json

def task() -> float:
    with open("input.json", "r", encoding="utf-8") as f:
        a = json.load(f)

    total = sum(item["score"] * item["weight"] for item in a)
    return round(total, 3)

print(task())