def verificar_nota(nota):
    if nota > 5:
        return "Aprovado"
    elif 3 <= nota <= 5:
        return "Recuperação"
    else:
        return "Reprovado"
