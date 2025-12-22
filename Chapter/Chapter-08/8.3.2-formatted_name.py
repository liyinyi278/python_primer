# 有时候，需要让实参变成可选的，
# 以便使用函数的人只在必要时才提供额外的信息。
# 可以使用默认值来让实参变成可选的。

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 在调用这个函数时，如果只想指定名和姓，调用起来将非常简单。
# 如果还要指定中间名，就必须确保它是最后一个实参，
# 这样 Python 才能正确地将位置实参关联到形参。
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 可选值在让函数能够处理各种不同情形的同时，确保函数调用尽可能简单。
