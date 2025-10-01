import string

# Step 1: Create letters
letters = []
for lc, uc in zip(string.ascii_lowercase, string.ascii_uppercase):
    letters.append(lc)
    letters.append(uc)

# Step 1b: Add symbols (excluding space for now)
symbols = ['.', ',', '?', '-', '_', '=', '+', "'", '"', '!']
letters.extend(symbols)

# Step 2: Write to mappings.txt
with open("mappings.txt", "w") as f:
    # First, assign space explicitly
    f.write(f" \n000000\n")  # space -> 000000

    # Then assign the rest starting from 1
    for i, letter in enumerate(letters):
        binary_code = format(i+1, "06b")  # 6-bit binary starting from 000001
        f.write(f"{letter}\n{binary_code}\n")

print("mappings.txt has been created")