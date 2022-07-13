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
    }
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuis = food["cuisine"]
        heat = food["heat_level"] * "🌶" 
        print(f"{name} ({cuis}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food


def getHeat(food):
  return food['heat_level']

def sort_by_heat(spicy_foods):
    #spicy_foods.sort(key=getHeat)
    return sorted(spicy_foods, key=lambda food: food['heat_level'] )
    #return spicy_foods

# print(sort_by_heat(spicy_foods))

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

# print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total / len(spicy_foods)
