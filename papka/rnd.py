import random 

counter = 0
my_rnd = 0

while not my_rnd == 100:
    my_rnd = random.randrange(101)
    counter += 1
    if my_rnd == 100:
        print("Выпало 100, это заняло", counter, "итераций")
		