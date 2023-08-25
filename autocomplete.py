from nltk.corpus import words
import nltk
nltk.download('words')

english_words = sorted(set(words.words()))


def is_subset(word, query):
    n = len(query)
    m = len(word)
    c = w = 0
    for i in query:
        while w < m:
            if i == word[w]:
                c += 1
                break
            w += 1

        w = 0

    if c == n:
        return True

    return False


def is_strict(word, query):
    matches = []
    c = 0
    start_index = word.index(query[0])
    indexes = [i for i, x in enumerate(word) if x == query[0]]

    for index in indexes:
        while c < len(query) and index < len(word):
            if word[index] == query[c]:
                matches.append(word[index] == query[c])
                index += 1
            else:
                c = 0
                matches = []
                break

            c += 1
            start_index += 1

    return len(matches) == len(query)


def is_sequential(word, query):
    strict = False
    i, j = 0, 0

    while i < len(query) and j < len(word):
        i += 1 if query[i] == word[j] else 0

        j += 1

    sequential = i == len(query)

    if sequential:
        strict = is_strict(word, query)

    return [sequential, strict]


def autoComplete(query):
    res = []
    count = 0
    for word in english_words:
        word_array = list(word.lower())
        query_array = list(query.lower().strip())
        if is_subset(word_array, query_array):
            sequential, strict = is_sequential(word_array, query_array)
            if sequential and strict:
                count += 1
                res.append(word)
    return res


QUERY = str(input("Enter Text to autocomplete: "))

results = autoComplete(QUERY)
for i in results:
    print(i)
print(f"There are {len(results)} word(s) with {QUERY} in them")
