# view/mahasiswa.py

class TampilMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        print("Daftar Nilai Mahasiswa")
        print("-----------------------------------------------------------------------------------------")
        print("| NO | NIM           | NAMA                 | TUGAS    | UTS      | UAS      | AKHIR    |")
        print("-----------------------------------------------------------------------------------------")
        if not data_mahasiswa:
            print("|                                    TIDAK ADA DATA                                     |")
            print("-----------------------------------------------------------------------------------------")
        else:
            for i, (nim, data) in enumerate(data_mahasiswa.items(), start=1):
                print(f"| {i:<2} | {nim:<13} | {data.nama:<20} | {data.tugas:<8.2f} | {data.uts:<8.2f} | {data.uas:<8.2f} | {data.nilai_akhir:<8.2f} |")
                print("-----------------------------------------------------------------------------------------")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(f"Nama: {mahasiswa.nama}")
            print(f"NIM: {mahasiswa.nim}")
            print(f"Tugas: {mahasiswa.tugas}")
            print(f"UTS: {mahasiswa.uts}")
            print(f"UAS: {mahasiswa.uas}")
            print(f"Nilai Akhir: {mahasiswa.nilai_akhir}")
        else:
            print("Mahasiswa tidak ditemukan.")
