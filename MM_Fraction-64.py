from fractions import Fraction
s = float(input('MM Radius? '))
s = s/25.4
s = Fraction(round(s/(1/64),0)*(1/64))
print(s)
l = input('Press Enter to close this script')
