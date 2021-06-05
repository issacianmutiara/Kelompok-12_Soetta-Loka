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


def frame_1(frame):
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


def ganti_list_tujuan_dan_hotel(e):
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


def ganti_list_waktu_dan_maskapai(e):
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

#  dataJumlahPenumbang = IntVar()
hargaMaskapaiPilihan = []
hargaHotelPilihan = []
e = []


def perhitunganHarga():
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
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[13])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[14])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[15])
    elif maskapai_input.get() == 'Batik Air':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[16])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[17])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[18])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[19])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[20])
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[21])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[22])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[23])
    elif maskapai_input.get() == 'Citilink':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[24])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[25])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[26])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[27])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[28])
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[29])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[30])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[31])
    elif maskapai_input.get() == 'AirAsia':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[32])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[33])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[34])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[35])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[36])
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[37])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[38])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[39])
    elif maskapai_input.get() == 'Singapore':
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[40])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[41])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[42])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[43])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[44])
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[45])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[46])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[47])
    else:
        if tujuan_input.get() == 'Jakarta - Solo':
            hargaMaskapaiPilihan.append(dataMaskapai[48])
        elif tujuan_input.get() == 'Jakarta - Denpasar':
            hargaMaskapaiPilihan.append(dataMaskapai[49])
        elif tujuan_input.get() == 'Jakarta - Makassar':
            hargaMaskapaiPilihan.append(dataMaskapai[50])
        elif tujuan_input.get() == 'Jakarta - Samarinda':
            hargaMaskapaiPilihan.append(dataMaskapai[51])
        elif tujuan_input.get() == 'Jakarta - Surabaya':
            hargaMaskapaiPilihan.append(dataMaskapai[52])
        elif tujuan_input.get() == 'Jakarta - Singapura':
            hargaMaskapaiPilihan.append(dataMaskapai[53])
        elif tujuan_input.get() == 'Jakarta - Hongkong':
            hargaMaskapaiPilihan.append(dataMaskapai[54])
        else:
            hargaMaskapaiPilihan.append(dataMaskapai[55])
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
    hargaTiketTotal = int(hargaMaskapaiPilihan[0]) * int(input_jumlah.get())
    e.append(hargaTiketTotal)


def tiketBill():
    perhitunganHarga()
    Label(bayar_frame, text='TICKET BILL').place(x=220, y=160)
    Label(bayar_frame, text='Tagihan yang perlu Anda bayar :').place(x=0, y=195)
    Label(bayar_frame, text='Jumlah tiket = ' + input_jumlah.get()).place(x=0, y=220)
    Label(bayar_frame, text='Tiket Maskapai = Rp' + str(hargaMaskapaiPilihan[0])).place(x=0, y=245)
    Label(bayar_frame, text='Tiket Maskapai Total = Rp' + str(e[0])).place(x=0, y=270)
    Label(bayar_frame, text='Penginapan = Rp' + str(hargaHotelPilihan[0])).place(x=0, y=295)
    Label(bayar_frame, text='TOTAL : Rp' + str(int(hargaHotelPilihan[0]) + int(e[0]))).place(x=0, y=315)


def cek_data1():
    Label(main_frame, text='Data Diri', font='Helvetica 13 bold', fg='#8cc53d', bg='black').place(x=240, y=175)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Nama').place(x=0, y=200)
    Label(main_frame, text=': ' + input_nama.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=200)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='TTL').place(x=0, y=227)
    Label(main_frame, text=': ' + input_ttl.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=227)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='No. KTP').place(x=0, y=252)
    Label(main_frame, text=': ' + input_noktp.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=252)
    Label(main_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Alamat').place(x=0, y=277)
    Label(main_frame, text=': ' + input_alamat.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=277)
    tombol2 = Button(main_frame, text='Input', width=10, command=lambda: frame_1(issa_frame)).place(x=120, y=305)


# TEMPAT NAMBAHIN FRAME
main_page = Frame(root)
main_page.grid(row=0, column=0, sticky='nsew')
main_frame = Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')
input_frame = Frame(root)
input_frame.grid(row=0, column=0, sticky='nsew')
issa_frame = Frame(root)
issa_frame.grid(row=0, column=0, sticky='nsew')
bayar_frame = Frame(root)
bayar_frame.grid(row=0, column=0, sticky='nsew')
berhasil_frame = Frame(root)
berhasil_frame.grid(row=0, column=0, sticky='nsew')
tiket_frame = Frame(root)
tiket_frame.grid(row=0, column=0, sticky='nsew')
myFrame = [main_page, main_frame, input_frame, issa_frame, bayar_frame, berhasil_frame, tiket_frame]
for frame in myFrame:
    frame.grid(row=0, column=0, sticky='nsew')

# MAIN PAGE (PESAN TIKET)
logo_mainpage = Image.open('logo soettaloka black resize.jpg')
logo_mainpage_ico = ImageTk.PhotoImage(logo_mainpage)
Label(main_page, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)
pesan_btm = Button(main_page, text='PESAN TIKET', bg='black', fg='#8cc53d', font='Helvetica 15 bold',
                   command=lambda: frame_1(input_frame))
pesan_btm.place(x=250, y=450, anchor='center')

# FRAME 1 On Booking Site
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

Button(input_frame, text='Next', width=10, command=lambda: frame_1(main_frame)).place(x=140, y=175)

# FRAME 2 Masukan Data Diri
logo_mainframe = Image.open('2.png')
logo_mainframe_ico = ImageTk.PhotoImage(logo_mainframe)
Label(main_frame, image=logo_mainframe_ico, bd=0, compound=CENTER).place(x=0, y=0)
top_label = Label(main_frame, text='Selamat Datang di Soetta-Loka\nMasukkan data diri anda!',
                  bg='black', fg='#8cc53d', font='Helvetica 15 bold')
top_label.grid(row=0, column=1, sticky='nsew')
label_jumlah = Label(main_frame, text='Jumlah', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=1, column=0, sticky='w')
label_nama = Label(main_frame, text='Nama', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=2, column=0, sticky='w')
label_ttl = Label(main_frame, text='TTL', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=3, column=0, sticky='w')
label_noktp = Label(main_frame, text='No.KTP', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=4, column=0, sticky='w')
label_alamat = Label(main_frame, text='Alamat', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=5, column=0, sticky='w')
input_jumlah = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
#  dataJumlahPenumbang.set(input_jumlah)
input_nama = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_ttl = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_noktp = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_alamat = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_jumlah.grid(row=1, column=1, columnspan=3)
input_nama.grid(row=2, column=1, columnspan=3)
input_ttl.grid(row=3, column=1, columnspan=3)
input_noktp.grid(row=4, column=1, columnspan=3)
input_alamat.grid(row=5, column=1, columnspan=3)

tombol1 = Button(main_frame, text='Cek Data', width=10, command=cek_data1).place(x=350, y=100)

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

tujuan_input = ttk.Combobox(input_frame, width=37)
tujuan_input['state'] = 'readonly'
tujuan_input.bind('<<ComboboxSelected>>', ganti_list_waktu_dan_maskapai)

waktu_input = ttk.Combobox(input_frame, width=37)
waktu_input['state'] = 'readonly'
# FRAME 3 Hot Deal
logo_issa_frame = Image.open('3.png')
logo_issa_frame_ico = ImageTk.PhotoImage(logo_issa_frame)
Label(issa_frame, image=logo_issa_frame_ico, bd=0, compound=CENTER).place(x=0, y=0)

maskapai_input = ttk.Combobox(input_frame, width=37)
maskapai_input['state'] = 'readonly'
Label(issa_frame, text='Hot Deals', font='Arial 20 bold').place(x=190, y=5)
Label(issa_frame, text='Nikmati hotel terbaik dengan promo menarik', font='Arial 12').place(x=105, y=40)
Label(issa_frame, text='Hotel').place(x=245, y=80)

kelas_input = ttk.Combobox(input_frame, width=37)
kelas_input['values'] = ['Ekonomi', 'Bisnis', 'Eksekutif']
kelas_input['state'] = 'readonly'
tombol3 = Button(issa_frame, text='Lewati', width=10, command=lambda: frame_1(bayar_frame)).place(x=130, y=200)
tombol4 = Button(issa_frame, text='Pilih', width=10, command=lambda: frame_1(bayar_frame)).place(x=290, y=200)

hotel_input = ttk.Combobox(issa_frame, width=37)
hotel_input['state'] = 'readonly'
hotel_input.place(x=130, y=120)

jenis_input.place(x=140, y=50)
tujuan_input.place(x=140, y=75)
waktu_input.place(x=140, y=100)
maskapai_input.place(x=140, y=125)
kelas_input.place(x=140, y=150)
hotel_input.place(x=100, y=80)

Button(input_frame, text='Next', width=10, command=lambda: frame_1(main_frame)).place(x=140, y=175)

# frame pesenan issa
Label(issa_frame, text='Hot Deals', font='Arial 20 bold').place(x=190, y=5)
Label(issa_frame, text='Nikmati hotel terbaik dengan promo menarik', font='Arial 12').place(x=110, y=40)
Label(issa_frame, text='Hotel').place(x=0, y=80)

# FRAME 4 Metode Pembayaran
logo_bayarframe = Image.open('4.png')
logo_bayarframe_ico = ImageTk.PhotoImage(logo_bayarframe)
Label(bayar_frame, image=logo_bayarframe_ico, bd=0, compound=CENTER).place(x=0, y=0)

Label(bayar_frame, text='Payment', font='Arial 20 bold').place(x=190, y=5)
Label(bayar_frame, text='Pilih metode pembayaran', font='Arial 12').place(x=150, y=40)
Label(bayar_frame, text='Bayar').place(x=0, y=80)

bayar_input = ttk.Combobox(bayar_frame, width=37)
bayar_input['state'] = 'readonly'
bayar_input['values'] = ['Transfer via virtual account', 'Kartu Kredit', 'Transfer via bank']
bayar_input.place(x=50, y=80)


tombol5 = Button(bayar_frame, text='Bayar', width=10, command=lambda: frame_1(bayar_frame)).place(x=50, y=110)
tombol_bayar = Button(bayar_frame, text='Input metode', command=lambda: tiketBill())
tombol_bayar.place(x=150, y=110)
tombol6 = Button(bayar_frame, text='Next', width=10, command=lambda: frame_1(berhasil_frame)).place(x=230, y=295)

# FRAME 5 Transaksi Berhasil
Label(berhasil_frame, text='Transaksi Berhasil', font='Helvetica 20 bold').place(x=130, y=180)
Label(berhasil_frame, text='Silahkan Print Tiket', font='Helvetica 20 bold').place(x=130, y=210)

tombol7 = Button(berhasil_frame, text='Next', width=10, command=lambda: frame_1(tiket_frame)).place(x=220, y=295)

# FRAME 6 TIKET
Label(tiket_frame, text='Informasi Ticket', font='Helvetica 20 bold').place(x=140, y=5)


def info_tiket():
    Label(tiket_frame, text='Boarding Pass', font='Helvetica 13 bold', fg='#8cc53d', bg='black').place(x=195, y=125)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Kelas').place(x=0, y=150)
    Label(tiket_frame, text=': ' + kelas_input.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black') \
        .place(x=120, y=150)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Nama').place(x=0, y=180)
    Label(tiket_frame, text=': ' + input_nama.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=180)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Tujuan').place(x=0, y=210)
    Label(tiket_frame, text=': ' + maskapai_input.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black') \
        .place(x=120, y=210)
    Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Waktu').place(x=0, y=240)
    Label(tiket_frame, text=': ' + waktu_input.get(), font='Helvetica 10 bold', fg='#8cc53d', bg='black')\
        .place(x=120, y=240)
    # Label(tiket_frame, font='Helvetica 10 bold', fg='#8cc53d', bg='black', text='Seat').place(x=0, y=270)
    # Label(tiket_frame, text=': ' + seat_penumpang.pack(), font='Helvetica 10 bold', fg='#8cc53d', bg='black').
    # place(x=120, y=270)

    tombol10 = Button(tiket_frame, text='Selesai', width=10, command=lambda: frame_1(tiket_frame)).place(x=220, y=320)


tombol8 = Button(tiket_frame, text='Lihat Ticket', width=10, command=info_tiket).place(x=220, y=80)

# ++++++++++++++++++++++++++++++++++++++++++++++++ END ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print(hargaMaskapaiPilihan)
frame_1(main_page)
root.mainloop()
