class Robot:
    # class variable contains population robots
    population = 0

    def __init__(self, name):
        """Init data."""
        self.name = name
        print('(Init {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        print('{0} delete!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was the last.'.format(self.name))
        else:
            print('We have {0:d} robots for work.'.format(Robot.population))

    def say_hi(self):
        print("Welcome! My owners call me {0}.".format(self.name))

    def how_many():
        print('We have {0:d} robots.'.format(Robot.population))

    how_many = staticmethod(how_many)


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()
droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print("\nHere, robots can do it some works.\n")

print("All robots finished works. We can kill they.")
del droid1
del droid2

Robot.how_many()
