user_name = input ("enter a name to store in a file or enter to proceed :  ")
if user_name:
    with open ('user_info.txt', 'a') as file :
       file.write(user_name + "\n")

show_info = input("do you want to see all user names? y/n :  ")
if show_info=='y':
    try:
        with open ('user_info.txt', 'r') as file :
            content = file.readlines()
    except Exception as e :
        print (e, type(e)) 
    else :
       for line in content :
        print (f'{line.rstrip()}')
        