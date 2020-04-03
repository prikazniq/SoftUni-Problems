import math

l = float(input()) * 100
w = float(input()) * 100 - 100
rab_mqsto_l = 120
rab_mqsto_w = 70
razpolagame_l = math.trunc(l / rab_mqsto_l)
razpolagame_w = math.trunc(w / rab_mqsto_w)
l_po_w = round(razpolagame_l, 0) * round(razpolagame_w, 0)- 3
print (math.trunc(l_po_w))