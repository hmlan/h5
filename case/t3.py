list=[1,23,6,9,112,45,36]
list.sort()
print(list)
list.reverse()
print(list)
l=[10*x for x in list if x<20]
print(l)
t=[[x,5*x] for x in list]
print(t)
a=1,2,3,4
print(a)
b=a,(2,4,8)
print(b)
basket={'s','s','g','g','f','f'}
print(basket)
m=set("allladdllll")
print(m)
n=set("kkshlll")
print(m-n)
tel={"username":"may","password":123456}
tel["yanzhengma"]=3333
print(tel)
print(tel.keys())
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print('What is your {0}?  It is {1}.'.format(q, a))