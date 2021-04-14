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

    def get_drinks(self, name, amount):
        if name in self.drinks and self.drinks[name] > amount:
            self.drinks[name] -= amount
            print('Here you are!')
            sale_drinks = {
                'name': name,
                'quantity': amount,
                'type': 'sale',
                'time': datetime.now(),
                }
            self.operations.append(sale_drinks)
        elif name in self.drinks and self.drinks[name] < amount:
            print('Sorry, We don"t have enough')
        else:
            print('Sorry, we don"t have it. Something else?')

    def supply(self, name, amount):
        if name in self.drinks:
            self.drinks[name] += amount
            arrival_drinks = {
                'name': name,
                'quantity': amount,
                'type': 'arrival',
                'time': datetime.now(),
                }
            self.operations.append(arrival_drinks)
        else:
            self.drinks[name] = amount
            arrival_drinks = {
                'name': name,
                'quantity': amount,
                'type': 'arrival',
                'time': datetime.now(),
                }
            self.operations.append(arrival_drinks)

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
bar.get_drinks(name=input('name: '), amount=int(input('How many?  ')))

if input('\nDo you need a product delivery? y/n  ') == 'y':
    print('What do we need?')
    bar.supply(name=input('name: '), amount=int(input('How many?  ')))
else:
    print('Ok, next time')

bar.print_operations()
