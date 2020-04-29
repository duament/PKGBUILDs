import re
from sys import argv

custom = [0x261D, 0x2639, 0x263A, 0x270C, 0x270D]
matcher = re.compile(r'^([0-9A-F]+)(\.\.([0-9A-F]+))?\s*;\s*Emoji_Presentation')
ttf = fontforge.open(argv[1])

def try_remove(val):
    try:
        ttf.removeGlyph(val)
    except ValueError:
        pass

for i in custom:
    try_remove(i)

for line in open(argv[2]):
    match = matcher.match(line)
    if match:
        val_start = int(match[1], 16)
        if match[3] == None:
            try_remove(val_start)
        else:
            val_end = int(match[3], 16)
            for i in range(val_start, val_end + 1):
                try_remove(i)

ttf.generate(argv[1])
