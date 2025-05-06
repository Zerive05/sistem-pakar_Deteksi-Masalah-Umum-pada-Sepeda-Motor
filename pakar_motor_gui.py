import tkinter as tk
from tkinter import messagebox

# Fungsi untuk mengajukan pertanyaan kepada pengguna
def tanya(pertanyaan):
    return messagebox.askyesno("Pertanyaan", pertanyaan)

# Fungsi untuk menentukan masalah berdasarkan jawaban
def konsultasi():
    if tanya("Apakah motor sulit dihidupkan?") and tanya("Apakah tidak ada letupan di knalpot?"):
        hasil = "Kemungkinan masalah: Busi mati"
    elif tanya("Apakah mesin tersendat?") and tanya("Apakah boros bensin?"):
        hasil = "Kemungkinan masalah: Karburator kotor"
    elif tanya("Apakah lampu redup?") and tanya("Apakah klakson lemah?"):
        hasil = "Kemungkinan masalah: Aki lemah"
    elif tanya("Apakah rem tidak pakem?") and tanya("Apakah ada suara berdecit?"):
        hasil = "Kemungkinan masalah: Kampas rem habis"
    else:
        hasil = "Maaf, sistem tidak dapat menentukan masalah motor Anda."
    
    # Menampilkan hasil konsultasi
    messagebox.showinfo("Hasil Konsultasi", hasil)

# Membuat jendela GUI utama
def main():
    window = tk.Tk()
    window.title("Sistem Pakar Deteksi Masalah Sepeda Motor")
    
    label = tk.Label(window, text="=== Sistem Pakar Deteksi Masalah Sepeda Motor ===", font=("Arial", 14))
    label.pack(pady=10)
    
    info_label = tk.Label(window, text="Jawab pertanyaan berikut dengan 'ya' atau 'tidak'.", font=("Arial", 10))
    info_label.pack(pady=10)
    
    konsultasi_button = tk.Button(window, text="Mulai Konsultasi", command=konsultasi, font=("Arial", 12))
    konsultasi_button.pack(pady=20)
    
    window.mainloop()

# Menjalankan program
if __name__ == "__main__":
    main()
