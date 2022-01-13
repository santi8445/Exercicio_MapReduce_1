#!/usr/bin/python3


import sys

salesTotales = 0

for line in sys.stdin:
    data_mapped = line.strip()

    thisSale = data_mapped

    salesTotales += float(thisSale)

print("Vendas totais \t", salesTotales)

