# -*- coding: utf-8 -*-
""""Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал
орел, а сколько - решка."""
import random

coint = 0
coint_1 = 0
coint_0 = 0
shot = 0

while shot < 100:
    coint = random.randint(1, 2)
    if coint == 1:
        coint_1 += 1
        shot += 1
    else:
        coint_0 += 1
        shot += 1
print "even " + str(coint_0) + ", not even " + str(coint_1)
