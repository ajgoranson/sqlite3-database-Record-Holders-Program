import unittest
import juggling_record
from juggling_record import RecordError
from unittest import TestCase
import sqlite3

class TestJugglingDB(TestCase):

    test_db_url = 'test_juggling.db'

    def setUp(self):


        juggling_record.db = self.test_db_url

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS juggleing (Name text, Country text, NumberOfCatches int)')


        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DELETE FROM juggleing')
        conn.close()

    def test_add_new_record(self):
        juggling_record.add_new_record('Aaron Goranson', 'United States', 106)

    def test_add_new_record_raises_error(self):
        with self.assertRaises(RecordError):
            juggling_record.add_new_record('', 'United States', 10)
            juggling_record.add_new_record('Jon Snow', '', 10)
            juggling_record.add_new_record('Jon Snow', 'United States', )
            juggling_record.add_new_record('', '', )

    def test_update_record(self):
        juggling_record.update_record('Aaron Goranson', 110)
        expected = ('Aaron Goranson', 'United States', 110)
        self.compare_db_to_expected(expected)

    

    def test_delete_record(self):
        juggling_record.delete_record('Aaron Goranson')

    def test_add_new_record_different_case(self):
        juggling_record.add_new_record('AaRon goRanSon', 'UnITed StAtes', 10)
        expected = ('Aaron Goranson', 'United States', 10)
        self.compare_db_to_expected(expected)
    
    

        


    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM juggleing').fetchall()

        for row in all_data:
            self.assertIn(row[0], expected)
        conn.close()


if __name__ == '__main__':
    unittest.main()