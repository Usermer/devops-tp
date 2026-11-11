from app import compter_mots, email_valide, est_palindrome, nettoyer_texte


def test_nettoyer_texte_supprime_les_espaces():
    assert nettoyer_texte("  Bonjour   LE monde  ") == "bonjour le monde"


def test_nettoyer_texte_accepte_une_chaine_vide():
    assert nettoyer_texte("   ") == ""


def test_compter_mots():
    assert compter_mots("Python est simple") == 3


def test_compter_mots_avec_espaces_multiples():
    assert compter_mots("  un   deux \n trois ") == 3


def test_compter_mots_avec_texte_vide():
    assert compter_mots("") == 0


def test_palindrome():
    assert est_palindrome("Esope reste ici et se repose") is True


def test_texte_non_palindrome():
    assert est_palindrome("GitHub Actions") is False


def test_palindrome_ignore_la_ponctuation():
    assert est_palindrome("Ésope ?") is False
    assert est_palindrome("A man, a plan, a canal: Panama") is True


def test_email_valide():
    assert email_valide("utilisateur@example.com") is True


def test_email_invalide_sans_arobase():
    assert email_valide("utilisateurexample.com") is False


def test_email_invalide_sans_domaine():
    assert email_valide("utilisateur@") is False


def test_email_invalide_avec_espace():
    assert email_valide("user name@example.com") is False
