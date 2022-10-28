from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(self):
        raise NotImplementedError
