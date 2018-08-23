import unittest

import pandas

from bigsrc.bigp import dataprep


class TestDataprep(unittest.TestCase):

    def test_one(self):
        df = pandas.read_csv('')
        data = dataprep.give_numbers_to_categories()