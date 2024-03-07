import tkinter as tk

def hide_container():
    container.place_forget()

def show_container():
    container.place(x=0, y=200)

def on_enter(event):
    event.widget.config(bg="green")

def on_leave(event):
    event.widget.config(bg="#9597a8")

def on_double_click(event):
    label_text = event.widget.cget("text")
    entry_title.delete(1.0, "end")
    entry_title.insert("end", label_text)

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

window = tk.Tk()
window.geometry("1500x800")

# Create a parent container frame
container = tk.Frame(window)
container.place(x=0, y=200)

# Create a Canvas widget
canvas = tk.Canvas(container, bg="green", height=538, width=590, bd=0, highlightthickness=0, relief="ridge")
canvas.pack(side=tk.LEFT, padx=211, pady=83)

# Add vertical scrollbar
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

# Configure canvas scrolling
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame to contain the labels
frame = tk.Frame(canvas, bg="orange", width=590)
canvas.create_window((0, 0), window=frame, anchor='nw')

# Add labels to the frame
for i in range(100):
    label = tk.Label(
        frame, 
        text=f"Label {i+1}", 
        bg="#9597a8", 
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
    label.bind("<Double-1>", on_double_click)

# Bind the update_scroll_region function to the frame's size change event
frame.bind("<Configure>", update_scroll_region)

# Entry for title
entry_title = tk.Text(container, bd=0, bg="#9597A8", fg="#000716", highlightthickness=0)
entry_title.place(x=857, y=250, width=356, height=67)

# Entry for description
entry_description = tk.Text(container, bd=0, bg="#9597A8", fg="#000716", highlightthickness=0)
entry_description.place(x=857, y=366, width=356, height=67)

# Entry for hashtags
hashtags_entry = tk.Text(container, bd=0, bg="#9597A8", fg="#000716", highlightthickness=0)
hashtags_entry.place(x=857, y=494, width=356, height=49)

# Create buttons
search_btn = tk.Button(
    container,
    text="Search",
    bg="#222222",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    command=lambda: print("search_btn clicked"),
    relief="flat",
    cursor="hand2"
)
search_btn.place(x=843, y=575, width=182, height=46)

add_to_queue_btn = tk.Button(
    container,
    text="Add to Queue",
    bg="#222222",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    command=lambda: print("add_to_queue_btn clicked"),
    relief="flat",
    cursor="hand2"
)
add_to_queue_btn.place(x=1040, y=575, width=182, height=46)

# Buttons to hide/show the container
hide_button = tk.Button(window, text="Hide Container", command=hide_container)
hide_button.pack()

show_button = tk.Button(window, text="Show Container", command=show_container)
show_button.pack()

window.mainloop()
