#Exercise 1 for Chapter 5

# count = 0
# total = 0
# average = None
# while True:
#     try:
#         text = input("Enter a number: ")
#         if text == "done":
#             break
#         num = int(text)
#     except:
#         print("Invalid input")
#         continue
#     total = total + num
#     count = count + 1
# if count > 0:
#     average = total / count
# print("Total:",total,"Count:",count,"Average:",average)
 
#Exercise 2 for Chapter 5
# largest = None
# smallest = None
# while True:
#     try:
#         text = input("Enter a number: ")
#         if text == "done":
#             break
#         num = int(text)
#     except:
#         print("Invalid input try again")
#         continue
#     if largest is None or largest < num:
#         largest = num
#     if smallest is None or smallest > num:
#         smallest = num
# print("Maximum:",largest ,"Minimum:",smallest)