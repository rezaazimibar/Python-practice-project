# --------------------builtin methods--------------------

# my_str = "hello it's me and my name is Reza"

# print(f"length of the my_str:\"{len(my_str)}\"")
# print(my_str[2:9:1])
# print(f"upper in the my_str:\"{my_str.upper()}\"")
# print(f"find 's in the my_str:\"{my_str.find('\'s')}\"")

# ----------------------enter data--------------------------

# birthday = input("enter your age:")
# print(f"your age is: {birthday}")
# name = input("enter your name:")
# print(f"your name is: {name}")

# -----------------------exercise one------------------------

userName = input("your user name is:")
password = input("enter your password:")
passwordLong = '*' * len(password)
unknownPassword = password.replace(password,passwordLong)

print(f'''{userName} 
your password \"{unknownPassword}\" is {len(password)} letters long''')

