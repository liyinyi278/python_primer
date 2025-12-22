# 函数可返回任何类型的值，包括列表和字典等较为复杂的数据结构。

# 在函数定义中，新增了一个可选形参 age，
# 其默认值被设置为特殊值None（表示变量没有值）。
# 可将 None 视为占位值。在条件测试中，None 相当于 False。
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
