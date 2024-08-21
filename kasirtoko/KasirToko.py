import tkinter as tk
from tkinter import ttk, messagebox
import csv
import pandas as pd

class KasirToko:
    def __init__(self, root):
        self.root = root
        self.root.title("Kasir Toko")

        self.kasirtoko = []

        # Fungsi dibawah ini untuk membuat tabel untuk menampilkan rincian pembelian
        columns = ("Nama_Barang","Satuan","Harga_Satuan","Total_Harga")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10)

        # untuk tempat menginputkan data
        nama_label = tk.Label(root, text="Nama_Barang:")
        nama_label.pack()
        self.nama_entry = tk.Entry(root)
        self.nama_entry.pack()

        satuan_label = tk.Label(root, text="Satuan:")
        satuan_label.pack()
        self.satuan_entry = tk.Entry(root)
        self.satuan_entry.pack()

        harga_label = tk.Label(root, text="Harga_Satuan:")
        harga_label.pack()
        self.harga_entry = tk.Entry(root)
        self.harga_entry.pack()

        jumlah_label = tk.Label(root, text="Total_Harga:")
        jumlah_label.pack()
        self.jumlah_entry = tk.Entry(root)
        self.jumlah_entry.pack()

        # Button untuk menambah seluruh data yang telah diinputkan
        add_button = tk.Button(root, text="Submit", command=self.add_pembelian)
        add_button.pack(pady=10)

        save_button = tk.Button(root, text="Simpan ke CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

        calculate_button = tk.Button(root, text="Total Pemasukan Toko", command=self.jumlahpembayaran)
        calculate_button.pack(pady=10)

        # Load data dari CSV
        self.load_hasilpembelian()

    def load_hasilpembelian(self):
        try:
            with open("catatan_pemasukan_toko.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(row["Nama_Barang"], row["Satuan"],row["Harga_Satuan"],row["Total_Harga"]))
                    self.kasirtoko.append(row)
        except FileNotFoundError:
            # untuk mengantisipasi jika file tidak ditemukan
            pass

    def jumlahpembayaran(self):
            try:
                # Membaca data dari file CSV menggunakan pandas
                df = pd.read_csv("catatan_pemasukan_toko.csv")

                # Menghitung total data pada kolom "Uang"
                total = df["Total_Harga"].sum()

                # Menampilkan hasil penjumlahan
                messagebox.showinfo("Total Pemasukan",f"Total Pemasukan: {total}")

            except FileNotFoundError:
                print("File tabungan.csv tidak ditemukan.")
            except KeyError:
                print("Kolom Uang tidak ditemukan dalam file CSV.")

    def add_pembelian(self):
        # untuk Mendapatkan nilai dari data yang sudah diinputkan
        nama = self.nama_entry.get()
        satuan = self.satuan_entry.get()        
        harga = self.harga_entry.get()
        jumlah = self.jumlah_entry.get()        
        
        # untuk menyimpan data diCSV
        self.kasirtoko.append({"Nama_Barang": nama, "Satuan": satuan, "Harga_Satuan": harga, "Total_Harga": jumlah})

        # Menambahkan data pengeluaran ke Treeview
        self.tree.insert("", "end", values=(nama, satuan, harga, jumlah))

        # untuk mengosongkan input data setelah ditambahkan
        self.nama_entry.delete(0, tk.END)
        self.satuan_entry.delete(0, tk.END)        
        self.harga_entry.delete(0, tk.END)
        self.jumlah_entry.delete(0, tk.END)        
   
    def save_to_csv(self):
    # Membuat DataFrame dari data hasil penjualan
        df = pd.DataFrame(self.kasirtoko)

    # Menyimpan DataFrame ke dalam file CSV tanpa menyertakan indeks
        df.to_csv("catatan_pemasukan_toko.csv", index=False)
        print("Data berhasil disimpan ke catatan_pemasukan_toko.csv")

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirToko(root)
    root.mainloop()