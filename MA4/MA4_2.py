#!/usr/bin/env python3
from person import Person
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter as pc

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def fib(n):
	if n <= 1:
		return n
	else:
		return(fib(n-1) + fib(n-2))

def fib_test():
	result_time_py = []
	result_time_numba = []
	n = [i for i in range(1, 20, 25, 30)]
	for i in n:
		start = pc()
		fib(i)
		end = pc()
		result_time_py.append(end - start)
  
		start = pc()  
		fib_numba(i) 
		end = pc()
		result_time_numba.append(end - start)
        

	plt.plot(n, result_time_py,label='python')
	plt.plot(n, result_time_numba,label='numba')
	plt.xlabel('n')
	plt.ylabel('time')
	plt.legend()
	plt.show()
	plt.savefig('prog2_MA4_plot1.png')	


	n = [i for i in range(1, 30, 35, 40, 45)]
	result_time_py = [] ; result_time_numba = [] ; result_time_cpp = []
	for i in n:

		start = pc()
		fib(i)
		end = pc()
		result_time_py.append(end - start)
   
		start = pc()
		fib_numba(i)
		end = pc()
		result_time_numba.append(end-start)
  
		f = Person(i)
		start = pc()
		f.fib()
		end = pc()
		result_time_cpp.append(end-start)

	plt.plot(n, result_time_py, label='python')
	plt.plot(n, result_time_numba, label='numba')
	plt.plot(n, result_time_cpp, label='c++')
	
	plt.legend()
	plt.xlabel('n')
	plt.ylabel('time')
	plt.show()
	plt.savefig('prog2_MA4_plot2.png')

if __name__ == '__main__':
	main()
	fib_test()
	f = Person(47)	
	print('Fib 47 c++', f.fib())
	print('Fib 47 numba', fib_numba(47))
 