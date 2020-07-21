from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def sell(self, sell_shares):
        self.shares -= sell_shares

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

# s = Stock("GOOG", 100, 490.10)
# print(s.name)
# __next__()
# print(s.shares)
# s.sell(25)
# print(s.shares)
# print(s.cost())
# import fileparse
# with open('Data/portfolio.csv') as lines:
#     portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'],types=[str,int,float])

# portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts]
# print(portfolio)
# print(sum([s.cost() for s in portfolio]))