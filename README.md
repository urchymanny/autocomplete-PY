# Autocomplete Python Script

This Python script provides a simple implementation of an autocompletion feature using the Natural Language Toolkit (NLTK) corpus of English words. When provided with a query string, it searches through the corpus to find and return words that could potentially complete the given query.

## Dependencies

The script relies on the NLTK library. Before running the script, ensure you have installed NLTK and downloaded the 'words' corpus by executing the following commands:

```python
import nltk
nltk.download('words')
```

## Functions

### 1. `is_subset(word, query) -> bool`

Checks if all characters in the query exist in the given word. Returns `True` if the condition is met, `False` otherwise.

### 2. `is_strict(word, query) -> bool`

Checks if the characters in the query appear in the exact sequence in the given word. Returns `True` if the condition is met, `False` otherwise.

### 3. `is_sequential(word, query) -> list`

Checks if the characters in the query appear sequentially (though not necessarily in a strict sequence) in the given word. Returns a list of two boolean values: the first indicating if the query is sequential, and the second indicating if the query is strict.

### 4. `starts_with(word, query) -> bool`

Checks if the given word starts with the characters in the query. Returns `True` if the condition is met, `False` otherwise.

### 5. `autoComplete(query) -> list`

The main function that utilizes the above helper functions to find and return a list of words from the NLTK corpus that could potentially complete the given query.

## Usage

To use the script, simply provide a query string to the `autoComplete` function and it will return a list of potential completions along with the total count of such words:

```python
QUERY = str(input("Enter Text to autocomplete: "))
results = autoComplete(QUERY)
for i in results:
    print(i)
print(f"There are {len(results)} word(s) with {QUERY} in them")
```

## Example

Input: `aut`
Output: 
```
auto
autobahn
autobiographical
...
There are 3 word(s) with aut in them
``` 

This script provides a simple way to implement an autocompletion feature using Python and the NLTK library.
