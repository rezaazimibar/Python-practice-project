# --------------------builtin methods-----------------------------------

# my_str = "hello it's me and my name is Reza"

# print(f"length of the my_str:\"{len(my_str)}\"")
# print(my_str[2:9:1])
# print(f"upper in the my_str:\"{my_str.upper()}\"")
# print(f"find 's in the my_str:\"{my_str.find('\'s')}\"")

# ----------------------enter data---------------------------------------

# birthday = input("enter your age:")
# print(f"your age is: {birthday}")
# name = input("enter your name:")
# print(f"your name is: {name}")

# -----------------------exercise one-------------------------------------

# userName = input("your user name is:")
# password = input("enter your password:")
# passwordLong = "*" * len(password)
# unknownPassword = password.replace(password, passwordLong)

# print(
#     f"""{userName}
# your password \"{unknownPassword}\" is {len(password)} letters long"""
# )

# --------------------------List------------------------------------------

# li1 = [23, "yellow", True]
# print(li1[2])
# print(len(li1))

# li2 = ["headphone", "phone", "mouse", "keyboard"]
# li2[0] = "laptop"

# print(f"my second list is; {li2[::2]}")

# ---------------------------matrix---------------------------------------

# myMatrix = [[1, 0, 1, 0], [1, 0, 1, 1], [1, 0, 0, 0], [1, 1, 1, 0]]

# print(f"My matrix is: {myMatrix[2][1]}")

# --------------------------List method-------------------------------------

# # adding method
# myNewList = ["apple", 343, False, "orange"]
# appendList = myNewList.append("USA")  #return none
# InsertList = myNewList.insert(2, "chine")  #return none
# extendList = myNewList.extend([343, 3232])  #return none

# print(f"my append list is: {appendList}")
# print(f"my append list is: {myNewList}")

# # removing method
# secondList = ["Iran", "Iraq", "quieti"]
# popList = secondList.pop(0)     #return value
# removeList = secondList.remove("Iraq")  # return none

# print(f"removing list is: {secondList}")
# print(f"pop value is: {popList}")

# countries=["Germany","Italy","Canada","USA","UAE","China"]

# print(f"use in method to know something exist in array :{"Germany" in countries} ")
# print(f"index of one country is: {countries.index("China")}")
# print(f"count how many item in array: {countries.count("China")}")

# cities=["Tehran","Hamburg","Loa Angeles","A", "Las Vegas","New York City"]
# cities.sort()

# print(f"sort of array is{cities}")

    
# print("3".join(["hel","low","my","dear"]))

# #produce List
# print(f"produce a list:{list(range(100,150))}")

#-------------------------------Dictionary-----------------------------------------------

# amazonList={"pen":2,'bag':3,}
# innerListDic=[
#     {
#         "li1":[3,2,1],
#         "bol":True,
#         "str":"my str"

#     },
#     {
#         "li2":[3,7,1],
#         "bol0":True,
#         "str":"my str"

#     },
#     {
#         "li3":[8,2,1],
#         "bol":True,
#         "str":"my str"

#     }
# ]

# print(f"dictionary value is: {amazonList['bag']}")
# print(f"inner document: {innerListDic[1]["li2"][1]}")

# #dictionary key
# dictionary1={
#     232:"this is the number ",
#     True:[34,23,"bool key"]
# }

# print(f"using number and bool key: {dictionary1[232]}")

#-------------------------------------Dictionary method-------------------------------

dictBasket={
    "trash":20,
    "accident":True,
    "password":"hello world"
}
builtDict=dict(name="john")

print(f"use get method: {dictBasket.get("tractor")}")
print(f"use get method: {dictBasket.get("trash",2000)}")
print(f"build a dictionary: {builtDict}")