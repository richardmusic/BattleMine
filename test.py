from browser import document, window

coordinates = ['_1A', '_1B', '_1C', '_2A', '_2B', '_2C', '_3A', '_3B', '_3C']
my_ships = []
computer_ships = []
my_score = 0
computer_score = 0
player_turn = True  # Flag to track whose turn it is

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def button_click(event):
    if len(my_ships) < 3:    # Populate 3 coordinates in my_ships list
        button_id = event.target.id
        if button_id not in my_ships:
            my_ships.append(button_id)  
            print(my_ships)
            document["s" + button_id[1:]].style.visibility = "visible"
            if len(my_ships) == 3:
                global computer_ships
                remaining_coordinates = [coord for coord in coordinates if coord not in my_ships] # Computer chooses 3 from remaining coordinates
                while True:
                    random_indexes = [window.getRandomInt(0, len(remaining_coordinates) - 1) for _ in range(3)] # Randomly chooses
                    computer_ships = [remaining_coordinates[i] for i in random_indexes]  # Populate computer_ships
                    if not has_duplicates(computer_ships):
                        break  # Exit the loop if all values are unique

                print("My Ships:", my_ships)
                print("Computer Ships:", computer_ships)
                document['fire'].style.visibility = "visible"
        else:
            print("Coordinate already selected")  # No duplicate coordinates
    else:
        print('Max coordinates chosen')  # Only up to 3 coordinates

def my_turn(event):
    global my_score, player_turn  # Declare my_score and player_turn as global
    button_id = event.target.id
    if button_id in coordinates and button_id not in my_ships:
        if button_id in computer_ships:
            document["cell" + button_id[1:].replace('_', '') + "g"].style.visibility = "visible"
            print("You HIT")
            my_score += 1
            if my_score == 3:
                print("YOU WON!")
                return
        else:
            print("You Missed")
        player_turn = False  # Switch to computer's turn
        computer_turn()  # Call computer's turn

def computer_turn():
    global computer_score, player_turn  # Declare global variables
    chosen_coordinate = None
    while not chosen_coordinate:
        chosen_coordinate = window.Math.floor(window.Math.random() * len(coordinates))
        if coordinates[chosen_coordinate] in computer_ships:
            chosen_coordinate = None
    if coordinates[chosen_coordinate] in my_ships:
        print("Computer Hit")
        document["cell" + coordinates[chosen_coordinate][1:].replace('_', '') + "r"].style.visibility = "visible"  # Show the red image
        computer_score += 1
        if computer_score == 3:
            print("COMPUTER WON!")
            return
    else:
        print("Computer Missed")
    player_turn = True  # Switch back to player's turn


def next(event):
    global player_turn
    print("Moving on")
    if player_turn:
        for button_id in coordinates:
            document[button_id].bind('click', my_turn)  # Bind player's turn event handler
        for button_id in coordinates:
            document[button_id].unbind('click', button_click)  # Unbind previous event handler
    else:
        computer_turn()

for button_id in coordinates:
    document[button_id].bind('click', button_click)
document['fire'].bind('click', next)
