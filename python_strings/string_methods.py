# String Methods Demonstration

s = "  hello world  "
text = "Python123"

# Case Conversion
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Title:", s.title())
print("Capitalize:", s.capitalize())
print("Swapcase:", s.swapcase())

print("-" * 40)

# Whitespace Removal
print("Strip:", s.strip())
print("Left Strip:", s.lstrip())
print("Right Strip:", s.rstrip())

print("-" * 40)

# Searching
print("Find 'world':", s.find("world"))
print("Count 'l':", s.count("l"))

print("-" * 40)

# Replacement
print("Replace world with Python:", s.replace("world", "Python"))

print("-" * 40)

# Splitting and Joining
words = s.strip().split()
print("Split:", words)

joined = "-".join(words)
print("Joined:", joined)

print("-" * 40)

# Checking Methods
print("Is Alpha:", text.isalpha())
print("Is Digit:", text.isdigit())
print("Is Alnum:", text.isalnum())
print("Is Lower:", s.islower())
print("Is Upper:", s.isupper())