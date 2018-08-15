import sys
from math import ceil, sqrt

s=input().strip()
exec("print(' '.join(map(lambda x: s[x::{0}], range({0}))))".format(ceil(sqrt(len(s)))))