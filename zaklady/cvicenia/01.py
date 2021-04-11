from math import pi
a1 = 3 ** 1/2
a2 = 5 ** 1/3 / 3
a3 = (1024 ** (1/5)) ** 5
a4 = (2 ** 20) ** (1/10)
print('a1 =', a1)
print('a2 =', a2)
print('a3 =', a3)
print('a4 -', a4)

print(pi)
# podiel 223 a 71
print((223/71)-pi)
# súčet zlomkov 22/17, 37/47 a 88/83
print(((22/17) + (37/47) + (88/83)) - pi)
# druhá mocnina 99 lomeno súčin 2206 krát druhá odmocnina z 2
print(((99**2)/(2206 * (2 ** (1/2))))-pi)
# druhá odmocnina z 5, k tomu plus 6, to celé druhá odmocnina,
# k tomu plus 7 a to celé opäť druhá odmocnina
print((((((5 ** (1/2)) + 6) ** (1/2)) + 7 ) ** (1/2))-pi)
# 10 na 100 lomeno 11222.11122 a to celé 193 odmocnina
print((((10**100)/11222.11122) ** (1/193))-pi)

n = int(input('zadaj n: '))
print(f'na {n}. políčku bude {2 ** (n-1)} zrniek ryže co je {2 ** (n-1)/50000} ton ryze ')
