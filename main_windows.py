# import modul yang dibutuhkan
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from csv import *
import random

# membuat root untuk aktivasi gui dan mengatur kondisi2 yang dikenakan pada gui utama
root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title('Soetta-Loka')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
logo = Image.open('logo soettaloka.png')
logo_ico = ImageTk.PhotoImage(logo)
root.wm_iconphoto(False, logo_ico)


# untuk menampilkan parameter frame pilihan dan memunculkannya pada root utama dengan .tkraise
def frame_utama(frame):
    frame.tkraise()


# mengambil data2 dari csv dan memasukkannya pada variabel yang telah dibuat
tujuan = []
with open('dom_nondom.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        if row[0] != 'NO':
            tujuan.append(row)
waktu = []
with open('waktu_penerbangan.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        if row[0] != 'NO':
            waktu.append(row)
maskapai = []
dataMaskapai = []
with open('data_maskapai.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        if row[0] != 'NO':
            maskapai.append(row)
            dataMaskapai.append(row[3])
hotel = []
dataHotel = []
with open('hotel.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        if row[0] != 'NO':
            hotel.append(row)
            dataHotel.append(row[3])


# untuk memilih ekspresi apa yang akan muncul di pilihan tujuan dan hotel berdasarkan input user
def ganti_list_tujuan_dan_hotel(event):
    values = []
    for row in tujuan:
        if row[1] == jenis_input.get():
            values.append(row[2])
    tujuan_input['values'] = values
    values = []
    for row in hotel:
        if row[2] == jenis_input.get():
            values.append(row[1])
    hotel_input['values'] = values


# untuk memilih ekspresi apa yang akan muncul di pilihan waktu dan maskapai berdasarkan input user
def ganti_list_waktu_dan_maskapai(event):
    values = []
    for row in waktu:
        if row[1] == tujuan_input.get():
            values.append(row[2])
            values.append(row[3])
            values.append(row[4])
    waktu_input['values'] = values
    values = []
    for row in maskapai:
        if row[2] == tujuan_input.get():
            values.append(row[1])
    maskapai_input['values'] = values


# variabel untuk menampung data(harga) berdasarkan input dari user, parameter tombol, dan variabel font agar memudahkan dalam pembuatan coding
hargaMaskapaiPilihan = []
hargaKelasPilihan = []
hargaHotelPilihan = []
tampung_harga1 = []
tampung_harga2 = []
tampung_total1 = []
tampung_total2 = []
parameter = []
fontme = 'Helvetica 10 bold'
fontme_normal = 'Helvetica 10'


# mengambil input yang dipilih user dan mencocokannya dengan data kemudian memasukkan data tersebut ke variabel tampung
def perhitungan_harga():
    if maskapai_input.get() == 'Garuda Indonesia':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[0])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[1])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[2])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[3])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[4])
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[5])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[6])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[7])
    elif maskapai_input.get() == 'Lion Air':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[8])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[9])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[10])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[11])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[12])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[13])
    elif maskapai_input.get() == 'Batik Air':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[14])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[15])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[16])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[17])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[18])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[19])
    elif maskapai_input.get() == 'Citilink':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[20])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[21])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[22])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[23])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[24])
    elif maskapai_input.get() == 'AirAsia':
        if tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[25])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[26])
    elif maskapai_input.get() == 'Singapore':
        if tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[27])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[28])
    else:
        if tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[29])
    if hotel_input.get() == 'Hotel Aston':
        hargaHotelPilihan.append(dataHotel[0])
    elif hotel_input.get() == 'Hotel Horison':
        hargaHotelPilihan.append(dataHotel[1])
    elif hotel_input.get() == 'Hotel Ibis':
        hargaHotelPilihan.append(dataHotel[2])
    elif hotel_input.get() == 'Mandarin Oriental':
        hargaHotelPilihan.append(dataHotel[3])
    elif hotel_input.get() == 'Carlton Hotel':
        hargaHotelPilihan.append(dataHotel[4])
    else:
        hargaHotelPilihan.append(dataHotel[5])


# fungsi untuk menghitung harga maskapai dan harga kelas yang dipilih apabila user memutuskan untuk mengambil hot deals
def hitung_harga1():
    if kelas_input.get() == 'Ekonomi':
        harga_total1 = int(int(hargaMaskapaiPilihan[0]) * 0.9)
    elif kelas_input.get() == 'Bisnis':
        harga_total1 = int(int(hargaMaskapaiPilihan[0]) * 0.9) * 2
    else:
        harga_total1 = int(int(hargaMaskapaiPilihan[0]) * 0.9) * 3
    tampung_harga1.append(harga_total1)


# fungsi untuk menghitung harga maskapai dan harga kelas yang dipilih apabila user memutuskan untuk tidak mengambil hot deals
def hitung_harga2():
    if kelas_input.get() == 'Ekonomi':
        harga_total2 = int(hargaMaskapaiPilihan[0])
    elif kelas_input.get() == 'Bisnis':
        harga_total2 = (int(hargaMaskapaiPilihan[0])) * 2
    else:
        harga_total2 = (int(hargaMaskapaiPilihan[0])) * 3
    tampung_harga2.append(harga_total2)


# memunculkan pesan apabila user tidak menginput pada menu on booking
def check_onbooking():
    if jenis_input.get() == '' or tujuan_input.get() == '' or waktu_input.get() == '' or maskapai_input.get() == '' or kelas_input.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan pilih input tiket anda!')
    else:
        frame_utama(data_frame)


# memunculkan pesan apabila user tidak menginput pada menu data diri
def check_datadiri():
    if input_nama.get() == '' or input_ttl.get() == '' or input_noktp.get() == '' or input_alamat.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan identitas anda!')
    else:
        frame_utama(hotel_frame)


# memunculkan pesan apabila user tidak menginput pada menu metode pembayaran
def check_metode():
    if bayar_input.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan metode pembayaran!')
    else:
        tiket_bill()


def check_metode1():
    if bayar_input.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan metode pembayaran!')
    else:
        cek_datadiri('pilih_klik')


def check_metode_lewati():
    if bayar_input1.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan metode pembayaran!')
    else:
        tiket_bill_lewati()


def check_metode2():
    if bayar_input1.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan metode pembayaran!')
    else:
        cek_datadiri('lewati_klik')


def check_metode3():
    if bayar_input.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan metode pembayaran!')
    else:
        frame_utama(berhasil_frame)


def check_metode4():
    if bayar_input1.get() == '':
        messagebox.showwarning('Peringatan', 'Silahkan masukkan metode pembayaran!')
    else:
        frame_utama(berhasil_frame)


# berisi frame apabila user memilih untuk mengambil hot deals
def tiket_bill():
    perhitungan_harga()
    hitung_harga1()
    Label(bayar_frame, text='Tagihan', font='Helvetica 13 bold').place(x=220, y=135)
    Label(bayar_frame, text='Kelas Penerbangan' + kelas_input.get(), font=fontme).place(x=0, y=170)
    Label(bayar_frame, text=': ' + kelas_input.get(), font=fontme_normal).place(x=250, y=170)
    Label(bayar_frame, text='Tiket Maskapai', font=fontme).place(x=0, y=195)
    Label(bayar_frame, text=': Rp ' + str(hargaMaskapaiPilihan[0]), font=fontme_normal).place(x=250, y=195)
    Label(bayar_frame, text='Tiket Maskapai Total', font=fontme).place(x=0, y=220)
    Label(bayar_frame, text=': Rp ' + str(tampung_harga1[0]), font=fontme_normal).place(x=250, y=220)
    Label(bayar_frame, text='Penginapan', font=fontme).place(x=0, y=245)
    Label(bayar_frame, text=': Rp ' + str(hargaHotelPilihan[0]), font=fontme_normal).place(x=250, y=245)
    Label(bayar_frame, text='TOTAL', font=fontme).place(x=0, y=270)
    Label(bayar_frame, text=': Rp ' + str(int(hargaHotelPilihan[0]) + int(tampung_harga1[0])), font=fontme_normal).place(x=250, y=270)
    x = str(int(hargaHotelPilihan[0]) + int(tampung_harga1[0]))
    tampung_total1.append(x)


# berisi frame apabila user memilih untuk tidak mengambil hot deals
def tiket_bill_lewati():
    perhitungan_harga()
    hitung_harga2()
    Label(lewati_frame, text='Tagihan', font='Helvetica 13 bold').place(x=220, y=135)
    Label(lewati_frame, text='Kelas Penerbangan' + kelas_input.get(), font=fontme).place(x=0, y=170)
    Label(lewati_frame, text=': ' + kelas_input.get(), font=fontme_normal).place(x=250, y=170)
    Label(lewati_frame, text='Tiket Maskapai', font=fontme).place(x=0, y=195)
    Label(lewati_frame, text=': Rp ' + str(hargaMaskapaiPilihan[0]), font=fontme_normal).place(x=250, y=195)
    Label(lewati_frame, text='Tiket Maskapai Total', font=fontme).place(x=0, y=220)
    Label(lewati_frame, text=': Rp ' + str(tampung_harga2[0]), font=fontme_normal).place(x=250, y=220)
    Label(lewati_frame, text='TOTAL', font=fontme).place(x=0, y=245)
    Label(lewati_frame, text=': Rp ' + str(tampung_harga2[0]), font=fontme_normal).place(x=250, y=245)
    y = str(tampung_harga2[0])
    tampung_total2.append(y)


# fungsi untuk memunculkan windows baru dari root yang berisi data diri dan info book (untuk mengecek kembali)
def cek_datadiri(check):
    parameter.append(check)
    cek_data = Toplevel(root)
    cek_data.title('Cek Data Diri')
    cek_data.geometry('500x500')
    cek_data.wm_iconphoto(False, logo_ico)
    cek_data.resizable(0, 0)
    Label(cek_data, text='Data Diri', font='Helvetica 15 bold').place(x=200, y=5)
    Label(cek_data, text='Nama', font=fontme).place(x=0, y=50)
    Label(cek_data, text='TTL', font=fontme).place(x=0, y=75)
    Label(cek_data, text='No. KTP', font=fontme).place(x=0, y=100)
    Label(cek_data, text='Alamat', font=fontme).place(x=0, y=125)
    Label(cek_data, text='Jenis Penerbangan', font=fontme).place(x=0, y=150)
    Label(cek_data, text='Tujuan', font=fontme).place(x=0, y=175)
    Label(cek_data, text='Waktu Keberangkatan', font=fontme).place(x=0, y=200)
    Label(cek_data, text='Maskapai', font=fontme).place(x=0, y=225)
    Label(cek_data, text='Kelas Penerbangan', font=fontme).place(x=0, y=250)
    if check == 'pilih_klik':
        Label(cek_data, text='Penginapan', font=fontme).place(x=0, y=275)
        Label(cek_data, text='Metode Pembayaran', font=fontme).place(x=0, y=300)
        Label(cek_data, text='TOTAL', font=fontme).place(x=0, y=325)
        Button(cek_data, text='Tutup', font=fontme, width=10, command=lambda: cek_data.destroy()).place(x=250, y=350)
    elif check == 'lewati_klik':
        Label(cek_data, text='Metode Pembayaran', font=fontme).place(x=0, y=275)
        Label(cek_data, text='TOTAL', font=fontme).place(x=0, y=300)
        Button(cek_data, text='Tutup', font=fontme, width=10, command=lambda: cek_data.destroy()).place(x=250, y=325)

    Label(cek_data, text=input_nama.get(), font=fontme_normal).place(x=250, y=50)
    Label(cek_data, text=input_ttl.get(), font=fontme_normal).place(x=250, y=75)
    Label(cek_data, text=input_noktp.get(), font=fontme_normal).place(x=250, y=100)
    Label(cek_data, text=input_alamat.get(), font=fontme_normal).place(x=250, y=125)
    Label(cek_data, text=jenis_input.get(), font=fontme_normal).place(x=250, y=150)
    Label(cek_data, text=tujuan_input.get(), font=fontme_normal).place(x=250, y=175)
    Label(cek_data, text=waktu_input.get(), font=fontme_normal).place(x=250, y=200)
    Label(cek_data, text=maskapai_input.get(), font=fontme_normal).place(x=250, y=225)
    Label(cek_data, text=kelas_input.get(), font=fontme_normal).place(x=250, y=250)
    if check == 'pilih_klik':
        Label(cek_data, text=hotel_input.get(), font=fontme_normal).place(x=250, y=275)
        Label(cek_data, text=bayar_input.get(), font=fontme_normal).place(x=250, y=300)
        Label(cek_data, text='Rp ' + str(int(hargaHotelPilihan[0]) + int(tampung_harga1[0])), font=fontme_normal)\
            .place(x=250, y=325)
    elif check == 'lewati_klik':
        Label(cek_data, text=bayar_input1.get(), font=fontme_normal).place(x=250, y=275)
        Label(cek_data, text='Rp ' + str(tampung_harga2[0]), font=fontme_normal).place(x=250, y=300)


# berisi frame yang menunjukkan bahwa transaksi telah berhasil
def transaksi_berhasil():
    Label(berhasil_frame, text='Transaksi Berhasil', font='Helvetica 15 bold').place(x=170, y=100)
    Button(berhasil_frame, text='Lihat Ticket', font=fontme, width=10, command=lambda: [frame_utama(tiket_frame), lihat_tiket()]).place(x=220, y=150)


# berisi sintaks random untuk kode tiket dan juga berisi frame terakhir yaitu info tiket
def lihat_tiket():
    rand_huruf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    kode_angka = f'{random.randint(100, 999)}-{random.randint(500, 999)}'
    kode_huruf1 = random.choice(rand_huruf)
    kode_huruf2 = random.choice(rand_huruf)
    kode_gate = random.randint(1, 11)
    kode_tddk = f'{random.randint(1,26)}{kode_huruf1}'
    kode_tiket = f'SH{kode_angka}{kode_huruf1}{kode_huruf2}'
    Label(tiket_frame, text='Soetta-Loka', font='Helvetica 15 bold').place(x=185, y=5)
    Label(tiket_frame, text='Nama', font=fontme).place(x=0, y=50)
    Label(tiket_frame, text='Jenis Penerbangan', font=fontme).place(x=0, y=75)
    Label(tiket_frame, text='Tujuan', font=fontme).place(x=0, y=100)
    Label(tiket_frame, text='Waktu Keberangkatan', font=fontme).place(x=0, y=125)
    Label(tiket_frame, text='Maskapai', font=fontme).place(x=0, y=150)
    Label(tiket_frame, text='Kelas Penerbangan', font=fontme).place(x=0, y=175)
    Label(tiket_frame, text='Nomor Tiket', font=fontme).place(x=0, y=200)
    Label(tiket_frame, text='Nomor Kursi', font=fontme).place(x=0, y=225)
    Label(tiket_frame, text='Gate', font=fontme).place(x=0, y=250)
    Button(tiket_frame, text='Tutup', font=fontme, width=10, command=lambda: root.destroy()).place(x=250, y=325)

    Label(tiket_frame, text=input_nama.get(), font=fontme_normal).place(x=250, y=50)
    Label(tiket_frame, text=jenis_input.get(), font=fontme_normal).place(x=250, y=75)
    Label(tiket_frame, text=tujuan_input.get(), font=fontme_normal).place(x=250, y=100)
    Label(tiket_frame, text=waktu_input.get(), font=fontme_normal).place(x=250, y=125)
    Label(tiket_frame, text=maskapai_input.get(), font=fontme_normal).place(x=250, y=150)
    Label(tiket_frame, text=kelas_input.get(), font=fontme_normal).place(x=250, y=175)
    Label(tiket_frame, text=kode_tiket, font=fontme_normal).place(x=250, y=200)
    Label(tiket_frame, text=kode_tddk, font=fontme_normal).place(x=250, y=225)
    Label(tiket_frame, text=kode_gate, font=fontme_normal).place(x=250, y=250)


# Tempat untuk menambah frame pada root
main_page = Frame(root)
main_page.grid(row=0, column=0, sticky='nsew')
data_frame = Frame(root)
data_frame.grid(row=0, column=0, sticky='nsew')
input_frame = Frame(root)
input_frame.grid(row=0, column=0, sticky='nsew')
hotel_frame = Frame(root)
hotel_frame.grid(row=0, column=0, sticky='nsew')
bayar_frame = Frame(root)
bayar_frame.grid(row=0, column=0, sticky='nsew')
lewati_frame = Frame(root)
lewati_frame.grid(row=0, column=0, sticky='nsew')
berhasil_frame = Frame(root)
berhasil_frame.grid(row=0, column=0, sticky='nsew')
tiket_frame = Frame(root)
tiket_frame.grid(row=0, column=0, sticky='nsew')
myFrame = [main_page, data_frame, input_frame, hotel_frame, bayar_frame, berhasil_frame, tiket_frame, lewati_frame]

# looping agar frame yang ada pada program tetap berada pada kondisi yang sama ketika ditampilkan
for frame in myFrame:
    frame.grid(row=0, column=0, sticky='nsew')

# Tampilan awal sebagai identitas Soetta-Loka
logo_mainpage = Image.open('logo soettaloka black resize.jpg')
logo_mainpage_ico = ImageTk.PhotoImage(logo_mainpage)
Label(main_page, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)
pesan_btm = Button(main_page, text='PESAN TIKET', bg='black', fg='#8cc53d', font='Helvetica 15 bold', command=lambda: frame_utama(input_frame))
pesan_btm.place(x=250, y=450, anchor='center')

# FRAME 1 On Booking Site, berisi wallpaper, tulisan, dan tombol
logo_inputframe = Image.open('1.png')
logo_inputframe_ico = ImageTk.PhotoImage(logo_inputframe)
Label(input_frame, image=logo_inputframe_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(input_frame, text='On-Booking Site', font='Helvetica 15 bold').place(x=170, y=5)
Label(input_frame, text='Jenis Penerbangan', font=fontme).place(x=0, y=50)
Label(input_frame, text='Tujuan', font=fontme).place(x=0, y=75)
Label(input_frame, text='Waktu Keberangkatan', font=fontme).place(x=0, y=100)
Label(input_frame, text='Maskapai', font=fontme).place(x=0, y=125)
Label(input_frame, text='Kelas Penerbangan', font=fontme).place(x=0, y=150)

# combobox digunakan untuk mengambil input dari user dengan cara mengarahkan user untuk memilih values yang telah diberikan
jenis_input = ttk.Combobox(input_frame, font=fontme_normal, width=37)
jenis_input['values'] = ['Domestik', 'Non-domestik']
jenis_input['state'] = 'readonly'
jenis_input.bind('<<ComboboxSelected>>', ganti_list_tujuan_dan_hotel)
jenis_input.place(x=150, y=50)

tujuan_input = ttk.Combobox(input_frame, font=fontme_normal, width=37)
tujuan_input['state'] = 'readonly'
tujuan_input.bind('<<ComboboxSelected>>', ganti_list_waktu_dan_maskapai)
tujuan_input.place(x=150, y=75)

waktu_input = ttk.Combobox(input_frame, font=fontme_normal, width=37)
waktu_input['state'] = 'readonly'
waktu_input.place(x=150, y=100)

maskapai_input = ttk.Combobox(input_frame, font=fontme_normal, width=37)
maskapai_input['state'] = 'readonly'
maskapai_input.place(x=150, y=125)

kelas_input = ttk.Combobox(input_frame, font=fontme_normal, width=37)
kelas_input['values'] = ['Ekonomi', 'Bisnis', 'Eksekutif']
kelas_input['state'] = 'readonly'
kelas_input.place(x=150, y=150)

Button(input_frame, text='Selanjutnya', width=10, command=lambda: check_onbooking(), font=fontme).place(x=150, y=175)

# FRAME 2 Masukan Data Diri, berisi wallpaper, tulisan, dan tombol
logo_mainframe = Image.open('2.png')
logo_mainframe_ico = ImageTk.PhotoImage(logo_mainframe)
Label(data_frame, image=logo_mainframe_ico, bd=0, compound=CENTER).place(x=0, y=0)
top_label = Label(data_frame, text='Masukkan data diri anda', font='Helvetica 15 bold').place(x=130, y=5)
label_nama = Label(data_frame, text='Nama Lengkap', font=fontme).place(x=0, y=50)
label_ttl = Label(data_frame, text='TTL', font=fontme).place(x=0, y=75)
label_noktp = Label(data_frame, text='No. KTP', font=fontme).place(x=0, y=100)
label_alamat = Label(data_frame, text='Alamat', font=fontme).place(x=0, y=125)

input_nama = Entry(data_frame, font=fontme_normal, width=37, borderwidth=2)
input_ttl = Entry(data_frame, font=fontme_normal, width=37, borderwidth=2)
input_noktp = Entry(data_frame, font=fontme_normal, width=37, borderwidth=2)
input_alamat = Entry(data_frame, font=fontme_normal, width=37, borderwidth=2)
input_nama.place(x=150, y=50)
input_ttl.place(x=150, y=75)
input_noktp.place(x=150, y=100)
input_alamat.place(x=150, y=125)

Button(data_frame, text='Selanjutnya', width=10, command=lambda: check_datadiri(), font=fontme).place(x=150, y=150)
Button(data_frame, text='Kembali', width=10, command=lambda: frame_utama(input_frame), font=fontme).place(x=250, y=150)

# FRAME 3 Hot Deal (Hotel), berisi wallpaper, tulisan, dan tombol
logo_hotel_frame = Image.open('3.png')
logo_hotel_frame_ico = ImageTk.PhotoImage(logo_hotel_frame)
Label(hotel_frame, image=logo_hotel_frame_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(hotel_frame, text='Hot Deals', font='Helvetica 15 bold').place(x=203, y=5)
Label(hotel_frame, text='Pilih Hotel dan Dapatkan Diskon 10%', font='Helvetica 13 bold').place(x=101, y=40)
Label(hotel_frame, text='Pilih Hotel', font=fontme).place(x=0, y=80)

hotel_input = ttk.Combobox(hotel_frame, font=fontme_normal, width=39)
hotel_input['state'] = 'readonly'
hotel_input.place(x=100, y=80)

Button(hotel_frame, text='Lewati', font=fontme, width=10, command=lambda: frame_utama(lewati_frame)).place(x=100, y=110)
Button(hotel_frame, text='Pilih', font=fontme, width=10, command=lambda: frame_utama(bayar_frame)).place(x=204, y=110)
Button(hotel_frame, text='Kembali', font=fontme, width=10, command=lambda: frame_utama(data_frame)).place(x=304, y=110)

# FRAME 4 Metode Pembayaran apabila user memilih untuk memesan hotel
logo_bayarframe = Image.open('4.png')
logo_bayarframe_ico = ImageTk.PhotoImage(logo_bayarframe)
Label(bayar_frame, image=logo_bayarframe_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(bayar_frame, text='Payment', font='Helvetica 15 bold').place(x=210, y=5)
Label(bayar_frame, text='Pilih metode pembayaran', font='Helvetica 13 bold').place(x=150, y=40)
Label(bayar_frame, text='Pilih Metode', font=fontme).place(x=0, y=80)

bayar_input = ttk.Combobox(bayar_frame, font=fontme_normal, width=39)
bayar_input['state'] = 'readonly'
bayar_input['values'] = ['Transfer Via Virtual Account', 'Kartu Kredit', 'Transfer Via Bank']
bayar_input.place(x=100, y=80)

Button(bayar_frame, text='Input metode', command=lambda: check_metode(), font=fontme).place(x=100, y=110)
Button(bayar_frame, text='Selanjutnya', width=10, command=lambda: [check_metode3(), parameter.append('pilih_klik')], font=fontme)\
    .place(x=150, y=325)
Button(bayar_frame, text='Cek data diri', width=10, command=lambda: check_metode1(), font=fontme).place(x=250, y=325)
Button(bayar_frame, text='Kembali', width=10, command=lambda: frame_utama(hotel_frame), font=fontme).place(x=350, y=325)

# FRAME 4 Metode Pembayaran apabila user memilih untuk tidak memesan hotel
logo_bayarframe1 = Image.open('4.png')
logo_bayarframe_ico1 = ImageTk.PhotoImage(logo_bayarframe1)
Label(lewati_frame, image=logo_bayarframe_ico1, bd=0, compound=CENTER).place(x=0, y=0)

Label(lewati_frame, text='Payment', font='Helvetica 15 bold').place(x=190, y=5)
Label(lewati_frame, text='Pilih metode pembayaran', font='Helvetica 13 bold').place(x=150, y=40)
Label(lewati_frame, text='Pilih Metode', font=fontme).place(x=0, y=80)

bayar_input1 = ttk.Combobox(lewati_frame, font=fontme, width=39)
bayar_input1['state'] = 'readonly'
bayar_input1['values'] = ['Transfer via virtual account', 'Kartu Kredit', 'Transfer via bank']
bayar_input1.place(x=100, y=80)

Button(lewati_frame, text='Input metode', command=lambda: check_metode_lewati(), font=fontme).place(x=100, y=110)
Button(lewati_frame, text='Selanjutnya', width=10, command=lambda: [check_metode4(), parameter.append('lewati_klik')], font=fontme).place(x=150, y=325)
Button(lewati_frame, text='Cek data diri', width=10, command=lambda: check_metode2(), font=fontme).place(x=250, y=325)
Button(lewati_frame, text='Kembali', width=10, command=lambda: frame_utama(hotel_frame), font=fontme).place(x=350, y=325)

# FRAME 5 Transaksi Berhasil, berisi wallpaper, tulisan, dan tombol
logo_berhasilframe = Image.open('5.png')
logo_berhasilframe_ico = ImageTk.PhotoImage(logo_berhasilframe)
Label(berhasil_frame, image=logo_berhasilframe_ico, bd=0, compound=CENTER).place(x=0, y=0)
Label(berhasil_frame, text='Silahkan Lakukan Pembayaran', font='Helvetica 15 bold').place(x=120, y=5)
Button(berhasil_frame, text='Selanjutnya', font=fontme, width=10, command=lambda: transaksi_berhasil()).place(x=220, y=50)

# FRAME 6 Info Tiket, berisi wallpaper, tulisan, dan tombol
logo_tiketframe = Image.open('6.png')
logo_tiketframe_ico = ImageTk.PhotoImage(logo_tiketframe)
Label(tiket_frame, image=logo_tiketframe_ico, bd=0, compound=CENTER).place(x=0, y=0)


# ++++++++++++++++++++++++++++++++++++++++++++++++ END ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# frame_utama(main_page) digunakan untuk memunculkan frame main_page saat program pertama kali dijalankan
# root.mainloop() adalah sintaks untuk gui tkinter agar gui tetap berjalan selama belum ada perintah destroy(tutup) ataupun user klik keluar
# lambda kami gunakan untuk memberi fungsi anonim agar fungsi yang ada pada command tetap "bersembunyi" selama tombol belum diklik
frame_utama(main_page)
root.mainloop()
