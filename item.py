from enum import Enum

ItemTypes = Enum('Bb', 'C', 'High', 'Cornet', 'Flugelhorn', 'Picc', 'Multiple', 'Others')

class Item:
    def __init__(self):
        self.title = ''
        self.url = ''
        self.brief = ''
        self.description = ''
        self.images = []
        self.price = ''
        self.visited = False
        self.itemType = ItemTypes.Others

