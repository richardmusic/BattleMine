import random, time
coordinates = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
my_score, computer_score = 0, 0
my_ships, computer_ships = [], []
computer_ships = random.sample(coordinates, 3)    
for i in range(3):
    order = ["first", "second", "third"]
    my_ship = input(f"Enter {order[i]} ship location: ")
    my_ships.append(my_ship)
print("Your ship coordinates are: ", my_ships)
while my_score < 3 and computer_score < 3:
        time.sleep(0.7)  # My turn
        print("                        ")
        my_shot = input("  Fire at will! -> ")
        time.sleep(0.4)
        if my_shot in computer_ships:
            my_score += 1
            print(f" 💥💥💥 Hit! 💥💥💥   ")
            if my_score == 3:
                break
        else:
            print(f"     ❌ Missed! ❌   ")
        time.sleep(1.3)
                            
        computer_shot = random.choice(coordinates)  # Computer turn
        print(f" \033[91mComputer fired at {computer_shot}\033[0m")
        time.sleep(0.8)
        if computer_shot in my_ships:
            computer_score += 1
            print(f" 💥💥 Computer hit! 💥💥   \n\033[90m You: {my_score}\033[0m  \033[90m Computer: {computer_score}\033[0m")
            print("\033[90m ____________________\033[0m")
            if computer_score == 3:
                break
        else:
            print(f" ❌ Computer missed! ❌   \n\033[90m You: {my_score}\033[0m   \033[90m Computer: {computer_score}\033[0m")
            print("\033[90m ____________________\033[0m")

time.sleep(0.5)
if my_score >=3:
    print("You sunk 3 ships   🥳🥳🥳 You Won! 🥳🥳🥳")
else:
    print("Computer sunk 3 ships   😡 You Lost! 😡")


"""
Create a grid of coordinates as array of dictionary 5x5Have dictionary choose 3 random coordinates.  Ask my input for my 3 chosen coordinates
Get input from me to choose a coordinate. If my coordinate is the same as one of the computers random coordinates, "Hit", else "Miss".Then computer randomly chooses a coordinate. If that is the same as one of my chosen coordinates then "Hit" otherwise "Miss". If I accumulate 3 Hits then " You win!", if computer accumulates 3 Hits, "Computer wins, you lose", "Game over, try again?"
"""