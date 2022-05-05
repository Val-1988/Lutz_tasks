class Super:

    def __str__(self):
        return f"<Instance of {self.__class__.__name__} ({self.__super_name()}), address {id(self)}\n " \
               f"{self.__attrnames()}"

    def __super_name(self):
        names = []
        for x in self.__class__.__bases__:
            names.append(x.__name__)

        return ','.join(names)

    def __attrnames(self):
        res = ''
        for attr in self.__dict__:
            res += f'{(attr, self.__dict__[attr])}'
        return res


class Lister:
    pass


class Sub(Super, Lister):
    def __init__(self):
        self.data = "mySubClass"

