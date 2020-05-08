import argparse

from .fizzbuzz import main

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)

args = parser.parse_args()
results = main(args.number)

for result in results:
    print(result, end=" ")
