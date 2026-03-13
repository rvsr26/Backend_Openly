from ai_utils import is_toxic

print("Test 1 Safe word: 'Hello world'")
print(is_toxic("Hello world"))

print("Test 2 Bad word: 'bitch'")
print(is_toxic("bitch"))

print("Test 3 Bad word: 'fuck'")
print(is_toxic("fuck"))
