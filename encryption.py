from fileinput import filename
import numpy as np
from keyGeneration import *
import random
import csv
from PIL import Image
from PIL import Image as im
from numpy import asarray
import generator.originalSbox
import generator.sbox
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

root = tk.Tk()


def chooseFile():
    global img
    f_types = [('PNG Files', '*.png')]
    global filename
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img = img.resize((300, 200))
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(image=img)
    img_label.image = img
    img_label.grid(column=1, row=1)

    enc_btn = tk.Button(root, textvariable=button_text, command=lambda: encrypt(),
                        font=("Raleway", 13), bg="#000000", fg="white", height=2, width=12)
    button_text.set("Encrypt")
    enc_btn.grid(column=1, row=2)


button_text = tk.StringVar()
send_btn_text = tk.StringVar()
send_btn = tk.Button(root, textvariable=send_btn_text, command=lambda: chooseFile(),
                     font=("Raleway", 13), bg="#000000", fg="white", height=2, width=12)
send_btn_text.set("Send")
send_btn.grid(column=1, row=0)


def encrypt():
    sbox96 = []
    # generate original AES-like S-box
    AES = generator.originalSbox.generateAES().tolist()
    with open("source.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(AES)

    def addToMainSbox(sbox32):
        for i in range(0, len(sbox32)):
            sbox96.append(sbox32[i])

    # row shuffling
    t1 = generator.sbox.getRowShuffled(AES)
    addToMainSbox(t1)

    # column shuffling
    t2 = generator.sbox.getColShuffled(AES)
    addToMainSbox(t2)

    # row-column shuffling
    t3 = generator.sbox.getRowColShuffled(AES)
    addToMainSbox(t3)

    def xor(op1, op2):
        xorArr = []
        for i in range(0, len(op1)):
            xorArr.append(op1[i] ^ op2[i])
        return xorArr

    # convert image into 1d array
    image = Image.open(filename)
    numpydata = asarray(image)

    try:
        row, col, z = numpydata.shape
    except:
        row, col = numpydata.shape
        z = 0

    with open("imgsize.txt", "w", newline="") as f:
        f.write(str(row))
        f.write("\n")
        f.write(str(col))
        f.write("\n")
        f.write(str(z))
        f.close()
    data = []
    pixels = numpydata

    for i in range(row):
        for j in range(col):
            if z != 0:
                for k in range(z):
                    data.append(pixels[i, j, k])
            else:
                data.append(pixels[i, j])

    # generate subkeys for all rounds
    roundkeys = generateKey()
    message = data

    # generate iv
    iv = []
    for i in range(0, 256):
        iv.append(random.randint(0, 255))

    np.savetxt("iv.csv", np.array(iv), delimiter=",", fmt='%d')

    # divide message into blocks of size 256
    i = 0
    blocksOfMessage = []
    while i < len(message)-(len(message) % 256):
        block = []
        for j in range(0, 256):
            block.append(message[i])
            i = i+1
        blocksOfMessage.append(block)

    block = []
    flag = False
    while i < len(message):
        block.append(message[i])
        flag = True
        i = i+1
    if(flag):
        if len(block) < 256:
            for i in range(len(block), 256):
                block.append(0)

        blocksOfMessage.append(block)

    block_num = len(blocksOfMessage)
    round = 8

    sboxIndices = []
    for i in range(0, (block_num*round)):
        sboxIndices.append(random.randint(0, 95))

    np.savetxt("indices.csv", np.array(sboxIndices), delimiter=",", fmt='%d')

    arr = []  # block
    cipher = []
    idx = 0

    for i in range(0, block_num):
        arr = blocksOfMessage[i]
        for j in range(0, round):
            arr = xor(arr, iv)

            # generate 96 sboxes and select one
            sbox = np.array(sbox96[sboxIndices[idx]])
            sbox = sbox.flatten()
            tempArr = xor(arr, sbox)
            arr = xor(tempArr, roundkeys[j])
            idx += 1
        iv = arr
        cipher.append(arr)

    cipher = np.array(cipher)

    np.savetxt("cipher.csv", cipher, delimiter=",", fmt='%d')

    with open('cipher.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    data = np.array(data)
    data = data.flatten()

    data = list(map(int, data))

    t1 = []
    x = 0
    for i in range(0, row):
        t2 = []
        for j in range(0, col):
            t3 = []
            if z != 0:
                for k in range(0, z):
                    t3.append(data[x])
                    x += 1
                t2.append(t3)
            else:
                t2.append(data[x])
                x += 1
        t1.append(t2)

    t1 = np.array(t1)
    try:
        data = Image.fromarray((t1 * 255).astype(np.uint8))
    except:
        data = Image.fromarray(t1)

    data.save('encImg.png')
    print("converted!!!")

    instr = tk.Label(
        root, text="Encrypted!", font="Raleway")
    instr.grid(columnspan=3, column=0, row=3)

    # display encrypted image
    img2 = Image.open('encImg.png')
    img2 = img2.resize((300, 200))
    img2 = ImageTk.PhotoImage(img2)
    img_label2 = tk.Label(image=img2)
    img_label2.image = img2
    img_label2.grid(column=1, row=4)


canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

root.mainloop()
