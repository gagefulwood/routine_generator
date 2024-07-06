import json
import os

class FileParsingService:

    @classmethod
    def get_file_extension(cls, filename):
        return os.path.splitext(filename)[1].lower()

    @classmethod
    def parse(cls, filename):
        if (cls.get_file_extension(filename) == "json"):
            pass
        elif (cls.get_file_extension(filename) == "sce"):
            pass