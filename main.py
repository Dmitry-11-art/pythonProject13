# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def fib(n):
   if n <= 2:
       return 1
   return fib(n-1)+fib(n-2)
print(fib(10))

print("Hello Github!!!!!!!!!!!!!!!1")

def func1(x, y):
    print(x)
    print(y)
    return x**2 + y**2
a = 4
b = 5
print(func1(a, b))

def func2(a,b):
    print(a)
    print(b)
    return a + b**2
print(func2(a, b))