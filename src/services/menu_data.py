import csv
from models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.generate_menu()

    def read(self):
        with open(self.source_path, encoding="utf-8") as file:
            data = csv.DictReader(file)
            return list(data)

    def generate_menu(self):
        data = self.read()
        dish_dict = {}

        for ingredient in data:
            dish_name = ingredient["dish"]
            dish_price = float(ingredient["price"])
            ingredient_name = ingredient["ingredient"]
            ingredient_amount = int(ingredient["recipe_amount"])

            if dish_name not in dish_dict:
                dish_dict[dish_name] = Dish(dish_name, dish_price)

            dish_dict[dish_name].add_ingredient_dependency(
                Ingredient(ingredient_name), ingredient_amount
            )

        self.dishes.update(dish_dict.values())
