import classes.Manga_App
import customtkinter as ctk
from classes.Manga_List_Frame import Manga_List_Frame
import os, re

def main(): 
    """Initializes the manga application and starts the main event loop.

    Creates the main application window, cleans up orphaned image files, and then runs the application's main loop.
    """
    app = classes.Manga_App.MangaApp()
    clear_images()
    app.mainloop()


def clear_images():
    """Removes images from the 'images' directory that are not associated with manga in the Manga_List_Frame.

    Iterates through files in 'images', checks if cleaned filenames match manga titles or 'placeholder', and removes unmatched files.
    """   
    manga_titles = list(map(clean_title, [manga.title for manga in Manga_List_Frame._manga_list]))
    for file in os.listdir("images"):
        filename_without_ext = get_filename_without_extension(file)
        if filename_without_ext not in manga_titles and filename_without_ext != "placeholder":
            os.remove(f"images/{file}")

def get_filename_without_extension(file):
    """Extracts the filename without its extension.

    Uses regular expression matching to isolate the filename and returns it. If no extension is found, returns the original input.
    """
    match = re.match(r"(.+)\.[^.]+$", file)
    return match[1] if match else file


def clean_title(title):
    """Cleans a title string by removing spaces and converting to lowercase.

    This prepares titles for consistent comparison, regardless of original formatting.
    """
    return title.replace(" ", "").lower()

if __name__ == "__main__":
    main()