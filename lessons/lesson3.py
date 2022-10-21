class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.__class__}\n' \
               f'{self.name}'

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}'


c = Cat('Beka', 90)
print(c)


class Poit:
    def __init__(self, *args):
        self.a = args

    def __len__(self):
        return len(self.a)

    def __abs__(self):
        return list(map(abs, self.a))




p = Poit(1, 1, 1, -1, -11, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1111)
print(len(p))
print(abs(p))


class Human:
    head = 1

    def __init__(self, name, age=12):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + ' eating')


class Adahan:
    def __init__(self, mack):
        self.mack = mack

    def learn_to_front(self):
        print(self.mack + " learn_to_front")

    # def eat(self):
    #     print(self.mack + ' eating to Adahan')


class A:...


class Mikhail(Human, Adahan):
    def __init__(self, name, age, mack):
        Human.__init__(self, name, age)
        Adahan.__init__(self, mack)


mih = Mikhail(name='Mikhail', age=12, mack=True, )
print(mih.name, mih.age, mih.mack)
print(mih)
