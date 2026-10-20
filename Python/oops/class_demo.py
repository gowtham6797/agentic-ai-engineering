class human:
    def walk(self):
        print("walking...")


gowtham = human()
gowtham.walk()


class computer:
    brand = "Lenovo"

    def __init__(self, cpu, ram, ssd):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self):
        print("config:", self.cpu, self.ram, self.ssd)

    @classmethod
    def info(cls):
        return cls.brand

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024**3)


comp1 = computer("i7", "16GB", "1TB")
comp2 = computer("i9", "96GB", "2TB")

comp1.config()
comp2.config()

print(computer.info())
print(computer.gb_to_bytes(16))
