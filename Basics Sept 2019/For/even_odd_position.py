import sys

maxcompare_odd = -sys.maxsize
mincompare_odd = sys.maxsize
maxcompare_even = -sys.maxsize
mincompare_even = sys.maxsize

oddsum = 0
oddmin = 0
oddmax = 0
evensum = 0
evenmin = 0
evenmax = 0
n = int(input())

for i in range(n):
    currentinput = float(input())
    if i % 2 == 0:
        oddsum += currentinput
        if currentinput < mincompare_odd:
            oddmin = currentinput
            mincompare_odd = oddmin
        if currentinput > maxcompare_odd:
            oddmax = currentinput
            maxcompare_odd = oddmax
    if i % 2 != 0:
        evensum += currentinput
        if currentinput < mincompare_even:
            evenmin = currentinput
            mincompare_even = evenmin
        if currentinput > maxcompare_even:
            evenmax = currentinput
            maxcompare_even = evenmax

print(f"OddSum={oddsum:.2f},")

if oddmin == 0 and oddmax == 0:
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddMin={oddmin:.2f},")
    print(f"OddMax={oddmax:.2f},")

print(f"EvenSum={evensum:.2f},")
if evenmin == 0 and evenmax == 0:
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"EvenMin={evenmin:.2f},")
    print(f"EvenMax={evenmax:.2f}")
