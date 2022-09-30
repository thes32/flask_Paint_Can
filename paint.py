class PaintCans:
    def __init__(self,name,color,type,sizes,prices,area):
        self.name = name
        self.color = color
        self.type = type
        self.sizes = sizes
        self.chosenSize = 0
        self.prices = prices
        self.chosenPrice = 0
        self.area = area

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getType(self):
        return self.type

    def getSizes(self):
        return self.sizes

    def getSize(self):
        return self.chosenSize

    def getPrices(self):
        return self.prices

    def getPrice(self):
        return self.chosenPrice

    def getArea(self):
        return self.area

    def setSize(self,indicator):
        self.chosenSize = self.sizes.split('/')[indicator]
