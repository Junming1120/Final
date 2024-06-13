import os
import random
import time
import threading

# 初始化变量
snake = [(5, 10), (5, 9), (5, 8)]
direction = "RIGHT"
food = (10, 20)
score = 0
game_over = False

# 打印游戏界面
def print_game():
    global game_over
    os.system("cls" if os.name == "nt" else "clear")
    for y in range(20):
        for x in range(40):
            if (y, x) in snake:
                print("O", end="")
            elif (y, x) == food:
                print("X", end="")
            else:
                print(" ", end="")
        print()
    print(f"Score: {score}")
    if game_over:
        print("Game Over!")

# 更新蛇的位置
def update_snake():
    global game_over, score, food
    head = snake[0]
    if direction == "UP":
        new_head = (head[0] - 1, head[1])
    elif direction == "DOWN":
        new_head = (head[0] + 1, head[1])
    elif direction == "LEFT":
        new_head = (head[0], head[1] - 1)
    elif direction == "RIGHT":
        new_head = (head[0], head[1] + 1)

    # 检查游戏结束条件
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= 20 or
        new_head[1] < 0 or new_head[1] >= 40):
        game_over = True
        return

    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = (random.randint(0, 19), random.randint(0, 39))
    else:
        snake.pop()

# 获取用户输入
def get_input():
    global direction
    while not game_over:
        key = input()
        if key in ["w", "a", "s", "d"]:
            if key == "w" and direction != "DOWN":
                direction = "UP"
            elif key == "s" and direction != "UP":
                direction = "DOWN"
            elif key == "a" and direction != "RIGHT":
                direction = "LEFT"
            elif key == "d" and direction != "LEFT":
                direction = "RIGHT"

# 主游戏循环
def main():
    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    while not game_over:
        update_snake()
        print_game()
        time.sleep(0.3)

    print_game()
    input_thread.join()

if __name__ == "__main__":
    main()
