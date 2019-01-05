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
