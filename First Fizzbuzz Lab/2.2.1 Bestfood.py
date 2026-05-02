# Ask the user to enter a food.
# Whatever the user types will be stored in the variable called food.
food = input("Enter a food: ")

# Check if the value in food is equal to "rice".
# The == symbol means "is equal to".
if food == "rice":
    # If the user typed rice, this line will run.
    print("Yes, rice is the best.")

# If the first condition was false, Python moves to elif.
# elif means "else if".
# This checks if the value in food is equal to "apple".
elif food == "apple":
    # If the user typed apple, this line will run.
    print("Apples aren't my cup of rice.")

# If the user did not type rice and did not type apple,
# Python will run the else block.
else:
    # This line runs for any other food.
    print("Never heard of it!")
