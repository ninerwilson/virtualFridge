from FridgeIngredient import FridgeIngredient


class Fridge:

    def __init__(self, items):
        try:
            if type(items) is list:
                self.items = items
                self.itemNames = []
                for i in self.items:
                    self.itemNames.append(i.name)
        except:
            raise Exception('Items in the frige must be a list of Ingredients')


    def addItem(self, newItem):
        if type(newItem) is not FridgeIngredient:
            print('Items in the frige must be an Ingredient')
        else:
            self.items.append(newItem)
            self.itemNames.append(newItem.name)

    def printIngredientsInFridge(self):
        for i in range(len(self.items)):
            print(self.items[i].name, ' ', self.items[i].quantity, ' ', self.items[i].unit)

    def putFridgeIngredientsInList(self):
        ingredientsInFridge = []
        for i in range(len(self.items)):
            ingredientsInFridge.append(self.items[i].name)
        return ingredientsInFridge

    # function to check if a recipes ingredients are in the fridge
    def checkForIngredients(self, recipe):
        for i in recipe.ingredients:

            if i.name not in self.itemNames:
                # print('You do not have all the ingredients to make this recipe')
                return False
                break
        return True

    # function to remove the required quantity of an item being used in a recipe from the fridge
    def useARecipe(self, recipe):
        if self.checkForIngredients(recipe) is False:
            print('You do not have all the ingredients for this recipe')
            return False
        ingredientsInRecipe = recipe.ingredients
        ingredientNames = []
        for i in ingredientsInRecipe:
            ingredientNames.append(i.name)
        for i in range(0, len(ingredientNames)):
            index = self.itemNames.index(ingredientNames[i])
            self.items[index].take_quantity(recipe.ingredients[i].quantity)

    def fractionOfIngredients(self, recipe):
        if self.checkForIngredients(recipe):
            return 1
        recipeIngredients = []
        matches = 0
        for i in recipe.ingredients:
            recipeIngredients.append(i)
        for i in recipeIngredients:
            if i.name in self.itemNames:
                matches = matches + 1
        return float(int(matches)/len(recipe.ingredients))


    def recommendation(self, listOfRecipes):
        completeRecipes = []
        incompleteRecipes = []
        recommendations = []
        for r in listOfRecipes:
            if self.checkForIngredients(r):
                completeRecipes.append(r)
            else:
                incompleteRecipes.append(r)
        ordering = {}
        fractions = []
        for r in incompleteRecipes:
            fractions.append(self.fractionOfIngredients(r))
        for i in range(0,len(incompleteRecipes)):
            ordering[i] = fractions[i]

        print(ordering.items())

        orderedOrdering = {k: v for k, v in sorted(ordering.items(), key=lambda item: item[1])}

        print(orderedOrdering.items())

        orderedOrderingINDEX = []
        for i in orderedOrdering:
            orderedOrderingINDEX.append(i)

        orderedOrderingINDEX.reverse()


        for i in completeRecipes:
            recommendations.append(i)

        for i in orderedOrderingINDEX:
            recommendations.append(incompleteRecipes[i])

        return recommendations
