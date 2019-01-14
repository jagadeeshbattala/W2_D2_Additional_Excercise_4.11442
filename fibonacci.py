#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:52:43 2019

@author: jagadeeshb
"""

def fibonacciTill(value):
    first = 0;
    second = 1;
    if(value < 0):
        print("Please provide the positive integer")
    elif(value == 0):
        print("Fibonacci sequence upto 0 is: 0")
    else:
        print("Fibonacci sequence upto {} is: ".format(value), end='')
        while(first <= value):
            print(first, end=', ')
            tmp = first
            first = first + second
            second = tmp
            
fibonacciTill(1000)