# view/input_view.py

class InputForm:
    @staticmethod
    def form_input():
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        return nim, nama, tugas, uts, uas
