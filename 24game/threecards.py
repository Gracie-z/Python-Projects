from twocards import TwoCards


class ThreeCards:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.psb = []
        self.equa = []

    def perm_three(self):
        return (self.num1, self.num2), (self.num2, self.num3), (self.num3, self.num1)

    def get_psb_two(self, n1, n2):
        self.psb_tem, self.equa_tem = TwoCards(n1, n2).perm()
        #print(self.equa_tem)
        for item in self.equa_tem:
            self.equa.append(item)
        for item in self.psb_tem:
            self.psb.append(item)
        #print(self.equa)

    def generate_psb(self):
        for args in self.perm_three():
            self.get_psb_two(*args)
        self.psb = []
        #print(self.equa[:5])
        for num in self.equa[:5]:
            self.get_psb_two(num, self.num3)
        self.equa = self.equa[5:]
        #print(self.equa)
        for num in self.equa[:5]:
            self.get_psb_two(num, self.num1)
        self.equa = self.equa[5:]
        #print(self.equa)
        for num in self.equa[:5]:
            self.get_psb_two(num, self.num2)
        self.equa = self.equa[5:]
        return self.psb, self.equa


if __name__ == '__main__':
    x = ThreeCards(1, 3, 8)
    x.generate_psb()
    print(x.psb, x.equa)