'''
Exercise: Make a cup of coffee
Introduction
In this exercise, you will practice the use of an algorithm to make a cup of instant coffee. The purpose is to lay out the steps required in order to get the final product. 

Instructions
Step 1: Start with the inputs - what is needed to make a cup of instant coffee?

Step 2: Think about all the steps required in the physical aspect of making a cup of instant coffee.

Step 3: Consider the edge cases of optional things like milk or sugar, some people may want it. 

Step 4: The algorithm when complete should have as its final result a cup of coffee.

Tips: Planning is key with any algorithm. Make sure you have all the steps neatly laid out. 
'''    

def main():
    ingredientes = 'Agua quente '
    
    elemento = input('café?')
    if elemento == 'y':
        ingredientes = ingredientes+' ,Cafe'
        
    elemento = input('Leite?')
    if elemento == 'y':
        ingredientes = ingredientes+' ,Leite'
        
    elemento = input('Acucar?')
    if elemento == 'y':
        ingredientes = ingredientes+' ,Acucar'
        
    print('pedido: ',ingredientes)
        
        
main()   