from tkinter import Tk, Canvas, Button, Text, Scrollbar, Frame, Label

window = Tk()

window.geometry("1250x670")
window.configure(bg="#FFFFFF")


# canvas = Canvas(
#     window,
#     bg="red",
#     height=670,
#     width=1250,
#     bd=0,
#     highlightthickness=0,
#     relief="ridge"
# )

# canvas.place(x=0, y=0)

##
##
################################
canvas = Canvas(
    window,
    bg="red",
    height=670,
    width=1250,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_rectangle(
    186.0,
    14.0,
    1239.0,
    659.0,
    fill="royalblue",
    outline="")
    

canvas.create_rectangle(
    843.0,
    451.0,
    1222.0,
    552.0,
    fill="#9597A8",
    outline="")


search_btn = Button(
    window,
    text="X",
    bg="#222222",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    command=lambda: print("load btn clicked"),
    relief="flat",
    cursor="hand2"
)
search_btn.place(
    x=1183.0,
    y=457.0,
    width=30.0,
    height=30.0
)


canvas.create_rectangle(
    843.0,
    338.0,
    1222.0,
    439.0,
    fill="#9597A8",
    outline="")

canvas.create_rectangle(
    843.0,
    223.0,
    1222.0,
    324.0,
    fill="#9597A8",
    outline="")

entry_title = Text(
    bd=0,
    bg="#9597A8",
    fg="#000716",
    highlightthickness=0
)
entry_title.place(
    x=857.0,
    y=250.0,
    width=356.0,
    height=67.0
)

entry_description = Text(
    bd=0,
    bg="#9597A8",
    fg="#000716",
    highlightthickness=0
)
entry_description.place(
    x=857.0,
    y=366.0,
    width=356.0,
    height=67.0
)

hashtags_entry = Text(
    bd=0,
    bg="#9597A8",
    fg="#000716",
    highlightthickness=0
)
hashtags_entry.place(
    x=857.0,
    y=494.0,
    width=356.0,
    height=49.0  # Adjusted height for two rows
)


canvas.create_text(
    857.0,
    227.0,
    anchor="nw",
    text="Entry’s Title :",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    857.0,
    343.0,
    anchor="nw",
    text="Entry’s Summary :",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    857.0,
    463.0,
    anchor="nw",
    text="Recent Hashtags :",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    211.0,
    29.0,
    anchor="nw",
    text="From : Example (15 entries)",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    211.0,
    48.0,
    anchor="nw",
    text="Feed : Some title here!",
    fill="#000000",
    font=("Inter", 20 * -1)
)










canvas.create_rectangle(
    843.0,
    37.0,
    1222.0,
    209.0,
    fill="yellow",
    outline="")

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_enter(event):
    event.widget.config(bg="green")

# Function to handle mouse leave event
def on_leave(event):
    event.widget.config(bg="#9597a8")

def on_double_click(event):
    label_text = event.widget.cget("text")
    entry_title.delete(1.0, "end")
    entry_title.insert("end", label_text)

# Create a canvas
canvas = Canvas(window, bg="#D7D9E5", height=538, width=590, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=211, y=83)

# Add vertical scrollbar
scrollbar = Scrollbar(window, orient="vertical")
scrollbar.place(x=810, y=83, height=538)

# Configure canvas scrolling
canvas.config(yscrollcommand=scrollbar.set)

# Bind scrollbar to canvas
scrollbar.config(command=canvas.yview)

# Create a frame to contain the labels
frame = Frame(canvas, bg="orange", width=590)
canvas.create_window((0, 0), window=frame, anchor='nw')


# Add labels to the frame
for i in range(100):
    label = Label(
        frame, 
        text=f"Label {i+1}", 
        # bg="#9597a8", 
        width=90,  
        anchor='w', 
        padx=7, 
        pady=7, 
        cursor='hand2', 
        wraplength=590, 
        justify='left'
    )
    label.pack(pady=0, fill='x')
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<Double-1>", on_double_click) # for double clicks

# Bind the update_scroll_region function to the frame's size change event
frame.bind("<Configure>", update_scroll_region)












search_btn = Button(
    window,
    text="Search",
    bg="#222222",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    command=lambda: print("search_btn clicked"),
    relief="flat",
    cursor="hand2"
)
search_btn.place(
    x=843.0,
    y=575.0,
    width=182.0,
    height=46.0
)

add_to_queue_btn = Button(
    window,
    text="Add to Queue",
    bg="#222222",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    command=lambda: print("add_to_queue_btn clicked"),
    relief="flat",
    cursor="hand2"
)
add_to_queue_btn.place(
    x=1040.0,
    y=575.0,
    width=182.0,
    height=46.0
)



window.resizable(False, False)

# Create scrollbars
scrollbar_entry_title = Scrollbar(window, orient="vertical", width=13, troughcolor="#9597A8", bd=0, command=entry_title.yview)
scrollbar_entry_description = Scrollbar(window, orient="vertical", width=13, troughcolor="#9597A8", bd=0, command=entry_description.yview)
scrollbar_hashtags_entry = Scrollbar(window, orient="vertical", width=13, troughcolor="#9597A8", bd=0, command=hashtags_entry.yview)

# Set scrollbar to the text areas
entry_title.config(yscrollcommand=scrollbar_entry_title.set)
entry_description.config(yscrollcommand=scrollbar_entry_description.set)
hashtags_entry.config(yscrollcommand=scrollbar_hashtags_entry.set)

# Place the scrollbars
scrollbar_entry_title.place(x=1220.0, y=223.0, height=101.0, anchor="nw")
scrollbar_entry_description.place(x=1220.0, y=338.0, height=101.0, anchor="nw")
scrollbar_hashtags_entry.place(x=1220.0, y=451.0, height=101.0, anchor="nw")

# Center the arrows horizontally
window.update_idletasks()
arrow_height = scrollbar_entry_title.winfo_reqheight() / 2
scrollbar_entry_title.config(command=entry_title.yview)
scrollbar_entry_description.config(command=entry_description.yview)
scrollbar_hashtags_entry.config(command=hashtags_entry.yview)

window.mainloop()
