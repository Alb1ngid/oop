class Kirill:
    head = 1

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Bektur:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return self.age


class Adil(Bektur, Kirill):
    def __init__(self, name, age):
        Kirill.__init__(self, name)
        Bektur.__init__(self, age)

    def __str__(self):
        return f'{self.name} {self.age}'


a = Adil('Adil', '14')
print(a)





