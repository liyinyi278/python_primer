# 练习 6.6：调查 
#   在 6.3.1 节编写的程序 favorite_languages.py中执行以下操作。
#   创建一个应该会接受调查的人的名单，其中有些人已在字典中，
#   而其他人不在字典中。遍历这个名单。对于已参与调查的人，打印一条消息表示感谢；
#   对于还未参与调查的人，打印一条邀请参加调查的消息。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jane': 'java',
    'tom': 'c++',
    'lucy': 'python',
    'jack': 'java',
    'peter': 'c',
    'lily': 'ruby',
    }

# 创建一个应该会接受调查的人的名单
for name in ['jen', 'sarah', 'edward', 'phil', 'jane', 'tom', 'lucy', 'jack', 'peter', 'lily', 'david', 'mike']:
    if name in favorite_languages:
        print("Thank you for participating in the survey, " + name.title() + ".")
    else:
        print("Dear " + name.title() + ", we invite you to participate in the survey.")
