import math

from pip._vendor.distlib.compat import raw_input

i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(math.max(lis))
