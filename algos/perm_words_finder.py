from typing import List


def findSubstring(s: str, words: List[str]) -> List[int]:
    words_len = len(words)
    word_len = len(words[0])
    seq_len = words_len * word_len
    str_len = len(s)
    idx_arr = []

    def count_words(word_list):
        count_dict = {}
        for word in words:
            if word in count_dict.keys():
                count_dict[word] += 1
                continue
            count_dict[word] = 1
        return count_dict

    words_count = count_words(words)

    # print(words_count)
    for i in range(0, str_len):
        if (i + seq_len) > str_len:
            break
        possible_seq = s[i : i + seq_len]
        is_valid = True
        # print(f'possible valid seq: {possible_seq}')
        seq_count = {}
        for j in range(0, len(possible_seq), word_len):
            word = possible_seq[j : j + word_len]
            if word in seq_count.keys():
                seq_count[word] += 1
                continue
            seq_count[word] = 1
            if word not in words:
                is_valid = False
                break
        if not is_valid:
            continue
        for word in words:
            if word not in seq_count.keys():
                is_valid = False
                break
            if words_count[word] != seq_count[word]:
                is_valid = False
                break
        if is_valid:
            idx_arr.append(i)
    return idx_arr


# passed
# words = ["word","good","best","word"]
# s = "wordgoodgoodgoodbestword"
# s = "barfoothefoobarman"
# words = ["foo","bar"]
# s= "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]

# failed
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]
print(findSubstring(s, words))
