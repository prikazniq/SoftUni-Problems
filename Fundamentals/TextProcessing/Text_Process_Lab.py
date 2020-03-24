# def reverse(a):
#     return ''.join(reversed(a))
#
#
# while True:
#     word = input()
#     if word == "end":
#         break
#     print(f"{word} = {reverse(word)}")
# ------------------------------------------------------------

#
# def repeat_by_len_of_string(a):
#     return a * len(a)
#
#
# words = input().split()
#
# for word in words:
#     print(repeat_by_len_of_string(word), end="")

# ------------------------------------------------------------------------
#
#
# def clear_word_from_string(words, strings):
#     while words in strings:
#         strings = strings.replace(words, "")
#     return strings
#
#
# word = input()
# string = input()
#
# print(clear_word_from_string(word, string))

# ------------------------------------------------------------------------

#
# word = input().split(', ')
# text = input()
#
# for i in word:
#     while i in text:
#         text = text.replace(i, len(i) * "*")
#
# print(text)


string = input()
digit = ""
text = ""
symbol = ""

for i in string:
    if i.isdigit():
        digit += i
    elif i.isalpha():
        text += i
    else:
        symbol += i

print(digit)
print(text)
print(symbol)