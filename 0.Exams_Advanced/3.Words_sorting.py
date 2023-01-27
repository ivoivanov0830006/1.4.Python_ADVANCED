def words_sorting(*args):
    all_words = {}
    result = ""
    total_sum = 0

    for word in args:
        word_sum = sum(ord(letter) for letter in word)
        if word not in all_words:
            all_words[word] = 0
        all_words[word] = word_sum
        total_sum += word_sum

    if total_sum % 2 == 0:
        sorted_all_words = sorted(all_words.items(), key=lambda x: x[0])
    else:
        sorted_all_words = sorted(all_words.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_all_words:
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

