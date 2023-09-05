import random as rand
import math
import matplotlib.pyplot as plt
import functools as ft
import concurrent.futures as future
from time import perf_counter as pc
import multiprocessing as mp

"uppgift 1.1"

def pi_plot(n, r):
    n_c = 0
    cirkel_x = []
    cirkel_y = []
    square_x = []
    square_y = []
    
    for i in range(n):
        x = rand.uniform(-r, r)
        y = rand.uniform(-r, r)
        
        if math.sqrt(x**2 + y**2) <= r:
            cirkel_x.append(x)
            cirkel_y.append(y)
            n_c += 1
            
        else:
            square_x.append(x)
            square_y.append(y)
    print('number of points in cirkle = ', n_c)
    return square_x, square_y, cirkel_x, cirkel_y, n_c

def pi_approx(n, r):
    sx, sy, cx, cy, nc = pi_plot(n, r)
    pi_app = 4*nc/n
    
    print(f'pi: {math.pi} and approximated pi: {pi_app}')
    
    plt.plot(sx, sy, 'r.', cx, cy, 'b.')
    plt.show()


"uppgift 1.2"
def hyper_exact(d, r):
    return math.pi**(d/2)/math.gamma(d/2+1)*r**d

def hyper_approx(d, n, r):
    ins = 0
    power = lambda x : x ** 2                                          #lambda
    dist = lambda x : math.sqrt(sum(list(map(power, x)))) #lambda and map                                  #lambda function
    for i in range(n):
        points_power_2 = [rand.uniform(-r, r) for i in range(d)]       #list comprehension
        dist_calc = dist(points_power_2)
        if dist_calc <= r:
            ins += 1
    return ins / n * (2 * r) ** d

"uppgift 1.3"

def hyper_approx2(d, n, r):
    ins = 0
    power = lambda x : x ** 2                                          #lambda
    dist = lambda x : math.sqrt(sum(list(map(power, x)))) #lambda and map                                  #lambda function
    for i in range(n):
        points_power_2 = [rand.uniform(-r, r) for i in range(d)]       #list comprehension
        dist_calc = dist(points_power_2)
        if dist_calc <= r:
            ins += 1
    return ins

def hyper_para(d, n, r):
    ins = 0
    with mp.Pool(mp.cpu_count()) as pool:
        args = [(d, int(n/mp.cpu_count()), r) for i in range(mp.cpu_count())]
        results = pool.starmap(hyper_approx2, args)
    ins = sum(results)
    return ins / n * (2 * r) ** d


if __name__ == '__main__':
    uppgift = input("uppgift?")
    
    if uppgift == "1.1":
        "uppgift 1.1"
        
        n = [10**x for x in range(3, 6)]
        r = int(input("Radie:" ))
    
        for i in n:
            pi_approx(i, r)
    
    if uppgift == "1.2":
        "uppgift 1.2"
        n = 100000
        r = int(input("Radie:" )) 
        d = [2, 11]
        for i in d:
            print(f"dimension = {i} gives approximation: {hyper_approx(i, n, r)} and exact {hyper_exact(i, r)}")
        
    if uppgift == '1.3':
        n, r, d = [1000000, 10000000], 1, 11

        "process one" #7,21
        start_1 = pc()
        hyper_approx(d, n[0], r)
        end_1 = pc()
        
        "process two" #5,14
        start_2 = pc()
        hyper_para(d, n[0], r)
        end_2 = pc()
        
        "process three" #52,08
        start_3 = pc()
        hyper_approx(d, n[1], r)
        end_3 = pc()
        
        "process four" #26,01
        start_4 = pc()
        hyper_para(d, n[1], r)
        end_4 = pc()        
        
        print(f"n = 1000000, original took {round(end_1 - start_1, 2)} seconds and parallel took {round(end_2 - start_2, 2)}")
        print(f"n = 10000000, original took {round(end_3 - start_3, 2)} seconds and parallel took {round(end_4 - start_4, 2)}")
        
        print(f'orginalet är trögare med en faktor på ungefär {round(end_3 - start_3, 2)/round(end_4 - start_4, 2)}') #2 gånger saktare beroende på hur stor n är