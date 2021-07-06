from types import List
from collections import Counter


class Solution1:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        orders_dict = dict()
        food_names = set()
        for _, table, food in orders:
            orders_dict.setdefault(table, list()).append(food)
            food_names.add(food)
        food_names = sorted(list(food_names))
        food_names.insert(0, "Table")

        result = [food_names]

        for table in sorted(orders_dict.keys(), key=lambda t: int(t)):
            food = Counter(orders_dict[table])
            raw = [table]
            for food_name in food_names:
                if food_name == "Table":
                    continue
                raw.append(str(food.get(food_name, 0)))
            result.append(raw)
        return result


class Solution2:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        orders_dict = dict()
        food_names = set()
        for _, table, food in orders:
            orders_dict.setdefault(table, list()).append(food)
            food_names.add(food)
        food_names = sorted(list(food_names))
        table_numbers = sorted(orders_dict.keys(), key=lambda t: int(t))
        result = [["0" for _ in range(len(food_names) + 1)] for _ in range(len(table_numbers) + 1)]
        result[0][0] = "Table"

        for i, food in enumerate(food_names):
            result[0][i + 1] = food
        for i, table in enumerate(table_numbers):
            row = i + 1
            result[row][0] = table
            food_counter = Counter(orders_dict[table])
            for j, food in enumerate(food_names):
                result[row][j + 1] = str(food_counter.get(food, 0))
        return result
