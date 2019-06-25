# print("hello python")
# def add_1(func):
#     def add1():
#         return "1+ " + func()
#     return add1
#
# @add_1
# def hello():
#     return "hello"
#
# print(hello())
# aList = (line for line in open('a.txt'))
# aList = (i.split() for i in aList if i.split())
# aList = (map(int, i) for i in aList)
# aList = [sum(i) for i in aList]
# print(list(aList))
# print(sum(aList))
#
# squared ={ x**2 for x in [1,2,3]}
# print(squared)
# aSet = set("123423141")
# print(aSet)


# from matplotlib import pyplot
#
# # pyplot.show([1,2,3,4,5],{"apple":1, "orange":2})
# pyplot.title("Matplotlib demo")
# pyplot.show()

# gcount = 0
#
# def global_test():
#     global gcount
#     gcount += 1
#     print (gcount)
# global_test()

import pygame  # 导入pygame库
from pygame.locals import *  # 导入pygame库中的一些常量
from sys import exit  # 导入sys库中的exit函数

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# 初始化游戏
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 初始化一个用于显示的窗口
pygame.display.set_caption('This is my first pygame-program')  # 设置窗口标题

# 事件循环(main loop)
while True:

    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()