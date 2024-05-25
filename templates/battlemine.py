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
            window.playSelectAudio() 
            print(my_ships)
            document["s" + button_id[1:]].style.visibility = "visible"
            if len(my_ships) == 3:
                global computer_ships
                remaining_coordinates = [coord for coord in coordinates if coord not in my_ships] # Computer chooses 3 from remaining coordinates
                while True:
                    random_indexes = [window.getRandomInt(0, len(remaining_coordinates) - 1) for _ in range(3)] # Randomly chooses
                    computer_ships = [remaining_coordinates[i] for i in random_indexes]  # Populate computer_ships
                    if not has_duplicates(computer_ships):
                        break  

                print("My Ships:", my_ships)
                print("Computer Ships:", computer_ships)
                document['fire'].style.visibility = "visible"
        else:
            print("Coordinate already selected")  # No duplicate coordinates
    else:
        print('Max coordinates chosen')  # Only up to 3 coordinates
def flicker_image(element_id, duration, interval):
    def toggle_visibility():
        element = document[element_id]
        if element.style.visibility == 'hidden':
            element.style.visibility = 'visible'
        else:
            element.style.visibility = 'hidden'
    end_time = window.Date.now() + duration
    def flicker():
        if window.Date.now() < end_time:
            toggle_visibility()
            window.setTimeout(flicker, interval)
        else:
            document[element_id].style.visibility = 'hidden'  # Ensure it's hidden at the end
    flicker()

def my_turn(event):
    global my_score, player_turn  
    button_id = event.target.id
    window.playClickAudio() 
    document["terminal2aMiss"].style.visibility = "hidden"
    document["terminal2aHit"].style.visibility = "hidden"
    document["terminal2aIncoming"].style.visibility = "visible"
    if button_id in coordinates and button_id not in my_ships:
        if button_id in computer_ships:
            document["cell" + button_id[1:].replace('_', '') + "g"].style.visibility = "visible"
            print("You HIT")
            window.playGreenAudio() 
            my_score += 1
            document["terminal2aMiss"].style.visibility = "hidden"
            document["terminal2aIncoming"].style.visibility = "hidden"
            document["terminal2aHit"].style.visibility = "visible"
            if my_score == 3:
                print("YOU WON!")
                document["won"].style.visibility = "visible"
                return
        else:
            print("You Missed")
            window.setTimeout(lambda: flicker_image("terminal1aIncoming", 1570, 70), 1000)  # Delay by 1 second
            document["terminal2aHit"].style.visibility = "hidden"
            document["terminal2aIncoming"].style.visibility = "hidden"
            document["terminal2aMiss"].style.visibility = "visible"
        player_turn = False  # Switch to computer's turn
        window.setTimeout(computer_turn, 2500)  # Call computer's turn after 2 seconds
def computer_turn():
    global computer_score, player_turn  # Declare global variables
    chosen_coordinate = None
    while not chosen_coordinate:
        random_index = window.Math.floor(window.Math.random() * len(coordinates))
        chosen_coordinate = coordinates[random_index]
        if chosen_coordinate not in my_ships and chosen_coordinate not in computer_ships:
            chosen_coordinate = None
    
    if chosen_coordinate in my_ships:
        document["cell" + chosen_coordinate[1:].replace('_', '') + "r"].style.visibility = "visible"  # Show the red image
        print("Computer Hit")
        document["terminal2aMiss"].style.visibility = "hidden"
        document["terminal2aIncoming"].style.visibility = "hidden"
        document["terminal2aHit"].style.visibility = "visible"
        window.playRedAudio() 
        computer_score += 1
        if computer_score == 3:
            print("COMPUTER WON!")
            document["lost"].style.visibility = "visible"
            return
    else:
        document["terminal2aHit"].style.visibility = "hidden"
        document["terminal2aMiss"].style.visibility = "hidden"
        document["terminal2aIncoming"].style.visibility = "visible"
        print("Computer Missed")
        document["terminal2aHit"].style.visibility = "hidden"
        document["terminal2aIncoming"].style.visibility = "hidden"
        document["terminal2aMiss"].style.visibility = "visible"
        window.playClickAudio() 
    player_turn = True  

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
    document[button_id].bind('mouseover', lambda event: window.playComputeAudio())
document['fire'].bind('click', next)

# audio volume up
# glowing effect / minimize on click for Fire at Will
# infographics/overlays
#hover over/enlarge opening buttons