# class Comment:
#     def __init__(self, username, content, likes = 0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
# comment = Comment("user1", "I like this book")
# print(comment.username)
# print(comment.content)
# print(comment.likes)

# --------------------------------------------------------------
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Party():
#     def __init__(self):
#         self.guests = []
#
#     def add_guests(self, person):
#         self.guests.append(person)
#
#     def summary_party(self):
#         guest_names = ", ".join([guest.name for guest in self.guests])
#         return f"Going: {guest_names}\nTotal: {len(self.guests)}"
#
#
# party = Party()
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     person_name = command
#     person = Person(person_name)
#     party.add_guests(person)
#
# print(party.summary_party())

# -------------------------------------------------------------------------
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Email:
#     def __init__(self, sender, recipient_name, content):
#         self.sender_name = sender_name
#         self.recipient_name = recipient_name
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender_name} says to {self.recipient_name}: {self.content}. Sent: {self.is_sent}"
#
# class MailBox:
#     def __init__(self):
#         self.emailbox = []
#
#     def add_email(self, email):
#         self.emailbox.append(email)
#
#     def send_emails(self, indexes):
#         for i in indexes:
#             self.emailbox[i].send()
#
#     def get_all_emails_info(self):
#         all_info = ""
#         for email in self.emailbox:
#             all_info += f"{email.get_info()}\n"
#         return all_info
#
# mailbox = MailBox()
#
# while True:
#     command = input()
#     if command == "Stop":
#         break
#     sender_name, recipient_name, content = command.split(" ", maxsplit=2)
#     sender = Person(sender_name)
#     recipient = Person(recipient_name)
#     email = Email(sender, recipient_name, content)
#     mailbox.add_email(email)
#
# sent_indexes = [int(i.strip()) for i in input().split(", ")]
# mailbox.send_emails(sent_indexes)
# print(mailbox.get_all_emails_info())


# -----------------------------------------------------------------------------

# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fish = []
#         self.birds = []
#
#     def add_animal(self, species, name_of_animal):
#         if species == "mammal":
#             self.mammals.append(name_of_animal)
#         elif species == "fish":
#             self.fish.append(name_of_animal)
#         elif species == "bird":
#             self.birds.append(name_of_animal)
#         Zoo.__animals += 1
#
#     def get_info(self, select_animal):
#         if select_animal == "mammal":
#             return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {animal_count}"
#         elif select_animal == "fish":
#             return f"Fishes in {self.name}: {', '.join(self.fish)}\nTotal animals: {animal_count}"
#         elif select_animal == "bird":
#             return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {animal_count}"
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# animal_count = int(input())
#
#
# for i in range(animal_count):
#     animal = input().split()
#     species = animal[0]
#     name_of_animal = animal[1]
#     zoo.add_animal(species, name_of_animal)
#
# select_animal = input()
#
# print(zoo.get_info(select_animal))

# -----------------------------------------------------------------
# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.radius = diameter / 2
#         self.diameter = diameter
#
#     def calculate_circumference(self):
#         return Circle.__pi * self.diameter
#
#     def calculate_area(self):
#         return Circle.__pi * self.radius * self.radius
#
#     def calculate_area_of_sector(self, angle):
#         return (angle / 360) * Circle.__pi * (self.radius * self.radius)
#
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")
