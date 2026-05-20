#Exercise 1 for Chapter 3

#hours = input("Enter hours: ")
#rate = input("Enter Rate: ")
#overtime = float(hours) - 40
#if float(hours) > 40 :
#    Pay = (overtime * (float(rate) * 1.5)) + (float(hours) - overtime) * float(rate)
#else :
#   Pay = float(hours) * float(rate)
#print("Pay:",Pay)

#Exercise 2 for Chapter 3

#hours = input("Enter Hours: ")
#rate = input("Enter Rate: ")
#try:
#    overtime = float(hours) - 40
#    if float(hours) > 40 :
#        Pay = (overtime * (float(rate) * 1.5)) + (float(hours) - overtime) * float(rate)
#    else:
#        Pay = float(hours) * float(rate)
#    print("Pay:",Pay)
#except:
#    print("Error, Please enter a numeric input")

#Exercise 3 for Chapter 3

#raw_score = input("Enter score: ")
#try:
    #score = float(raw_score)
    #if score >= 0.95 and score <= 1.0 :
    #    print("A")
    #elif score >= 0.8 and score < 0.95 :
    #    print("B")
    #elif score >= 0.7 and score < 0.8 :
    #    print("C")
    #elif score >= 0.6 and score < 0.7 :
    #    print("D")
    #elif score < 0.6 :
    #    print("F")
    #else :
    #    print("Please input a number in the range between 0.0 upto 1.0")
#except:
#    print("Bad score")