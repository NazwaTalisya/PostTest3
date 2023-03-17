#Nama : Nazwa Talisya Inaya
#NIM : 2209116063
#Kelas : Sistem Informasi B '22
from prettytable import PrettyTable
class Penerbangan:
    def __init__(self ,NamaLengkap, NoHp, KodePenerbangan, TanggalPenerbangan):
        self.NamaLengkap = NamaLengkap
        self.NoHp = NoHp
        self.KodePenerbangan = KodePenerbangan
        self.TanggalPenerbangan = TanggalPenerbangan
        self.next = None

class Linkedlist1:
    def __init__(self):
        self.head = None

    def tambah(self, NamaLengkap, NoHp, KodePenerbangan, TanggalPenerbangan):
        new_penerbangan = Penerbangan(NamaLengkap, NoHp, KodePenerbangan, TanggalPenerbangan)

        if not self.head:
            self.head = new_penerbangan
        else:
            current = self.head
            while current.next:
                current = current.next
                current.next = new_penerbangan

    def lihat(self):
        if not self.head:
            print("Penerbangan Tidak Ada")
        else:
            current = self.head
            table = PrettyTable(["Nama", "No-Hp", "Kode Penerbangan", "Tanggal Penerbangan"])
            while current:
                table.add_row([current.NamaLengkap, current.NoHp, current.KodePenerbangan, current.TanggalPenerbangan])
                current = current.next
            print(table)

    def cari(self, KodePenerbangan):
        current = self.head
        while current is not None:
            if current.KodePenerbangan == KodePenerbangan:
                return current
            current = current.next
        return None


    def hapus(self, KodePenerbangan):
        current = self.head
        if current and current.KodePenerbangan == KodePenerbangan:
            self.head = current.next
            current = None
            print("Data Penerbangan Telah Di Hapus")
            return
        prev = None
        while current and current.KodePenerbangan != KodePenerbangan:
            prev = current
            current = current.next
        if current is None:
            print("Data Penerbangan Tidak Ditemukan")
            return
        prev.next = current.next
        current = None
        print("Kode Penerbangan Berhasil Dihapus")


list = Linkedlist1()


while True:
    print("""
    |=======================================|
    |--------> Riwayat Penerbangan <--------|
    |=======================================|
    |1. Menambah Data Riwayat Penerbangan   |
    |2. Melihat data Riwayat Penerbangan    |
    |3. Mencari Data Riwayat Penerbangan    |
    |4. Menghapus Data Riwayat Penerbangan  |
    |5. Exit                                |
    |=======================================|
    """)
    pilih = input("Silahkan Memilih Menu: ")
    if pilih == "1":
        NamaLengkap = input("Silahkan Isi Nama Lengkap : ")
        NoHp = input("Silahkan Isi No-Hp : ")
        KodePenerbangan = input("Silahkan Isi Kode Penerbangan : ")
        TanggalPenerbangan = input("Silahkan Isi Tanggal Penerbangan :")
        list.tambah(NamaLengkap, NoHp, KodePenerbangan, TanggalPenerbangan)
        print("Berhasil, Silahkan Lihat Data Di Nomor 2")
    
    elif pilih == "2":
        list.lihat()
        
    elif pilih == "3":
        N = input("Silahkan Isi Kode Penerbangan Yang Ingin Dicari: ")
        Penerbangan = list.cari(KodePenerbangan)
        if Penerbangan:
            print(f"Nama Dengan Kode Penerbangan {KodePenerbangan} Telah Ditemukan")
            print(f"Nama  : {Penerbangan.NamaLengkap}")
            print(f"No-Hp : {Penerbangan.NoHp}")
            print(f"Kode Penerbangan : {Penerbangan.KodePenerbangan}")
            print(f"Tanggal Penerbangan : {Penerbangan.TanggalPenerbangan}")
        else:
            print(f"Nama Dengan Kode Penerbangan {KodePenerbangan} Tidak Ditemukan.")

    elif pilih == "4":
        list.lihat()
        KodePenerbangan = input("Silahkan Isi Kode Penerbangan Yang Ingin Dihapus: ")
        Penerbangan = list.cari(KodePenerbangan)
        if Penerbangan:
            list.hapus(KodePenerbangan)
        else:
            print(f"Penerbangan Dengan Kode Tersebut {KodePenerbangan} Tidak Ditemukan.")

    elif pilih == "5":
        exit()