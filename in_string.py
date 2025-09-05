def check_vowels():
    nombre = str(input("Nombre: ")).lower()
    a = "a" in nombre
    e = "e" in nombre
    i = "i" in nombre
    o = "o" in nombre
    u = "u" in nombre
    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")
