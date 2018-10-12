# print("hello,world")
# a='zhangsan'
# print("我的名字叫%r"%a)
# n=input("请输入你的内容:")
# print("你输入的内容时:%r"%n)
s = 0
for i in range(1,100):

    s=s+i
print(s)
dict={"usename":"Humaolan","password":"123455"}
# dict.values()
# dict.keys()
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# for key,values in dict.items():
# #     print(key,values)
# # import time
# # print(time.ctime()
# aa=0
# try:
#     open("a.txt",'r')
#     print(aa)
# except Exception as msg:
#     print(msg)
from random import randint
n=randint(1,10)
if n%2==0:
    raise NameError("%d is even"%n)
else:
    raise NameError("%d is odd"%n)
