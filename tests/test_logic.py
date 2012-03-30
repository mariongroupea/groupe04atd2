from unittest import TestCase
import logic

class LogicTests(TestCase):
    def test_and_(self):
        self.assertEquals(logic.and_(True, False), False)
    
    def test_or_(self):
        self.assertEquals(logic.or_(True, False), True)
