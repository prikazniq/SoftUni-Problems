size = float(input())
sourceMetric = input().lower()
destMetric = input().lower()
if sourceMetric == "mm":
    size = size * 1000
elif sourceMetric == "cm":
    size = size * 100
elif sourceMetric == "miles":
    size = size / 0.000621371192
elif sourceMetric == "inch":
    size = size * 39.3700787
elif sourceMetric == "km":
    size = size / 0.001
elif sourceMetric == "feet":
    size = size * 3.2808399
elif sourceMetric == "yards":
    size = size * 1.0936133
if destMetric == "mm":
    size = size * 1000
elif destMetric == "cm":
    size = size * 100
elif destMetric == "miles":
    size = size / 0.000621371192
elif destMetric == "inch":
    size = size * 39.3700787
elif destMetric == "km":
    size = size / 0.001
elif destMetric == "feet":
    size = size * 3.2808399
elif destMetric == "yards":
    size = size * 1.0936133
print(f"{size} {destMetric}")
