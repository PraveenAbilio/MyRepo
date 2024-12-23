def count_words_with_suffix(sentence, suffix):
    words = sentence.split()
    count = 0

    for word in words:
        if word.endswith(suffix):
            count += 1
    return count

input_string = "there is a mango in the tree where a monkey is hanging."
suffix_to_count = 'e'

result = count_words_with_suffix(input_string, suffix_to_count)

print(f"The number of words ending with '{suffix_to_count}' is: {result}")





