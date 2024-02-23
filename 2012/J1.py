sp = int(input("Enter the speed limit: "))

n = int(input("Enter the recorded speed of the car: "))

diff = n - sp

if diff >= 31:
    f = 500
elif diff >= 21:
    f = 270
elif diff >= 1:
    f = 100
else:
    f = 0

if f == 0:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is ${}.".format(f))