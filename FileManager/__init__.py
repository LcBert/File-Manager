import os
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""


class File:
    def __init__(self, filename: str = ""):
        self.filename = filename

    def rename(self, new_filename: str) -> None:
        """ Change file name """
        try:
            os.rename(self.filename, new_filename)
            self.filename = new_filename
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")
        except FileExistsError:
            raise FileExistsError(f"File {new_filename} already exists")

    def exists(self) -> bool:
        """ Check if file exists """
        return os.path.exists(self.filename)

    def is_empty(self) -> bool:
        """ Check if file is empty """
        try:
            return os.path.getsize(self.filename) == 0
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def create(self) -> None:
        """ Create file """
        try:
            open(self.filename, "x").close()
        except FileExistsError:
            raise FileExistsError(f"File {self.filename} already exists")

    def delete(self) -> None:
        """ Delete file """
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def read(self) -> str:
        """ Read file """
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def readlines(self) -> list:
        """ Read file lines """
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.filename} not found")

    def write(self, text: str) -> int:
        """ write in file """
        return self.__write(text, "w")

    def append(self, text: str) -> int:
        """ Append text in file """
        return self.__write(text, "a")

    def clear(self) -> None:
        """ Remove all text in the file """
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
