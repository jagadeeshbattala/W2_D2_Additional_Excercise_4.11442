#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:52:43 2019

@author: jagadeeshb
"""

def ispalindrome(input):
    return (input == input[::-1])

print("Hello is Palindrome: ", ispalindrome("Hello"))
print("malayalam is Palindrome: ", ispalindrome("malayalam"))