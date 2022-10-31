from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self._position = 0

    def __next__(self):
        try:
            inventory = self.data[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += 1
            return inventory
