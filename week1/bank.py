greeting = input("Greeting:" )
lowerGreeting = greeting.lower()
if "hello" in lowerGreeting:
    print("$0")
elif lowerGreeting[0] == "h":
    print("$20")
else:
    print("$100")
