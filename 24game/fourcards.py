"""
Just like threecards.py, this program gets all possible combinations recursively,
by first using class ThreeCards and then class TwoCards.
Finally, it searches for every single arithmetical combinations that yields 24
"""

from threecards import ThreeCards
from twocards import TwoCards


class FourCards:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.psb = []
        self.equa = []

    # Treat 4 numbers as 3+1 and send the first three numbers to class ThreeCards
    def perm_four(self):
        L = [self.num1, self.num2, self.num3, self.num4]
        for i in range(4):
            M = L[:]
            del M[i]
            obj = ThreeCards(*M)
            self.psb_temp, self.equa_temp = obj.generate_psb()
            for item in self.psb_temp:
                self.psb.append(item)
            for item in self.equa_temp:
                self.equa.append(item)
            self.equa_temp = []
            self.psb_temp = []

    # treat the previous result as one single number and sends it to class TwoNumbers
    # along with the remaining integer
    def get_psb_two(self, n1, n2):
        self.psb_tem, self.equa_tem = TwoCards(n1, n2).perm()
        for item in self.equa_tem:
            self.equa.append(item)
        for item in self.psb_tem:
            self.psb.append(item)

    def generate_psb(self):
        self.perm_four()
        self.psb = []
        for num in self.equa[:75]:
            self.get_psb_two(num, self.num1)
        self.equa = self.equa[75:]
        for num in self.equa[:75]:
            self.get_psb_two(num, self.num2)
        self.equa = self.equa[75:]
        for num in self.equa[:75]:
            self.get_psb_two(num, self.num3)
        self.equa = self.equa[75:]
        for num in self.equa[:75]:
            self.get_psb_two(num, self.num4)
        self.equa = self.equa[75:]
        return self.psb, self.equa

    # check the arithmetical combinations that yield 24
    def check(self):
        if 24 in self.psb:
            print("It works!")
            L = [i for i, value in enumerate(obj.psb) if value == 24]
            for i in L:
                print(obj.equa[i])

        else:
            print("Fails")


if __name__ == '__main__':
    again = 'y'
    while again == 'y':
        a = []
        for i in range(4):
            num = input("Enter an integer:")
            a.append(num)
        obj = FourCards(*a)
        obj.generate_psb()

        obj.check()
        again = input("Again?")
