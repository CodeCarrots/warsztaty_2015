sentence = "Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit."

print('original sentence #1:', sentence)

print()

print('sentence.capitalize():', sentence.capitalize())
print('sentence.lower():', sentence.lower())
print('sentence.upper():', sentence.upper())
print('sentence.title():', sentence.title())
print('sentence.swapcase():', sentence.swapcase())

print()

print('sentence.center(len(sentence) + 17, "="):', sentence.center(len(sentence) + 17, "="))
print('sentence.count("e"):', sentence.count("e"))
print('sentence.replace("e", "?"):', sentence.replace("e", "?"))

print()

splitted_sentence = sentence.split("e")
print('sentence.split("e"):', splitted_sentence)
joined_sentence = "e".join(splitted_sentence)
print('joined == sentence:', joined_sentence == sentence)

print()

print('sentence.startswith("L"):', sentence.startswith("L"))
print('sentence.startswith("l"):', sentence.startswith("l"))

print()

sentence = "     Give me some space... Like {0} as {1} or {0} but not {1}   "

print('original sentence #2:', sentence)

print()

print('sentence.strip():', sentence.strip())
print('sentence.format("one", "two"):', sentence.format("one", "two"))

