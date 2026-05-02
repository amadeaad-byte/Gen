# Create a list called names_i_like.
# A list is used to store multiple values in one place.
names_i_like = ["Thomson", "Thompson", "Haddock", "Snowy"]

# Start the internal_iterator at 0.
# This will be used to keep track of the position in the list.
internal_iterator = 0

# Keep looping while the current position exists in the list.
# len(names_i_like) gives the number of items in the list.
while internal_iterator < len(names_i_like):
    # Print the sentence and the current name in the list.
    print("I like this name: " + names_i_like[internal_iterator])

    # Add 1 to internal_iterator so the program moves to the next name.
    internal_iterator = internal_iterator + 1

#for yourself - enhance this program to ask the user what name they liked, and allow them to make a profile for their character.
#asking the user what name they like from the list
print("so, which out of those name do you like?")
user_name = input("choose a name")
if user_name == list(names_i_like):
    print("So you like " + user_name + ". Is that right?")