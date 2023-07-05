spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_keys = [key["name"] for key in spicy_foods]
    return spicy_keys

def get_spiciest_foods(spicy_foods):
    spiciest_items = [item for item in spicy_foods if item["heat_level"] >= 5]
    return spiciest_items

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        spicy_emojis = "🌶" * item["heat_level"]
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {spicy_emojis}" )
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"] == cuisine:
            return item
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for item in spiciest_foods:
        spicy_emojis = "🌶" * item["heat_level"]
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {spicy_emojis}")

def get_average_heat_level(spicy_foods):
    all_heats = [item["heat_level"] for item in spicy_foods]
    total_heat = sum(all_heats)
    return total_heat / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
