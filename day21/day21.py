import copy

def main():
    foods = open("input21.txt", "r").read().strip().split('\n')
    possible = {} # allergen -> possible ingrediens
    setOfIngredients = set()
    for food in foods: 
        food = food.split('(')
        ingredients = food[0].split(' ')[:-1]
        for i in ingredients:
            setOfIngredients.add(i)         #Add ingredient to setOfIngredient

        allergens = food[1].split(' ')[1:]
        allergens = [allergen[0:-1] for allergen in allergens]
        for allergen in allergens:          #For every allergen: Possible ingredients are the ones that appear in every food where the allergen appears.
            if allergen in possible.keys():
                possible[allergen] = possible[allergen] & set(ingredients)
            else:
                possible[allergen] = set(ingredients)

    for value in possible.values():         #To get which ingredients that can't be allergic. 
        setOfIngredients -= value

    ans1 = 0
    for food in foods:                      #Count how many times these ingredients appear to get answer for part1  
        food = food.split('(')
        ingredients = food[0].split(' ')[:-1]
        for i in ingredients:
            if i in setOfIngredients:
                ans1 += 1
    print(ans1)

    isUsed = set()
    pairs = []          #Pairs on form (Allergen, Ingredient)
    while len(isUsed) < len(possible.keys()):    
        for key in possible.keys():
            possibleIngredients = possible[key] - isUsed        #Remove used ingredients
            possible[key] = copy.copy(possibleIngredients)
            if len(possibleIngredients) == 1:           #If an allergic can only be one ingredient, but this pair in pairs and add the ingredient to isUsed.
                ingredient = possibleIngredients.pop()
                pairs.append((key, ingredient))
                isUsed.add(ingredient)

    pairs.sort(key = lambda x: x[0])    #Sort by Allergen
    ans2 = ''
    for pair in pairs:              #Make string on form 'ingredient1,ingredient2,ingredient3...'
        ans2 += pair[1] + ','
    ans2 = ans2[:-1]                #Remove trailiing comma
    
    print(ans2)

main()