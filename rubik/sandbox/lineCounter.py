
count = 0
fileName = 'cubeRotationDirection.py'

f = open("../" + fileName, "r")

for l in f:
    l = l.strip()
    if l and not l.startswith('#') and not l.startswith('"""'):
        count += 1

print(count)