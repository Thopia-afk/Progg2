
# n = [i for i in range(30, 45, 1)]
# print(n)

def fib(n):
	if n <= 1:
		return n
	else:
		return(fib(n-1) + fib(n-2))

print(1+1)
print(fib(40))
