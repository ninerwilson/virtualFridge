from Fridge import Fridge
from FridgeIngredient import FridgeIngredient
from Ingredient import Ingredient
from Recipe import Recipe

if __name__ == '__main__':
    pb = Ingredient('peanut butter', 2, 'tbsp')
    jelly = Ingredient('jelly', 2, 'tbsp')
    bread = Ingredient('bread', 2, 'slices')
    pbAndJ = Recipe('pbAndJ', True, True, True, False, False, 1, 5, 0, [pb, jelly, bread], {1: 'thr'})

    # pbAndJ.printRecipeIngredients()

    iF1 = FridgeIngredient('peanut butter', 32, 60, 'tbsp')
    iF2 = FridgeIngredient('jelly', 32, 60, 'tbsp')
    fridgeList = [iF1, iF2]
    testFridge = Fridge(fridgeList)

    # print(testFridge.itemNames)

    #print(testFridge.checkForIngredients(pbAndJ))

    iF3 = FridgeIngredient('bRead', 12, 7, 'slices')
    testFridge.addItem(iF3)

    mi = Ingredient('milk', .5, 'cup')
    ce = Ingredient('cereal', 1, 'cup')

    cereal = Recipe('cereal', True, False, False,False,True,1,0,5,[mi,ce], {1:'do it loser'} )

    miF = FridgeIngredient('milk', 4, 5, 'cup')

    testFridge.addItem(miF)

    print(testFridge.checkForIngredients(cereal))

    #print(testFridge.checkForIngredients(pbAndJ))

    i3 = Ingredient('rice', 1, 'cup')
    i4 = Ingredient('soy sauce', 2, 'tbsp')
    i5 = Ingredient('eggs', 1)
    i6 = Ingredient('sugar', 1, 'tbsp')
    i7 = Ingredient('garlic', 4, 'cloves')
    i8 = Ingredient('shallot', 1)
    i9 = Ingredient('red thai chile', 1)
    i10 = Ingredient('spring onion', 2)
    i11 = Ingredient('seasame oil', 2, 'tbsp')

    friedRiceSteps = {1: 'mince garlic and shallot. set aside.', 2: 'rough chop spring onion and red chile. set aside.',
                      3: 'crack and wisk egg. set aside.',
                      4: 'heat your wok', 5: 'add seasame oil to wok', 6: 'fry garlic and shallot until fragrent',
                      7: 'add whisked egg and stir',
                      8: 'when egg is almost cooked through, add rice',
                      9: 'add rice, stiring and flattening it constantly', 10: 'add soy sauce. stir',
                      11: 'when rice is almost done, add spring onion and chile. Stir for 30 seconds and serve'}

    friedRice = Recipe('Egg Fried Rice', True, False, True, False, True, 2, 20, [i3, i4, i5, i6, i7, i8, i9, i10, i11], friedRiceSteps,
                       3)

    iF12 = FridgeIngredient('rice', 1, 100, 'cup')
    iF4 = FridgeIngredient('soy sauce', 2, 100, 'tbsp',)
    iF5 = FridgeIngredient('eggs', 1, 10)
    iF6 = FridgeIngredient('sugar', 1, 100, 'tbsp',)
    iF7 = FridgeIngredient('garlic', 4, 10, 'cloves',)
    iF8 = FridgeIngredient('shallot', 1, 10)
    iF9 = FridgeIngredient('red thai chile', 1, 10)
    iF10 = FridgeIngredient('spring onion', 2, 10)
    iF11 = FridgeIngredient('seasame oil', 2, 10, 'tbsp')

    testFridge.addItem(iF12)
    testFridge.addItem(iF4)
    testFridge.addItem(iF5)
    testFridge.addItem(iF6)
    testFridge.addItem(iF7)
    testFridge.addItem(iF8)
    testFridge.addItem(iF9)

    #testFridge.checkForIngredients(friedRice)


    tom = Ingredient('tomato', 5)
    eg = Ingredient('egg', 5)
    o = Ingredient('oil', 1, 'tbsp')
    g = Ingredient('garlic', 1, 'tbsp')
    s = Ingredient('sugar', 2, 'tsp')
    sa = Ingredient('salt', 1, 'tsp')

    tAndESteps = {1: 'Cut the tomatoes into 3-5cm long pieces',
                  2: 'Stir the eggs and pan fry till it becomes a egg pancake, then put aside',
                  3: 'Put oil in pan and throw the chopped garlic to get the flavor',
                  4: 'Put tomatoes in, smash and stir till the juices come out',
                  5: 'Put eggs in and use spatula to cut into small pieces (similar size with the tomatoes) and mix the two well',
                  6: 'Put a good amount of sugar (two teaspoons) and salt (one) and stir everything'}

    tAndE = Recipe('Tomatoes and Eggs', True, False, True, True, True, 1, 0, 15, [tom, eg, o, g,s, sa], tAndESteps)

    tomF = FridgeIngredient('tomato', 5,10)
    egF = FridgeIngredient('egg', 5,10)
    oF = FridgeIngredient('oil', 1,100, 'tbsp')
    gF = FridgeIngredient('garlic', 1,10, 'tbsp')
    sF = FridgeIngredient('sugar', 2,100, 'tsp')
    #No salt in the fridge


    #print(tAndE.printRecipeIngredients())
    #print(testFridge.checkForIngredients(tAndE))

    testFridge.addItem(tomF)
    testFridge.addItem(egF)
    testFridge.addItem(oF)
    testFridge.addItem(gF)
    testFridge.addItem(sF)
    #print(testFridge.checkForIngredients(tAndE))

    berry = Ingredient('berry', 1, 'cup')
    green = Ingredient('spinach', 1)
    powder = Ingredient('powder', 1, 'scoop')

    smoothie = Recipe('smoothie', True, True, True, True, True, 1, 0, 5, [berry, green, powder], {1:'did you check neethma'})

    BF = FridgeIngredient('berry', 3, 100, 'cup')
    PF = FridgeIngredient('powder', 10, 100, 'scoop')

    testFridge.addItem(BF)
    testFridge.addItem(PF)


    listOfRecipes = [pbAndJ,tAndE, cereal, smoothie]


    print(testFridge.fractionOfIngredients(pbAndJ))
    print(testFridge.fractionOfIngredients(tAndE))
    print(testFridge.fractionOfIngredients(cereal))
    print('end of fraction\n')
    r = testFridge.recommendation(listOfRecipes)

    print('\nbegin of results')
    for i in r:
        print(i.name)