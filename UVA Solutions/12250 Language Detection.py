w = ''
c = 1
while w != "#":

    w = input()

    if w == 'HELLO':
        print(f"""Case {c}: ENGLISH""")
    
    elif w == 'HOLA':
        print(f"""Case {c}: SPANISH""")

    elif w == 'HALLO':
        print(f"""Case {c}: GERMAN""")

    elif w == 'BONJOUR':
        print(f"""Case {c}: FRENCH""")

    elif w == 'CIAO':
        print(f"""Case {c}: ITALIAN""")

    elif w == 'ZDRAVSTVUJTE':
        print(f"""Case {c}: RUSSIAN""")

    elif w == '#':
        break

    else: print(f"""Case {c}: UNKNOWN""")
    c += 1