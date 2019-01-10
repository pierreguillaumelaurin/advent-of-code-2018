import re

def multiline_input():
    lines = []
    while True:
        line = input()
        if line:
             lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text

def get_digits_group(line, i):
    matches = re.findall(r'\d+', line)
    digits = int(matches[i])
    return digits