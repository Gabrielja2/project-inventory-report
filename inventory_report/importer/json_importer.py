from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, path: str):

        with open(path) as file:

            try:
                inventory_file = json.loads(file.read())

            except ValueError:
                raise ValueError("Arquivo inválido")

        return inventory_file
