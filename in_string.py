def check_vowels():
    nombre = input("Nombre: ").lower()
    a = "a" in nombre
    e = "e" in nombre
    i = "i" in nombre
    o = "o" in nombre
    u = "u" in nombre
    print(f"Contiene a: {a}")
    print(f"contiene e: {e}")
    print(f"contiene i: {i}")
    print(f"contiene o: {o}")
    print(f"contiene u: {u}")
check_vowels()
