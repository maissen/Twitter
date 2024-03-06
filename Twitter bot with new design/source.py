from tkinter import Tk, Canvas, Entry, Button, PhotoImage

def sources_window():
    def button_click(button):
        # Change background color of all buttons to initial color
        for btn in buttons:
            btn.config(bg="#222222")
        # Change background color of the clicked button to a little brighter
        button.config(bg="#444")

    window = Tk()

    window.geometry("1250x670")
    window.configure(bg="#000")

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
        fill="#000",
        outline="")

    button_1 = Button(
        window,
        text="Sources",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: button_click(button_1),
        relief="flat",
        cursor="hand2"
    )
    button_1.place(
        x=12.0,
        y=14.0,
        width=151.0,
        height=36.0
    )

    button_2 = Button(
        window,
        text="Feed",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: button_click(button_2),
        relief="flat",
        cursor="hand2"
    )
    button_2.place(
        x=12.0,
        y=75.0,
        width=151.0,
        height=36.0
    )

    button_3 = Button(
        window,
        text="Queue",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: button_click(button_3),
        relief="flat",
        cursor="hand2"
    )
    button_3.place(
        x=12.0,
        y=136.0,
        width=151.0,
        height=36.0
    )

    buttons = [button_1, button_2, button_3]

    button_4 = Button(
        window,
        text="Exit",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: window.destroy(),
        relief="flat",
        cursor="hand2"
    )
    button_4.place(
        x=12.0,
        y=623.0,
        width=151.0,
        height=36.0
    )

    # Add more buttons similarly...
    
    #local frame to hide/display
    canvas.create_rectangle(
        186.0,
        14.0,
        1239.0,
        659.0,
        fill="green",
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
        text="Delete",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Delete Button clicked"),
        relief="flat",
        cursor="hand2"
    )
    button_5.place(
        x=808.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    button_6 = Button(
        window,
        text="Update",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Update Button clicked"),
        relief="flat",
        cursor="hand2"
    )
    button_6.place(
        x=650.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    button_7 = Button(
        window,
        text="Parse",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("Parse Button clicked"),
        relief="flat",
        cursor="hand2"
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

    # Automatically click the "Sources" button
    button_1.invoke()

    window.mainloop()

sources_window()
