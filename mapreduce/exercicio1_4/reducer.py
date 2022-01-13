#!/usr/bin/python3


import sys

salesMaisAlta = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip()
    
    thisSale = data_mapped
    
    if float(thisSale) > float(salesMaisAlta):
        salesMaisAlta = float(thisSale)

# Escribe o último par, unha vez rematado o bucle
print("Prezo máximo absoluto de todas as vendas rexistradas \t", salesMaisAlta)

