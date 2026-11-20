class Employee:
    def __init__(self, first, last, annual):
        self.first = first
        self.last = last
        self.annual = annual

    def give_raise(self, amt=5_000):
        self.annual = self.annual + amt
