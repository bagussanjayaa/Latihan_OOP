# Main.py

import time
from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_view import InputForm
from view.mahasiswa import TampilMahasiswa

def menu():
    data_mahasiswa = DataMahasiswa()

    while True:
        pilihan = input("[ (T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar ]: ").lower()

        if pilihan == 't':
            nim, nama, tugas, uts, uas = InputForm.form_input()
            mahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
            data_mahasiswa.tambah(mahasiswa)
        elif pilihan == 'u':
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama, tugas, uts, uas = InputForm.form_input()[1:]
            data_mahasiswa.ubah(nim, nama, tugas, uts, uas)
        elif pilihan == 'h':
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus(nim)
        elif pilihan == 'l':
            TampilMahasiswa.tampilkan_list(data_mahasiswa.lihat())
        elif pilihan == 'c':
            nim = input("Masukkan NIM mahasiswa yang dicari: ")
            mahasiswa = data_mahasiswa.cari(nim)
            TampilMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == 'k':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        time.sleep(1)

if __name__ == "__main__":
    menu()
