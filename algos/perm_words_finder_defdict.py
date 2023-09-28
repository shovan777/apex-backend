from collections import defaultdict
from typing import List


def findSubstring(s: str, words: List[str]) -> List[int]:
    words_len = len(words)
    word_len = len(words[0])
    seq_len = words_len * word_len
    str_len = len(s)
    idx_arr = []

    def count_words(word_list):
        count_dict = defaultdict(int)
        for word in words:
            count_dict[word] += 1
        return count_dict

    words_count = count_words(words)

    # is_valid = False
    # print(words_count)
    for i in range(0, str_len):
        if (i + seq_len) > str_len:
            break
        possible_seq = s[i : i + seq_len]
        is_valid = True
        # print(f'possible valid seq: {possible_seq}')
        seq_count = defaultdict(int)
        for j in range(0, len(possible_seq), word_len):
            word = possible_seq[j : j + word_len]
            seq_count[word] += 1
            if word not in words:
                is_valid = False
                break
        if not is_valid:
            continue
        if seq_count == words_count:
            idx_arr.append(i)
    return idx_arr


# passed
# words = ["word","good","best","word"]
# s = "wordgoodgoodgoodbestword"
s = "barfoothefoobarman"
# s = "barfoobarfoobarman"
words = ["foo", "bar"]
# s= "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo", "barr", "wing", "ding", "wing"]
print(findSubstring(s, words))
