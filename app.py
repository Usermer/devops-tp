import re


def nettoyer_texte(texte):
    """Supprime les espaces inutiles et normalise la casse."""
    return " ".join(texte.strip().split()).lower()


def compter_mots(texte):
    """Retourne le nombre de mots contenus dans un texte."""
    return len(nettoyer_texte(texte).split()) if texte.strip() else 0


def est_palindrome(texte):
    """Vérifie si un texte se lit pareil dans les deux sens."""
    normalise = re.sub(r"[^a-zA-Z0-9]", "", texte).lower()
    return normalise == normalise[::-1]


def email_valide(email):
    """Vérifie une adresse e-mail simple."""
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))


if __name__ == "__main__":
    phrase = "Python est simple et puissant"
    print(f"Texte : {nettoyer_texte(phrase)}")
    print(f"Nombre de mots : {compter_mots(phrase)}")
