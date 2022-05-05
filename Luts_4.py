class Attrs:
    def __getattr__(self, myattr):
        print(f"get = {myattr}")

    def __setattr__(self, myattr, value):
        print(f"get = {myattr},{myattr}")


a = Attrs()
a.append
a.new = 2
a[1]
print(a.__dict__)

