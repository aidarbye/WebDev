def cat_dog(string):
    return string.count('cat') == string.count('dog')

print(cat_dog('catdog'))           # Output: True
print(cat_dog('catcat'))           # Output: False
print(cat_dog('1cat1cadodog'))     # Output: True
