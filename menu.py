import sys

menu_list = ["1. do something cool", "2. be cool", \
"3. get outta da way"]

response_list = ["   Do something cool?", "   Be cool?", \
"   Get outta da way?"]

def menu_header() :
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
    
def get_response(x) :
    """
    x is the integer index for the response_list
    
    return the item inside the response_list that the user selected
    """
    return response_list[x]
    
def menu() :
    """
    the driver for the menu
    """
    print menu_header()
    input = get_input(sys.stdin)
    input -= 1 # zero base it
    print get_response(input)
    if input == 1 :
        print "You chose " + selection(input)
    elif input == 2 :
        print "   Back off, punk!"
    
    
    
menu()