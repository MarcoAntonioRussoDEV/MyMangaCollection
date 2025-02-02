import customtkinter as ctk
import csv
import os
from .Manga import Manga
from PIL import Image

class Manga_List_Frame(ctk.CTkScrollableFrame):
    """Displays a scrollable list of manga loaded from a CSV file.

    Each manga is displayed as a card with its title, author, genre, volumes, and optionally a cover image and description.
    """
    
    _manga_list: list[Manga] = []
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.load_manga_list()

    def load_manga_list(self):
        """
        Loads the manga list from a CSV file named 'mangas.csv' and populates the manga list.

        This method checks if the 'mangas.csv' file exists. If it does, it reads the file using a CSV
        dictionary reader and creates Manga objects from each row in the CSV file. Each Manga object
        is then appended to the manga list and displayed using the display_manga method.

        The CSV file is expected to have the following columns:
        - title: The title of the manga.
        - author: The author of the manga.
        - genre: The genre of the manga.
        - volumes: The number of volumes of the manga.
        - description: A brief description of the manga.
        - image (optional): A URL or path to an image of the manga.

        Raises:
            FileNotFoundError: If the 'mangas.csv' file does not exist.
            KeyError: If any of the required columns are missing in the CSV file.
        """
        if __ := os.path.exists('mangas.csv'):
            with open('mangas.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    manga = Manga(row['title'], row['author'], row['genre'], row['volumes'], row['description'], row.get('image'))
                    self._manga_list.append(manga)
                    self.display_manga(manga)
                    
    def refresh_manga_list(self):
        """
        Refreshes the manga list displayed in the frame.

        This method clears the current list of manga displayed in the frame by 
        destroying all child widgets and clearing the internal manga list. 
        It then reloads the manga list by calling the load_manga_list method.
        See:
            Add_Manga_Window.add_manga
        """
        # Clear the current list
        for widget in self.winfo_children():
            widget.destroy()
        self._manga_list.clear()
        # Reload the manga list
        self.load_manga_list()

    def display_manga(self, manga):
        """
        Displays the details of a manga in a formatted card frame.

        Args:
            manga (Manga): An object containing manga details such as image, title, author, genre, volumes, and description.

        The function creates a card frame with the following elements:
            - Image: Displays the manga's image if available, otherwise a placeholder image.
            - Title: Displays the title of the manga.
            - Author: Displays the author of the manga.
            - Genre: Displays the genre of the manga.
            - Volumes: Displays the number of volumes of the manga.
            - Description: Displays the description of the manga if available.

        The card frame is configured with padding and sticky options for proper layout.
        """
        card_frame = ctk.CTkFrame(self, border_width=1)
        card_frame.grid(padx=20, pady=5, sticky="ew")
        card_frame.grid_columnconfigure(2, weight=1)  

        # Image
        if manga.image:
            image_path = os.path.join(os.path.dirname(__file__), '..', manga.image)
            image = ctk.CTkImage(light_image=Image.open(image_path), size=(150, 200))
        else:
            image = ctk.CTkImage(light_image=Image.open("images/placeHolder.jpg"), size=(150, 200))
        image_label = ctk.CTkLabel(card_frame, text="", image=image)
        image_label.grid(row=0, column=0, rowspan=5, padx=10, pady=5, sticky="e")

        # Labels
        title_label = ctk.CTkLabel(card_frame, text=f"Title: {manga.title}", font=("Comic Sans MS", 14, "bold"))
        title_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        author_label = ctk.CTkLabel(card_frame, text=f"Author: {manga.author}", font=("Comic Sans MS", 12))
        author_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        genre_label = ctk.CTkLabel(card_frame, text=f"Genre: {manga.genre}", font=("Comic Sans MS", 12))
        genre_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        volumes_label = ctk.CTkLabel(card_frame, text=f"Volumes: {manga.volumes}", font=("Comic Sans MS", 12))
        volumes_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        if manga.description:
            description_label = ctk.CTkLabel(card_frame, text=f"{manga.description}", font=("Comic Sans MS", 16), justify="left", wraplength=self.winfo_width() + 300)
            description_label.grid(row=0, column=2, padx=20, pady=5, sticky="e", rowspan=5)
            
   