def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def check_for_null_inputs(name):
	if not name:
        	return ""

def add_padding_to_code(code, padding_char, length):
    return code.ljust(lenght, padding_char)

def if_break(soundex):
    return len(soundex) == 4

def if_continue(code):
    return code == '0'

def if_append(code, prev_code):
    return code != prev_code

def process_character(soundex, char, prev_code):
    code = get_soundex_code(char)
    if if_continue(code):
        return soundex, prev_code
    if if_append(code, prev_code):
        soundex += code
        prev_code = code
    return soundex, prev_code

def process_characters(name):
    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    
    for char in name[1:]:
        if if_break(soundex):
            break
        soundex, prev_code = process_character(soundex, char, prev_code)
            
    return ''.join(soundex)

def generate_soundex(name):
    processed_soundex = process_characters(name)
    return add_padding_to_code(processed_soundex, '0', 4)
