#!/usr/bin/python

import argparse

def find_max_profit(prices):
    prices = [int(price) for price in prices]

    if len(prices) < 2:
        return 0
    if len(prices) == 2:
        return prices[-1] - prices[0]
    else:
        last_price = prices[-1]
        profit = last_price - min(prices[:-1])
        return max([profit] + [find_max_profit(prices[:-1])])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
