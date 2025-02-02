import os
import pytest
from project import clear_images, get_filename_without_extension, clean_title
from classes.Manga_List_Frame import Manga_List_Frame
from classes.Manga import Manga

def test_clear_images(tmpdir):
    # Create a temporary images directory
    images_dir = tmpdir.mkdir("images")
    # Create some test image files
    images_dir.join("testmanga1.jpg").write("")
    images_dir.join("testmanga2.jpg").write("")
    images_dir.join("placeholder.jpg").write("")
    images_dir.join("unrelated.jpg").write("")

    # Create a mock manga list
    Manga_List_Frame._manga_list = [
        Manga("Test Manga 1", "Author 1", "Genre 1", "1", "Description 1", str(images_dir.join("testmanga1.jpg"))),
        Manga("Test Manga 2", "Author 2", "Genre 2", "2", "Description 2", str(images_dir.join("testmanga2.jpg")))
    ]

    # Temporarily change the working directory to the temp directory
    original_cwd = os.getcwd()
    os.chdir(tmpdir)

    try:
        # Call the clear_images function
        clear_images()

        # Check that only the expected files remain
        remaining_files = os.listdir(images_dir)
        assert "testmanga1.jpg" in remaining_files
        assert "testmanga2.jpg" in remaining_files
        assert "placeholder.jpg" in remaining_files
        assert "unrelated.jpg" not in remaining_files
    finally:
        # Restore the original working directory
        os.chdir(original_cwd)
        
def test_clean_title():
    assert clean_title("Test Manga") == "testmanga"
    assert clean_title("Another Test") == "anothertest"
    
    
def test_get_filename_without_extension():
    assert get_filename_without_extension("testmanga.jpg") == "testmanga"
    assert get_filename_without_extension("another_test.png") == "another_test"
    assert get_filename_without_extension("no_extension") == "no_extension"