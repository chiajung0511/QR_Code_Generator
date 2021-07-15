#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter,qrcode,os
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

main_win = tkinter.Tk()
main_win.title(' QR Code Generator ')   #視窗標題
main_win.geometry("680x680")           #修改視窗大小(寬x高)

#global vars
url = False
text = False
email = False
sms = False
qrcodeValue = ''
panel = tkinter.Label(main_win) # for panel.grid_forget()

def disableUrl():
    global url
    labelUrl.grid_forget()
    entryUrl.grid_forget()
    url = False

def disableText():
    global text
    labelText.grid_forget()
    entryText.grid_forget()
    text = False

def disableEmail():
    global email
    labelEmailQRcode.grid_forget()
    labelEmailEmail.grid_forget()
    labelEmailSubject.grid_forget()
    labelEmailMessage.grid_forget()
    entryEmail.grid_forget()
    entryEmailSubject.grid_forget()
    entryEmailMessage.grid_forget()
    email = False

def disableSms():
    global sms
    labelSmsQRcode.grid_forget()
    labelSmsNumber.grid_forget()
    labelSmsMessage.grid_forget()
    entrySmsNumber.grid_forget()
    entrySmsMessage.grid_forget()
    sms = False

def enableUrl():
    global url
    labelUrl.grid(column=1, row=0, padx=10)
    entryUrl.grid(column=2, row=0, padx=10)
    url = True

def enableText():
    global text
    labelText.grid(column=1, row=0, padx=10)
    entryText.grid(column=2, row=0, padx=10)
    text = True

def enableEmail():
    global email
    labelEmailQRcode.grid(column=1, row=0, padx=10,sticky = 'W')
    labelEmailEmail.grid(column=1, row=1, padx=10,sticky ='W')
    labelEmailSubject.grid(column=1, row=2, padx=10,sticky = 'W')
    labelEmailMessage.grid(column=1, row=3, padx=10,sticky = 'W')
    entryEmail.grid(column=2, row=1, padx=10)
    entryEmailSubject.grid(column=2, row=2, padx=10)
    entryEmailMessage.grid(column=2, row=3, padx=10)
    email = True

def enableSms():
    global sms
    labelSmsQRcode.grid(column=1, row=0, padx=10,sticky = 'W')
    labelSmsNumber.grid(column=1, row=1, padx=10,sticky = 'W')
    labelSmsMessage.grid(column=1, row=2, padx=10,sticky = 'W')
    entrySmsNumber.grid(column=2, row=1, padx=10)
    entrySmsMessage.grid(column=2, row=2, padx=10)
    sms = True

def buttonUrlCommand():
    disableText()
    disableEmail()
    disableSms()
    enableUrl()

def buttonTextCommand():
    disableUrl()
    disableEmail()
    disableSms()
    enableText()

def buttonEmailCommand():
    disableUrl()
    disableText()
    disableSms()
    enableEmail()

def buttonSmsCommand():
    disableUrl()
    disableText()
    disableEmail()
    enableSms()

def buttonSaveCommand():
    global qrcodeValue
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
    if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    if filename:
        abs_path = os.path.abspath(filename.name)
        img = qrcode.make(qrcodeValue)
        img.save(abs_path) # saves the image to the input file name. 

def buttonGenerateCommand():
    global url
    global text
    global email
    global sms
    global panel
    global qrcodeValue
    #disable show image
    panel.grid_forget()
    qrcodeValue = ''
    if url == True:
        #https://www.google.com/
        qrcodeValue = entryUrl.get()
    if text == True:
        #ABCD1234
        qrcodeValue = entryText.get()
    if email == True:
        # MATMSG:TO:AAAAA@gmail.com;SUB:email subject;BODY:email message;;
        qrcodeValue = 'MATMSG:TO:' + entryEmail.get() + ';SUB:' + entryEmailSubject.get() + ';BODY:' + entryEmailMessage.get() + ';;'
    if sms == True:
        # SMSTO:09123456789:SMS Message
        qrcodeValue = 'SMSTO:' + entrySmsNumber.get() + ':SMS ' + entrySmsMessage.get()

    img = qrcode.make(qrcodeValue)
    #show image
    imageTKimage = ImageTk.PhotoImage(img)
    panel = tkinter.Label(main_win, image = imageTKimage)
    panel.image = imageTKimage
    panel.grid( column=2,row=6, padx=10)
    
buttonUrl = tkinter.Button(main_win, text = "URL", width = 20, height = 1, background='#0080FF' ,command = buttonUrlCommand)
buttonText = tkinter.Button(main_win, text = "TEXT", width = 20, height = 1, background='#00E3E3', command = buttonTextCommand)
buttonEmail = tkinter.Button(main_win, text = "E-mail", width = 20, height = 1, background='#02F78E',command = buttonEmailCommand)
buttonSms = tkinter.Button(main_win, text = "SMS", width = 20, height = 1, background='#00EC00', command = buttonSmsCommand)
buttonGenerate = tkinter.Button(main_win, text = "Generate", width = 20, height = 1,background="#FF8F59", command = buttonGenerateCommand)
buttonSave = tkinter.Button(main_win, text = "Save", width = 20, height = 1, background='#CA8EFF' , command = buttonSaveCommand)

buttonUrl.grid(column=0, row=0, padx=10, pady=1)
buttonText.grid(column=0, row=1, padx=10, pady=1)
buttonEmail.grid(column=0, row=2, padx=10, pady=1)
buttonSms.grid(column=0, row=3, padx=10, pady=1)
buttonGenerate.grid(column=0, row=4, padx=10, pady=1)
buttonSave.grid(column=0,row=5,padx=10, pady=1)

labelUrl = tkinter.Label(main_win, text = 'URL:')
labelText = tkinter.Label(main_win, text = 'Text:')
labelEmailQRcode = tkinter.Label(main_win, text = 'Email QR Code')
labelEmailEmail = tkinter.Label(main_win, text = 'Email:')
labelEmailSubject = tkinter.Label(main_win, text = 'Subject:')
labelEmailMessage = tkinter.Label(main_win, text = 'Message:')

urlString = tkinter.StringVar()
textString = tkinter.StringVar()
entryUrl = tkinter.Entry(main_win, width=50, textvariable=urlString)
entryText = tkinter.Entry(main_win, width=50, textvariable=textString)

emailString = tkinter.StringVar()
emailSubjectString = tkinter.StringVar()
emailMessageString = tkinter.StringVar()
entryEmail = tkinter.Entry(main_win, width=50, textvariable=emailString)
entryEmailSubject = tkinter.Entry(main_win, width=50, textvariable=emailSubjectString)
entryEmailMessage = tkinter.Entry(main_win, width=50, textvariable=emailMessageString)

labelSmsQRcode = tkinter.Label(main_win, text = 'SMS QR Code')
labelSmsNumber = tkinter.Label(main_win, text = 'Number:')
labelSmsMessage = tkinter.Label(main_win, text = 'Message:')

smsNumberString = tkinter.StringVar()
smsMessageString = tkinter.StringVar()

entrySmsNumber = tkinter.Entry(main_win, width=50, textvariable=smsNumberString)
entrySmsMessage = tkinter.Entry(main_win, width=50, textvariable=smsMessageString)

main_win.mainloop()