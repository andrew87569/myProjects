# http://www.pythonchallenge.com/pc/def/linkedlist.php

string = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

import urllib.request
from urllib.parse import urljoin

def solve4(url):
    a = url
    for _ in range(401):
        a = urllib.request.urlopen(a)
        for line in a:
            nothing = line.decode("utf-8").split(' ')
        a = urljoin('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing', 'linkedlist.php?nothing=' + nothing[-1])
    return a

print(solve4(string))