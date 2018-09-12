score =float(input("Please enter your score:"))
if score >= 90 and score<=100:
    print("Your score is A.")
elif score >= 60 and score<90 :
    print("Your score is B.")
elif score <60 and score >= 0:
    print("Your score is C.")
elif score>100 or score<0:
    print("Error!")

