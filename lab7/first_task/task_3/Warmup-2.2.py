def string_splosion(string):
    result = ""
    for i in range(len(string)):
        result += string[:i+1]
    return result

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
