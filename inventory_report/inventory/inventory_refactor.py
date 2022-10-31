from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    __REPORT_CATALOG = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path, report_type):
        inventories_imported = self.importer.import_data(file_path)
        self.data.extend(inventories_imported)
        report_selected = self.__REPORT_CATALOG.get(report_type)
        return report_selected.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
