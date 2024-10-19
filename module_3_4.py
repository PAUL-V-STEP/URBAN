# Find the same root words
def single_root_words(root_word, *other_words):
    same_words = []
    for val in other_words:
        if (root_word.upper() in val.upper()) or (val.upper() in root_word.upper()):
            same_words.append(val)
    return same_words


# Main  19.10.2024 *PVS*
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print("Вариант 1:")
print(result1)
print(result2)


# Find the same root words V2.0
def single_root_words_2(root_word, *other_words):
    same_words = []
    rw_ = root_word.upper()
    for val in other_words:
        val_ = val.upper()
        if (rw_.find(val_) >= 0) or (val_.find(rw_) >= 0):
            same_words.append(val)
    return same_words


# Main V2.0  19.10.2024 *PVS*
result1 = single_root_words_2('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_2('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print("Вариант 2:")
print(result1)
print(result2)

