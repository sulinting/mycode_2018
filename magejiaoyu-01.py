#encoding: utf-8

import random

rand_num = random.randint(1,100)

max_guess_count = 5
guess_count = 0

while True:
    guess_num = int(input('请输入您的游戏数字：'))
    guess_count = guess_count + 1

    if guess_num == rand_num:
        print('恭喜您，猜对了')
        break
    elif guess_num < rand_num:
        print('您输入的数字小了')
    else :
        print('您输入的数字大了')
    if guess_count >= max_guess_count:
        print('你太笨了',max_guess_count,'都猜不对，正确数字是：',rand_num)

    else :
        print('剩余猜测机会还有：',max_guess_count - guess_count,'了，加油哦')








