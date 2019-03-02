
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay = self.pay * (1 + percent)

    def __repr__(self):
        return '[Person %s %s %s}' % (self.name, self.job, self.pay)


class Manager(Person):
        def __init__(self, name, pay):
            Person.__init__(self, name, 'mgr', pay)

        def giveraise(self, percent, bonus=.10):
            Person.giveraise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay='120000')
    tom = Manager('Tom Webster', pay='100000')

    print(bob)
    print(sue)
    print(tom)
