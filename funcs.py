def get_summ(one, two, delimeter='&'):
    #s = one + delimeter + two
    #s.upper()
    s = (f'{one} {delimeter} {two}').upper()
    return s

if __name__ == '__main__':
    print(get_summ('Learn', 'python'))

#print()