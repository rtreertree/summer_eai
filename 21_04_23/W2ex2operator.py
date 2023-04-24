f = float(input('Force (n) : '))
s = float(input('Displacement (m) : '))
t = float(input('Time (s) : '))
w = f*s
print(f'W = FS; W = {f}x{s}; Work = {w} (joules)')
print(f'P = W/T; P = {w}x{t}; Power = {w*t} (watts)')


#OUTPUT
"""
Force (n) : 12
Displacement (m) : 18
Time (s) : 1
W = FS; W = 12.0x18.0; Work = 216.0 (joules)
P = W/T; P = 216.0x1.0; Power = 216.0 (watts)
"""