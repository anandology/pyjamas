# Testing csv module

import sys
import UnitTest

import csv


class CsvModuleTest(UnitTest.UnitTest):

    def test_reader(self):
        lines = [
            '''1, 2,"3"\n''',
            ''' "s","a","as,2"\n''',
            ''' "s,"a" ,"as,2"\n''',
            '''""s, "a" ,"as,\n2"\n''',
            ''' ""s, "a" ,"as,2"\n''',
            '\n',
            '\n\n',
            '''1, 2,"3"''',
            '''""s, "a" ,"as,\n2"''',
            '',
        ]
        expected = [
            ['1', ' 2', '3'], 
            [' "s"', 'a', 'as,2'], 
            [' "s', 'a ', 'as,2'], 
            ['s', ' "a" ', 'as,\n2'], 
            [' ""s', ' "a" ', 'as,2'], 
            [], 
            [], 
            ['1', ' 2', '3'], 
            ['s', ' "a" ', 'as,\n2'], 
            [],
        ]
        reader = csv.reader(lines)
        rows = []
        idx = -1
        for row in reader:
            idx += 1
            self.assertEqual(row, expected[idx], 
                             "%d : %r != %r" % (idx, row, expected[idx]))
            rows.append(row)

        lines = [
            '''1,2,3\n''',
        ]
        expected = [
            ['1', '2', '3'],
        ]
        reader = csv.reader(lines)
        rows = []
        idx = -1
        for row in reader:
            idx += 1
            self.assertEqual(row, expected[idx], 
                             "%d : %r != %r" % (idx, row, expected[idx]))
            rows.append(row)

