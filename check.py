import sys
from neobase import NeoBase

NeoBase.skip = lambda *_: False

with open("optd_por_public.csv") as f:
    N = NeoBase(f)

for row in sys.stdin:
    city_name, name, key = row.rstrip().split(",")
    if key not in N:
        print(f"- [ ] `{key}`: {name} ({city_name})")
