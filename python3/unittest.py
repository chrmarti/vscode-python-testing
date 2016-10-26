import unittest

class TestHello(unittest.TestCase):

    def test_foo(self):
        self.assertEqual('foo'.capitalize(), 'Foo')

    def test_bar(self):
        self.assertEqual('bar'.capitalize(), 'Bar?')

unittest.main()
