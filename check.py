import sys
from neobase import NeoBase

with open("optd_por_public.csv") as f:
    N = NeoBase(f)

for row in sys.stdin:
    name, country, key = row.rstrip().split(",")
    if key not in N:
        print(key, name)
