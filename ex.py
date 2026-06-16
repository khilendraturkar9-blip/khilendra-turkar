# try:
#     num = int(input("enter the nambur"))
#     print(10/num)
# except ZeroDivisionError:
#     print("dont divide with zero")
# except ValueError:
#     print("type nambur only ")


# f = open ("text.txt","w")
# f.write("hello world")
# f.close()
# print("File Created !")

# f= open("text.txt","r")
# constant = f.read()
# print(constant)
# f.close()

# f = open ("text.txt","a")
# f.write("\n new line added")
# f.close()
# print("data added")
# # the modern , recommended way 
# with open ("student.txt","w")as f:
#     f.write("rahul - 85\n")
#     f.write("vaibhav- 60\n")
#     f.write("aditya - 70\n")
# print("student saved")

# jsan api
# import requests

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)
# data = response.json()

# for user in data:
#     print(f"Name: {user['name']} - Email: {user['email']}")


fruits = ["apple","banana","mango"]

fruits.append("orange")#Add at end
print(fruits)

fruits.insert(1,"grapes")#add at position
print(fruits)

fruits.remove("banana")#remove by value
print(fruits)

fruits.pop(2)#remove list
print(fruits)

print(len(fruits))#length
print(fruits.sort())#sort


