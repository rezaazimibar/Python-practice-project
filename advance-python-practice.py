#--------------------------------conditional-logic------------------------------------
# is_old=False
# is_young=True

# if is_old:
#     print("yes you can drive!!!")
# elif is_young:
#     print("you can run it")
# else:
#     print("you can't drive")

#-------------------------------ternary-operator---------------------------------------

# is_that_myfriend=True
# ternary_value="yes his my friend"if is_that_myfriend else "no he is not my friend"

# print(f"is he my friend: {ternary_value}")

#-------------------------------Logical-operator-------------------------------------

# if True and True:
#     print("it's used from and operator") 

# print(f"use logical operator: {3<4<6<7<40>=40!=800}")
# print(f"use not to show True: {not True}")

#--------------------------------Exercise---------------------------------------------

# is_magician=False
# is_expert=True

# if is_magician and is_expert:
#     print("you are a master magician")
# elif is_magician and not is_expert:
#     print("at least you are getting there")
# else :
#     print("you need magic powers")

#-----------------------------------------is-equal-==---------------------------------

# print(f"is 1 equal to True: {True==1}")
# print(f"is 1 super equal to True: {True is 1}")
# print(f"is 1 equal to '': {''==1}")
# print(f"is 1 equal to []: {[]==1}")
# print(f"is 10 equal to 10.0: {10==10.0}")
# print(f"is 10 super equal to 10.0: {10 is 10.0}")
# print(f"is [] equal to []: {[1]==[1]}")
# print(f"is [] super equal to []: {[1] is [1]}")
# #super equal check place store and type

#------------------------------------------for-loop-------------------------------------

for item in "hi my name is reza":
    print(item)
for set_item in (1,3,4,5,6,7):
    print(set_item)

for tuple_item in {3,5,1,6,7}:
    for list_item in ["hi",True,343,"my god"]:
        print(f"inner loop: {tuple_item,list_item}")
