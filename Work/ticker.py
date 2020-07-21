# ticker.py

from follow import follow
import csv
import report
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def filter_symbols(rows, names):
    # for row in rows:
    #     if row['name'] in names:
    #         yield row
    rows = (row for row in rows if row['name'] in names)
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])

    for row in rows:
        rowdata = [ row['name'], f'{row["price"]:0.2f}', f'{row["change"]:0.2f}' ]
        formatter.row(rowdata)


ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')

# import report
# portfolio = report.read_portfolio('Data/portfolio.csv')
# rows = parse_stock_data(follow('Data/stocklog.csv'))
# rows = filter_symbols(rows, portfolio)
# for row in rows:
#     print(f"{row['name']} {row['price']} {row['change']}")

# if __name__ == '__main__':
#     lines = follow('Data/stocklog.csv')
#     rows = parse_stock_data(lines)
#     for row in rows:
#         print(row)