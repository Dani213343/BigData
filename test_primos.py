from primos import es_primo

def test_numeros_primos():
    assert es_primo(2) is True
    assert es_primo(3) is True
    assert es_primo(5) is True
    assert es_primo(7) is True
    assert es_primo(11) is True


def test_numeros_no_primos():
    assert es_primo(1) is False
    assert es_primo(4) is False
    assert es_primo(6) is False
    assert es_primo(8) is False
    assert es_primo(9) is False


def test_casos_borde():
    assert es_primo(0) is False
    assert es_primo(-3) is False
