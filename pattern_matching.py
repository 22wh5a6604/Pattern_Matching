def match(string, pattern):
    if not string or not pattern:
        return False
    
    # Handle patterns with consecutive wildcards correctly
    pattern_list = [p for p in pattern.split('*') if p]
    
    start = 0
    for item in pattern_list:
        index = string.find(item, start)
        if index == -1:
            return False
        start = index + len(item)
    return True

def get_wildcard_values(string, pattern):
    if not string or not pattern:
        return []
    
    pattern_list = [p for p in pattern.split('*') if p]
    
    start = 0
    wildcard = []
    for item in pattern_list:
        index = string.find(item, start)
        if index > start:
            value = string[start:index]
            wildcard.append(value)
        start = index + len(item)
    
    # Capture any trailing wildcard values
    if start < len(string):
        wildcard.append(string[start:])
    return wildcard

def get_wildcard_lengths(string, pattern):
    if not string or not pattern:
        return []
    
    pattern_list = [p for p in pattern.split('*') if p]
    
    start = 0
    lengths = []
    for item in pattern_list:
        index = string.find(item, start)
        if index > start:
            length = index - start
            lengths.append(length)
        start = index + len(item)
    
    # Capture any trailing wildcard lengths
    if start < len(string):
        lengths.append(len(string) - start)
    return lengths

string = input("Enter a string: ")
pattern = input("Enter a pattern with a wildcard (*): ")

if match(string, pattern):
    wildcard_lengths = get_wildcard_lengths(string, pattern)
    wildcard_values = get_wildcard_values(string, pattern)
    print("The string matches the pattern.\nWildcards lengths:", wildcard_lengths)
    print("Wildcards values:", wildcard_values)
else:
    print("No match found.")
