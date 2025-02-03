s = set()

s.add(0)
s.add(1)
s.add(2)
s.add(3)

#s.add(3) again would not change anything as a set dosen't have repeat vals

print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements")