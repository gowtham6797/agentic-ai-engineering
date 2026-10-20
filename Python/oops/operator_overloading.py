class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} : {self.balance}"

    def __add__(self, other):
        return Account(self.name + " " + other.name, self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance


acc1 = Account("Gowtham", 5000)
acc2 = Account("Tara", 4000)

print(acc1)
print(acc2)
print(acc1 + acc2)

if acc1 > acc2:
    print(f"{acc1.name} pays the bill")
else:
    print(f"{acc2.name} pays the bill")
