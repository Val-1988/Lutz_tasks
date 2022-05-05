class MyList:
    def __init__(self, mylist):
        self.mylist = list(mylist)

    def __add__(self, other):
        return MyList(self.mylist + other)

    def __getitem__(self, other):
        # if isinstance(other, int):
        #     return self.mylist[other] # индексирование
        # else:
        #     return self.mylist[other]  # срез
        return self.mylist[other]

    def append(self, other):
        return self.mylist.append(other)

    def sort(self):
        return self.mylist.sort()

    def __getslice__(self, start, stop):
        return MyList(
            self.mylist[start:stop])  


class MyListSub(MyList):
    calls_number = 0

    def __init__(self, mylist):
        MyList.__init__(self, mylist)
        self.adds_number = 0

    def __add__(self, other):
        print(f"method add with argument {other}")  
        self.adds_number += 1  
        MyListSub.calls_number += 1
        return MyList.__add__(self, other) 

    def call_add_calculator(self):
        return self.adds_number, self.calls_number
