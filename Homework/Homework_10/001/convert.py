import re

def replace(line):
    line = re.sub(r'(\d)(x)', r'\1*\2', line)
    line = line.replace('^', '**')
    line = line[:-2:]
    return line