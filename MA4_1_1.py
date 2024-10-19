
"""
Solutions to module 4
Review date:
"""

student = "Lovisa Hambäck"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):  
     x_vals = [r.uniform(-1,1) for x in range(n)]
     y_vals = [r.uniform(-1, 1) for x in range(n)]
     n_c_x = []
     n_c_y = []
     n_out_x = []
     n_out_y = []
     for i in range(n):
         if x_vals[i]**2 + y_vals[i]**2 <= 1:
             n_c_x.append(x_vals[i])
             n_c_y.append(y_vals[i])
         else:
             n_out_x.append(x_vals[i])
             n_out_y.append(y_vals[i])
             
     pi_approx = 4*(len(n_c_x)/n)
     plt.scatter(n_c_x, n_c_y, c ='red')
     plt.scatter(n_out_x, n_out_y, c='blue')
     plt.savefig(str(n) + 'n.png')
     plt.show()
             
     return len(n_c_x), pi_approx
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        print(approximate_pi(n))
    print("The exact Pi is " + str(math.pi))

if __name__ == '__main__':
	main()
