class Pelanggan:
    def __init__(self, nama, alamat, telepon):
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon

class Laundry:
    def __init__(self):
        self.daftar_pelanggan = []

    def tambah_pelanggan(self, nama, alamat, telepon):
        pelanggan_baru = Pelanggan(nama, alamat, telepon)
        self.daftar_pelanggan.append(pelanggan_baru)
        print("Pelanggan", nama, "telah ditambahkan.")

    def lihat_pelanggan(self):
        if len(self.daftar_pelanggan) == 0:
            print("Belum ada pelanggan terdaftar.")
        else:
            print("Daftar Pelanggan:")
            for pelanggan in self.daftar_pelanggan:
                print("Nama:", pelanggan.nama)
                print("Alamat:", pelanggan.alamat)
                print("Telepon:", pelanggan.telepon)
                print("-----")

# Inisialisasi objek Laundry
laundry = Laundry()

# Menu
while True:
    print("\nSelamat datang di aplikasi Laundry")
    print("1. Tambah Pelanggan")
    print("2. Lihat Daftar Pelanggan")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        nama = input("Masukkan nama pelanggan: ")
        alamat = input("Masukkan alamat pelanggan: ")
        telepon = input("Masukkan nomor telepon pelanggan: ")
        laundry.tambah_pelanggan(nama, alamat, telepon)
    elif pilihan == "2":
        laundry.lihat_pelanggan()
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")