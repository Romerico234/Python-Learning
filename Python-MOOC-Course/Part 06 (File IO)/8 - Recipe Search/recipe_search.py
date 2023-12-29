def read_file(filename):
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip())
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new = { "ingredients": []}
    for row in rows:
        if name_in_row:
            new["name"] = row
            name_in_row = False
            prep_time_in_row = True
        elif prep_time_in_row:
            new["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0:
            new["ingredients"].append(row)
        else:
            recipes.append(new)
            name_in_row = True
            new = {"ingredients": []}
    recipes.append(new)
    return recipes
 
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
    return found
 
def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
    return found
 
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
    return found