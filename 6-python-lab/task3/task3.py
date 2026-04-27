import re
import math

def licz(fun):
    fun = fun.replace(' ', '')
    pattern = r'([+-]?\d*\.?\d*)x\^2|([+-]?\d*\.?\d*)x|([+-]?\d+\.?\d*)'
    matches = re.findall(pattern, fun)

    a, b, c = 0.0, 0.0, 0.0

    for m_a, m_b, m_c in matches:
        if m_a:
            if m_a in ('', '+'):
                a = 1.0
            elif m_a == '-':
                a = -1.0
            else:
                a = float(m_a)
        elif m_b:
            if m_b in ('', '+'):
                b = 1.0
            elif m_b == '-':
                b = -1.0
            else:
                b = float(m_b)
        elif m_c:  # Wyraz wolny
            c = float(m_c)

    if a == 0:
        raise ValueError("To nie jest równanie kwadratowe (a = 0).")

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return round(x, 2)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return sorted([round(x1, 2), round(x2, 2)], reverse=True)

wynik = licz('x^2+4x-21')
try:
    assert wynik == [3.0, -7.0], f"Błąd! Oczekiwano [3.0, -7.0], otrzymano {wynik}"
    print(f"Test zaliczony! Pierwiastki równania x^2+4x-21 to: {wynik}")
except AssertionError as e:
    print(e)