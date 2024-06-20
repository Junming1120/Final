import os
import random
import time
import threading

# Initialize variables
snake = [(5, 10), (5, 9), (5, 8)]  # Initialize the position of the snake with an initial length of 3
direction = "RIGHT"  # The initial direction is to the right
food = (10, 20)  # Initial food location
score = 0  # Initial score
game_over = False  # Game over sign

# Print the game interface
def print_game():
    global game_over
    os.system("cls" if os.name == "nt" else "clear")  ## Clear screen, Windows and Unix compatible
    for y in range(20):  
  
        for x in range(40):  
            if (y, x) in snake:  # If the snake is in its current position
                print("O", end="")  # Print the body of a snake
            elif (y, x) == food:  # If the food is in the current location
                print("X", end="")  # Printing food
            else:
                print(" ", end="")  # Print spaces
        print()  
    print(f"Score: {score}")  
    if game_over:  
        print("Game Over!") 

# Update the snake's position
def update_snake():
    global game_over, score, food
    head = snake[0]  
    if direction == "UP":
        new_head = (head[0] - 1, head[1])  # up
    elif direction == "DOWN":
        new_head = (head[0] + 1, head[1])  # down
    elif direction == "LEFT":
        new_head = (head[0], head[1] - 1)  # left
    elif direction == "RIGHT":
        new_head = (head[0], head[1] + 1)  # right

   
    if (new_head in snake or  # Run yourself down 
        new_head[0] < 0 or new_head[0] >= 20 or  # Hit the up and down wall
        new_head[1] < 0 or new_head[1] >= 40):  # left right
        game_over = True  # game over
        return

    snake.insert(0, new_head)  # Insertion of a new head in the position of the snake's head
    if new_head == food:  # if get food
        score += 1  
        food = (random.randint(0, 19), random.randint(0, 39))  # random food
    else:
        snake.pop() 


def get_input():
    global direction
    while not game_over:  
        key = input() 
        if key in ["w", "a", "s", "d"]: 
            if key == "w" and direction != "DOWN":  #Avoid reverse movement
                direction = "UP"
            elif key == "s" and direction != "UP":
                direction = "DOWN"
            elif key == "a" and direction != "RIGHT":
                direction = "LEFT"
            elif key == "d" and direction != "LEFT":
                direction = "RIGHT"


def main():
    input_thread = threading.Thread(target=get_input)  
    input_thread.start()  # star

    while not game_over:   
        update_snake()  
        print_game()  
        time.sleep(0.3)  # speed of the game

    print_game()  
    input_thread.join() 

if __name__ == "__main__":
    main()  

