class SizesUISizer:
    def __init__(self, x: float, y: float):
        self.x = x * 2
        self.y = y * 2
        self.geo = f"{self.x}x{self.y}"

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def Geo(self) -> str:
        return self.geo

class Win:
    def __init__(self, isShown: bool):
        self.isUIShown = isShown

    def isEnabled(self) -> bool:
        if self.isUIShown:
            return True

        return False
