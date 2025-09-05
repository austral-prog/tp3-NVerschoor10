def check_vowels():
    nombre = input("Nombre: ").lower()
    a = "a" in nombre
    e = "e" in nombre
    i = "i" in nombre
    o = "o" in nombre
    u = "u" in nombre
    print("contiene a:", {a})
    print("contiene e:", {e})
    print("contiene i:", {i})
    print("contiene o:", {o})
    print("contiene u:", {u})
