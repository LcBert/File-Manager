import os
from pathlib import Path


class File:
    """
    A file management class to easily handle file system operations.
    """

    def __init__(self, filename: str | Path) -> None:
        """
        Initializes the File instance with the absolute path of the given filename.

        Args:
            filename (str): The name or path of the file. Defaults to an empty string.
        """
        self.path: Path = Path(filename).resolve()

    def __fspath__(self) -> str:
        return str(self.path)

    def __str__(self) -> str:
        return str(self.path)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self.path)!r})"

    def get_filename(self) -> str:
        """
        Gets the base name of the file (e.g., 'document.txt').

        Returns:
            str: The base name of the file.
        """
        return self.path.name

    def get_parent(self) -> Path:
        """
        Gets the directory path where the file is located.

        Returns:
            str: The directory path of the file.
        """
        return self.path.parent

    def get_path(self) -> Path:
        """
        Gets the complete absolute path of the file.

        Returns:
            str: The full path of the file.
        """
        return self.path

    def rename(self, new_path: str | Path) -> None:
        """
        Renames or moves the file to a new name or path.

        If the file does not exist on the file system yet, it updates the internal
        filename reference.

        Args:
            new_path (str | Path): The new name or path for the file.

        Raises:
            FileExistsError: If a file with the new name already exists.
        """
        is_dir_intent = str(new_path).endswith(("/", "\\")) or Path(new_path).is_dir()
        target = Path(new_path).resolve()

        if is_dir_intent:
            target.mkdir(parents=True, exist_ok=True)
            target = target / self.path.name
        else:
            target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists():
            raise FileExistsError(f"File {target} already exists")

        if self.exists():
            self.path = self.path.rename(target)
        else:
            self.path = target

    def exists(self) -> bool:
        """
        Checks if the file currently exists on the file system.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return self.path.exists()

    def is_empty(self) -> bool:
        """
        Checks if the file is empty (size is 0 bytes).

        Returns:
            bool: True if the file is empty, False otherwise.
        """
        return self.path.stat().st_size == 0

    def create(self) -> None:
        """
        Creates a new empty file on the file system.
        """
        self.path.touch(exist_ok=False)

    def delete(self) -> None:
        """
        Deletes the file from the file system.
        """
        self.path.unlink()

    def read(self, encoding="utf-8") -> str:
        """
        Reads and returns the entire content of the file.

        Returns:
            str: The content of the file.
        """
        with open(self.path, "r", encoding=encoding) as file:
            return file.read()

    def readlines(self, encoding="utf-8") -> list:
        """
        Reads the file and returns a list of its lines.

        Returns:
            list: A list of strings, each representing a line in the file.
        """
        with open(self.path, "r", encoding=encoding) as file:
            return file.readlines()

    def write(self, text: str, encoding="utf-8") -> int:
        """
        Writes text to the file. Overwrites any existing content.

        Args:
            text (str): The string to write to the file.

        Returns:
            int: The number of characters written.
        """
        with open(self.path, "w", encoding=encoding) as file:
            return file.write(text)

    def append(self, text: str, encoding="utf-8") -> int:
        """
        Appends text to the end of the file.

        Args:
            text (str): The string to append to the file.

        Returns:
            int: The number of characters appended.
        """
        with open(self.path, "a", encoding=encoding) as file:
            return file.write(text)

    def clear(self) -> None:
        """
        Clears the content of the file, making it empty.
        """
        self.write("")
