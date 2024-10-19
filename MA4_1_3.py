
"""
Solutions to module 4
Review date:
"""

student = "Lovisa Hambäck"
reviewer = ""

import math as m
import random as r
import functools
from time import perf_counter as pc
import multiprocessing as mp
import concurrent.futures as future


def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    tot_lst = []
    
    for i in range(n):
        coordinates = [r.uniform(0,1) for x in range(d)]           #list comprehension
        f = lambda x:x**2
        coordinates_sqrd = [f(x) for x in coordinates] 
        coordinate_sum = sum(coordinates_sqrd)
        tot_lst.append(coordinate_sum)
    def func(x):
        return x <= 1
    in_ball = filter(func, tot_lst)               #Filter
    in_ball = list(in_ball)
    volume_approx = 2**d*(len(in_ball)/n)
    return volume_approx
    return  

def hypersphere_exact(n,d):
    Volume = (m.pi**(d/2))/m.gamma(d/2 +1)
    return Volume

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     with future.ProcessPoolExecutor() as ex:
         futures = []
         for _ in range(np):
             f = (ex.submit(sphere_volume, n, d))
             futures.append(f)
     res = [f.result() for f in futures]
     return sum(res)/len(res)

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
     # with future.ThreadPoolExecutor() as ex:
     #     lst = [n//np]*np
     #     d = [d]*np
     #     result = ex.map(sphere_volume, lst, d)
     # result = list(result)
     # return sum(result)/len(result)
     with future.ProcessPoolExecutor() as ex:
         futures = []
         for _ in range(np):
             f = (ex.submit(sphere_volume, n//np, d))
             futures.append(f)
     res = [f.result() for f in futures]
     return sum(res)/len(res)
         

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    end = pc()
    print(f"The non-parallell process took {round(end-start,2)} seconds")
    np = 10
    start = pc()
    print(sphere_volume_parallel1(n,d, np))
    end = pc()
    print(f"The parallell1 process took {round(end-start,2)} seconds")
    n = 1000000
    start = pc()
    print(sphere_volume_parallel2(n,d, np))
    end = pc()
    print(f"The parallell2 process took {round(end-start,2)} seconds")

if __name__ == '__main__':
	main()
