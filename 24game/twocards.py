"""
class TwoCards deal with only two cards
"""


class TwoCards:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.operations = ['+', '-', '*', '/']
        self.psb = []
        self.equa = []

    # enumerate all the arithmetical combinations of num1 and num2
    def perm(self):
        for operation in self.operations:
            for op in ['+', '-']:
                try:
                    self.psb.append(eval(op + str(self.num1) + operation + str(self.num2)))
                    self.equa.append("(" + op + str(self.num1) + operation + str(self.num2) + ")")

                except ZeroDivisionError:
                    pass
        for op in ['+', '-']:
            try:
                self.psb.append(eval(op + str(self.num2)) / eval(str(self.num1)))
                self.equa.append("(" + op + str(self.num2) + '/' + str(self.num1) + ")")
            except ZeroDivisionError:
                pass
        return self.psb, self.equa


if __name__ == "__main__":
    again = 'y'
    while again == 'y':
        num_1 = input("Enter an integer:")
        num_2 = input("Enter an integer:")
        obj = TwoCards(num_1, num_2)
        obj.perm()
        print(obj.perm())
        again = input("Again?")
