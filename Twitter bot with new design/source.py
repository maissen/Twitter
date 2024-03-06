from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkinter.ttk import Combobox

def sources_window():
    def button_click(button):
        # Change background color of all buttons to initial color
        for btn in buttons:
            btn.config(bg="#222222")
        # Change background color of the clicked button to a little brighter
        button.config(bg="#444")

    window = Tk()

    window_width = 1250
    window_height = 670

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
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
        outline=""
    )

    #navbar 
    canvas.create_rectangle(
        0.0,
        0.0,
        174.0,
        670.0,
        fill="#000",
        outline=""
    )

    sources_btn = Button(
        window,
        text="Sources",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: button_click(sources_btn),
        relief="flat",
        cursor="hand2"
    )
    sources_btn.place(
        x=12.0,
        y=14.0,
        width=151.0,
        height=36.0
    )

    feed_btn = Button(
        window,
        text="Feed",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: button_click(feed_btn),
        relief="flat",
        cursor="hand2"
    )
    feed_btn.place(
        x=12.0,
        y=75.0,
        width=151.0,
        height=36.0
    )

    queue_btn = Button(
        window,
        text="Queue",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: button_click(queue_btn),
        relief="flat",
        cursor="hand2"
    )
    queue_btn.place(
        x=12.0,
        y=136.0,
        width=151.0,
        height=36.0
    )

    buttons = [sources_btn, feed_btn, queue_btn]

    exit_btn = Button(
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
    exit_btn.place(
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
        outline=""
    )

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

    link_entry = Entry(
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    link_entry.place(
        x=492.0,
        y=157.0,
        width=439.0,
        height=33.0
    )

    title_entry = Entry(
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    title_entry.place(
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

    combobox = Combobox(
        window,
        values=["Option 1", "Option 2", "Option 3"],
        state="readonly"
    )
    combobox.place(
        x=492.0,
        y=430.0,
        width=446.0,
        height=39.0
    )

    delete_btn = Button(
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
    delete_btn.place(
        x=808.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    update_btn = Button(
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
    update_btn.place(
        x=650.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

    parse_btn = Button(
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
    parse_btn.place(
        x=492.0,
        y=507.0,
        width=130.0,
        height=36.0
    )

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
    sources_btn.invoke()

    window.mainloop()

sources_window()
