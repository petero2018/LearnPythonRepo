import re

s = 'asdf=5;iwantthis'
result = re.search('asdf=5;(.*)', s)
print(result.group(1))