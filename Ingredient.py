class Ingredient:

    def __init__(self, name, quantity, unit='None'):

        # Constructor (String name, Int/Float Quantity, Unit (if available))

        # make sure name is a string
        try:
            self.name = name.lower()
        except:
            raise Exception('The name of an ingredient must be a string')

        # make sure quantity in a number
        try:
            q = float(quantity)
            self.quantity = q
        except:
            raise Exception('The quantity of an ingredient must be a number')

        # make sure unit is a string
        try:
            self.unit = unit.lower()
        except:
            raise Exception('The unit of an ingredient\'s quantity  must be a string')


    # add a quantity of the ingredient
    def add_quantity(self, newQuantity):
        # convert_Unit()
        self.quantity += newQuantity

    # remove a quantity of the ingredient
    def remove_quantity(self, newQuantity):
        # convert_Unit()
        self.quantity -= newQuantity

    def convert_unit(self, unit):
        if self.unit == 'None' or self.unit == unit:
            return
        quantity = self.quantity
        dryWeights = ['gram', 'kilogram', 'pound', 'ounce']
        wetWeights = ['gallon', 'quart', 'pint', 'cup', 'fluid ounce', 'tablespoon', 'teaspoon', 'liter', 'milliliter']
        if self.unit in dryWeights and unit in dryWeights:
            if self.unit == 'kilogram':
                quantity *= 1000
            elif self.unit == 'pound':
                quantity *= 453.592
            elif self.unit == 'ounce':
                quantity *= 28.3495

        elif self.unit in wetWeights and unit in wetWeights:
            if self.unit == 'liter':
                quantity *= 1000
            elif self.unit == 'cup':
                quantity *= 240
            elif self.unit == 'pint':
                quantity *= 473
            elif self.unit == 'quart':
                quantity *= 946.4
            elif self.unit == 'gallon':
                quantity *= 3785
            elif self.unit == 'fluid ounce':
                quantity *= 29.574
            elif self.unit == 'tablespoon':
                quantity *= 14.787
            elif self.unit == 'teaspoon':
                quantity *= 4.929
        else:
            raise Exception('Ingredient unit incompatible: Different ingredient units detected')

        self.unit = unit
        if self.unit in dryWeights:
            if self.unit == 'kilogram':
                quantity /= 1000
            elif self.unit == 'pound':
                quantity /= 453.592
            elif self.unit == 'ounce':
                quantity /= 28.3495

        elif self.unit in wetWeights:
            if self.unit == 'liter':
                quantity /= 1000
            elif self.unit == 'cup':
                quantity /= 240
            elif self.unit == 'pint':
                quantity /= 473
            elif self.unit == 'quart':
                quantity /= 946.4
            elif self.unit == 'gallon':
                quantity /= 3785
            elif self.unit == 'fluid ounce':
                quantity /= 29.574
            elif self.unit == 'tablespoon':
                quantity /= 14.787
            elif self.unit == 'teaspoon':
                quantity /= 4.929
                quantity = round(quantity, 3)
        self.quantity = quantity