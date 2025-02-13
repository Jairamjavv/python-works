# Simple hashmap creation
my_hash_map = {}
my_another_map = dict()

# Adding values to them
my_hash_map = {"age": 28}
my_hash_map["name"] = "jayam"

print(my_hash_map)

# Lets add hashing
words_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
