# pcost.py

import report
import fileparse
import stock

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''

    # with open(filename) as lines:
    #     portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
    # portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

    # return sum([s.shares * s.price for s in portfolio])
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
