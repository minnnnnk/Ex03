'''
aList = ["고양이", "강아지", "호랑이"]

for  name  in  aList :
    print(name)
'''

friendList = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]

for friend in friendList :
    print("이름:", friend[0], ", 나이:", friend[1])

print("=============================")
for name, age in friendList :
    print("이름:%s, 나이:%d"%(name,age))
print("-----------------------------")
for name, age in friendList:
    print("이름:{0} , 나이:{1}".format(name,age))