import customtkinter as ctk

from .Manga_List_Frame import Manga_List_Frame
from .Add_Manga_Window import Add_Manga_Window

class MangaApp(ctk.CTk):
    """
    A class to represent the Manga Application.
    Inherits from:
        ctk.CTk: A custom tkinter class.
    Attributes:
        app_font (ctk.CTkFont): The font used in the application.
        add_manga_button (ctk.CTkButton): Button to add a new manga.
        manga_list (Manga_List_Frame): Frame to display the list of mangas.
    Methods:
        __init__(): Initializes the MangaApp window and its components.
        open_add_window(): Opens a new window to add a manga.
    """
    def __init__(self):
        super().__init__()
        # App font
        self.app_font = ctk.CTkFont(family="Comic Sans MS", size=16)
        # Set the icon
        self.iconbitmap("public/icon.ico")
        # Initialize window
        self.title("My Manga Collection")
        self.geometry("800x600")
        self.minsize(800,600)
        self._set_appearance_mode("system")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Configura la riga 1 per espandersi

        # Add manga button
        self.add_manga_button = ctk.CTkButton(self, text="Add Manga", command=self.open_add_window, font=self.app_font)
        self.add_manga_button.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        
        # Manga list frame
        self.manga_list = Manga_List_Frame(self)
        self.manga_list.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    def open_add_window(self):
        """
        Opens a new window to add a manga to the manga list.

        This method creates an instance of the Add_Manga_Window class, passing
        the current instance and the manga list as arguments. The new window
        allows the user to input details for a new manga and add it to the list.

        Args:
            None

        Returns:
            None
        """
        Add_Manga_Window(self, self.manga_list)

