from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    __REPORT_CATALOG = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    __IMPORTER_TYPE = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }

    @classmethod
    def import_data(cls, file_path, report):
        file_extension = file_path.split(".")[1]
        file_selected = cls.__IMPORTER_TYPE.get(file_extension)
        inventories = file_selected.import_data(file_path)
        report_selected = cls.__REPORT_CATALOG.get(report)
        return report_selected.generate(inventories)
