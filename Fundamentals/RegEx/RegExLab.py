# import re
#
# pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
# text = input()
#
# result = re.findall(pattern, text)
#
# print(" ".join(result))
# ------------------------------------------------------------------
# import re
#
# pattern = r"(\+359([-| ])2\2\d{3}\2\d{4}\b)"
# result = re.findall(pattern, input())
# print(', '.join([phone for phone, sep in result]))
#
# -------------------------------------------------------------------
#
# import re
#
# pattern = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
# date = input()
# result = re.findall(pattern, date)
#
# for match in result:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# ------------------------------------------------------------------------
# import re
#
# pattern = r"(^|(?<=\s))-?\d+(.\d+)?($|(?=\s))"
# numbers = input()
#
# result = re.finditer(pattern, numbers)
#
# for i in result:
#     print(i.group(0), end=" ")