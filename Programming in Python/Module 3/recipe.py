class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
        
    def contents(self):
        print(str(self.dish) + ' has '+ str(self.items) + ' and takes '+str(self.time)+ ' minutes')
        
        
pizza = Recipe("pizza", ['queijo','massa'],45)
pasta = Recipe("pasta", ['molho','massa'],25)

print(pizza.contents())
print(pasta.contents())