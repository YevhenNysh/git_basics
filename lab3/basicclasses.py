class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'{self.name} ({self.weight} грамів)'


class Berry(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.name} ({self.weight} грамів)'


class Apple(Fruit):
    def __init__(self, name, weight, variety):
        super().__init__(name, weight)
        self.variety = variety

    def __repr__(self):
        return f'{self.variety} {self.name} ({self.weight} грамів)'


class Citrus(Fruit):
    def __init__(self, name, weight, taste):
        super().__init__(name, weight)
        self.taste = taste

    def __repr__(self):
        return f'{self.taste} {self.name} ({self.weight} грамів)'


class Orange(Citrus):
    def __init__(self, name, weight, taste, origin):
        super().__init__(name, weight, taste)
        self.origin = origin

    def __repr__(self):
        return f'{self.taste} {self.name} ({self.weight} грамів) з {self.origin}'


class Grapefruit(Citrus):
    def __init__(self, name, weight, taste, color):
        super().__init__(name, weight, taste)
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.taste} {self.name} ({self.weight} грамів)'


class Strawberry(Berry):
    def __init__(self, name, weight, color, taste):
        super().__init__(name, weight, color)
        self.taste = taste

    def __repr__(self):
        return f'{self.color} {self.taste} {self.name} ({self.weight} грамів)'


class Blueberry(Berry):
    def __init__(self, name, weight, color, size):
        super().__init__(name, weight, color)
        self.size = size

    def __repr__(self):
        return f'{self.color} {self.size} {self.name} ({self.weight} грамів)'
