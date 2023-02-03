variavel = "esta é uma variavel de teste"

def getStr(variavel, first, last):
    try:
        comeco = variavel.index(first) + len(first)
        final = variavel.index(last, comeco)
        return variavel[comeco:final]
    except ValueError:
        return ""

print(getStr(variavel, "uma ", " de"))