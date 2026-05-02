#Program Variables
count = 1
x = "Fizz"
y = "Buzz"
z = "Fizzbuzz"

#Playing the Game
while count < 1001:
    if count % 15 == 0:
        print(z)
    elif count % 5 == 0:
        print(y)
    elif count % 3 == 0:
        print(x)
    else: 
        print(count)
    count = count + 1
