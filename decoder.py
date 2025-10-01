from PIL import Image as I
import os, re

def mappings_load(filename="mappings.txt"):
    mappings = {}
    reverse_mappings = {}
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
            reverse_mappings[num] = " "
        else:
            mappings[char] = num
            reverse_mappings[num] = char

        i += 2

    return mappings, reverse_mappings


def pixel_to_bit(pixel):
    r, g, b = pixel
    brightness = (r + g + b) / 3
    return "1" if brightness > 127 else "0"


def convert_image_to_text(image_path, filename="mappings.txt"):
    _, reverse_mappings = mappings_load(filename)

    img = I.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    binary_string = ""
    for y in range(height):
        for x in range(width):
            binary_string += pixel_to_bit(pixels[x, y])

    # Split into 6-bit chunks
    chunks = [binary_string[i:i+6] for i in range(0, len(binary_string), 6)]

    decoded_text = ""
    for chunk in chunks:
        if len(chunk) < 6:
            continue
        if chunk in reverse_mappings:
            decoded_text += reverse_mappings[chunk]
        else:
            decoded_text += "?"

    return decoded_text



if __name__ == "__main__":
    name = input("image name >: ")
    path = f"{name}.png"

    if not os.path.exists(path):
        print(f"Image '{path}' not found!")
        exit(1)

    decoded = convert_image_to_text(path)

    os.makedirs("generated", exist_ok=True)
    with open("generated/encoded.txt", "w", encoding="utf-8") as f:
        f.write(decoded)

    print(f"Decoded text saved to generated/encoded.txt")
    wait = input()
