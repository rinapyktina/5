# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

from math import sqrt

if __name__ == '__main__':

    def prime_number(l):
        count = 0
        if l in [0, 1]:
            return False
        for i in range(2, int(sqrt(l)) + 1):
            if l % i == 0:
                count += 1
        if count > 0:
            return False
        return True
l = int(input())
print(prime_number(l))