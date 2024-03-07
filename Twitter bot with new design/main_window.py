from tkinter import Tk, Canvas, Entry, Button, Text, Scrollbar, Frame, Label
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import Image, ImageTk
import pickle
import webbrowser
from my_functions import *


def popup_message(title, message):
    # Create the popup window
    popup = tk.Toplevel()
    popup.title(title)
    popup_width = 300
    popup_height = 80

    # Get the screen width and height
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Calculate the position of the popup window to center it on the screen
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2

    # Set the geometry of the popup window
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    # Create and pack the label
    label = ttk.Label(popup, text=message)
    label.pack(pady=20)

    # Schedule the closing of the popup after 3500 milliseconds (3.5 seconds)
    popup.after(3500, popup.destroy)


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
    def save_rss(saved_links_from_file, rss_title, rss_link):
        title = rss_title.get()
        link = rss_link.get()
        
        if title and link:
            try:
                with open("My_rss_sources.dat", "rb") as file:
                    rss_sources = pickle.load(file)
            except FileNotFoundError:
                rss_sources = []

            for source in rss_sources:
                if source["title"] == title:
                    popup_message("Error", "RSS title already exists!")
                    return
                if source["link"] == link:
                    popup_message("Error", "RSS link already exists!")
                    return

            rss_sources.append({"title": title, "link": link})
            with open("My_rss_sources.dat", "wb") as file:
                pickle.dump(rss_sources, file)

            if "-- There's no RSS saved --" in saved_links_from_file["values"]:
                saved_links_from_file.delete(saved_links_from_file["values"].index("-- There's no RSS saved --"))

            saved_links_from_file["values"] = [source["title"] for source in rss_sources]
            saved_links_from_file.set(title)

            rss_title.delete(0, tk.END)
            rss_link.delete(0, tk.END)

            popup_message("Success", f"{title} saved successfully")
        else:
            if not link:
                popup_message("Error", "Please enter a Link!")
            elif not title:
                popup_message("Error", "Please enter a Title!")


    def delete_rss(saved_links_from_file):
        title_to_delete = saved_links_from_file.get()
        if title_to_delete:
            try:
                with open("My_rss_sources.dat", "rb") as file:
                    rss_sources = pickle.load(file)
            except FileNotFoundError:
                rss_sources = []

            updated_sources = [source for source in rss_sources if source["title"] != title_to_delete]

            with open("My_rss_sources.dat", "wb") as file:
                pickle.dump(updated_sources, file)

            if updated_sources:
                saved_links_from_file["values"] = [source["title"] for source in updated_sources]
                saved_links_from_file.set(updated_sources[0]["title"])
                popup_message("Success", f"{title_to_delete} deleted successfully")
            else:
                saved_links_from_file["values"] = []
                saved_links_from_file.set("-- There's no RSS saved --")
                popup_message("Warning", "There's no saved RSS to delete")
        else:
            popup_message("Error", "No RSS title selected!")


    def delete_confirm_window(saved_links_from_file, rss_source):
        # Create the main window
        window = tk.Tk()
        window.title("Delete Confirmation")

        # Set window width and height
        window_width = 400
        window_height = 140

        # Calculate the center position of the screen
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set window geometry
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create label
        label = ttk.Label(window, text=f"Are you sure you want to delete {rss_source}?")
        label.pack(pady=20)

        # Function to handle delete button click
        def delete_clicked():
            delete_rss(saved_links_from_file)
            window.destroy()
        
        def cancel_clicked():
            window.destroy()
            

        # Create a frame to hold the buttons aligned to the right
        button_frame = ttk.Frame(window)
        button_frame.pack(side="bottom", pady=20)

        # Create the delete button with padding and aligned to the right
        delete_button = ttk.Button(button_frame, text="Delete", command=delete_clicked)
        delete_button.pack(side="right", padx=10)

        # Create the cancel button with padding and aligned to the right
        cancel_button = ttk.Button(button_frame, text="Cancel", command=cancel_clicked)
        cancel_button.pack(side="right", padx=10)

        # Run the main event loop
        window.mainloop()

        def update_rss(saved_links_from_file, new_title, new_link, window):
            # Check if new_title and new_link are not empty
            if not new_title.strip() or not new_link.strip():
                popup_message("Error", "Please enter both title and link!")
                return

            title_to_update = saved_links_from_file.get()
            if title_to_update:
                try:
                    with open("My_rss_sources.dat", "rb") as file:
                        rss_sources = pickle.load(file)
                except FileNotFoundError:
                    rss_sources = []

                # Check if the new title or link already exists
                for source in rss_sources:
                    if source["title"] != title_to_update:  # Skip the current title being updated
                        if source["title"] == new_title:
                            popup_message("Error", "RSS title already exists!")
                            return
                        if source["link"] == new_link:
                            popup_message("Error", "RSS link already exists!")
                            return

                # Update the title and link
                for source in rss_sources:
                    if source["title"] == title_to_update:
                        old_title = source["title"]
                        old_link = source["link"]

                        source["title"] = new_title
                        source["link"] = new_link
                        break

                # Save the updated data back to the file
                with open("My_rss_sources.dat", "wb") as file:
                    pickle.dump(rss_sources, file)

                # Update the values in the combobox
                saved_links_from_file["values"] = [source["title"] for source in rss_sources]
                saved_links_from_file.set(new_title)
                print("Updated!")
                window.destroy()
            else:
                popup_message("Error", "No RSS title selected!")


    def update_rss(saved_links_from_file, new_title, new_link, window):
        # Check if new_title and new_link are not empty
        if not new_title.strip() or not new_link.strip():
            popup_message("Error", "Please enter both title and link!")
            return

        title_to_update = saved_links_from_file.get()
        if title_to_update:
            try:
                with open("My_rss_sources.dat", "rb") as file:
                    rss_sources = pickle.load(file)
            except FileNotFoundError:
                rss_sources = []

            # Check if the new title or link already exists
            for source in rss_sources:
                if source["title"] != title_to_update:  # Skip the current title being updated
                    if source["title"] == new_title:
                        popup_message("Error", "RSS title already exists!")
                        return
                    if source["link"] == new_link:
                        popup_message("Error", "RSS link already exists!")
                        return

            # Update the title and link
            for source in rss_sources:
                if source["title"] == title_to_update:
                    old_title = source["title"]
                    old_link = source["link"]

                    source["title"] = new_title
                    source["link"] = new_link
                    break

            # Save the updated data back to the file
            with open("My_rss_sources.dat", "wb") as file:
                pickle.dump(rss_sources, file)

            # Update the values in the combobox
            saved_links_from_file["values"] = [source["title"] for source in rss_sources]
            saved_links_from_file.set(new_title)
            print("Updated!")
            window.destroy()
        else:
            popup_message("Error", "No RSS title selected!")

    def update_rss_window(saved_links_from_file):
        title_to_update = saved_links_from_file.get()
        if title_to_update:
            try:
                with open("My_rss_sources.dat", "rb") as file:
                    rss_sources = pickle.load(file)
            except FileNotFoundError:
                rss_sources = []

            for source in rss_sources:
                if source["title"] == title_to_update:
                    old_title = source["title"]
                    old_link = source["link"]
                    
                    # Create main window
                    window = tk.Tk()
                    window.title("Update RSS")

                    # Calculate the center position of the screen
                    window_width = 400  # You can adjust this value as needed
                    window_height = 200  # You can adjust this value as needed
                    screen_width = window.winfo_screenwidth()
                    screen_height = window.winfo_screenheight()
                    x = (screen_width - window_width) // 2
                    y = (screen_height - window_height) // 2

                    # Set window geometry
                    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

                    # Create frame for inputs
                    input_frame = ttk.Frame(window)
                    input_frame.pack(padx=10, pady=10)

                    # Label and input for updating link
                    link_label = ttk.Label(input_frame, text="Update link:")
                    link_label.grid(row=0, column=0, sticky="w", padx=(0, 5))

                    link_input = ttk.Entry(input_frame, width=40)
                    link_input.insert(0, old_link)
                    link_input.grid(row=0, column=1, sticky="w")

                    # Add margin between the two lines
                    ttk.Label(input_frame).grid(row=1, columnspan=2, pady=1)

                    # Label and input for updating title
                    title_label = ttk.Label(input_frame, text="Update title:")
                    title_label.grid(row=2, column=0, sticky="w", padx=(0, 5))

                    title_input = ttk.Entry(input_frame, width=40)
                    title_input.insert(0, old_title)
                    title_input.grid(row=2, column=1, sticky="w")

                    # Error label
                    error_label = ttk.Label(window, text="", foreground="red")
                    error_label.pack(pady=(0, 5))

                    # Button to update RSS
                    update_button = ttk.Button(window, text="Update", command=lambda: update_rss(saved_links_from_file, title_input.get(), link_input.get(), window))
                    update_button.pack(pady=0)

                    # Run the main event loop
                    window.mainloop()
                    
                    return  # Exit the function after creating and running the window

            # If the loop completes without finding a matching title, show an error message
            popup_message("Error", "RSS title not found!")
        else:
            popup_message("Error", "No RSS title selected!")

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

    rss_link = tk.Entry(
        sources_frame,
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    rss_link.place(
        x=492.0 - 186.0,
        y=157.0 - 14.0,
        width=439.0,
        height=33.0
    )

    rss_title = tk.Entry(
        sources_frame,
        bd=0,
        bg="#BEBEBE",
        fg="#000716",
        highlightthickness=0
    )
    rss_title.place(
        x=492.0 - 186.0,
        y=265.0 - 14.0,
        width=439.0,
        height=33.0
    )

    sources_frame.create_text(
        623.0 - 186.0,
        46.0 - 14.0,
        anchor="nw",
        text="Add new source",
        fill="#000000",
        font=("Inter", 24)
    )

    saved_links_from_file = Combobox(
        sources_frame,
        state="readonly"
    )
    saved_links_from_file.set("-- There's no RSS saved --")
    saved_links_from_file.place(
        x=492.0 - 186.0,
        y=430.0 - 14.0,
        width=446.0,
        height=39.0
    )
    load_saved_sources(saved_links_from_file)

    delete_btn = tk.Button(
        sources_frame,
        text="Delete",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        command=lambda: delete_confirm_window(saved_links_from_file, saved_links_from_file.get()),
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
         command=lambda: update_rss_window(saved_links_from_file),
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

    

    add_source = tk.Button(
        sources_frame,
        text="Add Source",
        bg="#222222",
        fg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        command=lambda: save_rss(saved_links_from_file, rss_title, rss_link),
    )
    add_source.place(
        x=622,
        y=305,
        width=130.0,
        height=36.0
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
        queue_list.crpost = tk.Canvas(queue_list, bg="#d9d9d9", width=996, height=130)
        queue_list.create_window(14, y, anchor="nw", window=post)

        # Load the image
        image_path = "C:/Users/Maissen Belgacem/Desktop/Twitter Bot/Twitter bot with new design/picture.jpg"
        image = Image.open(image_path)

        # Resize the image as needed
        image = image.resize((168, 115))  # Adjust the dimensions as per your requirement

        # Convert the image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)

        post.create_rectangle(  # entry img
            11.5,
            10,
            180,
            125,
            fill="royalblue",
            outline="#bfbfbf",
            width=1
        )

        # Create the image inside the royal blue rectangle
        post_img = post.create_image(
            6 + (180 - 168) / 2,  # Adjust x-coordinate to center the image horizontally
            5 + (125 - 115) / 2,     # Adjust y-coordinate to center the image vertically
            anchor=tk.NW,             # Set anchor to top-left corner
            image=tk_image            # Use the loaded image
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
    sources_btn.invoke()

    window.mainloop()

load_main_window()
