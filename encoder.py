from PIL import Image as I
import math as M, re, numpy as np, os

def is_valid_text(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z ]+", s))

def mappings_load(filename="mappings.txt"):
    mappings = {}
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n\r") for line in f]

    i = 0
    while i < len(lines) - 1:
        char = lines[i]
        num_line = lines[i + 1].strip()

        if not num_line.isdigit():
            raise ValueError(f"Invalid number mapping for '{char}': '{num_line}'")

        num = f"{int(num_line):06d}"

        if char == "" or char == " ":
            mappings[" "] = num
        else:
            mappings[char] = num

        i += 2

    return mappings


def convert_to_image(input_string, filename="mappings.txt"):
    mappings = mappings_load(filename)
    result = []
    for ch in input_string:
        if ch in mappings:
            result.append(mappings[ch])
        else:
            raise ValueError(f"No mapping found for character '{ch}'")
    return result

name = input("generated image name >:")
text = input("text >: ")


imgw = M.ceil(M.sqrt(len(text)*6))
imgh = imgw

output = I.new("RGB", (imgw, imgh), "black")
loaded = output.load()

x, y = 0, 0

mappings_load()
for b in convert_to_image(text):
    for n in b:
        value = int(n)
        print(n, end="")
        loaded[x, y] = (255, 255, 255) if value == 1 else (0, 0, 0)
        x += 1
        if x >= imgw:
            x = 0
            y += 1
    if y >= imgh:
        break

print()
print(f"Message length: {len(text)} characters")
print(f"Output size: {imgw}px by {imgh}px")
wait = input("-- Press Enter to generate the image --")

os.makedirs("generated", exist_ok=True)
output.save(f"generated/{name}.png")