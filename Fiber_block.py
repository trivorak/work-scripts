s = float(input('Thickness of part = '))
t = float(input('Lens Distance = '))
u = float(input('Fiber Distance = '))
v = abs(t-(s-u))

if v>.157:
    a = round(v-.157,4)
    v = str(round(v,4))
    a = str(a)
    print()
    print(v + ' Actual')
    print(a + ' OMT')
    print()
    print('Part is Bad')
    print()
elif v<.147:
    a = round(.147-v,v)
    v = str(round(v,4))
    a = str(a)
    print()
    print(v + ' Actual')
    print(a + ' UMT')
    print()
    print('Part is Bad')
    print()
else:
    v= str(round(v,4))
    print()
    print(v + ' Actual')
    print()
    print('Part is Good')
    print()
    
x = input('Press Any Key to Exit!')
