#  training #1
# user = int(input("say me a number"))
#
# item = ""
# for i in range(1, user * 2 + 1, 3):
#     item = item + " " + str(i)
# print(item)

# training #2
user = int(input("how many numbers do you wanna?"))
counter = 0
total = 0
for answer in range(user):
    counter = counter + 1
    collecting = int(input("what is number " + str(counter) + "? "))
    total = total + collecting
print(total)