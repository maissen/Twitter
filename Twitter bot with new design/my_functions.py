import pickle
import tkinter as tk
from tkinter import ttk  # Add this line to import the ttk module

def load_saved_sources(saved_links_input):
    try:
        with open("My_rss_sources.dat", "rb") as file:
            rss_sources = pickle.load(file)
            titles = [source["title"] for source in rss_sources]
            if titles:
                saved_links_input["values"] = titles
                saved_links_input.set(titles[0])
    except FileNotFoundError:
        with open("My_rss_sources.dat", "wb") as file:
            rss_sources = []
            pickle.dump(rss_sources, file)
