def count_vowels(s):
    if not isinstance(s, str):
        raise TypeError("Expected a String")
    return sum(1 for c in s.lower() if c in "aeiou")