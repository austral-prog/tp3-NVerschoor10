def check_vowels():
    nombre = input("Nombre: ").lower()
    a = "a" in nombre
    e = "e" in nombre
    i = "i" in nombre
    o = "o" in nombre
    u = "u" in nombre
    print("Contiene a:", {a})
    print("Contiene e:", {e})
    print("Contiene i:", {i})
    print("Contiene o:", {o})
    print("Contiene u:", {u})
