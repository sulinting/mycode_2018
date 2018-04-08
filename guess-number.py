# _*_ Coding:utf-8 _*_

import random
answer = random.randint(1,10)
print('猜数字游戏')
num = input('请输入你猜测的数字\n')
guess = int(num)
n = 0
while n<2:
    if guess == answer and n == 0:
        print('么么哒。对啦')
        print('厉害了一次就对了')
        break
    if guess < answer:
        print('不对哦，太小了')
    elif guess > answer:
        print('不对哦，太大了')
    elif guess == answer:
        print('么么哒，对啦')
    num = input('请你重新输入\n')
    guess = int(num)
    n = n+1
    if n == 1 and guess == answer:
        print('可以哦，第二次就对了')
        break
    elif n == 2 and guess == answer:
        print('还行，终于猜出来了')
        break
    elif n==2 and guess !=answer:
        print('不行哦，三次都不对')
        break
print('游戏结束')
