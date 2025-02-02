import re
import customtkinter as ctk
from tkinter import filedialog, messagebox
import csv
import os
import shutil

class Add_Manga_Window(ctk.CTkToplevel):
    """
    A window for adding a new manga entry.
    Attributes:
        __entry_config (dict): Configuration for entry widgets.
        __genre_options (list): List of genre options.
        __padx (int): Padding in x direction.
        __pady (int): Padding in y direction.
        __font (tuple): Font configuration.
        manga_list_frame (object): Reference to the parent frame containing the manga list.
        title_entry (ctk.CTkEntry): Entry widget for the manga title.
        author_entry (ctk.CTkEntry): Entry widget for the manga author.
        genre_options (ctk.CTkOptionMenu): Option menu for selecting manga genre.
        volumes_entry (ctk.CTkEntry): Entry widget for the number of volumes.
        description_entry (ctk.CTkTextbox): Textbox widget for the manga description.
        image_entry (ctk.CTkEntry): Entry widget for the image path.
    Methods:
        __init__(parent, manga_list_frame):
            Initializes the Add_Manga_Window instance.
        browse_image():
            Opens a file dialog to browse and select an image file.
        add_manga():
            Validates the input fields and adds the manga entry to the CSV file.
        is_valid_filename(filename):
            Checks if the given filename contains invalid characters.
    """
    
    __entry_config = {
        "width": 150,
        "height": 24
    }
    
    __genre_options = [
        "shonen",
        "shojo",
        "seinen",
        "josei",
        "kodomo",
        "mecha",
        "isekai",
        "fantasy",
        "sci-fi",
        "horror",
        "mystery",
        "romance",
        "slice of life",
        "sports",
        "comedy",
        "drama",
        "historical",
        "supernatural",
        "psychological",
        "adventure"
    ]
    
    __padx = 20
    __pady = 5
    __font = ("Comic Sans MS", 12)
    
    def __init__(self, parent, manga_list_frame):
        super().__init__(parent)
        self.manga_list_frame = manga_list_frame
        # Initialize window
        self.title("Add Manga")
        self.geometry("400x420")
        self.minsize(400, 400)
        self.attributes("-topmost", True)
        self.grab_set()
        self.focus_force()

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Title
        title_label = ctk.CTkLabel(self, text="Title:", font=self.__font)
        title_label.grid(row=0, column=0, pady=self.__pady, padx=self.__padx, sticky="w")
        
        self.title_entry = ctk.CTkEntry(self, **self.__entry_config)
        self.title_entry.grid(row=1, column=0, pady=self.__pady, padx=self.__padx, sticky="ew")
        
        # Get the properties for uniformity
        fg_color = self.title_entry.cget("fg_color")
        border_width = self.title_entry.cget("border_width")
        border_color = self.title_entry.cget("border_color")

        # Author
        author_label = ctk.CTkLabel(self, text="Author:", font=self.__font)
        author_label.grid(row=0, column=1, pady=self.__pady, padx=self.__padx, sticky="w")
        
        self.author_entry = ctk.CTkEntry(self, **self.__entry_config)
        self.author_entry.grid(row=1, column=1, pady=self.__pady, padx=self.__padx, sticky="ew")

        # Genre
        genre_label = ctk.CTkLabel(self, text="Genre:", font=self.__font)
        genre_label.grid(row=2, column=0, pady=self.__pady, padx=self.__padx, sticky="w")
        
        self.genre_options = ctk.CTkOptionMenu(self, values=self.__genre_options, font=self.__font, **self.__entry_config, fg_color=fg_color, button_color=fg_color, dropdown_font=self.__font)
        self.genre_options.grid(row=3, column=0, pady=self.__pady, padx=self.__padx, sticky="w")

        # Volumes
        volumes_label = ctk.CTkLabel(self, text="Volumes:", font=self.__font)
        volumes_label.grid(row=2, column=1, pady=self.__pady, padx=self.__padx, sticky="w")
        
        self.volumes_entry = ctk.CTkEntry(self, **self.__entry_config)
        self.volumes_entry.grid(row=3, column=1, pady=self.__pady, padx=self.__padx, sticky="ew")

        # Description
        description_label = ctk.CTkLabel(self, text="Description:", font=self.__font)
        description_label.grid(row=4, column=0, pady=self.__pady, padx=self.__padx, sticky="w")
        
        self.description_entry = ctk.CTkTextbox(self, width=self.__entry_config["width"], height=64, border_width=border_width, border_color=border_color, fg_color=fg_color)
        self.description_entry.grid(row=5, column=0, columnspan=2 , pady=self.__pady, padx=self.__padx, sticky="ew")

        # Image
        image_label = ctk.CTkLabel(self, text="Image path:", font=self.__font)
        image_label.grid(row=6, column=0, pady=self.__pady, padx=self.__padx, sticky="w")
        
        self.image_entry = ctk.CTkEntry(self, **self.__entry_config)
        self.image_entry.grid(row=7, column=0, pady=self.__pady, padx=self.__padx, sticky="w")
        
        image_button = ctk.CTkButton(self, text="Browse", command=self.browse_image)
        image_button.grid(row=7, column=1, pady=self.__pady, padx=self.__padx, sticky="w")
        
        # Add button
        add_button = ctk.CTkButton(self, text="Save", command=self.add_manga, font=self.__font)
        add_button.grid(row=8, column=0, columnspan=2, pady=40, padx=self.__padx, sticky="ew")

    def browse_image(self):
        """
        Opens a file dialog to browse and select an image file. If a file is selected,
        the file path is inserted into the image entry widget.

        The file dialog filters for image files with extensions .jpg, .jpeg, and .png.

        Returns:
            None
        """
        if file_path := filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        ):
            self.image_entry.delete(0, ctk.END)
            self.image_entry.insert(0, file_path)
            
    def add_manga(self):
        """
        Adds a new manga entry to the system.
        This method retrieves the manga details from the user input fields, validates the input,
        saves the manga information to a CSV file, and optionally saves an image associated with the manga.
        It also displays appropriate messages based on the success or failure of the operation.
        Raises:
            messagebox.showerror: If the volumes field is not a number.
            messagebox.showerror: If the title contains invalid characters.
            messagebox.showerror: If any required field (title, author, genre, volumes, description) is empty.
        Displays:
            messagebox.showinfo: If the manga is added successfully.
        Side Effects:
            - Saves the manga data to 'mangas.csv'.
            - Copies the image to the 'images' directory.
            - Refreshes the manga list in the UI.
            - Closes the current window.
        """
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_options.get()
        volumes = self.volumes_entry.get()
        description = self.description_entry.get("1.0", "end-1c")
        image_path = self.image_entry.get()

        if not volumes.isdigit():
            messagebox.showerror("Error", "Volumes must be a number.")
        elif not self.is_valid_filename(title):
            messagebox.showerror("Error", "Title contains invalid characters.")
        else:
            if not title or not author or not genre or not volumes or not description:
                messagebox.showerror("Error", "All fields, except image, are required.")
            else:
                # Save the image
                if image_path:
                    title_clean = title.replace(" ", "").lower()
                    new_image_path = os.path.join("images", f"{title_clean}.jpg")
                    os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
                    shutil.copy(image_path, new_image_path)
                else:
                    new_image_path = "images/placeHolder.jpg"

                # Save the manga data
                file_exists = os.path.isfile('mangas.csv')
                with open('mangas.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['title', 'author', 'genre', 'volumes', 'description', 'image']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow({
                        'title': title,
                        'author': author,
                        'genre': genre,
                        'volumes': volumes,
                        'description': description,
                        'image': new_image_path
                    })
                
                messagebox.showinfo("Success", "Manga added successfully.")
                self.manga_list_frame.refresh_manga_list()  # Refresh the manga list
                self.destroy()
                
    def is_valid_filename(self, filename):
        """
        Check if the given filename is valid.

        A valid filename does not contain any of the following characters:
        < > : " / \ | ? *

        Args:
            filename (str): The filename to check.

        Returns:
            bool: True if the filename is valid, False otherwise.
        """
        # Define a regex pattern for invalid file characters
        pattern = r'[<>:"/\\|?*]'
        return not re.search(pattern, filename)