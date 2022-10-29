from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(self, file_path: str):
        if file_path.endswith("xml"):
            xml = ET.parse(file_path)
            root = xml.getroot()

            inventories = list()

            for records in root:
                record = dict()
                for inventory in records:
                    record.update({inventory.tag: inventory.text})
                inventories.append(record)

            return inventories

        raise ValueError("Arquivo inválido")
