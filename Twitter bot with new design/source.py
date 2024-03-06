from tkinter import Tk, Canvas, Entry, Button, PhotoImage

def sources_window():
    window = Tk()

    window.geometry("1250x670")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=670,
        width=1250,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        174.0,
        0.0,
        1250.0,
        670.0,
        fill="#D7D9E5",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        174.0,
        670.0,
        fill="#222222",
        outline="")

    button_1 = Button(
        window,
        text="Button 1",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=12.0,
        y=14.0,
        width=151.0,
        height=36.0
    )

    button_2 = Button(
        window,
        text="Button 2",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=12.0,
        y=75.0,
        width=151.0,
        height=36.0
    )

    button_3 = Button(
        window,
        text="Button 3",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=12.0,
        y=136.0,
        width=151.0,
        height=36.0
    )

    button_4 = Button(
        window,
        text="Button 4",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=12.0,
        y=623.0,
        width=151.0,
        height=36.0
    )

    # Add more buttons similarly...

    canvas.create_rectangle(
        186.0,
        14.0,
        1239.0,
        659.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        492.0,
        129.0,
        anchor="nw",
        text="Enter rss Link :",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    canvas.create_text(
        492.0,
        237.0,
        anchor="nw",
        text="Enter rss Title :",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    entry_1 = Entry(
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=492.0,
        y=157.0,
        width=439.0,
        height=33.0
    )

    entry_2 = Entry(
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=492.0,
        y=265.0,
        width=439.0,
        height=33.0
    )

    canvas.create_text(
        623.0,
        46.0,
        anchor="nw",
        text="Add new source",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_5 = Button(
        window,
        text="Button 5",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=808.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    button_6 = Button(
        window,
        text="Button 6",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=650.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    button_7 = Button(
        window,
        text="Button 7",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Button 7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=492.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    canvas.create_rectangle(
        492.0,
        430.0,
        938.0,
        469.0,
        fill="#BEBEBE",
        outline="")

    canvas.create_text(
        492.0,
        404.0,
        anchor="nw",
        text="Saved Sources",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    canvas.create_rectangle(
        561.0,
        92.0,
        861.0016784667969,
        93.0,
        fill="#000000",
        outline=""
    )

    window.resizable(False, False)
    window.mainloop()


