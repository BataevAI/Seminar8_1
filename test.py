
import re
str_1 =  'Baffie                         | 12445'


b = str_1.split()
b = ''.join(b)
c = b.split('|')
for id, item in enumerate(c):
    print(id, item)