import unittest
from unittest import TestCase
from csvVerbinndung import *


class TestCsvVerbindung(TestCase):

    def setUp(self):
        self.csvfile = csvVerbindung("/home/sarahkreutzer/Desktop/csv_test.csv")
        pass

    def test_csvFile(self):
        self.csvfile.einlesen()
        self.csvfile.schreiben()

    def test_dialects(self):
        self.csvfile.einlesen()
        self.csvfile.schreiben()

    def test_noneDialect(self):
        self.csvfile.einlesen()
        self.csvfile.schreiben()

if __name__ == "__main__":
    unittest.main()
