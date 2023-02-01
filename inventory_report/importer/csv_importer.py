from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path: str):

        if "csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            inventory_file = csv.DictReader(file)

            return list(inventory_file)
