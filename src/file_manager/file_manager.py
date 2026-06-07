import os


class File:
    """
    A file management class to easily handle file system operations.
    """

    def __init__(self, filename: str = "") -> None:
        """
        Initializes the File instance with the absolute path of the given filename.

        Args:
            filename (str): The name or path of the file. Defaults to an empty string.
        """
        self.filename = os.path.abspath(filename)

    def get_filename(self) -> str:
        """
        Gets the base name of the file (e.g., 'document.txt').

        Returns:
            str: The base name of the file.
        """
        return os.path.basename(self.filename)

    def get_filepath(self) -> str:
        """
        Gets the directory path where the file is located.

        Returns:
            str: The directory path of the file.
        """
        return os.path.dirname(self.filename)

    def get_fullpath(self) -> str:
        """
        Gets the complete absolute path of the file.

        Returns:
            str: The full path of the file.
        """
        return os.path.join(self.get_filepath(), self.get_filename())

    def rename(self, new_filename: str) -> None:
        """
        Renames the file to a new name or path.

        If the file does not exist on the file system yet, it updates the internal
        filename reference.

        Args:
            new_filename (str): The new name or path for the file.

        Raises:
            FileExistsError: If a file with the new name already exists.
        """
        new_abspath = os.path.abspath(new_filename)
        if (os.path.exists(new_abspath)):
            raise FileExistsError(f"File {new_filename} already exists")

        if not self.exists():
            self.filename = new_abspath
            return

        os.rename(self.filename, new_abspath)
        self.filename = new_abspath

    def exists(self) -> bool:
        """
        Checks if the file currently exists on the file system.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.exists(self.filename)

    def is_empty(self) -> bool:
        """
        Checks if the file is empty (size is 0 bytes).

        Returns:
            bool: True if the file is empty, False otherwise.
        """
        return os.path.getsize(self.filename) == 0

    def create(self) -> None:
        """
        Creates a new empty file on the file system.
        """
        open(self.filename, "x").close()

    def delete(self) -> None:
        """
        Deletes the file from the file system.
        """
        os.remove(self.filename)

    def read(self) -> str:
        """
        Reads and returns the entire content of the file.

        Returns:
            str: The content of the file.
        """
        with open(self.filename, "r") as file:
            return file.read()

    def readlines(self) -> list:
        """
        Reads the file and returns a list of its lines.

        Returns:
            list: A list of strings, each representing a line in the file.
        """
        with open(self.filename, "r") as file:
            return file.readlines()

    def write(self, text: str) -> int:
        """
        Writes text to the file. Overwrites any existing content.

        Args:
            text (str): The string to write to the file.

        Returns:
            int: The number of characters written.
        """
        with open(self.filename, "w") as file:
            return file.write(text)

    def append(self, text: str) -> int:
        """
        Appends text to the end of the file.

        Args:
            text (str): The string to append to the file.

        Returns:
            int: The number of characters appended.
        """
        with open(self.filename, "a") as file:
            return file.write(text)

    def clear(self) -> None:
        """
        Clears the content of the file, making it empty.
        """
        with open(self.filename, "w") as file:
            file.write("")
