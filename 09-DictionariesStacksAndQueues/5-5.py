paragraph = "cat dog mouse cat rat cat mouse"
word_count = {}
for word in paragraph.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)  # Output: {'cat': 3, 'dog': 1, 'mouse': 2, 'rat': 1}