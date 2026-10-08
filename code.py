txt = """code"""

txt = txt.split()

for member in txt:
    original = ???(member) - 1001
    caractere = chr(int(str(original), 2))
    print(caractere, end="")

# sometimes it's doing shit with somes characterer so that's okay if some sentences are wierd.