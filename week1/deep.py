answer = input("What is the great question to life? ")
lowerAnswer = answer.lower()
okAnswer = lowerAnswer.strip()
if(okAnswer == "42" or okAnswer == "forty-two" or okAnswer == "forty two"):
    print("Yes")
else:
    print("No")
