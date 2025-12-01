import os
import json
from datetime import datetime

class SistemInventaris:
    def __init__(self):
        self.inventory_file = "inventaris.txt"
        self.peminjaman_file = "peminjaman.txt"
        self.inventory = self.load_data(self.inventory_file)
        self.peminjaman = self.load_data(self.peminjaman_file)
    
    def load_data(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        return json.loads(content)
                    return []
            except json.JSONDecodeError:
                print(f"File {filename} rusak, nggawe anyar...")
                return []
        return []
    
    def save_data(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"data udah kesimpen di {filename} nih")
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_header(self, title):
        print("\n" + "="*60)
        print(f"  {title.upper()}")
        print("="*60 + "\n")
    
    # === FUNGSI INVENTARIS ===
    
    def tambah_inventaris(self):
        self.clear_screen()
        self.show_header("Tambah Inventaris")
        
        kode = input("Kode Barang: ").strip()
        if not kode:
            print("kodenya diisi duluu")
            input("\nTekan Enter untuk kembali...")
            return
        
        for item in self.inventory:
            if item['kode'] == kode:
                print(f"yahh, kode barang {kode} udah ada!")
                input("\nTekan Enter untuk kembali...")
                return
        
        nama = input("Nama Barang: ").strip()
        kategori = input("Kategori: ").strip()
        
        try:
            jumlah = int(input("Jumlah: "))
            if jumlah < 0:
                raise ValueError
        except ValueError:
            print("maaf, jumlahnya cuma bisa angka positif aja")
            input("\nTekan Enter untuk kembali...")
            return
        
        kondisi = input("Kondisi (Baik/Rusak): ").strip()
        lokasi = input("Lokasi: ").strip()
        
        item = {
            'kode': kode,
            'nama': nama,
            'kategori': kategori,
            'jumlah': jumlah,
            'kondisi': kondisi,
            'lokasi': lokasi,
            'tanggal_input': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.inventory.append(item)
        self.save_data(self.inventory, self.inventory_file)
        print("\nyeyy, inventarisnya berhasil ditambahin!")
        input("\nTekan Enter untuk kembali...")
    
    def lihat_inventaris(self):
        self.clear_screen()
        self.show_header("Daftar Inventaris")
        
        if not self.inventory:
            print("bzz bzz, tidak ada data inventaris🤖")
        else:
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. Kode: {item['kode']}")
                print(f"   Nama: {item['nama']}")
                print(f"   Kategori: {item['kategori']}")
                print(f"   Jumlah: {item['jumlah']}")
                print(f"   Kondisi: {item['kondisi']}")
                print(f"   Lokasi: {item['lokasi']}")
                print(f"   Tanggal Input: {item['tanggal_input']}")
                print("-" * 60)
        
        input("\nTekan Enter untuk kembali...")
    
    def edit_inventaris(self):
        self.clear_screen()
        self.show_header("Edit Inventaris")
        
        if not self.inventory:
            print("bzz bzz, tidak ada data inventaris🤖")
            input("\nTekan Enter untuk kembali...")
            return
        
        kode = input("mau edit id berapa nih? ").strip()
        
        for item in self.inventory:
            if item['kode'] == kode:
                print(f"\nData saat ini:")
                print(f"Nama: {item['nama']}")
                print(f"Kategori: {item['kategori']}")
                print(f"Jumlah: {item['jumlah']}")
                print(f"Kondisi: {item['kondisi']}")
                print(f"Lokasi: {item['lokasi']}")
                
                print("\n(Tekan Enter buat lanjut tanpa ngubah)")
                
                nama = input(f"Nama baru [{item['nama']}]: ").strip()
                kategori = input(f"Kategori baru [{item['kategori']}]: ").strip()
                jumlah_str = input(f"Jumlah baru [{item['jumlah']}]: ").strip()
                kondisi = input(f"Kondisi baru [{item['kondisi']}]: ").strip()
                lokasi = input(f"Lokasi baru [{item['lokasi']}]: ").strip()
                
                if nama:
                    item['nama'] = nama
                if kategori:
                    item['kategori'] = kategori
                if jumlah_str:
                    try:
                        jumlah = int(jumlah_str)
                        if jumlah >= 0:
                            item['jumlah'] = jumlah
                    except ValueError:
                        print("yahh jumlahnya gak valid, coba lagi yaa")
                if kondisi:
                    item['kondisi'] = kondisi
                if lokasi:
                    item['lokasi'] = lokasi
                
                self.save_data(self.inventory, self.inventory_file)
                print("\nyeyy, inventaris berhasil diupdate!")
                input("\nTekan Enter untuk kembali...")
                return
        
        print(f"kode barang {kode} belum terdaftar nih")
        input("\nTekan Enter untuk kembali...")
    
    def hapus_inventaris(self):
        self.clear_screen()
        self.show_header("Hapus Inventaris")
        
        if not self.inventory:
            print("bzz bzz, tidak ada data inventaris🤖")
            input("\nTekan Enter untuk kembali...")
            return
        
        kode = input("Mau hapus kode barang yang mana? ").strip()
        
        for i, item in enumerate(self.inventory):
            if item['kode'] == kode:
                print(f"\nBarang yang akan dihapus:")
                print(f"Kode: {item['kode']}")
                print(f"Nama: {item['nama']}")
                
                konfirmasi = input("\nYakin mau hapus? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    self.inventory.pop(i)
                    self.save_data(self.inventory, self.inventory_file)
                    print("\nckring, inventaris berhasil dihapus!")
                else:
                    print("\nPenghapusan dibatalkan.")
                
                input("\nTekan Enter untuk kembali...")
                return
        
        print(f"kode barang {kode} belum terdaftar nih")
        input("\nTekan Enter untuk kembali...")
    
    # === FUNGSI PEMINJAMAN ===
    
    def tambah_peminjaman(self):
        self.clear_screen()
        self.show_header("Tambah Peminjaman")
        
        id_pinjam = input("ID Peminjaman: ").strip()
        if not id_pinjam:
            print(" ID peminjaman masih kosong nih, isi dulu yaa")
            input("\nTekan Enter untuk kembali...")
            return
        
        # Cek duplikasi
        for p in self.peminjaman:
            if p['id_pinjam'] == id_pinjam:
                print(f"yahh ID peminjaman {id_pinjam} udah ada!")
                input("\nTekan Enter untuk kembali...")
                return
        
        kode_barang = input("Kode Barang: ").strip()
        
        barang_ada = False
        for item in self.inventory:
            if item['kode'] == kode_barang:
                barang_ada = True
                print(f"   → Barang: {item['nama']}")
                break
        
        if not barang_ada:
            print(f" Kode barang {kode_barang} yang kamu cari belum ada")
        
        peminjam = input("Nama Peminjam: ").strip()
        
        try:
            jumlah = int(input("Jumlah Dipinjam: "))
            if jumlah <= 0:
                raise ValueError
        except ValueError:
            print("Jumlah harus angka positif yaa")
            input("\nTekan Enter untuk kembali...")
            return
        
        tanggal_pinjam = input("Tanggal Pinjam (YYYY-MM-DD) [Enter=hari ini]: ").strip()
        if not tanggal_pinjam:
            tanggal_pinjam = datetime.now().strftime("%Y-%m-%d")
        
        tanggal_kembali = input("Tanggal Kembali (YYYY-MM-DD): ").strip()
        status = input("Status (Dipinjam/Dikembalikan) [Dipinjam]: ").strip() or "Dipinjam"
        
        pinjam = {
            'id_pinjam': id_pinjam,
            'kode_barang': kode_barang,
            'peminjam': peminjam,
            'jumlah': jumlah,
            'tanggal_pinjam': tanggal_pinjam,
            'tanggal_kembali': tanggal_kembali,
            'status': status,
            'tanggal_input': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.peminjaman.append(pinjam)
        self.save_data(self.peminjaman, self.peminjaman_file)
        print("\nckring, peminjaman berhasil ditambahin")
        input("\nTekan Enter untuk kembali...")
    
    def lihat_peminjaman(self):
        self.clear_screen()
        self.show_header("Daftar Peminjaman")
        
        if not self.peminjaman:
            print("bzz bzz, tidak ada data peminjaman🤖")
        else:
            for i, p in enumerate(self.peminjaman, 1):
                print(f"{i}. ID Peminjaman: {p['id_pinjam']}")
                print(f"   Kode Barang: {p['kode_barang']}")
                print(f"   Peminjam: {p['peminjam']}")
                print(f"   Jumlah: {p['jumlah']}")
                print(f"   Tanggal Pinjam: {p['tanggal_pinjam']}")
                print(f"   Tanggal Kembali: {p['tanggal_kembali']}")
                print(f"   Status: {p['status']}")
                print("-" * 60)
        
        input("\nTekan Enter untuk kembali...")
    
    def edit_peminjaman(self):
        self.clear_screen()
        self.show_header("Edit Peminjaman")
        
        if not self.peminjaman:
            print("bzz bzz, tidak ada data peminjaman🤖")
            input("\nTekan Enter untuk kembali...")
            return
        
        id_pinjam = input("Masukkan ID peminjaman yang akan diedit: ").strip()
        
        for p in self.peminjaman:
            if p['id_pinjam'] == id_pinjam:
                print(f"\nData saat ini:")
                print(f"Kode Barang: {p['kode_barang']}")
                print(f"Peminjam: {p['peminjam']}")
                print(f"Jumlah: {p['jumlah']}")
                print(f"Tanggal Pinjam: {p['tanggal_pinjam']}")
                print(f"Tanggal Kembali: {p['tanggal_kembali']}")
                print(f"Status: {p['status']}")
                
                print("\n(Tekan Enter untuk tidak mengubah)")
                
                kode_barang = input(f"Kode Barang baru [{p['kode_barang']}]: ").strip()
                peminjam = input(f"Peminjam baru [{p['peminjam']}]: ").strip()
                jumlah_str = input(f"Jumlah baru [{p['jumlah']}]: ").strip()
                tanggal_pinjam = input(f"Tanggal Pinjam baru [{p['tanggal_pinjam']}]: ").strip()
                tanggal_kembali = input(f"Tanggal Kembali baru [{p['tanggal_kembali']}]: ").strip()
                status = input(f"Status baru [{p['status']}]: ").strip()
                
                if kode_barang:
                    p['kode_barang'] = kode_barang
                if peminjam:
                    p['peminjam'] = peminjam
                if jumlah_str:
                    try:
                        jumlah = int(jumlah_str)
                        if jumlah > 0:
                            p['jumlah'] = jumlah
                    except ValueError:
                        print("Jumlah gak valid, coba lagi yaa")
                if tanggal_pinjam:
                    p['tanggal_pinjam'] = tanggal_pinjam
                if tanggal_kembali:
                    p['tanggal_kembali'] = tanggal_kembali
                if status:
                    p['status'] = status
                
                self.save_data(self.peminjaman, self.peminjaman_file)
                print("\nckring, peminjaman berhasil diupdate!")
                input("\nTekan Enter untuk kembali...")
                return
        
        print(f" ID peminjaman {id_pinjam} belum terdaftar nih")
        input("\nTekan Enter untuk kembali...")
    
    def hapus_peminjaman(self):
        self.clear_screen()
        self.show_header("Hapus Peminjaman")
        
        if not self.peminjaman:
            print("bzz bzz, tidak ada data peminjaman🤖")
            input("\nTekan Enter untuk kembali...")
            return
        
        id_pinjam = input("Masukkin ID peminjaman yang mau kamu hapus: ").strip()
        
        for i, p in enumerate(self.peminjaman):
            if p['id_pinjam'] == id_pinjam:
                print(f"\nPeminjaman yang akan dihapus:")
                print(f"ID: {p['id_pinjam']}")
                print(f"Peminjam: {p['peminjam']}")
                print(f"Kode Barang: {p['kode_barang']}")
                
                konfirmasi = input("\nYakin ingin menghapus? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    self.peminjaman.pop(i)
                    self.save_data(self.peminjaman, self.peminjaman_file)
                    print("\nckring, peminjaman berhasil dihapus!")
                else:
                    print("\nengga jadi hapus yaa")
                
                input("\nTekan Enter untuk kembali...")
                return
        
        print(f"ID peminjaman {id_pinjam} belum ada nih")
        input("\nTekan Enter untuk kembali...")
    
    
    def menu_inventaris(self):
        while True:
            self.clear_screen()
            self.show_header("Menu Inventaris")
            print("1. Tambah Inventaris")
            print("2. Lihat Inventaris")
            print("3. Edit Inventaris")
            print("4. Hapus Inventaris")
            print("0. Kembali ke Menu Utama")
            
            pilihan = input("\nPilih menu: ").strip()
            
            if pilihan == '1':
                self.tambah_inventaris()
            elif pilihan == '2':
                self.lihat_inventaris()
            elif pilihan == '3':
                self.edit_inventaris()
            elif pilihan == '4':
                self.hapus_inventaris()
            elif pilihan == '0':
                break
            else:
                print("Pilihan kamu gak valid nih!")
                input("\nTekan Enter untuk kembali...")
    
    def menu_peminjaman(self):
        """Menu peminjaman"""
        while True:
            self.clear_screen()
            self.show_header("Menu Peminjaman")
            print("1. Tambah Peminjaman")
            print("2. Lihat Peminjaman")
            print("3. Edit Peminjaman")
            print("4. Hapus Peminjaman")
            print("0. Kembali ke Menu Utama")
            
            pilihan = input("\nPilih menu: ").strip()
            
            if pilihan == '1':
                self.tambah_peminjaman()
            elif pilihan == '2':
                self.lihat_peminjaman()
            elif pilihan == '3':
                self.edit_peminjaman()
            elif pilihan == '4':
                self.hapus_peminjaman()
            elif pilihan == '0':
                break
            else:
                print("Pilihan kamu gak valid nih!")
                input("\nTekan Enter untuk kembali...")
    
    def run(self):
        while True:
            self.clear_screen()
            self.show_header("Sistem Inventaris Kampus")
            print("1. Menu Inventaris")
            print("2. Menu Peminjaman")
            print("0. Keluar")
            
            pilihan = input("\nPilih menu: ").strip()
            
            if pilihan == '1':
                self.menu_inventaris()
            elif pilihan == '2':
                self.menu_peminjaman()
            elif pilihan == '0':
                self.clear_screen()
                print("\n" + "="*60)
                print("  Terima kasih telah menggunakan Sistem Inventaris Kampus")
                print("                   see you next time! 👋")
                print("="*60 + "\n")
                break
            else:
                print("pilihan kamu gak valid nih!")
                input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
    app = SistemInventaris()
    app.run()