def get_closest_vowel(word):
    word = word[::-1]
    for i in range(1, len(word)-1):
        if word[i] in "aeiouAEIOU":
            if word[i-1] not in "aeiouAEIOU" and word[i+1] not in "aeiouAEIOU":
                return word[i]
    return ""
