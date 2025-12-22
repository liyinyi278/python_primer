# def：定义函数
# """显示简单的问候语"""：是称为文档字符串（docstring）的注释，用于解释函数是做什么的。
# Python 在为程序中的函数生成文档时，会查找紧跟在函数定义后的字符串。

def greet_user():
    """显示简单的问候语"""
    print("Hello!")

greet_user()

def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# 在同一个文件中，定义同名函数，后面的函数会覆盖前面的函数
# greet_user()，会运行错误。