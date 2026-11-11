def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Impossible de diviser par zéro")
    return a / b


def moyenne(valeurs):
    if not valeurs:
        raise ValueError("La liste ne peut pas être vide")
    return sum(valeurs) / len(valeurs)


if __name__ == "__main__":
    result = addition(5, 3)
    print("The sum is:", result)