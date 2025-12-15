class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"
    def __gt__(self, other):
        return self.nilai > other.nilai
    def __add__(self, other):
        return self.nilai + other.nilai
    def __mul__(self, faktor):
        return self.nilai * faktor
    # b. __len__ -> panjang nama mahasiswa
    def __len__(self):
        return len(self.nama)
    # c. __eq__ -> sama jika nilai sama
    def __eq__(self, other):
        return self.nilai == other.nilai
# d. Buat objek mahasiswa lain
m1 = Mahasiswa("Zaldy", 100)
m2 = Mahasiswa("Agus", 85)
m3 = Mahasiswa("Wasa", 100)
# Tampilkan representasi string
print(m1)
print(m2)
print(m3)
# Panjang nama (__len__)
print("Panjang nama Wasa =", len(m3))
# Perbandingan kesetaraan nilai
print("Apakah Zaldy dan Agus punya nilai sama?", m1 == m2)
# Operasi matematika
print("m1 + m3 =", m1 + m3)
print("m2 * 2 =", m2 * 2)
# Sorting berdasarkan nilai
list_mhs = [m1, m2, m3]
urutan = sorted(list_mhs, key=lambda x: x.nilai)
print("\nUrutan mahasiswa berdasarkan nilai:")
for m in urutan:
    print(m)
