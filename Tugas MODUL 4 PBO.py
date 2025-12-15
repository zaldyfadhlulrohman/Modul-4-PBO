from abc import ABC, abstractmethod
# ================================
# 1. ABSTRACT CLASS
# ================================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama
    @abstractmethod
    def akses(self):
        pass
# ================================
# 4. CUSTOM EXCEPTION
# ================================
class PoinTidakValidError(Exception):
    """Dilempar jika poin bernilai negatif."""
    pass
# ================================
# 2. CLASS TURUNAN + SPECIAL METHODS
# ================================
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        if poin < 0:
            raise PoinTidakValidError("Poin tidak boleh negatif!")
        self.poin = poin

    def akses(self):
        return f"Member {self.nama} memiliki akses penuh ke fitur premium."

    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        if not isinstance(other, Member):
            return NotImplemented
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)

# ================================
# 3. INPUT + EXCEPTION HANDLING
# ================================
def input_poin(prompt):
    while True:
        try:
            nilai = input(prompt).strip()

            if nilai == "":
                raise ValueError("Input tidak boleh kosong.")

            poin = int(nilai)

            if poin < 0:
                raise PoinTidakValidError("Poin tidak boleh negatif!")

            return poin

        except ValueError as ve:
            print(f"[ValueError] {ve}")
        except PoinTidakValidError as pe:
            print(f"[PoinTidakValidError] {pe}")
# ================================
# PROGRAM UTAMA
# ================================
if __name__ == "__main__":
    print("=== Program Member Premium ===")
    # Input 2 member
    nama1 = input("Masukkan nama member 1: ")
    poin1 = input_poin("Masukkan poin member 1: ")
    nama2 = input("Masukkan nama member 2: ")
    poin2 = input_poin("Masukkan poin member 2: ")
    try:
        m1 = Member(nama1, poin1)
        m2 = Member(nama2, poin2)
    except PoinTidakValidError as e:
        print("Gagal membuat member:", e)
    else:
        # Tampilkan info member
        print("\n=== OUTPUT ===")
        print(m1)
        print(m2)
        # Jumlah poin
        print("Total poin (m1 + m2):", m1 + m2)
        # Panjang nama
        print(f"Panjang nama {m1.nama} adalah:", len(m1))
        # Akses member
        print("Akses m1:", m1.akses())
        print("Akses m2:", m2.akses())
    # Uji exception negatif
    print("\n=== UJI ERROR NEGATIF ===")
    try:
        tes = Member("Tester", -10)
    except PoinTidakValidError as e:
        print("Berhasil menangkap error:", e)
