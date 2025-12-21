# for 循环是一种遍历列表的有效方式，但不应该在 for 循环中修改列表，
# 否则将导致 Python 难以跟踪其中的元素。
# 要在遍历列表的同时修改它，可使用 while 循环。
# 通过将 while 循环与列表和字典结合起来使用，可收集、存储并组织大量的输入，供以后查看和使用。

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print()
