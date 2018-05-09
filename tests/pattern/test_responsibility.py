import unittest

from powerpy.pattern.responsibility import Handler


class Under(Handler):
    def handle(self, obj):
        if obj <= 100:
            return Under
        return self.next_handler(obj)


class Between(Handler):
    @Handler.forward_if("NEXT")
    def handle(self, obj):
        if 100 < obj <= 200:
            return Between
        return "NEXT"


class Upper(Handler):
    @Handler.forward_if()
    def handle(self, obj):
        if 200 < obj <= 1000:
            return Upper
        return None


class TestResponsibility(unittest.TestCase):
    def test_chain(self):
        u = Under()
        u.set_next(Between()).set_next(Upper())
        self.assertEqual(u.handle(100), Under)
        self.assertEqual(u.handle(101), Between)
        self.assertEqual(u.handle(500), Upper)
        self.assertEqual(u.handle(1001), None)
