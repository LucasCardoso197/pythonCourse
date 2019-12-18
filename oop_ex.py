class Line():
    def __init__(self, coord1, coord2):
        self.pi = coord1
        self.pf = coord2

    def distance(self):
        return (((self.pi[0]-self.pf[0])**2)+((self.pi[1]-self.pf[1])**2))**(1/2)

    def slope(self):
        return (self.pf[1]-self.pi[1])/(self.pf[0]-self.pi[0])


#l = Line((3, 2), (8, 10))
#print(l.distance())
#print(l.slope())

class Cylinder():
    pi = 3.1415

    def __init__(self, height=1, radius=1):
        self.radius = radius
        self.heigh = height

    def volume(self):
        return Cylinder.pi*(self.radius**2)*self.heigh

    def surface_area(self):
        lateral_area = 2*Cylinder.pi*self.radius*self.heigh
        top_area = Cylinder.pi*(self.radius**2)
        return lateral_area+2*top_area

#c = Cylinder(2,3)
#print(f"{c.volume():.2f}")
#print(f"{c.surface_area():.2f}")


class Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return "Account owner:    "+self.name+f"\nAccount balance:  ${self.balance}"

    def deposit(self, value):
        self.balance += value
        print("Deposit accepted")

    def withdraw(self, value):
        if self.balance-value > 0:
            self.balance -= value
            print("Withdraw accepted")
        else:
            print("Withdraw rejected: insuficient funds")

#a = Account('Lucas', 150)
#print(a)
#print(a.name)
#print(a.balance)
#a.deposit(150)
#a.withdraw(100)
#a.withdraw(500)
#print(a.balance)