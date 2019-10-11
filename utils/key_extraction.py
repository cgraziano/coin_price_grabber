#methods to extract key.

def getApiKeyFromFile(relativePath):
    file = open(relativePath, 'r')
    key = file.read()
    return removeLeadingAndTrailingNewLineChars(key)

def removeLeadingAndTrailingNewLineChars(string):
    return string.rstrip().lstrip()
