
"""
Solutions to module 4
Review date:
"""

student = "Lovisa Hambäck"
reviewer = ""

import math as m
import random as r
import functools

def sphere_volume(n, d):   
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    
    tot_lst = []
    
    for i in range(n):
        coordinates = [r.uniform(0,1) for x in range(d)]           #list comprehension
        f = lambda x:x**2
        coordinates_sqrd = [f(x) for x in coordinates] 
        coordinate_sum = functools.reduce(lambda a,b: a+b, coordinates_sqrd)
        tot_lst.append(coordinate_sum)
    def func(x):
        return x <= 1
    in_ball = filter(func, tot_lst)               #Filter
    in_ball = list(in_ball)
    volume_approx = 2**d*(len(in_ball)/n)
    return volume_approx


def hypersphere_exact(n,d):
    Volume = (m.pi**(d/2))/m.gamma(d/2 +1)
    return Volume
     
def main():
    n = 100000
    d = 2
    print(sphere_volume(n,d))
    print(hypersphere_exact(n,d))
    d = 11
    print(sphere_volume(n,d))
    print(hypersphere_exact(n,d))


if __name__ == '__main__':
	main()
