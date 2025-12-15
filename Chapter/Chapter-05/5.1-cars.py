cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# lower() 方法不会修改存储在变量 car 中的值，
# 因此进行这样的比较不会影响原来的变量.
car = 'Audi'
if car.lower() == 'audi':
    print("True")
print(car)


        