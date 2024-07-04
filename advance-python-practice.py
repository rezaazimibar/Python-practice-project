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

# for item in "hi my name is reza":
#     print(item)

# for set_item in (1,3,4,5,6,7):
#     print(set_item)

# for tuple_item in {3,5,1,6,7}:
#     for list_item in ["hi",True,343,"my god"]:
#         print(f"inner loop: {tuple_item,list_item}")
#         print(tuple_item,list_item)

#--------------------------------------iterable-----------------------------

# #iterable can be set list dictionary tuple string
# #it mean you looping over the something
# myDict={"name":"reza","age":34,"single":True}

# for key,value in myDict.items():
#     # key,value=item; instead we can modify up
#     print(key,value)

# for item in myDict.values(): #we can use key to show key
#     print(item)
#----------------------------------------exercise--------------------------------

# my_list=[1,2,3,4,5]

# total=0
# for item in my_list:
#     total=total +item
#     print(total)

# print(total)

#-----------------------------------------range-()----------------------------------

# for item in range(0,100,11):
#     print(item)

# for rangeItem in range(100,0,-7):
#     print(set(range(4)))

#-----------------------------------------enumerate-()--------------------------------

# for i,item in enumerate("hi reza how are you man"):
#     print(i,item)

# #fun exercise
# for i, item in enumerate(list(range(100))):
#     if item ==50:
#         print(f"the index of fifty is: {i}")

#------------------------------------------while-loop-----------------------------------

# i=0
# while i<50:
#     print(i)
#     i +=1
# else:
#     print("job is done")

# while True:
#     print("infinite loop bread")
#     break       #so important if it is not we have infinite loop that dangerous

# while True :
#     result= input("say something: ")
#     if result=="goodbye":
#       break

#----------------------------------break-continue-pass-----------------------------

# for item in "hi my name is reza":
#     print("i love you and continue")
#     continue #go to the up first of the loop
#     print("hi there")
#     pass #do nothing

#---------------------------------------exercise--------------------------------------

# picture=[
#     [1,1,1,0,1,1,1],
#     [1,0,1,1,0,0,1],
#     [1,0,1,1,0,0,1],
#     [1,0,1,1,0,0,1],
#     [1,0,1,1,0,0,1],
#     [1,0,1,1,0,0,1],
#     [1,0,1,1,0,0,1],
#     [1,0,1,1,0,0,1],
# ]

# for item in picture:
#     for items in item:
#         if items:
#             print("*",end='')
#         else:
#             print(' ',end='')    
#     print('')

#---------------------------------------exercise-----------------------------------

# some_list=['b','d','g','e','d','a','a']
# my_list=[]

# for items in some_list:
#     if some_list.count(items)>1:
#         if items not in my_list:
#             my_list.append(items)

# print(my_list)

#-----------------------------------functions---------------------------------------

# def say_hello():
#     print("hello")

# say_hello()
# print(say_hello())

# def say_inParameter(name,favor): #parameter
#     print(f"hi {name} and you are the best in {favor}")


# say_inParameter("reza","basketball") #position arguments

# #default parameters that allow us to give them default value
# def logic_method(name='no name',age='2',License='False  '): 
#     if age>18 and License=="yes":
#         print(f"mr/mss {name} you can drive thats ok")
#     elif age>18 or License=="yes":
#         print(f"sorry dude you can not drive")
#     else:
#         print("you and play with your toys")
#     return -1

# name=input("your name is: ")
# age=int(input("your age is: "))
# lice=input("do you have license: ")

# #key word argument that allow us to give argument in disorder way
# print(logic_method(name=name,age=age,License=lice))

#---------------------------------return---------------------------------------

def Sumer(x1,x2):
    z=x1+x2
    return z

print(Sumer(32,Sumer(10,10)))

def outerFunc(num1,num2):
    def innerFunc(n1,n2):
        return n1+n2
    return innerFunc(num1,num2)

print(outerFunc(2,2))
