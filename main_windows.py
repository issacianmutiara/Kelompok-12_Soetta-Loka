from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from csv import *

root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title('Soetta-Loka')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
logo = Image.open('logo soettaloka.png')
logo_ico = ImageTk.PhotoImage(logo)
root.wm_iconphoto(False, logo_ico)


def frame_utama(frame):
    frame.tkraise()


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


hargaMaskapaiPilihan = []
hargaKelasPilihan = []
hargaHotelPilihan = []
tampung_harga1 = []
tampung_harga2 = []
tampung_total1 = []
tampung_total2 = []
cek_data = ''


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


def info_tiket():
    Label(tiket_frame, text='Boarding Pass', font='Helvetica 13 bold', fg='#8cc53d', bg='black').place(x=195, y=125)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Kelas').place(x=0, y=150)
    Label(tiket_frame, text=': ' + kelas_input.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black') \
        .place(x=120, y=150)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Nama').place(x=0, y=180)
    Label(tiket_frame, text=': ' + input_nama.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black') \
        .place(x=120, y=180)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Jenis Maskapai').place(x=0, y=210)
    Label(tiket_frame, text=': ' + maskapai_input.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black') \
        .place(x=120, y=210)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Waktu').place(x=0, y=240)
    Label(tiket_frame, text=': ' + waktu_input.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black') \
        .place(x=120, y=240)

    Button(tiket_frame, text='Selesai', width=10, command=lambda: frame_utama(tiket_frame)).place(x=220, y=320)


def hitung_harga1():
    if kelas_input.get() == 'Ekonomi':
        harga_total1 = int(int(hargaMaskapaiPilihan[0]) * 0.9) * int(input_jumlah.get())
    elif kelas_input.get() == 'Bisnis':
        harga_total1 = (int(int(hargaMaskapaiPilihan[0]) * 0.9)) * 2 * int(input_jumlah.get())
    else:
        harga_total1 = (int(int(hargaMaskapaiPilihan[0]) * 0.9)) * 3 * int(input_jumlah.get())
    tampung_harga1.append(harga_total1)


def hitung_harga2():
    if kelas_input.get() == 'Ekonomi':
        harga_total2 = int(hargaMaskapaiPilihan[0]) * int(input_jumlah.get())
    elif kelas_input.get() == 'Bisnis':
        harga_total2 = (int(hargaMaskapaiPilihan[0])) * 2 * int(input_jumlah.get())
    else:
        harga_total2 = (int(hargaMaskapaiPilihan[0])) * 3 * int(input_jumlah.get())
    tampung_harga2.append(harga_total2)


def tiket_bill():
    perhitungan_harga()
    hitung_harga1()
    Label(bayar_frame, text='TICKET BILL').place(x=50, y=160)
    Label(bayar_frame, text='Tagihan yang perlu Anda bayar :').place(x=0, y=195)
    Label(bayar_frame, text='Jumlah tiket = ' + input_jumlah.get()).place(x=0, y=220)
    Label(bayar_frame, text='Kelas Penerbangan = ' + kelas_input.get()).place(x=0, y=245)
    Label(bayar_frame, text='Tiket Maskapai = Rp' + str(hargaMaskapaiPilihan[0])).place(x=0, y=270)
    Label(bayar_frame, text='Tiket Maskapai Total = Rp' + str(tampung_harga1[0])).place(x=0, y=295)
    Label(bayar_frame, text='Penginapan = Rp' + str(hargaHotelPilihan[0])).place(x=0, y=320)
    Label(bayar_frame, text='TOTAL : Rp' + str(int(hargaHotelPilihan[0]) + int(tampung_harga1[0]))).place(x=0, y=345)
    x = str(int(hargaHotelPilihan[0]) + int(tampung_harga1[0]))
    tampung_total1.append(x)


def tiket_bill_lewati():
    perhitungan_harga()
    hitung_harga2()
    Label(lewati_frame, text='Tagihan yang perlu Anda bayar :').place(x=150, y=150)
    Label(lewati_frame, text='Jumlah tiket = ' + input_jumlah.get()).place(x=0, y=220)
    Label(lewati_frame, text='Kelas Penerbangan = ' + kelas_input.get()).place(x=0, y=245)
    Label(lewati_frame, text='Tiket Maskapai = Rp' + str(hargaMaskapaiPilihan[0])).place(x=0, y=270)
    Label(lewati_frame, text='Tiket Maskapai Total = Rp' + str(tampung_harga2[0])).place(x=0, y=295)
    Label(lewati_frame, text='TOTAL : Rp' + str(tampung_harga2[0])).place(x=0, y=320)
    y = str(tampung_harga2[0])
    tampung_total2.append(y)


def cek_datadiri(check):
    global cek_data
    cek_data = Toplevel(root)
    cek_data.title('Cek Data Diri')
    cek_data.geometry('500x500')
    cek_data.wm_iconphoto(False, logo_ico)
    cek_data.resizable(0, 0)
    Label(cek_data, text='Data Diri', font='Helvetica 15 bold').place(x=200, y=5)
    Label(cek_data, text='Nama', font='Helvetica 10 bold').place(x=0, y=50)
    Label(cek_data, text='TTL', font='Helvetica 10 bold').place(x=0, y=75)
    Label(cek_data, text='No. KTP', font='Helvetica 10 bold').place(x=0, y=100)
    Label(cek_data, text='Alamat', font='Helvetica 10 bold').place(x=0, y=125)
    Label(cek_data, text='Jenis Penerbangan', font='Helvetica 10 bold').place(x=0, y=150)
    Label(cek_data, text='Tujuan', font='Helvetica 10 bold').place(x=0, y=175)
    Label(cek_data, text='Waktu Keberangkatan', font='Helvetica 10 bold').place(x=0, y=200)
    Label(cek_data, text='Maskapai', font='Helvetica 10 bold').place(x=0, y=225)
    Label(cek_data, text='Kelas Penerbangan', font='Helvetica 10 bold').place(x=0, y=250)
    Label(cek_data, text='Jumlah Tiket', font='Helvetica 10 bold').place(x=0, y=275)
    if check == 'pilih_klik':
        Label(cek_data, text='Penginapan', font='Helvetica 10 bold').place(x=0, y=300)
        Label(cek_data, text='Metode Pembayaran', font='Helvetica 10 bold').place(x=0, y=325)
        Label(cek_data, text='TOTAL', font='Helvetica 10 bold').place(x=0, y=350)
        Button(cek_data, text='Tutup', font='Helvetica 10 bold', command=lambda: cek_data.destroy()).place(x=250, y=375)
    elif check == 'lewati_klik':
        Label(cek_data, text='Metode Pembayaran', font='Helvetica 10 bold').place(x=0, y=300)
        Label(cek_data, text='TOTAL', font='Helvetica 10 bold').place(x=0, y=325)
        Button(cek_data, text='Tutup', font='Helvetica 10 bold', command=lambda: cek_data.destroy()).place(x=250, y=350)

    Label(cek_data, text=input_nama.get(), font='Helvetica 10').place(x=250, y=50)
    Label(cek_data, text=input_ttl.get(), font='Helvetica 10').place(x=250, y=75)
    Label(cek_data, text=input_noktp.get(), font='Helvetica 10').place(x=250, y=100)
    Label(cek_data, text=input_alamat.get(), font='Helvetica 10').place(x=250, y=125)
    Label(cek_data, text=jenis_input.get(), font='Helvetica 10').place(x=250, y=150)
    Label(cek_data, text=tujuan_input.get(), font='Helvetica 10').place(x=250, y=175)
    Label(cek_data, text=waktu_input.get(), font='Helvetica 10').place(x=250, y=200)
    Label(cek_data, text=maskapai_input.get(), font='Helvetica 10').place(x=250, y=225)
    Label(cek_data, text=kelas_input.get(), font='Helvetica 10').place(x=250, y=250)
    Label(cek_data, text=input_jumlah.get(), font='Helvetica 10').place(x=250, y=275)
    if check == 'pilih_klik':
        Label(cek_data, text=hotel_input.get(), font='Helvetica 10').place(x=250, y=300)
        Label(cek_data, text=bayar_input.get(), font='Helvetica 10').place(x=250, y=325)
        Label(cek_data, text='Rp ' + str(int(hargaHotelPilihan[0]) + int(tampung_harga1[0]))).place(x=250, y=350)
    elif check == 'lewati_klik':
        Label(cek_data, text=bayar_input1.get(), font='Helvetica 10').place(x=250, y=300)
        Label(cek_data, text='Rp ' + str(tampung_harga2[0])).place(x=250, y=325)


# TEMPAT NAMBAHIN FRAME
main_page = Frame(root)
main_page.grid(row=0, column=0, sticky='nsew')
main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')
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
myFrame = [main_page, main_frame, input_frame, hotel_frame, bayar_frame, berhasil_frame, tiket_frame, lewati_frame]
for frame in myFrame:
    frame.grid(row=0, column=0, sticky='nsew')

# MAIN WINDOWS (PESAN TIKET)
logo_mainpage = Image.open('logo soettaloka black resize.jpg')
logo_mainpage_ico = ImageTk.PhotoImage(logo_mainpage)
Label(main_page, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)
pesan_btm = Button(main_page, text='PESAN TIKET', bg='black', fg='#8cc53d', font='Helvetica 15 bold',
                   command=lambda: frame_utama(input_frame))
pesan_btm.place(x=250, y=450, anchor='center')

# FRAME 1 On Booking Site
logo_inputframe = Image.open('1.png')
logo_inputframe_ico = ImageTk.PhotoImage(logo_inputframe)
Label(input_frame, image=logo_inputframe_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(input_frame, text='On-Booking Site', font='Helvetica 15 bold').place(x=170, y=5)
Label(input_frame, text='Jenis Penerbangan', font='Helvetica 10 bold').place(x=0, y=50)
Label(input_frame, text='Tujuan', font='Helvetica 10 bold').place(x=0, y=75)
Label(input_frame, text='Waktu Keberangkatan', font='Helvetica 10 bold').place(x=0, y=100)
Label(input_frame, text='Maskapai', font='Helvetica 10 bold').place(x=0, y=125)
Label(input_frame, text='Kelas Penerbangan', font='Helvetica 10 bold').place(x=0, y=150)

jenis_input = ttk.Combobox(input_frame, width=37)
jenis_input['values'] = ['Domestik', 'Non-domestik']
jenis_input['state'] = 'readonly'
jenis_input.bind('<<ComboboxSelected>>', ganti_list_tujuan_dan_hotel)
jenis_input.place(x=140, y=50)

tujuan_input = ttk.Combobox(input_frame, width=37)
tujuan_input['state'] = 'readonly'
tujuan_input.bind('<<ComboboxSelected>>', ganti_list_waktu_dan_maskapai)
tujuan_input.place(x=140, y=75)

waktu_input = ttk.Combobox(input_frame, width=37)
waktu_input['state'] = 'readonly'
waktu_input.place(x=140, y=100)

maskapai_input = ttk.Combobox(input_frame, width=37)
maskapai_input['state'] = 'readonly'
maskapai_input.place(x=140, y=125)

kelas_input = ttk.Combobox(input_frame, width=37)
kelas_input['values'] = ['Ekonomi', 'Bisnis', 'Eksekutif']
kelas_input['state'] = 'readonly'
kelas_input.place(x=140, y=150)

Button(input_frame, text='Selanjutnya', width=10, command=lambda: frame_utama(main_frame)).place(x=140, y=175)

# FRAME 2 Masukan Data Diri
logo_mainframe = Image.open('2.png')
logo_mainframe_ico = ImageTk.PhotoImage(logo_mainframe)
Label(main_frame, image=logo_mainframe_ico, bd=0, compound=CENTER).place(x=0, y=0)
top_label = Label(main_frame, text='Masukkan data diri anda', font='Helvetica 15 bold') \
    .place(x=100, y=5)
label_jumlah = Label(main_frame, text='Jumlah', font='Helvetica 10 bold').place(x=0, y=50)
label_nama = Label(main_frame, text='Nama', font='Helvetica 10 bold').place(x=0, y=75)
label_ttl = Label(main_frame, text='TTL', font='Helvetica 10 bold').place(x=0, y=100)
label_noktp = Label(main_frame, text='No.KTP', font='Helvetica 10 bold').place(x=0, y=125)
label_alamat = Label(main_frame, text='Alamat', font='Helvetica 10 bold').place(x=0, y=150)

input_jumlah = Entry(main_frame, width=40)
input_nama = Entry(main_frame, width=40)
input_ttl = Entry(main_frame, width=40)
input_noktp = Entry(main_frame, width=40)
input_alamat = Entry(main_frame, width=40)
input_jumlah.place(x=140, y=50)
input_nama.place(x=140, y=75)
input_ttl.place(x=140, y=100)
input_noktp.place(x=140, y=125)
input_alamat.place(x=140, y=150)

Button(main_frame, text='Selanjutnya', width=10, command=lambda: frame_utama(hotel_frame)).place(x=140, y=175)

logo_inputframe = Image.open('1.png')
logo_inputframe_ico = ImageTk.PhotoImage(logo_inputframe)
Label(input_frame, image=logo_inputframe_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(input_frame, text='On-Booking Site', font='Helvetica 15 bold').place(x=170, y=5)
Label(input_frame, text='Jenis Penerbangan').place(x=0, y=50)
Label(input_frame, text='Tujuan').place(x=0, y=75)
Label(input_frame, text='Waktu Keberangkatan').place(x=0, y=100)
Label(input_frame, text='Maskapai').place(x=0, y=125)
Label(input_frame, text='Kelas Penerbangan').place(x=0, y=150)

jenis_input = ttk.Combobox(input_frame, width=37)
jenis_input['values'] = ['Domestik', 'Non-domestik']
jenis_input['state'] = 'readonly'
jenis_input.bind('<<ComboboxSelected>>', ganti_list_tujuan_dan_hotel)
jenis_input.place(x=140, y=50)

tujuan_input = ttk.Combobox(input_frame, width=37)
tujuan_input['state'] = 'readonly'
tujuan_input.bind('<<ComboboxSelected>>', ganti_list_waktu_dan_maskapai)
tujuan_input.place(x=140, y=75)

waktu_input = ttk.Combobox(input_frame, width=37)
waktu_input['state'] = 'readonly'
waktu_input.place(x=140, y=100)

maskapai_input = ttk.Combobox(input_frame, width=37)
maskapai_input['state'] = 'readonly'
maskapai_input.place(x=140, y=125)

kelas_input = ttk.Combobox(input_frame, width=37)
kelas_input['values'] = ['Ekonomi', 'Bisnis', 'Eksekutif']
kelas_input['state'] = 'readonly'
kelas_input.place(x=140, y=150)

# FRAME 3 Hot Deal (Hotel)
logo_hotel_frame = Image.open('3.png')
logo_hotel_frame_ico = ImageTk.PhotoImage(logo_hotel_frame)
Label(hotel_frame, image=logo_hotel_frame_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(hotel_frame, text='Hot Deals', font='Arial 20 bold').place(x=190, y=5)
Label(hotel_frame, text='Nikmati hotel terbaik dengan promo menarik', font='Arial 12').place(x=105, y=40)
Label(hotel_frame, text='Hotel').place(x=245, y=80)

Button(hotel_frame, text='Lewati', width=10, command=lambda: frame_utama(lewati_frame)).place(x=130, y=200)
Button(hotel_frame, text='Pilih', width=10, command=lambda: frame_utama(bayar_frame)).place(x=290, y=200)

hotel_input = ttk.Combobox(hotel_frame, width=37)
hotel_input['state'] = 'readonly'
hotel_input.place(x=130, y=120)
hotel_input.place(x=100, y=80)

Button(input_frame, text='Selanjutnya', width=10, command=lambda: frame_utama(main_frame)).place(x=140, y=175)

Label(hotel_frame, text='Hot Deals', font='Arial 20 bold').place(x=190, y=5)
Label(hotel_frame, text='Nikmati hotel terbaik dengan promo menarik', font='Arial 12').place(x=110, y=40)
Label(hotel_frame, text='Hotel').place(x=0, y=80)

# FRAME 4 Metode Pembayaran Jika Memesan Hotel
logo_bayarframe = Image.open('4.png')
logo_bayarframe_ico = ImageTk.PhotoImage(logo_bayarframe)
Label(bayar_frame, image=logo_bayarframe_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(bayar_frame, text='Payment', font='Arial 20 bold').place(x=190, y=5)
Label(bayar_frame, text='Pilih metode pembayaran', font='Arial 12').place(x=150, y=40)
Label(bayar_frame, text='Metode').place(x=0, y=80)

bayar_input = ttk.Combobox(bayar_frame, width=37)
bayar_input['state'] = 'readonly'
bayar_input['values'] = ['Transfer via virtual account', 'Kartu Kredit', 'Transfer via bank']
bayar_input.place(x=50, y=80)

Button(bayar_frame, text='Input metode', command=lambda: tiket_bill()).place(x=150, y=110)
Button(bayar_frame, text='Selanjutnya', width=10, command=lambda: frame_utama(berhasil_frame)).place(x=250, y=330)
Button(bayar_frame, text='Cek data diri', width=10, command=lambda: cek_datadiri('pilih_klik')).place(x=250, y=295)

# FRAME 4 apabila dilewati
logo_bayarframe1 = Image.open('4.png')
logo_bayarframe_ico1 = ImageTk.PhotoImage(logo_bayarframe1)
Label(lewati_frame, image=logo_bayarframe_ico1, bd=0, compound=CENTER).place(x=0, y=0)

Label(lewati_frame, text='Payment', font='Arial 20 bold').place(x=190, y=5)
Label(lewati_frame, text='Pilih metode pembayaran', font='Arial 12').place(x=150, y=40)
Label(lewati_frame, text='Metode').place(x=0, y=80)

bayar_input1 = ttk.Combobox(lewati_frame, width=37)
bayar_input1['state'] = 'readonly'
bayar_input1['values'] = ['Transfer via virtual account', 'Kartu Kredit', 'Transfer via bank']
bayar_input1.place(x=50, y=80)

Button(lewati_frame, text='Input metode', command=lambda: tiket_bill_lewati()).place(x=50, y=110)
Button(lewati_frame, text='Selanjutnya', width=10, command=lambda: frame_utama(berhasil_frame)).place(x=100, y=295)
Button(lewati_frame, text='Cek data diri', width=10, command=lambda: cek_datadiri('lewati_klik')).place(x=250, y=295)

# FRAME 5 Transaksi Berhasil
logo_berhasilframe = Image.open('5.png')
logo_berhasilframe_ico = ImageTk.PhotoImage(logo_berhasilframe)
Label(berhasil_frame, image=logo_berhasilframe_ico, bd=0, compound=CENTER).place(x=0, y=0)
Label(berhasil_frame, text='Transaksi Berhasil', font='Helvetica 20 bold').place(x=130, y=180)
Label(berhasil_frame, text='Silahkan Print Tiket', font='Helvetica 20 bold').place(x=130, y=210)

Button(berhasil_frame, text='Selanjutnya', width=10, command=lambda: frame_utama(tiket_frame)).place(x=220, y=295)

# FRAME 6 TIKET
logo_tiketframe = Image.open('6.png')
logo_tiketframe_ico = ImageTk.PhotoImage(logo_tiketframe)
Label(tiket_frame, image=logo_tiketframe_ico, bd=0, compound=CENTER).place(x=0, y=0)
Label(tiket_frame, text='Informasi Ticket', font='Helvetica 20 bold').place(x=140, y=5)

Button(tiket_frame, text='Lihat Ticket', width=10, command=info_tiket).place(x=220, y=80)

# ++++++++++++++++++++++++++++++++++++++++++++++++ END ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  fg='#8cc53d'
frame_utama(main_page)
root.mainloop()
