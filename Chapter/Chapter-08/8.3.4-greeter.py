# 可将函数与本书前面介绍的所有 Python 结构结合起来使用。
# 例如，下面将结合使用 get_formatted_name() 函数和 while 循环，
# 以更正规的方式问候用户。

# 测试数据：eric matthes
# 测试数据：gretchen hughes

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")