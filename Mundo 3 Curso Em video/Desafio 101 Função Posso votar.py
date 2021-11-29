def voto(n):
    from datetime import datetime
    idade = datetime.now().year - n
    if 16 <= idade < 18 or idade >= 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    elif 65 > idade >= 18:
        return f"Com {idade} anos: VOTO OBRIGATORIO"
    else:
        return f"Com {idade} anos: NÂO PODE VOTAR"

n = int(input("Ano de nascimento?"))
print(voto(n))