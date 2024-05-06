import csv
from typing import Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self):
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self):
        """indexed_dataset"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """return a dictionary with the following key-value pairs"""
        assert index is None or (isinstance(index, int) and index >= 0), \
            "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"
        assert index is None or index < len(self.indexed_dataset()), \
            "Index out of range"

        if index is None:
            index = 0

        next_index = min(index + page_size, len(self.indexed_dataset()))

        data = []
        for i in range(index, next_index):
            if i in self.indexed_dataset():
                data.append(self.indexed_dataset()[i])

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
