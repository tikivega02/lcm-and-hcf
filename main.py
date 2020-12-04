def hcf(entry1, entry2):
	try:
		number1 = floor(entry1)
		number2 = floor(entry2)

		floor1 = []
		floor2 = []
		floor3 = []
		floor4 = []
		floor5 = []
		floor6 = []
		cf = []

		# number 1
		for a in number1:
			if a not in floor1:
				floor1.append(a)

		for b in floor1:
			if b > 0:
				floor2.append(b)

		for c in floor2:
			if int(entry1)%c == 0:
				floor3.append(c)
				floor3.sort()



		# number 2
		for d in number2:
			if d not in floor4:
				floor4.append(d)

		for e in floor4:
			if e > 0:
				floor5.append(e)

		for f in floor5:
			if int(entry2)%f == 0:
				floor6.append(f)
				floor6.sort()
				 
		# CF
		for g in floor3:
			if g in floor6:
				cf.append(g)

		hcf = cf[0]

		# HCF
		for h in cf:
			if h > hcf:
				hcf = h
		label3['text'] = f'{entry1} = {floor3} \n\n{entry2} = {floor6} \n\nC.F = {cf} \n\nH.C.F = {hcf}'

	except ValueError:
		label3['text'] = 'The entrys are empty'

	except IndexError:
		label3['text'] = 'Sorry, you entrys are out of range  (it must be between 1 to 103)'


def lcm(entry1, entry2):
	try:
		number1 = multi(entry1)
		number2 = multi(entry2)

		cm = []

		for inside in number2:
			if inside in number1:
				cm.append(inside)

		lcm = cm[0]

		if inside < lcm:
			lcm = inside

		label3['text'] = f'{entry1} = {number1}\n\n{entry2} = {number2}\n\nC.M = {cm}\n\nL.C.M = {lcm}'

	except ValueError:
		label3['text'] = 'The entrys are empty'

	except IndexError:
		label3['text'] = f"{entry1} = {number1}\n\n{entry2} = {number2}\n\nSorry, {entry1} and {entry2} do not have any common multiples"


from module import *
from tkinter import *
import tkinter.ttk as ttk

win = Tk()
win.geometry('620x520')
win.title('Find LCM AND HCF')
win.maxsize(620, 520)
#win.minsize(620, 520)
#win.iconbitmap(r'img/icon.ico')
bg = PhotoImage(file='img/landscape.png') 
label = ttk.Label(win, image=bg)
label.place(relwidth=1, relheight=1)

# Frame
frame1 = ttk.Frame(label)
frame1.place(relwidth= 0.4, relheight=0.1, relx=0.05, rely=0.01)
frame2 = ttk.Frame(label)
frame2.place(relwidth= 0.4, relheight=0.1, relx=0.05, rely=0.12)
frame3 = ttk.Frame(label)
frame3.place(relx=0.48, rely=0.01, relwidth=0.2, relheight=0.21)
frame4 = Frame(label, bg='gold', bd=5)
frame4.place(relwidth= 0.9, relheight=0.7, relx=0.05, rely=0.25)
frame6 = ttk.Frame(label)
frame6.place(relx=0.7, rely=0.01, relwidth=0.2, relheight=0.21)

# Label
label1 = ttk.Label(frame1, text='Number:')
label1.place(relheight=1, relwidth=0.3)
label2 = ttk.Label(frame2, text='Number:')
label2.place(relheight=1, relwidth=0.3)
label3 = ttk.Label(frame4, font=('Courier', 13), justify=LEFT, anchor=NW, wraplength='10cm')
label3.place(relwidth=1, relheight=1)

# Entry
entry1 = ttk.Entry(frame1, width=251, font=8)
entry1.place(relheight=1, relx=0.3)
entry2 = ttk.Entry(frame2, width=251, font=8)
entry2.place(relheight=1, relx=0.3)

# Button
button1 = ttk.Button(frame3, text='Find LCM', command=lambda: lcm(entry1.get(), entry2.get()))
button1.place(relwidth=1, relheight=1)
button2 = ttk.Button(frame6, text='Find HCF', command=lambda: hcf(entry1.get(), entry2.get()))
button2.place(relwidth=1, relheight=1)

win.mainloop()
