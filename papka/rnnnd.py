import random 

koni_khana = 3
koni_ilyi = 3
counter = 0
my_rnd = 0
user_koni = int(input("Сколько коней вы хотите поставить? "))

while not my_rnd == 100:
    my_rnd = random.randrange(2)
    counter += 1
if my_rnd == 0:
    koni_khana += user_koni
    koni_ilyi -= user_koni
    print("Вы проиграли, у вас осталось", koni_ilyi, "коней")
else:
    koni_khana += -1
    koni_ilyi += 1
    print("Вы выиграли, у вас осталось", koni_ilyi, "коней")
