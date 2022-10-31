import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

IMPORTER = {
    "csv": CsvImporter,
    "json": JsonImporter,
    "xml": XmlImporter,
}


def main():
    try:
        _, path_file, report_type = sys.argv
        file_type = path_file.split(".")[1]
        inventories = InventoryRefactor(IMPORTER[file_type])
        report = inventories.import_data(path_file, report_type)
        print(report, end="")
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
