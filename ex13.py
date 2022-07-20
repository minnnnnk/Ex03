def plus(a,b):
    sum = a+b
    return sum

result = plus(4,7)
print(result)

def sum_and_mul(a, b):
    sum = a+b
    mul = a*b

    return sum, mul


result = sum_and_mul(3,7)
print(result, type(result))

print("===================")
def plusPrint(a=0, b=0):
    print("a=%d, b=%d 이고 합은 %d 입니다." % (a,b, a+b))

plusPrint()
plusPrint(30)
# plusPrint(, 70)  #오류
plusPrint(b=70)
plusPrint(b=100, a=200)

print("===========")
def sum_many(*data):
    sum = 0
    for num in data:
        sum = sum + num
    return sum


print(sum_many(1,2,3,4,5,6,7,8,9,))

print(sum_many(1,2))
print(sum_many(1,2,3))
print(sum_many(1,2,3,4))

print("=========================")
def sum_mul(mode, *args):
    print(mode)
    if mode == "sum":
        result = 0
        for i in args:
            result = result + i
    elif mode == "mul":
        result = 1
        for i in args:
            result = result * i
    else:
        result = "오류"
    return result

print(sum_mul("sum", 1, 2, 3, 4, 5))
print(sum_mul("mul", 2, 3, 7))

print("----------")
def addPerson(hp, **kwargs):
    print(hp)
    print(kwargs)     # 타입 딕션어리

addPerson('010-222-3333', name='황일영', age=28)

print("=============")
def addPerson2(*hp, **kwargs):
    print(hp)       # 타입 튜플
    print(kwargs) # 타입 딕션어리

addPerson2('010-222-3333', name='황일영', age=28)
addPerson2('010-222-3333','02-333-3333', name='황일영', age=28)
addPerson2('010-222-3333','02-333-3333', '02-456-6434', name='황일영', age=28)
