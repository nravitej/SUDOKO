# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 01:44:32 2021

@author: narah
"""

def fibonacci(x):
    count=2
    s=0
    a=0
    #print(a)
    #print("\n")
    b=1
    while count<x:
        s=a+b
        #print(s)
        #print("\n")
        a=b
        b=s
        count=count+1
    return s



if __name__ == "__main__":
    import sys
    print(fibonacci(int(sys.argv[1])))

