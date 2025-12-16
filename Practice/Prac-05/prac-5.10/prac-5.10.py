current_users = ['admin', 'Joe', 'Sarah', 'MIKE', 'James', 'Jaden']
new_users = ['joe', 'lilei', 'hanmeimei', 'mike', 'lixiaolong']

lower_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print("Sorry, " + new_user + " is already taken.")
    else:
        print("Welcome, " + new_user + "!")