
class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply_num(self, x, y):
        self.x = x
        self.y = y
        a = self.x * self.y
        return a


    def subtract_num(self, x, y):
        self.x = x
        self.y = y
        a = self.x - self.y
        return a

    def add_num(self, x, y):
        self.x = x
        self.y = y
        a = self.x + self.y
        return a

    def divide_num(self, x, y):
        if (y == 0) or (x ==0):
            a = "You can't divide by zero!"
        else:
            a = self.x / self.y
        return a

go_again = False
while go_again is False:
    x = float(input('Enter your first number: '))
    y = float(input('Enter your second number: '))
    math = Calculator(x, y)
    # # work_out = 1
    # while work_out !=0:
    z = 1

    while z != 0:
        print('''Menu
                1.Multiplication
                2.Subtraction
                3.Add
                4.Division
                  ''')
        z = int(input("what do option do you want to do [1,2,3,4]: "))
        if z in (1, 2, 3, 4):

                if z == 1:
                    print('{} * {} = '.format(x, y))
                    print(math.multiply_num(x, y))
                    break

                elif z == 2:
                    print('{} - {} = '.format(x, y))
                    print(math.subtract_num(x, y))

                elif z == 3:
                    print('{} + {} = '.format(x, y))
                    print(math.add_num(x, y))

                elif z == 4:
                    print('{} / {} = '.format(x, y))
                    print(math.divide_num(x, y))

        else:
            print("Invalid Input, Enter Again")

        next_calculation = input("Wanna do another calculation? (yes/no): ")
        if next_calculation == "Y" or next_calculation == "y":
            # z = 0
            break
            # go_again = True
        elif next_calculation == "N" or next_calculation == "n":
            go_again = True
            z = 0






