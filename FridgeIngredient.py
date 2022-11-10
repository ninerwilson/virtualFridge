class FridgeIngredient:
    def __init__(self, name, quantity, goodFor,unit = 'None'):
        try:
            self.name = name.lower()
        except:
            raise Exception('The name of an ingredient must be a string')

        try:
            q = float(quantity)
            self.quantity = q
        except:
            raise Exception('The quantity of an ingredient must be a number')

        try:
            if type(goodFor) is int:
                self.goodFor = goodFor
        except:
            raise Exception('Ingredient must have shelf life')

        # make sure unit is a string
        try:
            self.unit = unit.lower()
        except:
            raise Exception('The unit of an ingredient\'s quantity  must be a string')

    # store ingredient in fridge. Assuming same goodFor days (if different, create another new FridgeIngredient entry). This uncommented code ignores unit conversion
    def store_quantity(self, quantity):
        self.quantity += quantity

    # take ingredient from fridge
    def take_quantity(self, quantity):
        self.quantity -= quantity

