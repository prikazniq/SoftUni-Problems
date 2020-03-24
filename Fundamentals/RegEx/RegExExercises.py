# import re
#
# pattern = r"\d+"
# text = input()
#
# while text != "":
#     result = re.findall(pattern, text)
#     if not result:
#         text = input()
#         continue
#     else:
#         print(" ".join(result), end=" ")
#         text = input()
# -------------------------------------------------------------
# import re
#
# pattern = r"\b_{1}([^\W_]+\b)"
# text = input()
# result = re.findall(pattern, text)
#
# print(','.join(result))
# ------------------------------------------------------------
# import re
#
# sentence = input()
# keyword = r"\b" + input() + r"\b"
# result = re.findall(keyword, sentence,re.IGNORECASE)
#
# print(len(result))
# ---------------------------------------------------------------
# import re
#
# pattern = r"[ |^]([a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[^\.\s\,])"
# text_with_email = input()
# result = re.findall(pattern, text_with_email)
#
#
# print("\n".join(result))
# ---------------------------------------------------------------------
# import re
#
# pattern = r">>([A-Za-z0-9]+)<<([0-9]+\.?[0-9]+)!([0-9]+)"
# bought_furniture = []
# furniture = ""
# price = 0
# quantity = 0
# total = 0
#
# while True:
#     command = input()
#     if command == "Purchase":
#         break
#     result = re.findall(pattern, command)
#     if not result:
#         continue
#     furniture, price, quantity = result[0]
#     total += float(price) * int(quantity)
#     bought_furniture.append(furniture)
#
# print(f"Bought furniture: ")
# print("\n".join(bought_furniture))
# print(f"Total money spend: {total:.2f}")
