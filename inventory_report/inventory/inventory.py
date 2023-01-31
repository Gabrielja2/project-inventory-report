from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(self, path, tipo):
        if "csv" in path:
            return Inventory.open_csv(path, tipo)
        elif "json" in path:
            return Inventory.open_json(path, tipo)

        return Inventory.open_xml(path, tipo)

    @classmethod
    def open_csv(self, path, tipo):
        with open(path, encoding="utf-8") as file:
            inventory_file = csv.DictReader(file, delimiter=",", quotechar='"')
            if tipo == "simples":
                return SimpleReport.generate(list(inventory_file))

            return CompleteReport.generate(list(inventory_file))

    @classmethod
    def open_json(self, path, tipo):
        with open(path) as file:
            inventory_file = json.load(file)
            if tipo == "simples":
                return SimpleReport.generate(list(inventory_file))

            return CompleteReport.generate(list(inventory_file))
