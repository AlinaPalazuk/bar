from datetime import datetime


TIME_FORMAT = '%m.%d.%Y, %H:%M:%S'


class Bar:
    def __init__(self):
        self.operations = []
        self.drinks = {
            'wine': 3,
            'beer': 6,
            'rum': 11,
        }

    def add_operation(self, name, amount, op_type):
        self.operations.append(
            {
                'name': name,
                'quantity': amount,
                'type': op_type,
                'time': datetime.now(),
            }
        )

    def get_drinks(self, name, amount):
        if name not in self.drinks:
            return (False, False)
        if self.drinks[name] >= amount:
            self.drinks[name] -= amount
            self.add_operation(name=name, amount=amount, op_type='sale')
            return (True, True)
        return (True, False)

    def supply(self, name, amount):
        if name in self.drinks:
            self.drinks[name] += amount
        else:
            self.drinks[name] = amount
        self.add_operation(name=name, amount=amount, op_type='arrival')

    def print_operations(self):
        for operation in self.operations:
            print(
                operation['name'],
                operation['quantity'],
                operation['type'],
                operation['time'].strftime(TIME_FORMAT),
            )

bar = Bar()

print('Hello! What drink do you want?')
while True:
    present, available = bar.get_drinks(
        name=input('name: '),
        amount=int(input('How many?  '))
    )
    if present:
        if available:
            print('Here you are!')
        else:
            print("Sorry, we don't have this much")
    else:
        print("Sorry, we don't have it")
    if input("something else?(y/n)\n") == "n":
        break

if input('\nDo you need a product delivery? y/n  ') == 'y':
    print('What do we need?')
    bar.supply(name=input('name: '), amount=int(input('How many?  ')))
else:
    print('Ok, next time')

bar.print_operations()
