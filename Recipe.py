from typing import List, Any
from Fridge import Fridge
from FridgeIngredient import FridgeIngredient
from Ingredient import Ingredient



class Recipe:
    def __init__(self, name, vegetarian, vegan, dairyFree, glutenFree, nutFree, difficulty, spice, time, ingredients, steps):
        # make sure name is a string
        try:
            self.name = name.lower()
        except:
            raise Exception('The name of an ingredient must be a string')
        # Creation of recipe
        try:
            if difficulty <= 6 and difficulty > 0:
                self.difficulty = difficulty
        except:
            raise Exception('Difficulty must be a number between 1 and 5')

        try:
            if type(time) is int:
                self.time = time
        except:
            raise Exception('Recipe time must be a number')

        self.ingredients = ingredients
        self.steps = steps
        #self.goodForFridge = goodForFridge
        #self.goodForFreezer = goodForFreezer
        try:
            if spice <= 3 and spice >= 0:
                self.spice = spice
        except:
            raise Exception('Spice level must be a number between 0 and 3')

        # list of tags for sorting and fridge or pantry display on front end
        self.tags = list[vegetarian, vegan, dairyFree, glutenFree, nutFree]


    # returns list of ingredients
    def returnRecipeIngredients(self):
        return self.ingredients

    def returnRecipeSteps(self):
        return self.steps

    def printRecipeIngredients(self):
        for i in range(len(self.ingredients)):
            print(self.ingredients[i].name, ' ', self.ingredients[i].quantity, ' ', self.ingredients[i].unit)

    def printRecipeSteps(self):
        for i in self.steps.values():
            print(i)

    # returns a recipe object based on user input
    def createRecipe():
        while True:
            print('Do you want to create a new Recipe?\n[y/n]')
            ui = input('\n >> ')
            if (ui == 'n'):
                break

            print('What is the name of your recipe?')
            ui = input('\n >> ')
            title = ui

            veggie = False
            print('Is your recipe vegetarian?\n[y/n]')
            ui = input('\n >> ')
            if (ui == 'y'):
                veggie = True

            vegan = False
            print('Is your recipe vegan?\n[y/n]')
            ui = input('\n >> ')
            if (ui == 'y'):
                vegan = True

            dairyF = False
            print('Is your recipe dairy-free?\n[y/n]')
            ui = input('\n >> ')
            if (ui == 'y'):
                dairyF = True

            nutsInMe = False
            print('Is your recipe nut free?\n[y/n]')
            ui = input('\n >> ')
            if (ui == 'y'):
                nutsInMe = True

            glutenF = False
            print('Is your recipe gluten-free?\n[y/n]')
            ui = input('\n >> ')
            if (ui == 'y'):
                glutenF = True

            print('How difficult is your recipe?\n[1-5, 5 being hardest]')
            ui = input('\n >> ')
            difficult = int(ui)

            print('How spicy is your recipe?\n[0-3, 3 being very very spicy, 0 being not spicy]')
            ui = input('\n >> ')
            spicy = int(ui)

            print('How long does your recipe take to make?\n[Time in minutes]')
            ui = input('\n >> ')
            length = int(ui)

            print('How many days is your recipe good for in the fridge?\n[A number of days]')
            ui = input('\n >> ')
            good4Fridge = int(ui)

            print('How many days is your recipe good for if you freeze it?\n[A number of days]')
            ui = input('\n >> ')
            good4Freezer = int(ui)

            ingredientsList = []
            print('What ingredients are needed for your recipe?\n[write one ingredient at a time]')
            while True:
                print('What is the name of the ingredient?')
                ui = input('\n >> ')
                name = ui
                print('How much of this ingredient?\n[a number]')
                ui = input('\n >> ')
                quantity = int(ui)
                print('Does this ingredient have an associated unit?\n[If not write \'n\']')
                ui = input('\n >> ')
                if (ui == 'n'):
                    unit = 'None'
                else:
                    unit = ui

                i1 = Ingredient(name, quantity, unit)
                ingredientsList.append(i1)

                print('Do you need to add more ingredients?\n[y/n]')
                ui = input('\n >> ')
                if (ui == 'n'):
                    break
                else:
                    continue

            stepsDict = {}
            i = 1
            print('Let\'s write the steps for this recipe!')
            while True:
                print('What\'s the next step?\n[Just write the step, no special instructions!]')
                ui = input('\n >> ')
                stepsDict[i] = ui
                i += 1
                print('Are there more steps?\n[y/n]')
                ui = input('\n >> ')
                if (ui == 'n'):
                    break
                else:
                    continue
            print('You\'re all done!')
            return Recipe(title, veggie, vegan, dairyF, glutenF, nutsInMe, difficult, length, ingredientsList,
                          stepsDict, good4Fridge, good4Freezer, spicy)




