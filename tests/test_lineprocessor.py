import re
import unittest
from unittest.mock import MagicMock

from ..lineprocessor import LineProcessor

class TestLineProcessor(unittest.TestCase):
    def test__init_takes_rules(self):
        rules = {'a':'b'}
        lp = LineProcessor(rules)
        assert lp.rules == rules

    def test__process_line_dispatches_according_to_rules(self):
        first_handler = MagicMock(name='first_handler')
        second_handler = MagicMock(name='second_handler')
        print(first_handler)
        print(second_handler)
        rules = [
            (re.compile(r'ABC'), first_handler),
            (re.compile(r'ABC'), second_handler),
        ]
        lp = LineProcessor(rules)

        lp.process_line('ABC')

        assert first_handler.call_count == 1
        assert second_handler.call_count == 0
        # expect the argument passed to the handler to quack like a match object
        assert first_handler.call_args[0][0].group() == 'ABC'
        assert first_handler.call_args[0][0].string == 'ABC'
