chars = {'A': '.­', 'B': '­...', 'C': '­.­.', 'D': '­..', 'E': '.', 'F': '..­.', 'G': '­­.',
         'H': '....', 'I': '..', 'J': '.­­­', 'K': '­.­', 'L': '.­..', 'M': '­­', 'N': '­.',
         'O': '­­­', 'P': '.­­.', 'Q': '­­.­', 'R': '.­.', 'S': '...', 'T': '­',
         'U': '..­', 'V': '...­', 'W': '.­­', 'X': '­..­', 'Y': '­.­­', 'Z': '­­..',
         '1': '.­­­­', '2': '..­­­', '3': '...­­', '4': '....­', '5': '.....',
         '6': '­....', '7': '­­...', '8': '­­­..', '9': '­­­­.', '0': '­­­­­',
         '.': '.­.­.­', ':': '­­­...', ',': '­­..­­', ';': '­.­.­.',
         '?': '..­­..', '=': '­...­', '\'': '.­­­­.', '/': '­..­.',
         '!': '­.­.­­', '-': '­....­', '_': '..­­.­', '\"': '.­..­.',
         '(': '­.­­.', ')': '­.­­.­', '$': '...­..­', '&': '.­...',
         '@': '.­­.­.', '+': '.­.­.', ' ': ' '}
morse = {value: key for key, value in chars.items()}


def encode():
    string = input('please input the string you want to encode:')
    string = string.upper()
    outstring = ''
    for i in range(len(string)):
        outstring += chars[string[i]] + '/'
    print(outstring)


def decode():
    string = input('please input the Morse Code you want to decode:')
    string = string.split('/')
    outstring = ''
    for i in range(len(string) - 1):
        outstring += morse[string[i]]
    outstring = outstring.lower()
    print(outstring)


while True:
    func = int(input('choose the function you want(1:encode;2:decode):'))
    if func == 1:
        encode()
    elif func == 2:
        decode()
    else:
        print('error')
