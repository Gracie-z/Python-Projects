"""
This program deals with the situation where three cards are present.
It first find all the possible combinations of two out of the three numbers recursively,
using class TwoCards; then treats the outcome as one number and sends the remaining one to class TwoCards
again.
"""

from twocards import TwoCards


class ThreeCards:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.psb = []
        self.equa = []

    # combinations of picking two numbers out of four
    def perm_three(self):
        return (self.num1, self.num2), (self.num2, self.num3), (self.num3, self.num1)

    # using class TwoCards to generate all the results of the two numbers
    def get_psb_two(self, n1, n2):
        self.psb_tem, self.equa_tem = TwoCards(n1, n2).perm()
        for item in self.equa_tem:
            self.equa.append(item)
        for item in self.psb_tem:
            self.psb.append(item)

    # treats the previous result as one single number and sends it back, along with the third number,
    # to class TwoCards again
    def generate_psb(self):
        for args in self.perm_three():
            self.get_psb_two(*args)
        self.psb = []
        for num in self.equa[:10]:
            self.get_psb_two(num, self.num3)
        self.equa = self.equa[10:]
        for num in self.equa[:10]:
            self.get_psb_two(num, self.num1)
        self.equa = self.equa[10:]
        for num in self.equa[:10]:
            self.get_psb_two(num, self.num2)
        self.equa = self.equa[10:]
        return self.psb, self.equa


if __name__ == '__main__':
    num1 = input("Enter an integer:")
    num2 = input("Enter an integer:")
    num3 = input("Enter an integer:")
    x = ThreeCards(num1, num2, num3)
    x.generate_psb()
    #print(set(x.psb))


