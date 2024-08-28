#reference game created by ai that i will use to reference specifics

def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself at a crossroads in a dark forest.")
    print("Do you want to go left or right?")
    
    choice = input("Type 'left' or 'right': ").strip().lower()
    
    if choice == 'left':
        go_left()
    elif choice == 'right':
        go_right()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        start_adventure()

def go_left():
    print("You chose the left path.")
    print("After walking for a while, you encounter a wise old man.")
    print("He offers you two options: a shiny key or a mysterious map.")
    print("Do you take the key or the map?")
    
    choice = input("Type 'key' or 'map': ").strip().lower()
    
    if choice == 'key':
        take_key()
    elif choice == 'map':
        take_map()
    else:
        print("Invalid choice. Please type 'key' or 'map'.")
        go_left()

def go_right():
    print("You chose the right path.")
    print("Suddenly, you find yourself at the edge of a deep, dark chasm.")
    print("There is a narrow bridge across the chasm.")
    print("Do you cross the bridge or go back?")
    
    choice = input("Type 'cross' or 'back': ").strip().lower()
    
    if choice == 'cross':
        cross_bridge()
    elif choice == 'back':
        start_adventure()
    else:
        print("Invalid choice. Please type 'cross' or 'back'.")
        go_right()

def take_key():
    print("You chose the key.")
    print("The old man smiles and tells you that the key will open a hidden door.")
    print("You find a hidden door nearby and use the key to unlock it.")
    print("Congratulations! You've found the treasure room and won the game!")

def take_map():
    print("You chose the map.")
    print("The old man says the map will guide you to a hidden treasure.")
    print("You follow the map and find a chest filled with gold.")
    print("Congratulations! You've found the treasure and won the game!")

def cross_bridge():
    print("You decide to cross the bridge.")
    print("Halfway across, the bridge starts to shake!")
    print("You make it to the other side safely and find a beautiful garden.")
    print("Congratulations! You've found a magical place and won the game!")

# Start the game
start_adventure()
