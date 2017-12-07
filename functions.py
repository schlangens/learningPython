def hows_the_parrot():
    print("He's pining for the fjords!")

hows_the_parrot()


def  lumberjack(name):
    if name.lower() == 'kenneth':
        print("Kenneth's a lumberjack, and he's okay!")
    else:
        print("{} sleeps all night and {} works all day".format(name, name))

lumberjack("Kenneth")
lumberjack("Bob")


def average(num1, num2):
    return (num1+num2) / 2

print(average(2, 8))
