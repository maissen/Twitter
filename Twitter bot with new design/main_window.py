from tkinter import Tk, Canvas, Entry, Button, Text, Scrollbar, Frame, Label
from tkinter.ttk import Combobox
import tkinter as tk

canvas = None  # Define canvas as a global variable

# def load_sources_frame():
    
#     container = Tk.Canvas(window, bg="green", width=1239, height=659, highlightthickness=0, bd=0)
#     container.place(x=186.0, y=14.0)

#     # Set the z-index of the green rectangle to 1
#     canvas.tag_lower("all")

#     # Create a parent container frame
#     container = tk.Canvas(window, bg="green", width=1239.0-186.0, height=659.0-14.0, highlightthickness=0, bd=0)
#     container.place(x=186.0, y=14.0)

#     # Add elements to the parent container
#     container.create_text(
#         492.0 - 186.0,
#         129.0 - 14.0,
#         anchor="nw",
#         text="Enter rss Link :",
#         fill="#000000",
#         font=("Inter", 15)
#     )

#     container.create_text(
#         492.0 - 186.0,
#         237.0 - 14.0,
#         anchor="nw",
#         text="Enter rss Title :",
#         fill="#000000",
#         font=("Inter", 15)
#     )

#     link_entry = tk.Entry(
#         container,
#         bd=0,
#         bg="#9597a8",
#         fg="#000716",
#         highlightthickness=0
#     )
#     link_entry.place(
#         x=492.0 - 186.0,
#         y=157.0 - 14.0,
#         width=439.0,
#         height=33.0
#     )

#     title_entry = tk.Entry(
#         container,
#         bd=0,
#         bg="#BEBEBE",
#         fg="#000716",
#         highlightthickness=0
#     )
#     title_entry.place(
#         x=492.0 - 186.0,
#         y=265.0 - 14.0,
#         width=439.0,
#         height=33.0
#     )

#     container.create_text(
#         623.0 - 186.0,
#         46.0 - 14.0,
#         anchor="nw",
#         text="Add new source",
#         fill="#000000",
#         font=("Inter", 24)
#     )

#     combobox = Combobox(
#         container,
#         values=["Option 1", "Option 2", "Option 3"],
#         state="readonly"
#     )
#     combobox.place(
#         x=492.0 - 186.0,
#         y=430.0 - 14.0,
#         width=446.0,
#         height=39.0
#     )

#     delete_btn = tk.Button(
#         container,
#         text="Delete",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("Delete Button clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     delete_btn.place(
#         x=808.0 - 186.0,
#         y=507.0 - 14.0,
#         width=130.0,
#         height=36.0
#     )

#     update_btn = tk.Button(
#         container,
#         text="Update",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("Update Button clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     update_btn.place(
#         x=650.0 - 186.0,
#         y=507.0 - 14.0,
#         width=130.0,
#         height=36.0
#     )

#     parse_btn = tk.Button(
#         container,
#         text="Parse",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("Parse Button clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     parse_btn.place(
#         x=492.0 - 186.0,
#         y=507.0 - 14.0,
#         width=130.0,
#         height=36.0
#     )

#     container.create_text(
#         492.0 - 186.0,
#         404.0 - 14.0,
#         anchor="nw",
#         text="Saved Sources",
#         fill="#000000",
#         font=("Inter", 15)
#     )

#     container.create_rectangle(
#         561.0 - 186.0,
#         92.0 - 14.0,
#         861.0016784667969 - 186.0,
#         93.0 - 14.0,
#         fill="#000000",
#         outline=""
#     )

#     container.pack()


# def load_feed_frame():
#     global canvas  # Use the global canvas variable
#     main_window.create_rectangle(
#         186.0,
#         14.0,
#         1239.0,
#         659.0,
#         fill="blue",
#         outline=""
#     )

#     main_window.create_text(
#         492.0,
#         129.0,
#         anchor="nw",
#         text="Enter rss Link 2:",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     main_window.create_text(
#         492.0,
#         237.0,
#         anchor="nw",
#         text="Enter rss Title 2:",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     main_window.create_text(
#         492.0,
#         337.0,
#         anchor="nw",
#         text="Enter Hello Title 2:",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     link_entry = Entry(
#         bd=0,
#         bg="#BEBEBE",
#         fg="#000716",
#         highlightthickness=0
#     )
#     link_entry.place(
#         x=492.0,
#         y=157.0,
#         width=439.0,
#         height=33.0
#     )

#     title_entry = Entry(
#         bd=0,
#         bg="#BEBEBE",
#         fg="#000716",
#         highlightthickness=0
#     )
#     title_entry.place(
#         x=492.0,
#         y=265.0,
#         width=439.0,
#         height=33.0
#     )

#     main_window.create_text(
#         623.0,
#         46.0,
#         anchor="nw",
#         text="Your Feed",
#         fill="#000000",
#         font=("Inter", 24 * -1)
#     )

#     combobox = Combobox(
#         values=["Option 1", "Option 2", "Option 3"],
#         state="readonly"
#     )
#     combobox.place(
#         x=492.0,
#         y=430.0,
#         width=446.0,
#         height=39.0
#     )

#     delete_btn = Button(
#         text="Delete",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("Delete Button clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     delete_btn.place(
#         x=808.0,
#         y=507.0,
#         width=130.0,
#         height=36.0
#     )

#     update_btn = Button(
#         text="Update",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("Update Button clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     update_btn.place(
#         x=650.0,
#         y=507.0,
#         width=130.0,
#         height=36.0
#     )

#     parse_btn = Button(
#         text="Parse",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("Parse Button clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     parse_btn.place(
#         x=492.0,
#         y=507.0,
#         width=130.0,
#         height=36.0
#     )

#     main_window.create_text(
#         492.0,
#         404.0,
#         anchor="nw",
#         text="Saved Sources 2",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     main_window.create_rectangle(
#         561.0,
#         92.0,
#         861.0016784667969,
#         93.0,
#         fill="#000000",
#         outline=""
#     )

# def load_queue_frame():
#     global canvas  # Use the global canvas variable
#     canvas.create_rectangle(
#         186.0,
#         14.0,
#         1239.0,
#         659.0,
#         fill="orange",
#         outline=""
#     )

#     ##
#     ##
#     ################################
#     canvas.create_rectangle(
#         186.0,
#         14.0,
#         1239.0,
#         659.0,
#         fill="#d9d9d9",
#         outline="")

#     canvas.create_rectangle(
#         843.0,
#         451.0,
#         1222.0,
#         552.0,
#         fill="#9597A8",
#         outline="")


#     search_btn = Button(
#         window,
#         text="X",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("load btn clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     search_btn.place(
#         x=1183.0,
#         y=457.0,
#         width=30.0,
#         height=30.0
#     )


#     canvas.create_rectangle(
#         843.0,
#         338.0,
#         1222.0,
#         439.0,
#         fill="#9597A8",
#         outline="")

#     canvas.create_rectangle(
#         843.0,
#         223.0,
#         1222.0,
#         324.0,
#         fill="#9597A8",
#         outline="")

#     entry_title = Text(
#         bd=0,
#         bg="#9597A8",
#         fg="#000716",
#         highlightthickness=0
#     )
#     entry_title.place(
#         x=857.0,
#         y=250.0,
#         width=356.0,
#         height=67.0
#     )

#     entry_description = Text(
#         bd=0,
#         bg="#9597A8",
#         fg="#000716",
#         highlightthickness=0
#     )
#     entry_description.place(
#         x=857.0,
#         y=366.0,
#         width=356.0,
#         height=67.0
#     )

#     hashtags_entry = Text(
#         bd=0,
#         bg="#9597A8",
#         fg="#000716",
#         highlightthickness=0
#     )
#     hashtags_entry.place(
#         x=857.0,
#         y=494.0,
#         width=356.0,
#         height=49.0  # Adjusted height for two rows
#     )


#     canvas.create_text(
#         857.0,
#         227.0,
#         anchor="nw",
#         text="Entry’s Title :",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     canvas.create_text(
#         857.0,
#         343.0,
#         anchor="nw",
#         text="Entry’s Summary :",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     canvas.create_text(
#         857.0,
#         463.0,
#         anchor="nw",
#         text="Recent Hashtags :",
#         fill="#000000",
#         font=("Inter", 15 * -1)
#     )

#     canvas.create_text(
#         211.0,
#         29.0,
#         anchor="nw",
#         text="From : Example (15 entries)",
#         fill="#000000",
#         font=("Inter", 14 * -1)
#     )

#     canvas.create_text(
#         211.0,
#         48.0,
#         anchor="nw",
#         text="Feed : Some title here!",
#         fill="#000000",
#         font=("Inter", 20 * -1)
#     )

#     canvas.create_rectangle(
#         843.0,
#         37.0,
#         1222.0,
#         209.0,
#         fill="yellow",
#         outline="")

#     def update_scroll_region(event):
#         canvas.configure(scrollregion=canvas.bbox("all"))

#     def on_enter(event):
#         event.widget.config(bg="green")

#     # Function to handle mouse leave event
#     def on_leave(event):
#         event.widget.config(bg="#9597a8")

#     def on_double_click(event):
#         label_text = event.widget.cget("text")
#         entry_title.delete(1.0, "end")
#         entry_title.insert("end", label_text)

#     # Create a canvas
#     canvas = Canvas(window, bg="#D7D9E5", height=538, width=590, bd=0, highlightthickness=0, relief="ridge")
#     canvas.place(x=211, y=83)

#     # Add vertical scrollbar
#     scrollbar = Scrollbar(window, orient="vertical")
#     scrollbar.place(x=810, y=83, height=538)

#     # Configure canvas scrolling
#     canvas.config(yscrollcommand=scrollbar.set)

#     # Bind scrollbar to canvas
#     scrollbar.config(command=canvas.yview)

#     # Create a frame to contain the labels
#     frame = Frame(canvas, bg="orange", width=590)
#     canvas.create_window((0, 0), window=frame, anchor='nw')


#     # Add labels to the frame
#     for i in range(100):
#         label = Label(
#             frame, 
#             text=f"Label {i+1}", 
#             bg="#9597a8", 
#             width=90,  
#             anchor='w', 
#             padx=7, 
#             pady=7, 
#             cursor='hand2', 
#             wraplength=590, 
#             justify='left'
#         )
#         label.pack(pady=0, fill='x')
#         label.bind("<Enter>", on_enter)
#         label.bind("<Leave>", on_leave)
#         label.bind("<Double-1>", on_double_click) # for double clicks

#     # Bind the update_scroll_region function to the frame's size change event
#     frame.bind("<Configure>", update_scroll_region)

#     search_btn = Button(
#         window,
#         text="Search",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("search_btn clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     search_btn.place(
#         x=843.0,
#         y=575.0,
#         width=182.0,
#         height=46.0
#     )

#     add_to_queue_btn = Button(
#         window,
#         text="Add to Queue",
#         bg="#222222",
#         fg="#FFFFFF",
#         bd=0,
#         highlightthickness=0,
#         command=lambda: print("add_to_queue_btn clicked"),
#         relief="flat",
#         cursor="hand2"
#     )
#     add_to_queue_btn.place(
#         x=1040.0,
#         y=575.0,
#         width=182.0,
#         height=46.0
#     )

#     window.resizable(False, False)

#     # Create scrollbars
#     scrollbar_entry_title = Scrollbar(window, orient="vertical", width=13, troughcolor="#9597A8", bd=0, command=entry_title.yview)
#     scrollbar_entry_description = Scrollbar(window, orient="vertical", width=13, troughcolor="#9597A8", bd=0, command=entry_description.yview)
#     scrollbar_hashtags_entry = Scrollbar(window, orient="vertical", width=13, troughcolor="#9597A8", bd=0, command=hashtags_entry.yview)

#     # Set scrollbar to the text areas
#     entry_title.config(yscrollcommand=scrollbar_entry_title.set)
#     entry_description.config(yscrollcommand=scrollbar_entry_description.set)
#     hashtags_entry.config(yscrollcommand=scrollbar_hashtags_entry.set)

#     # Place the scrollbars
#     scrollbar_entry_title.place(x=1220.0, y=223.0, height=101.0, anchor="nw")
#     scrollbar_entry_description.place(x=1220.0, y=338.0, height=101.0, anchor="nw")
#     scrollbar_hashtags_entry.place(x=1220.0, y=451.0, height=101.0, anchor="nw")

#     # Center the arrows horizontally
#     window.update_idletasks()
#     arrow_height = scrollbar_entry_title.winfo_reqheight() / 2
#     scrollbar_entry_title.config(command=entry_title.yview)
#     scrollbar_entry_description.config(command=entry_description.yview)
#     scrollbar_hashtags_entry.config(command=hashtags_entry.yview)

def load_main_window():
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

    # red rectangle
    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        174.0,
        0.0,
        1250.0,
        670.0,
        fill="#d9d9d9",
        outline=""
    )

    # navbar 
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

    
    ##############################################################################################################################
    # Sources section
    sources_frame = tk.Canvas(window, bg="#d9d9d9", width=1050, height=644, highlightthickness=0, bd=0)
    sources_frame.place(x=1239.0, y=659.0)

    # Add elements to the parent sources_frame
    sources_frame.create_text(
        492.0 - 186.0,
        129.0 - 14.0,
        anchor="nw",
        text="Enter rss Link :",
        fill="#000000",
        font=("Inter", 15)
    )

    sources_frame.create_text(
        492.0 - 186.0,
        237.0 - 14.0,
        anchor="nw",
        text="Enter rss Title :",
        fill="#000000",
        font=("Inter", 15)
    )

    link_entry = tk.Entry(
        sources_frame,
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    link_entry.place(
        x=492.0 - 186.0,
        y=157.0 - 14.0,
        width=439.0,
        height=33.0
    )

    title_entry = tk.Entry(
        sources_frame,
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    title_entry.place(
        x=492.0 - 186.0,
        y=265.0 - 14.0,
        width=439.0,
        height=33.0
    )

    add_source = tk.Button(
        sources_frame,
        text="Add Source",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        command=lambda: print("Add source Button clicked"),
    )
    add_source.place(
        x=622,
        y=305,
        width=130.0,
        height=36.0
    )

    sources_frame.create_text(
        623.0 - 186.0,
        46.0 - 14.0,
        anchor="nw",
        text="Add new source",
        fill="#000000",
        font=("Inter", 24)
    )

    combobox = Combobox(
        sources_frame,
        values=["Option 1", "Option 2", "Option 3"],
        state="readonly"
    )
    combobox.place(
        x=492.0 - 186.0,
        y=430.0 - 14.0,
        width=446.0,
        height=39.0
    )

    delete_btn = tk.Button(
        sources_frame,
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
        x=808.0 - 186.0,
        y=507.0 - 14.0,
        width=130.0,
        height=36.0
    )

    update_btn = tk.Button(
        sources_frame,
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
        x=650.0 - 186.0,
        y=507.0 - 14.0,
        width=130.0,
        height=36.0
    )

    parse_btn = tk.Button(
        sources_frame,
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
        x=492.0 - 186.0,
        y=507.0 - 14.0,
        width=130.0,
        height=36.0
    )

    sources_frame.create_text(
        492.0 - 186.0,
        404.0 - 14.0,
        anchor="nw",
        text="Saved Sources",
        fill="#000000",
        font=("Inter", 15)
    )

    sources_frame.create_rectangle(
        561.0 - 186.0,
        92.0 - 14.0,
        861.0016784667969 - 186.0,
        93.0 - 14.0,
        fill="#000000",
        outline=""
    )

    ##############################################################################################################################



    ##############################################################################################################################
    # Feed section
    feed_frame = tk.Canvas(window, bg="#d9d9d9", width=1050, height=644, highlightthickness=0, bd=0)
    feed_frame.place(x=1239.0, y=659.0)

    feed_frame.create_rectangle( #hashtags
    657,
    437,
    1036,
    538.0,
    fill="#9597a8",
    outline="")

    load_hashtags_btn = tk.Button(
        feed_frame,
        text="L",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("load btn clicked"),
        relief="flat",
        cursor="hand2"
    )
    load_hashtags_btn.place(
        x=997,
        y=443,
        width=30,
        height=30.0
    )

    feed_frame.create_rectangle( #summary
    657,
    324,
    1036,
    425,
    fill="#9597a8",
    outline="")

    feed_frame.create_rectangle( #title
    657,
    209,
    1036,
    310,
    fill="#9597a8",
    outline="")

    entry_title = tk.Text(#title input
        feed_frame,
        bd=0,
        bg="#9597a8",
        fg="#000",
        highlightthickness=0
    )
    entry_title.place(
        x=671,
        y=236,
        width=356,
        height=69
    )

    entry_description = tk.Text( #summary input
        feed_frame,
        bd=0,
        bg="#9597a8",
        fg="#000",
        highlightthickness=0
    )
    entry_description.place(
        x=671,
        y=352,
        width=356,
        height=69
    )

    hashtags_entry = tk.Text( #hashtags input
        feed_frame,
        bd=0,
        bg="#9597a8",
        fg="#000",
        highlightthickness=0
    )
    hashtags_entry.place(
        x=671,
        y=480,
        width=356,
        height=51
    )


    feed_frame.create_text(
    671,
    213.0,
    anchor="nw",
    text="Entry’s Title :",
    fill="#000000",
    font=("Inter", 15 * -1)
    )

    feed_frame.create_text(
        671,
        329,
        anchor="nw",
        text="Entry’s Summary :",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    feed_frame.create_text(
        671,
        449,
        anchor="nw",
        text="Recent Hashtags :",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    feed_frame.create_text(
    25,
    15,
    anchor="nw",
    text="From : Example (15 entries)",
    fill="#000000",
    font=("Inter", 12 * -1)
    )

    feed_frame.create_text(
        25,
        34,
        anchor="nw",
        text="Feed : Some title here!",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    
    feed_frame.create_rectangle( # entry img
    657,
    23.0,
    657 + 379,
    23 + 172,
    fill="yellow",
    outline="")


    def on_enter(event):
        event.widget.config(bg="royalblue")

    # Function to handle mouse leave event
    def on_leave(event):
        event.widget.config(bg="#d9d9d9")

    def on_double_click(event):
        label_text = event.widget.cget("text")
        entry_title.delete(1.0, "end")
        entry_title.insert("end", label_text)



    # Create a canvas
    entries_frame = Canvas(feed_frame, bg="#D7D9E5", height=538, width=590, bd=0, highlightthickness=0, relief="ridge")
    entries_frame.place(x=25, y=69)

    # Add vertical scrollbar
    scrollbar = Scrollbar(feed_frame, orient="vertical")
    scrollbar.place(x=25 + 590, y=69, height=538)

    # Configure entries_frame scrolling
    entries_frame.config(yscrollcommand=scrollbar.set)

    # Bind scrollbar to entries_frame
    scrollbar.config(command=entries_frame.yview)

    # Create a frame to contain the labels
    entries_list = Frame(entries_frame, bg="orange", width=590)
    entries_frame.create_window((0, 0), window=entries_list, anchor='nw')

    # Add labels to the frame
    # for i in range(100):
    #     label = Label(
    #         frame, 
    #         text=f"Label {i+1}", 
    #         # bg="#9597a8", 
    #         width=90,  
    #         anchor='w', 
    #         padx=7, 
    #         pady=7, 
    #         cursor='hand2', 
    #         wraplength=590, 
    #         justify='left'
    #     )
    for i in range(100):
        label = Label(
            entries_list, 
            text=f"Label {i+1}", 
            bg="#d9d9d9", 
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

    # Function to update scroll region
    def update_scroll_region(event):
        entries_frame.configure(scrollregion=entries_frame.bbox("all"))

    # Bind the update_scroll_region function to the frame's size change event
    entries_list.bind("<Configure>", update_scroll_region)







    search_btn = Button(
    feed_frame,
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
        x=657,
        y=575.0,
        width=182.0,
        height=46.0
    )

    add_to_queue_btn = Button(
    feed_frame,
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
        x=854,
        y=575.0,
        width=182.0,
        height=46.0
    )
    
    
    
    

    ##############################################################################################################################


    ##############################################################################################################################
    # Add to queue section!
    # Create a frame to contain the posts
    # Create the queue_frame
    # Create the queue_frame
    queue_frame = tk.Frame(window, bg="#d9d9d9", width=1253, height=644, highlightthickness=0, bd=0)
    queue_frame.place(x=1239.0, y=659.0)

    # Add text label above the queue_list canvas
    queue_label = tk.Label(queue_frame, text="Your Queue list", bg="#d9d9d9", fg="black", font=("Inter", 16))
    queue_label.pack(pady=10)  # Adjust padding according to your preference

    # Create a canvas to contain the posts
    queue_list = tk.Canvas(queue_frame, bg="#d9d9d9", width=1023, height=543)
    queue_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Adjust this according to your layout requirements

    # Calculate total content height
    total_content_height = (3 * (15 + 130)) + 100  # Height of 10 rectangles

    # Configure canvas scrolling
    queue_list.config(scrollregion=(0, 0, 1010, total_content_height))  # Adjust width according to your content

    # Create a vertical scrollbar for the canvas
    scrollbar = tk.Scrollbar(queue_frame, orient="vertical", command=queue_list.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure canvas scrolling
    queue_list.config(yscrollcommand=scrollbar.set)

    # Create rectangles as posts
    y = 15
    for i in range(3):  # Loop only until the second-to-last rectangle
        post = tk.Canvas(queue_list, bg="#d9d9d9", width=996, height=130)
        queue_list.create_window(14, y, anchor="nw", window=post)

        post.create_rectangle(  # entry img
            11.5,
            10,
            180,
            125,
            fill="royalblue",
            outline="#bfbfbf",
            width=1
        )

        # Create Post's title
        label = tk.Label(post, text="Post title", bg=post.cget('bg'))
        label.place(x=180+15, y=10)
        # Create Posts's description
        description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        if len(description) > 300:
            label = tk.Label(post, text=f"{description[:300]}...", bg=post.cget('bg'), wraplength=700, anchor="w", justify="left")
        else:
            label = tk.Label(post, text=f"{description}", bg=post.cget('bg'), wraplength=700, anchor="w", justify="left")
        label.place(x=180+15, y=40)

        # label of Post's date
        label = tk.Label(post, text="18 Oct 2024", bg=post.cget('bg'))
        label.place(x=180+15, y=102)

        delete_post_from_queue_btn = tk.Button(
            post,
            text="D",
            bg="#222222",
            fg="#FFFFFF",
            bd=0,
            highlightthickness=0,
            command=lambda: print("delete_post_from_queue_btn clicked"),
            relief="flat",
            cursor="hand2"
        )
        delete_post_from_queue_btn.place(
            x=992-25-3,
            y=9,
            width=25,
            height=25
        )

        push_post_from_queue = tk.Button(
            post,
            text="P",
            bg="#222222",
            fg="#FFFFFF",
            bd=0,
            highlightthickness=0,
            command=lambda: print("push_post_from_queue clicked"),
            relief="flat",
            cursor="hand2"
        )
        push_post_from_queue.place(
            x=992-25*2-10,
            y=9,
            width=25,
            height=25
        )

        view_post_from_queue = tk.Button(
            post,
            text="V",
            bg="#222222",
            fg="#FFFFFF",
            bd=0,
            highlightthickness=0,
            command=lambda: print("view_post_from_queue clicked"),
            relief="flat",
            cursor="hand2"
        )
        view_post_from_queue.place(
            x=992-25*3-17,
            y=9,
            width=25,
            height=25
        )



        y += 15 + 130  # Increment y-coordinate to properly position each child canvas
        
    

    push_posts = tk.Button(
        queue_frame,
        text="Push All Posts",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: print("push_posts clicked"),
        relief="flat",
        cursor="hand2"
    )
    push_posts.place(
        x=425,  # Adjust the x-coordinate to move the button to a visible location
        y=550,  # Adjust the y-coordinate to move the button to a visible location
        width=182.0,
        height=46.0
    )
    ##############################################################################################################################
    def button_click(button):
        # Change background color of all buttons to initial color
        for btn in buttons:
            btn.config(bg="#222222")
        # Change background color of the clicked button to a little brighter
        button.config(bg="#444")

        if button == sources_btn:
            sources_frame.place_configure(x=186.0, y=14.0)
            feed_frame.place_configure(x=1000.0, y=1000.0)
            queue_frame.place_configure(x=1000.0, y=1000.0)
            pass
        elif button == feed_btn:
            feed_frame.place_configure(x=186.0, y=14.0)
            sources_frame.place_configure(x=1000.0, y=1000.0)
            queue_frame.place_configure(x=1000.0, y=1000.0)
            pass
        elif button == queue_btn:
            feed_frame.place_configure(x=1000.0, y=1000.0)
            sources_frame.place_configure(x=1000.0, y=1000.0)
            queue_frame.place_configure(x=186.0, y=14.0)
            pass

    window.resizable(False, False)
    # Automatically click the "Sources" button
    queue_btn.invoke()

    window.mainloop()

load_main_window()
