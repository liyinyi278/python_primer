# 在用单引号引起的字符串中包含撇号，这将导致错误。
# 解决办法：使用双引号来包围字符串，或者使用反斜杠对撇号进行转义。
#   也可以用单引号来包围字符串，并在字符串内部使用双引号。
# 如下所示：
message = "one of Python's strengths is its diverse community."
print(message)

# message = 'One of Python's strengths is its diverse community.'
# print(message)

# 以上代码将导致如下错误提示：
#   File "apostrophe.py", line 1
#       message = 'One of Python's strengths is its diverse community.'
# SyntaxError: unterminated string literal (detected at line 1)