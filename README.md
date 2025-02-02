[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# My Manga Collection

## Overview

This project is a desktop application for managing a manga collection. It allows users to add, view, and manage manga entries, including details such as title, author, genre, number of volumes, description, and cover image.

#### Video Demo: <URL HERE>

## Project Structure

-   `classes/`

    -   `Manga.py`: Defines the `Manga` class, representing a manga with its details.
    -   `Manga_List_Frame.py`: Contains the `Manga_List_Frame` class, which displays a scrollable list of manga loaded from a CSV file.
    -   `Manga_App.py`: Contains the `MangaApp` class, which is the main application window.
    -   `Add_Manga_Window.py`: Contains the `Add_Manga_Window` class, which provides a window for adding new manga entries.

-   `watchdog_script.py`: Monitors the project files for changes and restarts the application when modifications are detected.

-   `test_project.py`: Contains tests for various functions in the project.

-   `mangas.csv`: A CSV file storing the manga entries.

-   `requirements.txt`: Lists the dependencies required for the project.

-   `project.py`: The main script that initializes and runs the application.

## Dependencies

The project requires the following Python packages:

-   `tkinter`
-   `customtkinter`
-   `watchdog`
-   `PIL`
-   `pytest`

These can be installed using the following command:

```sh
pip install -r requirements.txt
```

## Usage

1. **Running the Application**:

    - Execute `project.py` to start the application.

    ```sh
    python project.py
    ```

2. **Adding a Manga**:

    - Click the "Add Manga" button in the application window.
    - Fill in the details in the pop-up window and click "Save".

3. **Viewing Manga**:

    - The manga list is displayed in the main application window, showing details such as title, author, genre, volumes, and description.

4. **Monitoring Changes**:
    - Run `watchdog_script.py` to monitor changes in the project files and automatically restart the application upon modifications.
    ```sh
    python watchdog_script.py
    ```

## Testing

Run the tests using `pytest`:

```sh
pytest test_project.py
```

## License

This project is licensed under the MIT License.

## Author

![Marco Antonio Russo Logo](public/SVG_GRADIENT_WHITE.svg)
