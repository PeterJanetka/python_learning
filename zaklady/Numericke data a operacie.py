"""
### Numeric Types — int, float, complex

int = cele cislo
float = cislo s desatinnou ciarkou
complex =


x + y   sum of x and y

x - y   difference of x and y

x * y   product of x and y

x / y   quotient of x and y

x // y  floored quotient of x and y
        Vydeli a potom zaokruhli na najblizsie cele cislo
        8 // 3 = 2 namiesto 2,666~
        !!!!! -(8 // 3): -2
        !!!!! (-8 // 3): -3

x % y   remainder of x / y,
        IBA zvysok z delenia x/y

-x      x negated

+x      x unchanged
integer is complex number which is absolute pri
abs(x)  absolute value or magnitude of x

int(x)  x converted to integer

float(x)    x converted to floating point

complex(re, im) a complex number with real part re,
                imaginary part im. im defaults to zero.

c.conjugate()   conjugate of the complex number c
                Komplexne združené číslo cisla c            ̅z,
                imaginarna cast je rovnako velke ale opacne znamienko

divmod(x, y)    the pair (x // y, x % y) => divmod(12, 5) = (2, 2)

pow(x, y)  x to the power y  =>  x ** y  x to the power y  umocnovanie


x +=  42  =>  x = x + 42
x -=  42  =>  x = x - 42
x *=  42  =>  x = x * 42
x /=  42  =>  x = x / 42
x %=  42  =>  x = x % 42
x //= 42  =>  x = x // 42
x **= 42  =>  x = x**42
input complex 


    round(3.14) => 3
    round(-0.74) => -1
    round(3.14, 1) => 3.1
    round(2563, -2) => 2600

Since n and m are integers, n - m*(n // m) - (n % m)

!!! a^b == bitwise exclusive OR of a and b

"""
print(divmod(12, 5))
