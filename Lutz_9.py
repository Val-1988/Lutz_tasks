class Scene:

    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()


class Customer:

    def line(self):
        print("Thant's one ex-bird")


class Clerk:
    def line(self):
        print("no it isn't...")


class Parrot:
    def line(self):
        print(None)


