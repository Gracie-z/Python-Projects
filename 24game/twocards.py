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
            try:
                self.psb.append(eval(str(self.num1) + operation + str(self.num2)))
                self.equa.append("("+str(self.num1) + operation + str(self.num2)+")")
            except ZeroDivisionError:
                pass
        try:
            self.psb.append(eval(str(self.num2)) / eval(str(self.num1)))
            self.equa.append("("+str(self.num2) + '/' + str(self.num1)+")")
        except ZeroDivisionError:
            pass
        return self.psb, self.equa

# check whether the two numbers can yield 24 and returns the arithmetics
    def check(self):
        if 24 in self.psb:
            index = [i for (i, value) in enumerate(self.psb) if value == 24]
            print(list(self.equa[i] for i in index))
        else:
            print("NOT POSSIBLE !")


if __name__ == "__main__":
    again = 'y'
    while again == 'y':
        num_1 = input("Enter an integer:")
        num_2 = input("Enter an integer:")
        start_game = TwoCards(num_1, num_2)
        start_game.perm()
        start_game.check()
        print(start_game.perm())
        again = input("Again?")
