# 函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。
# 函数返回的值称为返回值。
# 在函数中，可以使用 return 语句将值返回到调用函数的那行代码。
# 返回值让你能够将程序的大部分繁重工作移到函数中完成，从而简化主程序。

def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)