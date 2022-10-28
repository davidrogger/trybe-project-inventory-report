import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, file_path: str):
        if file_path.endswith("json"):
            with open(file_path, "r") as file:
                inventories = json.load(file)

            return inventories

        raise ValueError("Arquivo inválido")
