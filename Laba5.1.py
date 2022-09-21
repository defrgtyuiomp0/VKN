import math
x = float(input('Задайте Х: '))
if x >= 5.2:
    y = math.pow(math.e,3.27*math.fabs(x-9)+1)
elif 0.19 < x < 5.2:
    y = math.cos(x)+(1/math.tan(x)+math.sqrt(math.fabs(x-7.84)))
else:
    y = math.sin(math.fabs(x-0.7))+3.33*math.pow(2,x)
print('Вшдповідь: ',y)