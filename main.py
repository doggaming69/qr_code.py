from tkinter import * #python qr code gui tkinter
import qrcode
img = qrcode.make ('https://github.com/doggaming69/rps.py') #link here
img.save('img.png')
window = Tk()
window.title ("qr code")
qrcode = PhotoImage(file='img.png')
label = Label(image=qrcode)
label.pack()
window.mainloop()
