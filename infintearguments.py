                            #infinite arguments
                            #infinite arguments are nothing but passing data/parameters from a list/array

def shoppingcart(*cart):
    for items in cart:
        print("Item you have is", items)


shoppingcart("tomatoes", "onions", "pasta", "carrots")
#the above line is a list which contains the passing arguments