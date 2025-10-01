# Read the file
with open("sanitaze.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Allowed characters according to your mapping
allowed_chars = set(
    "abcdefghijklmnopqrstuvwxyz"  # lowercase
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # uppercase
    " .,?-_+=!'\""                 # symbols
    " "                             # space
)

# Replace newlines with double space
text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "  ")

# Replace backticks with single quote
text = text.replace("`", "'")

# Filter out disallowed characters
text = "".join(ch for ch in text if ch in allowed_chars)

# Write sanitized text to a new file
with open("sanitazed.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Output written to sanitazed.txt")