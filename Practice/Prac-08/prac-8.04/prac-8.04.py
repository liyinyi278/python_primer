# 练习 8.4：大号 T 恤 
#   修改 make_shirt() 函数，
#       使其在默认情况下制作一件印有“I love Python”字样的大号 T 恤。
#   调用这个函数分别制作:
#       一件印有默认字样的大号 T 恤，
#       一件印有默认字样的中号 T 恤，
#       以及一件印有其他字样的 T 恤（尺码无关紧要）。

def make_shirt(size = "Large", text = "I love Python"):
    print(f"The size of the shirt is '{size}' and the text on the shirt is '{text}'")

make_shirt()
make_shirt("Medium")
make_shirt(size = "Small", text = "Python is awesome")
make_shirt(text = "Python is great", size = "Extra Large")