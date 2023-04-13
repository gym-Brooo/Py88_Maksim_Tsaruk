import random
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


def fac(x):
    res = 1
    while x > 0:
        res *= x
        x -= 1
    return res


a = 5
print(fac(a))
print(factorial(a))
names = {
    1: "Maksim",
    False: "Vanya",
    (1, 2, 3): 5
}
print(names.get((1, 2, 3)))

new_dict = dict((b,a) for a,b in names.items()) # beautiful
print(new_dict)


def dictionary():
    random_list = [random.randint(1, 100) for i in range(15)]
    num_dict = {}
    for i in range(100):
        if i in random_list:
            num_dict.update({i: random_list.count(i)})
    return num_dict


print(dictionary())






