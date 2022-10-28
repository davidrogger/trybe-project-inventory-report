import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, file_path: str):
        if file_path.endswith("csv"):
            with open(file_path, "r") as file:
                content = csv.DictReader(file)
                inventories = [*content]
            return inventories

        raise ValueError("Arquivo inválido")
