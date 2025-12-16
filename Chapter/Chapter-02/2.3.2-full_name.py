first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# rstrip()​ 是字符串对象的内置方法，
# 用于移除字符串末尾（右侧）的指定字符（默认为空白字符）。
# 它返回一个新字符串，原始字符串不会被修改（字符串不可变）。
favorite_language = 'python '
print(favorite_language.rstrip())

# removeprefix()​ 是字符串对象的方法（Python 3.9+ 新增），
# 用于移除字符串开头（左侧）的指定前缀。
# 如果字符串以给定前缀开头，则移除该前缀；否则返回原字符串。
# 不匹配时不修改字符串（与 lstrip()有本质区别）

# 示例：s = "aaaHello"
#   removeprefix()  精确匹配整个前缀字符串                          s.removeprefix("aa")→ "aHello"
#   lstrip()        移除开头所有在字符集合中的字符（不要求连续匹配）   s.lstrip("a")→ "Hello"
nostarch_url = 'https://nostarch.com/'
simple_url = nostarch_url.removeprefix('https://') 
print(simple_url) 