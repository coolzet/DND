import random


def rnd():
    return int(random.uniform(1, 20))


class DndCheck:
    def __init__(self):

        self.highNumber = 0
        self.lowNumber = 0
        self.mediumNumber = 0
        self.result = 0
        self.countSame = 0

    def generate(self):
        self.subResult = rnd()
        if self.subResult == self.result:
            self.countSame += 1
            while self.countSame > 1:
                self.subResult = rnd()
                if self.subResult != self.result:
                    print("SAMEEEE")
                    self.countSame = 0
        if self.subResult >= 18:
            self.highNumber += 1
        elif self.result <= 3 and self.result != 0:
            self.highNumber += 1
        difference = abs(self.highNumber - self.lowNumber)
        print(difference)
        if difference > 2:
            if self.subResult >= 18:
                self.subResult -= int(random.uniform(3, 8))
                self.highNumber = 0
                self.lowNumber = 0
            elif self.subResult <= 3:
                self.subResult += int(random.uniform(3, 8))
                self.highNumber = 0
                self.lowNumber = 0
            self.result = self.subResult
            print("ultraRARE:", self.result)
        else:
            self.result = self.subResult
            print("casual:", self.result)


if __name__ == "__main__":
    pers = DndCheck()
    pers.generate()
    for i in range(50):
        pers.generate()
