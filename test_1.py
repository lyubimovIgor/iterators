import pprint

class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.current_list_idx = 0
        self.current_item_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_idx >= len(self.list_of_lists):
            raise StopIteration

        current_list = self.list_of_lists[self.current_list_idx]
        if self.current_item_idx >= len(current_list):
            self.current_list_idx += 1
            self.current_item_idx = 0
            return next(self)

        item = current_list[self.current_item_idx]
        self.current_item_idx += 1

        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    pprint.pprint(list(FlatIterator(list_of_lists_1)))


if __name__ == '__main__':
    test_1()
