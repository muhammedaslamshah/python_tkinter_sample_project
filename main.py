from tkinter import*

window = Tk()


window.title("NEWWESTERLUND")
window.geometry("600x400")
window.resizable(False, False)
window.iconbitmap("./icon.ico")
window.configure(bg="")
# window.attributes("-topmost", 1)


label = Label(window, text="Enter Your Message below")
label.pack()

text_box = Entry(window)
text_box.pack()


def message_sender_function():
    message = text_box.get()
    label_2nd = Label(window, text=" Messeage Send Successfully...\n Message content is : " + message)
    label_2nd.pack()


btn_1 = Button(window, text="Click here", command=message_sender_function)
btn_1.pack()


window.mainloop()