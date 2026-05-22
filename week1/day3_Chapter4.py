#Exercise 6 for Chapter 4

# def computepay(hours,rate) :
#     if overtime > 0:
#         Pay = ((40) * float(rate)) + (overtime * float(rate) * 1.5)
#     else:
#         Pay = float(hours) * float(rate)
#     return Pay
# try:
#     hours = input("Enter Hours: ")
#     rate = input("Enter Rate: ")
#     overtime = float(hours) - 40
#     x = computepay(hours,rate)
#     print("Pay:",x)
# except:
#     print("You must input a number")

#Exercise 7 for Chapter 4

def computegrade(score) :
    if score < 0.0 or score > 1.0:
        return "Bad Score"
    elif score >= 0.9 :
        return "A"
    elif score >= 0.8 :
        return "B"
    elif score >= 0.7 :
        return "C"
    elif score >= 0.6 :
        return "D"
    elif score < 0.6:
        return "F"
try:
    rawScore = float(input("Enter Score: "))
    grade = computegrade(rawScore)
    print(grade)
except:
    print("Bad score")
