class Laptop:
    def build(self):
        print("Laptop builds")

class Desktop:
    def build(self):
        print("Desktop builds")  

class Tablet:
    def open_pdf(self):
        print("Tablet opens pdf")

class Alien:
    def code(self,machine:Laptop):
        print("Alien building")
        machine.build()

asus=Laptop()
dell=Desktop()
lenovo_tab=Tablet()

gowtham=Alien()
gowtham.code(asus)                  