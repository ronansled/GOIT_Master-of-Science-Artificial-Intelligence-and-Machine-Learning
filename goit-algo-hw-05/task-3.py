import timeit
import os
import chardet


# ---------------------------------------------------------
# 1. АЛГОРИТМ КНУТА–МОРРІСА–ПРАТТА (KMP)
# ---------------------------------------------------------
def kmp_search(text, pattern):
    if pattern == "":
        return 0

    # Префікс-функція
    lps = [0] * len(pattern)
    j = 0

    # Будуємо lps-масив
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    # Пошук
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j  # знайдено
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


# ---------------------------------------------------------
# 2. АЛГОРИТМ РАБІНА–КАРПА (RK)
# ---------------------------------------------------------
def rabin_karp(text, pattern):
    if pattern == "":
        return 0

    m, n = len(pattern), len(text)
    
    # Перевірка граничного випадку
    if m > n:
        return -1
    
    base = 256
    mod = 10**9 + 7

    p_hash = 0
    t_hash = 0
    h = pow(base, m - 1, mod)

    # Початкові хеші
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod

    # Пошук
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t_hash = (t_hash - ord(text[i]) * h) % mod
            t_hash = (t_hash * base + ord(text[i + m])) % mod
            if t_hash < 0:
                t_hash += mod

    return -1


# ---------------------------------------------------------
# 3. АЛГОРИТМ БОЄРА–МУРА (BM)
# ---------------------------------------------------------
def boyer_moore(text, pattern):
    if pattern == "":
        return 0

    m = len(pattern)
    n = len(text)
    
    # Перевірка граничного випадку
    if m > n:
        return -1

    # Таблиця зсувів (словник замість списку для підтримки Unicode)
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s
        else:
            # Використовуємо .get() для безпечного доступу до словника
            shift = j - bad_char.get(text[s + j], -1)
            s += max(1, shift)

    return -1


# ---------------------------------------------------------
# 4. ЧИТАННЯ СТАТЕЙ
# ---------------------------------------------------------
def load_file(filename):
    """Завантажує файл із автоматичним визначенням кодування"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл не знайдено: {filepath}")
    
    # Визначаємо кодування автоматично
    with open(filepath, "rb") as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result.get('encoding', 'utf-8')
    
    # Читаємо файл з визначеним кодуванням
    try:
        with open(filepath, "r", encoding=encoding) as f:
            return f.read()
    except (UnicodeDecodeError, LookupError):
        # Fallback на utf-8 з ігноруванням помилок
        with open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            return f.read()


# ---------------------------------------------------------
# 5. БЕНЧМАРК ДЛЯ 1 АЛГОРИТМУ, 1 ТЕКСТУ, 1 ПАТЕРНА
# ---------------------------------------------------------
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=5)


def format_result(algo_name, result, time_taken):
    """Форматує результат пошуку"""
    if result == -1:
        status = "❌ НЕ ЗНАЙДЕНО"
    else:
        status = f"✓ ЗНАЙДЕНО на позиції {result}"
    
    return f"{algo_name:12} | {status:30} | {time_taken:.6f} сек"


# ---------------------------------------------------------
# 6. ЗАГАЛЬНИЙ ЗАПУСК
# ---------------------------------------------------------
def main():
    try:
        text1 = load_file("article_1.txt")
        text2 = load_file("article_2.txt")
    except FileNotFoundError as e:
        print(f"Помилка: {e}")
        return

    # Перевірка мінімальної довжини тексту
    if len(text1) < 150:
        print("Помилка: article_1.txt занадто короткий")
        return
    if len(text2) < 220:
        print("Помилка: article_2.txt занадто короткий")
        return




    # Патерни — приклади
    real1 = text1[100:150]          # існує
    real2 = text2[200:220]          # існує
    fake = "!!!3 Піци 4 сира з сирними бортиками!!!"

    algorithms = [
        ("KMP", kmp_search),
        ("Rabin-Karp", rabin_karp),
        ("Boyer-Moore", boyer_moore),
    ]

    for i, (text, real) in enumerate([(text1, real1), (text2, real2)], start=1):
        print(f"\n{'='*80}")
        print(f"{'ТЕКСТ №' + str(i):^80}")
        print(f"{'='*80}")

        print(f"\n📌 РЕАЛЬНИЙ ПІДРЯДОК: '{real}'")
        print(f"{'-'*80}")
        for name, algo in algorithms:
            result = algo(text, real)
            t = measure_time(algo, text, real)
            print(format_result(name, result, t))

        print(f"\n❌ ВИГАДАНИЙ ПІДРЯДОК: '{fake}'")
        print(f"{'-'*80}")
        for name, algo in algorithms:
            result = algo(text, fake)
            t = measure_time(algo, text, fake)
            print(format_result(name, result, t))

    print(f"\n{'='*80}")
    print("✅ Готово! Дивіться результати вище.")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
