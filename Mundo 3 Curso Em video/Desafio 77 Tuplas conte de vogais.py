y = "aprender", "programar", "linguagem", 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
x = "bcdfghjkltmnpqrsvwyxz"
for a in y:
    h = a
    for n in x:
        h = h.replace(n, " ")
        if n == "z":
            print(f"Na palavra {a.upper()} temos a seguintes vogais: {h.upper().strip()}")