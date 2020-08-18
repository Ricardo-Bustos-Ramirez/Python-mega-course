name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message_1 = "Hello %s %s!" % (name, surname)    # This works for both Python 2 and 3
message_2 = f"Hello {name} {surname}. What's up {when}?"       # New way for Python 3.6

print(message_1)
print(message_2)