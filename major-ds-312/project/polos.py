class Polo():
    def __init__(self, color, size, price=99.00, style=None):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

polo1 = Polo(color = 'Blue', size = 'L', price = 4.99)
print(polo1.color)
print(polo1.price)

polo2 = Polo(color='Yellow', size = 'S')
print(polo2.color)
print(polo2.price)