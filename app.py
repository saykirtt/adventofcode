from src.utils.api import get_input
from src.utils.new_file import new_file
import argparse

parser = argparse.ArgumentParser(description='Init puzzle file')
parser.add_argument('year', type=int, help='the event year')
parser.add_argument('day' ,type=int,help='the day')

args = parser.parse_args()

#YEAR = 2022
#DAY = 6

new_file(args.year,args.day)
get_input(args.year,args.day)
