a=float(input('Введіть число Ах: '))
A=float(input('Введіть число Аy: '))
b=float(input('Введіть число Bx: '))
B=float(input('Введіть число By: '))
c=float(input('Введіть число Cx: '))
C=float(input('Введіть число Cy: '))
if (a**2)+(A**2) < (b**2)+(B**2) and (a**2)+(A**2) < (c**2)+(C**2):
    print('Точка А ближча')
elif (b**2)+(B**2) < (a**2)+(A**2) and (b**2)+(B**2) < (c**2)+(C**2):
    print('Точка B ближча')
else:
    print('Точка C ближча')