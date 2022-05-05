class Adder:

    def __init__(self, data=[]):
        self.data = data

    def __add__(self, other):
        return self.add(self.data, other)

    def add(self, x, y):
        return f'Not Implemented'


class ListAdder(Adder):

    def add(self, x, y):
        return x + y


class DictAdder(Adder):

    def add(self, x, y):
        add_dict = {}
        for k in x.keys():
            add_dict[k] = x[k]

        for k in y.keys():
            add_dict[k] = x[k]
        return add_dict
