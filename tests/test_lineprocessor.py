import re
import unittest
from unittest.mock import MagicMock

from ..lineprocessor import LineProcessor, UnexpectedLineError

class TestLineProcessor(unittest.TestCase):
    def test__init_takes_rules(self):
        rules = [('a','b')]
        lp = LineProcessor(rules)
        self.assertEqual(rules, lp.rules, 'The LineProcessor instance should have the rules we initialized with')
        assert lp.rules == rules

    def test__dispatch_line(self):
        first_handler = MagicMock(name='first_handler')
        second_handler = MagicMock(name='second_handler')
        print(first_handler)
        print(second_handler)
        rules = [
            (re.compile(r'ABC'), first_handler),
            (re.compile(r'ABC'), second_handler),
        ]
        lp = LineProcessor(rules)

        lp.dispatch_line('ABC')

        assert first_handler.call_count == 1
        assert second_handler.call_count == 0
        # expect the argument passed to the handler to quack like a match object
        assert first_handler.call_args[0][0].group() == 'ABC'
        assert first_handler.call_args[0][0].string == 'ABC'

    def test__dispatch_line_raises_if_no_match(self):
        lp = LineProcessor([])

        with self.assertRaises(UnexpectedLineError) as cm:
            lp.process_lines(['abc'])
        self.assertIsInstance(cm.exception.line_number, int, 'The exception should have an integer line number')

    def test__process_lines(self):
        letters_handler = MagicMock(name='letters_handler')
        mixed_handler = MagicMock(name='mixed_handler')
        rules = [
            (re.compile(r'^([a-zA-Z]+)$'), letters_handler),
            (re.compile(r'^(\w+)$'), mixed_handler),
        ]
        lp = LineProcessor(rules)

        lp.process_lines(['abc', 'def', 'gh6', 'ij7'])

        assert letters_handler.call_count == 2
        assert mixed_handler.call_count == 2


class TestUnexpectedLineError(unittest.TestCase):
    def test__repr_shows_line_and_number(self):
        line = 'abcdef12345'
        e = UnexpectedLineError("I'm the message", line)
        e.line_number = 99

        r = repr(e)

        self.assertIn(line, r)
        self.assertIn('99', r)


