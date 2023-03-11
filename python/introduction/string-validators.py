if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


    #!/bin/python3

import sys
import os
import urllib.request
import json

# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=
def  getCountries(s, p):
    url = "https://jsonmock.hackerrank.com/api/countries/search?name="
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        res = response.read()
    
    
f = open(os.environ['OUTPUT_PATH'], 'w')
    

try:
    _s = str(input())
except:
    _s = None


_p = int(input());

res = getCountries(_s, _p)
f.write(str(res) + "\n")

f.close()
