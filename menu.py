import sys

menu_list = ["1. do something cool", "2. be cool", \
"3. get outta da way"]

def menu() :
    """
    return the menu header as a string
    """
    menu = "What would you like to do today?\n"
    for v in menu_list :
        menu += " " + v + "\n"
    #menu_list = ["list"]
    return menu
    
def get_input(r) :
    """
    r is a reader
    
    return the input as an integer
    """
    x = r.readline()
    return int(x)
    
def selection(x) :
    """
    x is the integer index for the menu_list
    
    return the item inside the menu_list that the user selected
    """
    return menu_list[x]
    
print menu()
print selection(get_input(sys.stdin) - 1) # zero base it