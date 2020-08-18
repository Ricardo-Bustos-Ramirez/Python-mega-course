user_input = input("Enter your name: ")
message_1 = "Hello %s!" % user_input    # This works for both Python 2 and 3
message_2 = f"Hello {user_input}"       # New way for Python 3.6
print(message_1)
print(message_2)