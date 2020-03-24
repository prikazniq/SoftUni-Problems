# class Storage:
#     storage = []
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def add_product(self, product):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#
#     def get_products(self):
#         return self.storage
#
# ---------------------------------------------------------------------------
# class Weapon:
#     def __init__(self, bullets):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return "shooting..."
#         else:
#             return "no bullets left"
#
#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"

# --------------------------------------------------------------------------
#
# class Catalogue:
#     products = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def get_by_letter(self, first_letter):
#         return [p for p in self.products if first_letter == p[0]]
#
#     def __repr__(self):
#         res = f"Items in the {self.name} catalogue:\n"
#         join = "\n".join(sorted(self.products))
#         return f"{res}{join}"
# -------------------------------------------------------------------------------

# class Town:
#     def __init__(self, name):
#         self.name = name
#     def set_latitude(self, latitude):
#         self.latitude = latitude
#     def set_longitude(self, longitude):
#         self.longitude = longitude
#     def __repr__(self):
#         return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

# -------------------------------------------------------------------------------
#
# class Inventory:
#     items = []
#
#     def __init__(self, capacity):
#         self.__capacity = capacity
#
#     def add_item(self, item):
#         self.item = item
#         self.items.append(self.item)
#         if self.__capacity < len(self.items):
#             self.items.remove(item)
#             return "not enough room in the inventory"
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"
# -------------------------------------------------------------------------------------------

# class Article:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author
#
#     def edit(self, new_content):
#         self.content = new_content
#
#     def change_author(self, new_author):
#         self.author = new_author
#
#     def rename(self, new_title):
#         self.title = new_title
#
#     def __repr__(self):
#         return f"{self.title} - {self.content}: {self.author}"

# ----------------------------------------------------------------------------
# class Class:
#     __students_count = 22
#
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#         self.grades = []
#
#     def add_student(self, name, grade):
#         if Class.__students_count:
#             self.students.append(name)
#             self.grades.append(grade)
#             Class.__students_count -= 1
#
#     def get_average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#     def __repr__(self):
#         return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"