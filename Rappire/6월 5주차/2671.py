import sys
import re

input = sys.stdin.readline

pattern = re.compile("(100+1+|01)+")
str = input().rstrip()

if pattern.fullmatch(str):
    print("SUBMARINE")
else:
    print("NOISE")
