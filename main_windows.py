from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from csv import *

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
with open('data_maskapai.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        if row[0] != 'NO':
            maskapai.append(row)

hotel = []
with open('hotel.csv') as file_csv:
    reader_csv = reader(file_csv, delimiter=',')
    for row in reader_csv:
        if row[0] != 'NO':
            hotel.append(row)

def frame_1(frame):
    frame.tkraise()


root = Tk()
root.geometry('500x500')
#  root.state('zoomed')
root.title('Soetta-Loka')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


logo = Image.open('logo soettaloka.png')
logo_ico = ImageTk.PhotoImage(logo)
root.wm_iconphoto(False, logo_ico)

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


# kalau mau nambah frame, masukin ke list ini ya
myFrame = [main_page, main_frame, input_frame, issa_frame, bayar_frame]
for frame in myFrame:
    frame.grid(row=0, column=0, sticky='nsew')

# main page
logo_mainpage = Image.open('logo soettaloka black resize.jpg')
logo_mainpage_ico = ImageTk.PhotoImage(logo_mainpage)
Label(main_page, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)

pesan_btm = Button(main_page, text='PESAN TIKET', bg='black', fg='#8cc53d', font='Helvetica 15 bold',
                   command=lambda: frame_1(input_frame))
pesan_btm.place(x=250, y=450, anchor='center')


# frame 1
Label(main_frame, image=logo_mainpage_ico, bd=0, compound=CENTER).place(x=0, y=0)
top_label = Label(main_frame, text='Selamat Datang di Soetta-Loka\nMasukkan data diri anda!',
                  bg='black', fg='#8cc53d', font='Helvetica 15 bold')
top_label.grid(row=0, column=1, sticky='nsew')

label_nama = Label(main_frame, text='Nama', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=1, column=0, sticky='w')
label_ttl = Label(main_frame, text='TTL', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=2, column=0, sticky='w')
label_noktp = Label(main_frame, text='No. KTP', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=3, column=0, sticky='w')
label_alamat = Label(main_frame, text='Alamat', bg='black', fg='#8cc53d', font='Helvetica 10 bold')\
    .grid(row=4, column=0, sticky='w')

input_nama = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_ttl = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_noktp = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_alamat = Entry(main_frame, width=40, borderwidth=3, fg='black', bg='white', font='Helvetica 10')
input_nama.grid(row=1, column=1, columnspan=3)
input_ttl.grid(row=2, column=1, columnspan=3)
input_noktp.grid(row=3, column=1, columnspan=3)
input_alamat.grid(row=4, column=1, columnspan=3)


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
        #  kalau mau ngubah tombol disini saa, posisinya ini di frame ketiga
    tombol2 = Button(main_frame, text='Input', width=10, command=lambda: frame_1(issa_frame)).place(x=120, y=305)



tombol1 = Button(main_frame, text='Cek Data', width=10, command=cek_data1).place(x=120, y=150)
tombol3 = Button(issa_frame, text='Lewati', width=10, command=cek_data1).place(x=100, y=150)
tombol4 = Button(issa_frame, text='Pilih', width=10, command=lambda: frame_1(bayar_frame)).place(x=250, y=150)

# frame 2, input frame
Label(input_frame, text='On-Booking Site', font='Helvetica 15 bold').place(x=170, y=5)
Label(input_frame, text='Jenis Penerbangan').place(x=0, y=50)
Label(input_frame, text='Tujuan').place(x=0, y=75)
Label(input_frame, text='Waktu Keberangkatan').place(x=0, y=100)
Label(input_frame, text='Maskapai').place(x=0, y=125)
Label(input_frame, text='Kelas Penerbangan').place(x=0, y=150)

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
            values.append(row[1] + ' (rute ' + row[2] +')')
    maskapai_input['values'] = values

def harga_kelas(e):
    values = []
    for row in kelas_input :
        if kelas_input.get() == 'Ekonomi' :
            eko=1

#aku bingung deh disini


jenis_input = ttk.Combobox(input_frame, width=37)
jenis_input['values'] = ['Domestik', 'Non-domestik']
jenis_input['state'] = 'readonly'
jenis_input.bind('<<ComboboxSelected>>', ganti_list_tujuan_dan_hotel)

tujuan_input = ttk.Combobox(input_frame, width=37)
tujuan_input['state'] = 'readonly'
tujuan_input.bind('<<ComboboxSelected>>', ganti_list_waktu_dan_maskapai)

waktu_input = ttk.Combobox(input_frame, width=37)
waktu_input['state'] = 'readonly'

maskapai_input = ttk.Combobox(input_frame, width=37)
maskapai_input['state'] = 'readonly'

kelas_input = ttk.Combobox(input_frame, width=37)
kelas_input['values'] = ['Ekonomi', 'Bisnis', 'Eksekutif']
kelas_input['state'] = 'readonly'

hotel_input = ttk.Combobox(issa_frame, width=37)
hotel_input['state'] = 'readonly'



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

#frame bayar
Label(bayar_frame, text='Payment', font='Arial 20 bold').place(x=190, y=5)
Label(bayar_frame, text='Pilih metode pembayaran', font='Arial 12').place(x=150, y=40)
Label(bayar_frame, text='Bayar').place(x=0, y=80)



frame_1(main_page)
root.mainloop()
