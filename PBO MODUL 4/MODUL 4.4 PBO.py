class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass
class UmurTerlaluMudaError(Exception):
    """Kesalahan jika umur terlalu muda (<5)."""
    pass
class UmurTerlaluTuaError(Exception):
    """Kesalahan jika umur terlalu tua (>100)."""
    pass
class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur tidak memenuhi syarat membuat akun."""
    pass
def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal 100 tahun.")
    return umur
def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya boleh dibuat oleh umur 18+.")
    return "Akun berhasil dibuat!"
if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
        except ValueError:
            print("Input harus berupa angka bulat!")
        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print("Error:", e)
        else:
            print("Umur valid:", umur)
            break   # keluar loop jika umur valid
    # Coba buat akun
    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print("Gagal membuat akun:", e)
