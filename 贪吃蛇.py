import os
import random
import time
import threading

# 初始化变量
snake = [(5, 10), (5, 9), (5, 8)]  # 初始化蛇的位置，初始长度为3
direction = "RIGHT"  # 初始方向为向右
food = (10, 20)  # 初始食物位置
score = 0  # 初始得分
game_over = False  # 游戏结束标志

# 打印游戏界面
def print_game():
    global game_over
    os.system("cls" if os.name == "nt" else "clear")  # 清屏，兼容Windows和Unix
    for y in range(20):  # 遍历行
        for x in range(40):  # 遍历列
            if (y, x) in snake:  # 如果蛇在当前位置
                print("O", end="")  # 打印蛇的身体
            elif (y, x) == food:  # 如果食物在当前位置
                print("X", end="")  # 打印食物
            else:
                print(" ", end="")  # 打印空格
        print()  # 换行
    print(f"Score: {score}")  # 打印当前得分
    if game_over:  # 如果游戏结束
        print("Game Over!")  # 打印游戏结束信息

# 更新蛇的位置
def update_snake():
    global game_over, score, food
    head = snake[0]  # 获取蛇头位置
    if direction == "UP":
        new_head = (head[0] - 1, head[1])  # 向上移动
    elif direction == "DOWN":
        new_head = (head[0] + 1, head[1])  # 向下移动
    elif direction == "LEFT":
        new_head = (head[0], head[1] - 1)  # 向左移动
    elif direction == "RIGHT":
        new_head = (head[0], head[1] + 1)  # 向右移动

    # 检查游戏结束条件
    if (new_head in snake or  # 撞到自己
        new_head[0] < 0 or new_head[0] >= 20 or  # 撞到上下墙
        new_head[1] < 0 or new_head[1] >= 40):  # 撞到左右墙
        game_over = True  # 游戏结束
        return

    snake.insert(0, new_head)  # 在蛇头位置插入新头
    if new_head == food:  # 如果吃到食物
        score += 1  # 得分加1
        food = (random.randint(0, 19), random.randint(0, 39))  # 随机生成新食物
    else:
        snake.pop()  # 否则移除蛇尾，保持长度不变

# 获取用户输入
def get_input():
    global direction
    while not game_over:  # 游戏未结束
        key = input()  # 获取用户输入
        if key in ["w", "a", "s", "d"]:  # 如果输入合法
            if key == "w" and direction != "DOWN":  # 避免反向移动
                direction = "UP"
            elif key == "s" and direction != "UP":
                direction = "DOWN"
            elif key == "a" and direction != "RIGHT":
                direction = "LEFT"
            elif key == "d" and direction != "LEFT":
                direction = "RIGHT"

# 主游戏循环
def main():
    input_thread = threading.Thread(target=get_input)  # 创建线程获取用户输入
    input_thread.start()  # 启动线程

    while not game_over:  # 游戏未结束
        update_snake()  # 更新蛇的位置
        print_game()  # 打印游戏界面
        time.sleep(0.3)  # 控制游戏速度

    print_game()  # 最后打印一次游戏界面
    input_thread.join()  # 等待输入线程结束

if __name__ == "__main__":
    main()  # 运行主程序

