import sys
from fractions import Fraction
from decimal import Decimal as D

ideal_temp = 95.5
current_temp = 95.49999999999

print(f"ideal tempreture {ideal_temp}")
print(f"current tempreture {current_temp}")
print(f"Difference in tempreture: {ideal_temp - current_temp}")
print(sys.float_info)