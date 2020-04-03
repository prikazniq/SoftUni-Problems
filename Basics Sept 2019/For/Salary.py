tabs = int(input())
salary = int(input())

for i in range(tabs):
    site = input()
    if site == "Facebook":
        salary -= 150
    if site == "Instagram":
        salary -= 100
    if site == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)