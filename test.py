import re
from collections import Counter

str = """[1 4 1 4 1 0 4 4 4 4 2 4 4 3 0 0 3 0 3 4 3 0 0 0 4 3 0 4 3 0 0 0 4 0 3 0 2
 4 0 2 4 2 4 0 2 0 2 2 3 0 0 0 3 3 0 2 3 0 2 2 4 3 2 3 2 2 3 2 2 3 2 2 3 0
 0 3 0 1 0 4 2 2 1 2 1 0 4 0 4 2 4 2 0 0 4 2 4 4 2 0 4 4 4 4 4 0 3 2 0 2 0
 4 2 4 2 2 4 2 3 3 4 2 2 2 2 4 2 4 2 0 2]"""
list = re.findall("\d", str)
result = Counter(list)
print(result)
print(f"perforce: {37/len(list)}")