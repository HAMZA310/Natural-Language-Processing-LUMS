"""
Approach:
    Using dynamic programming (top down approach using recursive calls), find
    all possible cases through which source string
    can be converted to target string, and then choose 
    the case which gives minimum cost.
"""

import sys

s = sys.argv[1]
t = sys.argv[2]
insertion_cost = int(input('input inertion cost: '))
deletion_cost = int(input('input deletion cost: '))
substitution_cost = int(input('input substitution cost: '))

def main():
	edit_dist = min_dist(s,t)
	print(edit_dist)

def ins_cost(c1, c2):
    if c1 == c2:
        return 0
    return substitution_cost

def min_dist(s, t):
    if len(s) == 0:
        return len(t) * insertion_cost 
    if len(t) == 0:
        return len(s) * deletion_cost
    
    return min (min_dist(s[1:], t) + deletion_cost, \
    				min_dist(s, t[1:]) + insertion_cost, \
    					min_dist(s[1:], t[1:]) + ins_cost(s[0], t[0]))
     


if __name__ == "__main__":
	main()