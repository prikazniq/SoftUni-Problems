month = input()
nights = int(input())
discount_studio = 0
discount_apartment = 0
total_studio = 0
total_apartment = 0

if month == "May" or month == "October":
    if nights < 7:
        total_studio = nights * 50
        total_apartment = nights * 65
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")
    if nights <= 7 or nights == 14:
        total_apartment = 65 * nights
        discount_studio = 50 - (50 * 0.05)
        total_studio = discount_studio * nights
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")
    if nights > 14:
        discount_studio = 50 - (50 * 0.3)
        total_studio = discount_studio * nights
        discount_apartment = 65 - (65 * 0.1)
        total_apartment = discount_apartment * nights
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")

if month == "June" or month == "September":
    if nights < 7:
        total_studio = nights * 75.20
        total_apartment = nights * 68.70
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")
    if nights <= 7 or nights == 14:
        total_studio = nights * 75.20
        total_apartment = nights * 68.70
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")
    if nights > 14:
        discount_studio = 75.20 - (75.20 * 0.2)
        total_studio = discount_studio * nights
        discount_apartment = 68.70 - (68.70 * 0.1)
        total_apartment = discount_apartment * nights
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")

if month == "July" or month == "August":
    if nights < 7:
        total_studio = nights * 76
        total_apartment = nights * 77
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")
    if nights <= 7 or nights == 14:
        total_studio = nights * 76
        total_apartment = nights * 77
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")
    if nights > 14:
        total_studio = nights * 76
        discount_apartment = 77 - (77 * 0.1)
        total_apartment = discount_apartment * nights
        print(f"Apartment: {total_apartment:.2f} lv.")
        print(f"Studio: {total_studio:.2f} lv.")