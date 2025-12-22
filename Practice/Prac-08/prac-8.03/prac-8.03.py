# 练习 8.3：T 恤 
#   编写一个名为 make_shirt() 的函数，
#   它接受一个尺码以及要印到 T 恤上的字样。
#   这个函数应该打印一个句子，简要地说明 T 恤的尺码和字样。
#   先使用位置实参调用这个函数来制作一件 T 恤，再使用关键字实参来调用这个函数。

def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text on the shirt is '{text}'.")

make_shirt(24, "I love Python")
make_shirt(size=24, text="I love Python")

