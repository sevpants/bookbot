import time


with open('books/frankenstein.txt') as f:
    file_contents = f.read()

print(f"--- Begin analysis of a {f.name} as dict and list ---\n")


words = file_contents.split()
print(len(words))

start_write_dict = time.time()
chars = {}
for word in words:
    for char in word.lower():
        if char.isalpha() == False:
            continue
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
end_write_dict = time.time()

print(f"--- Begin report of {f.name} as a dictionary---")
print(f"{len(words)} words found in the document\n")

start_read_dict = time.time()
for c in chars:
    print(f"The {c} character was found {chars[c]} times")
end_read_dict = time.time()

print(f"\n--- End report of {f.name} ---\n")

print(f"--- Begin report of {f.name} as an ordered list ---")
# ordered
sorted_chars = list(chars)
sorted_chars.sort()

start_read_list_dict = time.time()
for c in sorted_chars:
    print(f"The {c} character was found {chars[c]} times")
end_read_list_dict = time.time()

print(f"\n--- End report of {f.name} as an ordered list ---\n")


print(f"--- Begin report of {f.name} as a list ---")
start_write_list = time.time()
char_list = []
char_count = []
for word in words:
    for char in word.lower():
        if char.isalpha() == False:
            continue
        char_in_list = False
        for c in char_list:
            if c[0] == char:
                c[1] += 1
                char_in_list = True
                break
        if not char_in_list:
            char_list.append([char, 1])

end_write_list = time.time()

start_read_list = time.time()
for c in char_list:
    print(f"The {c[0]} character was found {c[1]} times")
end_read_list = time.time()

print(f"\n--- End report of {f.name} ---\n")

print(f"Dictionary write time (s): {end_write_dict - start_write_dict}")
print(f"List write time (s): {end_write_list - start_write_list}")
print(f"Dictionary read time (s): {end_read_dict - start_read_dict}")
print(f"List read time (s): {end_read_list - start_read_list}")
print(f"List+dict read time (s): {end_read_list_dict - start_read_list_dict}")

print(f"Total dictionary time (s): {end_read_dict - start_write_dict}")
print(f"Total list time (s): {end_read_list - start_write_list}")

