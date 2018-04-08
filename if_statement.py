#coding=utf-8


# age = int(input('请输入您的年龄：'))
# if age>=18:
#     print ("我年轻力壮")
# elif age>=6:
#     print('我还是个孩子')
# elif age>=0:
#     print('我还是个小宝宝')
# else:
#     print ("我不是人")


#if条件判断语句
#
# age = 18
# sex = 'M'
#
# if sex =='F':
#     print('我是女孩子')
#     if age >= 16:
#         print('二八年华')
#     elif age >= 13:
#         print('豆蔻年华')
#     elif age >= 0:
#         print('我是女宝宝')
# elif sex =='M':
#     print('我不是男孩子')
# else:
#     print('我是大猩猩')


#while循环语句

# age = 0
# while (age < 7):
#     print('我还在',age,"岁，我不上学")
#     age = age + 1
#
# print('我要上学了')


#for循环语句

# companys = ['google','baidu','alli','taobao']
#
# for company in companys:
#     print (company)
#     if company == 'google':
#         print('Google是个不作恶的公司')
#     elif company == 'baidu':
#         print('中国搜索公司')
#     else:
#         print('非搜索引擎公司')

#for循环做乘法口诀(不能换行很好)

# for first_number in range(1,10):
#     for second_number in range(1,first_number+1):
#         print (first_number,'x',second_number,'=',first_number*second_number,)
#     print('\n')




#异常处理

x = 10
y = 2

try:
    result = x/y
except ZeroDivisionError:
    print('除数不能为0')
else:
    print('结果是',result)
finally:
    print('任何情况下都有我的存在')
