import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import dictionary_functions 

class TestDictionaryFunctions(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    @patch('dictionary_functions.load_table')
    @patch('dictionary_functions.pd.DataFrame')
    @patch('builtins.print')
    @patch('dictionary_functions.tabulate')
    def test_view_table(self, mock_tabulate: MagicMock, mock_print :MagicMock, mock_df :MagicMock, mock_load:MagicMock):
        mock_load.return_value = [{'TestKey1':'TestValue1', 'TestKey2':'TestValue2'}]
        dictionary_functions.view_table('tests')
        mock_load.assert_called_once_with('tests')
        mock_df.assert_called_once_with(data = mock_load())
        mock_tabulate.assert_called_once()
        mock_print.assert_called_once()
    
    @patch('dictionary_functions.load_table')
    @patch('dictionary_functions.view_table')
    @patch('builtins.input')
    def test_dictionary_select(self, mock_input:MagicMock,mock_view:MagicMock, mock_load:MagicMock):
        mock_load.return_value = [{'test_id': 1,'TestKey1':'TestValue1', 'TestKey2':'TestValue2'}]
        mock_input.return_value = '1'
        actual = dictionary_functions.dictionary_select('tests')
        mock_load.assert_called_once_with('tests')
        mock_view.assert_called_once_with('tests')
        expected = {'test_id': 1,'TestKey1':'TestValue1', 'TestKey2':'TestValue2'}
        self.assertEqual(actual, expected)
    
    @patch('dictionary_functions.load_table')
    @patch('dictionary_functions.view_table')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_add_new(self, mock_print: MagicMock, mock_input: MagicMock, mock_view: MagicMock, mock_load: MagicMock):
        mock_load.return_value = [{'product_id':'','product':'','price':''}]
        mock_input.side_effect = ['test_product','test_price']
        actual =  dictionary_functions.add_new('products')
        mock_print.assert_called_once_with('New entry successfully added')
        mock_load.assert_called_once_with('products')
        expected = {'product':'test_product','price':'test_price'}
        self.assertEqual(actual, expected)
    


    