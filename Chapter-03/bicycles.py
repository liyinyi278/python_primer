bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

# Python 为访问最后一个列表元素提供了一种特殊语法。
# 通过将索引指定为-1，可让 Python 返回最后一个列表元素：
# -1 表示最后一个元素，-2 表示倒数第二个元素，以此类推。
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)