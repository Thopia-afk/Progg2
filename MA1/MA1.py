"""
Solutions to module 1
Student: Karl Johansson
Mail: achates02@hotmail.com
Reviewed by: Olle Virding
Reviewed date: 2023-03-31
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib functionen.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math
def power(x, n: int):                        # Optional
    """ Computes x**n using multiplications and/or division """
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1/x*(power(x, n + 1))


def multiply(m: int, n: int) -> int:         # Compulsory
    """ Computes m*n using additions"""
    if n == 0:
        return 0
    elif n < 0:
        return m + multiply(m, n + 1)
    else:
        return m + multiply(m, n - 1)


def divide(t: int, n: int) -> int:           # Optional
    """ Computes m*n using subtractions"""
    if n > t:
        return 0
    else:
        return 1 + divide(t - n, n)


def harmonic(n: int) -> str:                 # Compulsory
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 0:
        return 0
    else:
        return 1/n + harmonic(n-1)


def digit_sum(x: int, base=10) -> int:       # Optional
    """ Computes and returns the sum of the decimal (or other base) digits in x"""
    if x == 0:
        return 0
    else:
        return x%base + digit_sum(x//base, base)


def get_binary(x: int) -> str:               # Compulsary
    """ Returns the binary representation of x """
    if int(x) == 0:
        return str(0)
    elif x < 0:
        return '-' + get_binary(-x)
    else:
        return str(int(x)%2 + 10*(int(get_binary(int(x)//2))))


def reverse_string(s: str) -> str:           # Optional
    """ Returns the s reversed """
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s[0]
    else: 
        return reverse_string(s[1:]) + reverse_string(s[0:1])


def largest(a: iter):                        # Compulsory
    """ Returns the largest element in a"""
    if len(a) == 1:
        return a[0]
    elif a[0] < a[1]:
        return largest(a[1:])
    else:
        return largest(a[1:]+a[0:1])


def count(x, s: list) -> int:                # Compulsory
    """ Counts the number of occurences of x on all levels in s"""
    if len(s) == 0:
        return 0
    elif s[0] == x:
        return 1 + count(x, s[1:])
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return count(x, s[1:])


def zippa(l1: list, l2: list) -> list:       # Compulsory
    """ Returns a new list from the elements in l1 and l2 like the zip function"""

    if len(l1) == 0 or len(l2) == 0:
        return l1 + l2
    else:
        return [l1[0]] + [l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f: str, t: str, h: str, n: int) -> str:  # Compulsory
    """ Returns a string of instruction ow to move the tiles """
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1)


def fib(n: int) -> int:                       # Compulsory
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib\n')

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  t(n) = 2^n-1
  t(50) = 1125899906842623 sekunder
  = 35702052 år = 35,7 miljoner år
  
  
  
  
  Exercise 17: Time for Fibonacci:
  
 n = [35, 36, 37, 38, 39]
 returned 
 tid = [4.3028078999999995, 7.371958800000001, 12.418600800000002, 20.3105247, 31.093510700000003] sekunder
 tid = [4.556216810877626, 7.6752786155747845, 12.552858281829417, 19.217250123609396] sekunder         (calculated, nära)

 tid/1.618 = [2.6593373918417793, 4.556216810877626, 7.6752786155747845, 12.552858281829417, 19.217250123609396] sekunder


 c * 1,618^n = tid    gives c values
 c = [2.0869106369500593e-07, 2.2098168330664258e-07, 2.30073991775048e-07, 2.325613214885661e-07, 2.2004301465057237e-07]
 c(medel) = 2.225*e**(-7)

 c(medel)*1.618**50 = 6255 (sekunder) = 1.7 (timmar)
 c(medel)*1.618**100 = 175842399792965 (sekunder) = 5.6 (miljoner år)

 

  Exercise 20: Comparison sorting methods:

  c(stick) = 1/1000^2
  c(merge) = 1/(1000*log1000)
  
  n = 10^6:
  stick = 10^12*c = 1000000 (sec) = 12 (dagar)
  merge = 6000000*c = 2000 (sec) = 33 (min)

  n = 10^9
  stick = 10^18*c = 10^12 (sec) = 31710 (år)
  merge = 9000000000*c = 3000000 (sec) = 35 (dagar)
  


  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  A: n steg ger n sekunder
  B: n = 10 steg ger 1 sekund
  tid(B) = c(B)*n*log(n) <-> c(B) = 1/(10*log(10)) = 0.1

  n = 0.1*n*log(n) <-> 1 = 0.1*log(n) <-> 10 = log(n) <-> 10^10 = n
  

"""
