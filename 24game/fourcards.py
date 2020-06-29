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
        self.psb_1 = []
        self.equa_1 = []
        self.psb_2 = []
        self.equa_2 = []

    def perm_two_two(self):
        return ((self.num1, self.num2), (self.num3, self.num4)), ((self.num1, self.num3), (self.num2, self.num4)), \
               ((self.num1, self.num4), (self.num2, self.num3))

    def generate_psb_2(self):
        for pair in self.perm_two_two():
            num1_obj = TwoCards(*pair[0])
            num2_obj = TwoCards(*pair[1])
            num1_psb, num1_equa = num1_obj.perm()
            num2_psb, num2_equa = num2_obj.perm()
            for num1 in num1_equa:
                for num2 in num2_equa:
                    num = TwoCards(num1, num2)
                    num_psb, num_equa = num.perm()
                    for item in num_equa:
                        self.equa_2.append(item)
                    for item in num_psb:
                        self.psb_2.append(item)

    # Treat 4 numbers as 3+1 and send the first three numbers to class ThreeCards
    def perm_four(self):
        L = [self.num1, self.num2, self.num3, self.num4]
        for i in range(4):
            M = L[:]
            del M[i]
            obj = ThreeCards(*M)
            self.psb_temp, self.equa_temp = obj.generate_psb()
            for item in self.psb_temp:
                self.psb_1.append(item)
            for item in self.equa_temp:
                self.equa_1.append(item)
            self.equa_temp = []
            self.psb_temp = []

    # treat the previous result as one single number and sends it to class TwoNumbers
    # along with the remaining integer
    def get_psb_two(self, n1, n2):
        self.psb_tem, self.equa_tem = TwoCards(n1, n2).perm()
        for item in self.equa_tem:
            self.equa_1.append(item)
        for item in self.psb_tem:
            self.psb_1.append(item)

    def generate_psb(self):
        self.perm_four()
        a = int(len(self.equa_1) / 4)
        print(a)
        # print(len(self.equa_1))
        # print(len(self.psb_1))
        self.psb_1 = []
        for num in self.equa_1[:a]:
            self.get_psb_two(num, self.num1)
        # print(len(self.psb_1))
        # print(len(self.equa_1))
        self.equa_1 = self.equa_1[a:]
        # print(len(self.equa_1))
        for num in self.equa_1[:a]:
            self.get_psb_two(num, self.num2)
        # print(len(self.equa_1))
        # print(len(self.psb_1))
        self.equa_1 = self.equa_1[a:]
        # print(len(self.equa_1))
        for num in self.equa_1[:a]:
            self.get_psb_two(num, self.num3)
        # print(len(self.equa_1))
        # print(len(self.psb_1))
        self.equa_1 = self.equa_1[a:]
        # print(len(self.equa_1))
        for num in self.equa_1[:a]:
            self.get_psb_two(num, self.num4)
        # print(len(self.equa_1))
        # print(len(self.psb_1))
        self.equa_1 = self.equa_1[a:]
        return self.psb_1, self.equa_1

    # check the arithmetical combinations that yield 24
    def check(self):
        if 24 in self.psb_1 or 24 in self.psb_2:
            print("It works!")
            # L = [i for i, value in enumerate(obj.psb_1) if value == 24]
            # for i in L:
            # print(obj.equa_1[i])
            if 24 in self.psb_1:
                i = self.psb_1.index(24)
                print(self.equa_1[i])
            if 24 in self.psb_2:
                i = self.psb_2.index(24)
                print(self.equa_2[i])

        else:
            print("Fails")


if __name__ == '__main__':
    a = []
    for i in range(4):
        num = input("Enter an integer:")
        a.append(num)
    obj = FourCards(*a)
    obj.generate_psb()
    obj.generate_psb_2()
    print(len(obj.psb_1))
    print(len(obj.equa_1))
    obj.check()
