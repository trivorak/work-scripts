from fractions import Fraction
s = float(input('Decimal Radius? '))
s = Fraction(round(s/(1/64),0)*(1/64))
print(s)
l = input('Press Enter to close this script')
