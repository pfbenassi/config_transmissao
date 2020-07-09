from tkinter import*

def save_info():
    faceServer_info = faceServer_txt.get()
    faceKey_info = faceKey_txt.get()

    youTubeServer_info = youTubeServer_txt.get()
    youTubeKey_info = youTubeKey_txt.get()

    print(faceServer_info, faceKey_info, youTubeServer_info, youTubeKey_info)

    file = open("info_key.txt", "w")
    file.write("Facebook Server: {}".format(faceServer_info))
    file.write("\nFacebook Key: {}".format(faceKey_info))
    file.write("\nYouTube Server: {}".format(youTubeServer_info))
    file.write("\nYouTube Key: {}".format(youTubeKey_info))
    file.close()

    screen.destroy()


screen = Tk()
screen.geometry("500x320")
screen.title("Configuração de Transmissão")
heading = Label(text = "Configuração de Transmissão", bg = "grey", fg = "black", width="500", height = "2")
heading.pack()

# Campos para Facebook
faceServer_lbl = Label(text = "Servidor RMTP Facebook ", )
faceKey_lbl = Label(text = "Chave de Stream Facebook ", )
faceServer_lbl.place(x = 15, y = 50)
faceKey_lbl.place(x = 15, y = 100)

faceServer = StringVar()
faceKey = StringVar()

faceServer_txt = Entry(textvariable = faceServer, width = "50")
faceKey_txt = Entry(textvariable = faceKey, width= "50")
faceServer_txt.place(x=180 , y=50)
faceKey_txt.place(x=180 , y=100)

# Campos para YouTube
youTubeServer_lbl = Label(text = "Servidor RMTP YouTube ", )
youTubeKey_lbl = Label(text = "Chave de Stream YouTube ", )
youTubeServer_lbl.place(x = 15, y = 150)
youTubeKey_lbl.place(x = 15, y = 200)

youTubeServer = StringVar()
youTubeKey = StringVar()

youTubeServer_txt = Entry(textvariable = youTubeServer, width = "50")
youTubeKey_txt = Entry(textvariable = youTubeKey, width = "50")
youTubeServer_txt.place(x=180 , y=150)
youTubeKey_txt.place(x=180 , y=200)

register_btn = Button(screen, text = "Salvar", width = "20", height = "2", command = save_info, bg = "grey")
register_btn.place(x=150, y = 250)

screen.mainloop()