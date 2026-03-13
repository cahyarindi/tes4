"""
check_number.py

Tujuan:
    Menyediakan fungsi sederhana untuk memeriksa apakah sebuah nilai
    berada dalam rentang bilangan positif kurang dari 100.

Fitur Utama:
    - Validasi nilai agar tidak None
    - Pemeriksaan rentang nilai (0 < n < 100)

Penulis:
    Nama Anda

Tanggal Pembaruan Terakhir:
    13 Maret 2026
"""


def check(n):
    """
    Periksa apakah nilai berada dalam rentang 1 sampai 99.

    Pastikan parameter tidak bernilai None dan merupakan bilangan
    yang lebih besar dari 0 serta lebih kecil dari 100.

    Parameters:
        n (int | float): Nilai numerik yang akan diperiksa.

    Returns:
        bool: True jika n tidak None dan berada pada rentang
        0 < n < 100, False jika tidak memenuhi syarat.

    Contoh:
        >>> check(50)
        True
        >>> check(0)
        False
        >>> check(None)
        False
    """
    return n is not None and 0 < n < 100


if __name__ == "__main__":
    print(check(50))