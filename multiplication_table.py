#coding:utf8

# x = 'spam'
# while x:
#     print(x,end=' ')
#     x = x[1:]


# x = 10
# while x:
#     x = x-1
#     if x % 2 !=0:
#         continue
#     print(x,end = ' ')



# while True:
#     name = input('请输入名字：')
#     if name =='stop':
#         break
#     age = input('请输入年龄：')
#     print('Hello',name,'=>',int(age)**2)
#     break


#
# for x in ['spam','eggs','ham']:
#     print(x,end=' ')





# sum = 0
# for x in[1,2,3,4]:
#     sum = sum + x
#     print (sum,end=' ')
#




# prod = 1
# for item in [1,2,3,4]:
#     prod *= item
#     print(prod,end=' ')
#

# pi = 3.1415926
# r= 10
# print('hello world')
# #计算10厘米员的周长
# print(2*pi*r)
# #计算10厘米圆的面积
# print(pi *r*r)
# #加法运算
# print('100+2=',100+2)
# #减法运算
# print('1-5=',1-5)
# #乘法运算
# print('5*6=',5*6)
# #除法运算
# print('9/4=',9/4)


#input函数使用
# name = input('请输入你的名字：')
# print('你输入的名字是：',name)

# height = 1.71
# age = 26
# weight = 110
# score = 5.5
# pi = 3.1415926
# negative = -1
#
# print(height)
# print(age)
# print(weight)
# print(score)
# print(pi)
# print(negative)
#

# name = input('请输入您的名字：')
# age = input('请输入您的年龄：')
# print('我的名字是：'+ name + '我的年龄是：' + age)
#


# #要求用户输入数字语句
# i = (input('请输入第一个数字：'))
# j = (input('请输入第二个数字：'))
# #将用户输入的str转换为int
# i = int(i)
# j = int(j)
# #将用户输入的两个数字进行数学运算
# print(i, '+', j, '=', i + j)
# print(i, '-', j, '=',i - j)
# print(i, '*', j, '=',i * j)
# print(i, '/', j, '=',i / j)

# is_boy = True
# is_girl = False
# print(is_boy,is_girl)
#
# print(type(is_boy))
# print(type(is_girl))


# print(True or False)
# print(True or True)
# print(False or True)
# print(False or False)
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)



# print(True + True)
# print(True - True)
# print(True - False)
# print(True * True)
# print(True / True)

# print(int(True))
# print(int(False))
#
# print(float(True))
# print(float(False))
#
# print(str(True))
# print(str(False))


# print(bool(1))
# print(bool(0))
# print(bool(1.0))
# print(bool(0.0))
# #非空、非0的字符串转换为bool都是True
# #bool类型只会把0、0.0、‘’空，转换为False，其它都为True
# print(bool('False'))
#




#关系运算>  < <= >= !=

# print(1==2)
# print(1!=2)
# print(1>=2)
# print(1<=2)



#if语句

# print('>>>买一斤包子')
#
# show = input('你看到西瓜了吗？')
#
# if show == '看到了':
#     print('>>>买一个西瓜')

# show =input('你看到西瓜了吗？')
#
# if show == '看到了':
#     print('>>>买一个包子')
# else:
#     print('>>>买一斤包子')

# i = input('请输入分数：')
# score = int(i)
#
# if score >= 90:
#     print('优秀学生')
# elif score >= 80:
#     print('成绩良好')
# elif score >= 60:
#     print('及格')
# elif score < 60:
#     print('不及格')
# else :
#     print('您输入的不是分数')



# year = input('请输入当前年份：')
# year = int(year)
# i = year % 4
# j = year % 100
# p = year % 400
#
# if (i == 0) and j != 0:
#     print('这是一个闰年')
# elif p == 0:
#     print('这是一个闰年')
# else:
#     print('这不是一个闰年')




#利用while循环求和1-100

# index = 1
# index_sum = 0
#
# while index <= 100:
#     index_sum = index_sum + index
#     index = index + 1
#
# print(index_sum)



# text = input('请输入一个数字或输入exit结束程序')
#
# input_sum = 0
# input_count = 0
#
# while text != 'exit':
#     input_sum = float(text) + input_sum
#     input_count = input_count + 1
#     text =  input('请输入一个数字或输入exit结束程序')
#
# if input_count == 0:
#     print('sum:0 ,avg:0')
# else:
#     print('sum:',input_sum,'avg:',input_sum / input_count)


# index = 0
#
# while index <= 5:
#     index = index + 1
#     if index == 3:
#         break
#     print(index)




# index = 0
#
# while index <= 5:
#     index = index + 1
#     if index == 3:
#         continue
#     print(index)

#for循环遍历列表元素
#
# users = ['lynn','jon','iron','leon']
# for user in users:
#     print(user)

#作业
#1、文件名称使用python变量名命名规则
#2、while,if ,else,elif 后面的表达式可以不适用（）保护
#3、变量名先定义再使用（在使用的同一级或者在前N级）
#4、缩进：tab和空格，不要混用，copy到其它操作系统上会有问题
#5、





#打印乘法口诀

# nums = [1,2,3,4,5,6,7,8,9]
# count = 1
#
# for num in nums:
#     product = num * count
#     count=count + 1
#
#     print(num,'*',count,'=',product,'',end='')
#

#打印乘法口诀

# row = 1
#
# while row <= 9 :
#     col = 1
#     while col <= 9:
#         if row >= col:
#             print(row,'*',col,'=',row * col,end='\t')
#         col = col + 1
#     row = row + 1
#     print('')
#




# import random
#
# rand_num = random.randint(0,100)
#
# max_guess_count = 5
# guess_count = 0
#
# while True:
#     guess_num = input('请输入游戏数字：')
#     guess_num = int(guess_num)
#     guess_count = guess_count + 1
#
#     if rand_num == guess_num:
#         print('你猜对了')
#         break
#     elif rand_num < guess_num:
#         print('你猜大了')
#     else:
#         print('你猜小了')
#
#     if guess_count >= max_guess_count:
#         print('你真笨',max_guess_count,'次都没猜对，正确值是：',rand_num)
#         break
#     else:
#         print('剩余猜测机会：',max_guess_count - guess_count,'次')
#


#列表的遍历及修改

# users = ['lynn','leon','jon','marry']
#
# users[0] = 'jerry'
#



#用for遍历range函数做乘法口诀
#
# for row in range(1,10):
#     for col in range(1,row + 1):
#         print(row,'*',col,'=',row * col,end='\t')
#     print()

#从Nums中找出最大的数字
#方法
#1、从Numszhong 拿到第一个数到变量hand中
#2、从nums第二个元素开始比较，如果比hand中大，则重新赋值

#方法
#0、hand手里没有值
#1、从Numszhong 拿到第一个数到变量hand中
#2、从nums第二个元素开始比较，如果hand是none或者比hand中大，则重新赋值




#
# nums = [6,11,7,9,4,2,1]
#
# for j in range(len(nums) - 1):
#
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             temp = nums[i]
#             nums[i] = nums[i + 1]
#             nums[i + 1] = temp
#     print(nums)
# print(nums)





#todolist知识点

'''
1.存储所有的任务用List ,tasks
2、while
3、input
4、输入非do，append
       do，按照先进先出原则
       （检查lisp是否为空，为空则打印无任务退出）
       把任务弹出pop(0),并打印
'''

tasks = []

# while True:
#     input_text = input('please input do or a task:')
#     if input_text != 'do':
#         tasks.append(input_text)
#     else:
#         if len(tasks) ==0:
#             print('无任务')
#             break
#         else:
#             task = tasks.pop(0)
#             print('任务是：',task)
#


#找出两个列表里面相同的数字放到新的列表里面
#1、定义list存放结果
#result = 【】
#2、遍历一个list，判断是否在另一个list中，如果存在相同元素则放到新的列表result中

# nums_1 = [1,2,3,4,5,3,10,11]
# nums_2 = [1,2,3,1,4,5,5,3,12,34]
#
# result = []
#
# for num in nums_1:
#     if num in nums_2 and num not in result:
#         result.append(num)
# print(result)



#字典

# languages = ['python','java','python','c','c++','go','c#','c++','lisp','c','javascript','java','python','matlab','python','go','c','java','c#']
#
#
# stat_dict = {}
#
# for language in languages:
#     if language not in stat_dict:
#         stat_dict[language] = 1
#     else:
#         stat_dict[language] = 1 + stat_dict[language]
# print(stat_dict)
#




artcle = ["I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complan, for their disease is contagious. Le."]

stat_dict = {}

for ch in artcle:
    stat_dict[ch] = stat_dict.get('ch',0) + 1
print(stat_dict)

















































