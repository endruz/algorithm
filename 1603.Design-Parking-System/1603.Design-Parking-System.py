class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.maxBig = big
        self.maxMedium = medium
        self.maxSmall = small
        self.bigCount = 0
        self.mediumCount = 0
        self.smallCount = 0


    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigCount < self.maxBig:
                self.bigCount += 1
                return True
            else:
                return False
        elif carType == 2:
            if self.mediumCount < self.maxMedium:
                self.mediumCount += 1
                return True
            else:
                return False
        elif carType == 3:
            if self.smallCount < self.maxSmall:
                self.smallCount += 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)