import os
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""


class File:
    """
    A SIMPLE FILE MANAGER\n
    `get_filename` -> Return the file name\n
    `get_filepath` -> Return the file path\n
    `rename` -> Rename the file\n
    `exists` -> Check if file exists\n
    `is_empty` -> Check if file is empty\n
    `create` -> Create the file\n
    `delete` -> Delete the file\n
    `read` -> Read file content\n
    `readlines` -> Read file content\n
    `write` -> Write text in file\n
    `append` -> Write text in file in append mode\n
    `clear` -> Remove all text in the file
    """

    def __init__(self, filename: str = ""):
        self.filename = filename

    def get_filename(self) -> str:
        """ Get file name """
        return self.filename.split("/")[-1]

    def get_filepath(self) -> str:
        """ Get file path """
        return self.filename

    def rename(self, new_filename: str) -> None:
        """
        Rename the current file to a new filename\n
        Args:
            `new_filename (str)`: The new name for the file
        Raises:
            `FileNotFoundError`: If the current file does not exist
            `FileExistsError`: If a file with the new filename already exists
        """
        try:
            os.rename(self.filename, new_filename)
            self.filename = new_filename
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")
        except FileExistsError:
            raise FileExistsError(f"File {new_filename} already exists")

    def exists(self) -> bool:
        """
        Check if file exists\n
        Returns:
            `bool`: True if file exists, False otherwise
        """
        return os.path.exists(self.filename)

    def is_empty(self) -> bool:
        """
        Check if file is empty\n
        Returns:
            `bool`: True if file is empty, False otherwise
        """
        try:
            return os.path.getsize(self.filename) == 0
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def create(self) -> None:
        """
        Create the file\n
        Raises:
            `FileExistsError`: If the file already exists
        """
        try:
            open(self.filename, "x").close()
        except FileExistsError:
            raise FileExistsError(f"File {self.filename} already exists")

    def delete(self) -> None:
        """
        Delete the file\n
        Raises:
            `FileNotFoundError`: If the file does not exist
        """
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def read(self) -> str:
        """
        Read file content\n
        Returns:
            `str`: The file content
        """
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def readlines(self) -> list:
        """
        Read file content\n
        Returns:
            `list`: A list containing all lines in the file
        """
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def write(self, text: str) -> int:
        """
        Write text in file\n
        Args:
            `text (str)`: The text to write in the file
        Returns:
            `int`: 0 if file exists, 1 otherwise
        """
        return self.__write(text, "w")

    def append(self, text: str) -> int:
        """
        Write text in file in append mode\n
        Args:
            `text (str)`: The text to append in the file
        Returns:
            `int`: 0 if file exists, 1 otherwise
        """
        return self.__write(text, "a")

    def clear(self) -> None:
        """
        Remove all text in the file\n
        Raises:
            `FileNotFoundError`: If the file does not exist
        """
        if (not self.exists()):
            raise FileNotFoundError(f"File {self.filename} not found")
        with open(self.filename, "w") as file:
            file.write("")

    def __write(self, text: str, mode: str):
        return_value = 0
        if (not self.exists()):
            return_value = 1
        with open(self.filename, mode) as file:
            file.write(text)
        return return_value
