from unittest import TestCase
from unittest.mock import patch
from buh import get_doc_owner, get_doc_shelf, get_list, add_document, del_doc, move_document, add_shelf


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


class TestBuh(TestCase):
    def test_get_doc_owner(self):
        self.assertEqual(get_doc_owner(documents, '10006'), 'Аристарх Павлов')
        self.assertEqual(get_doc_owner(documents, '10001'), None)

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf(directories, '10006'), '2')
        self.assertEqual(get_doc_shelf(directories, '10001'), None)

    def test_get_list(self):
        self.assertEqual(get_list(documents), None)

    @patch('builtins.input', side_effect=['123', 'passport', 'Ivan Off', '3', '123', 'passport', 'Ivan On', '4'])
    def test_add_document(self, mock_input):
        self.assertEqual(add_document(documents, directories), True)
        self.assertEqual(add_document(documents, directories), False)

    @patch('builtins.input', side_effect=['11-2'])
    def test_del_doc(self, mock_input):
        self.assertEqual(del_doc(documents), True)

    @patch('builtins.input', side_effect=['10006', '3', '123', '5'])
    def test_move_document(self, mock_input):
        self.assertEqual(move_document(documents, directories), True)
        self.assertEqual(move_document(documents, directories), False)

    @patch('builtins.input', side_effect=['4', '3'])
    def test_add_shelf(self, mock_input):
        self.assertEqual(add_shelf(directories), True)
        self.assertEqual(add_shelf(directories), False)

