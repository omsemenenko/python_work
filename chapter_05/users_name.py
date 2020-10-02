current_users = ['ivan', 'konni', 'edward', 'sarah', 'jaden']
new_users = ['john', 'poul', 'sam', 'jim', 'edward']

for new_user in new_users:
    if new_user in current_users:
        print("Please, select new name.")
    else:
        print("You can use this name.")

