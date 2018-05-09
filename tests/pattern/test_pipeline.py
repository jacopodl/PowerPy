import unittest

from powerpy.pattern.pipeline import Pipeline, Pipe


class SplitDot(Pipe):
    def execute(self, obj):
        return obj.split('.')


class Reverse(Pipe):
    def execute(self, obj):
        return obj[::-1]


class JoinWithDot(Pipe):
    def execute(self, obj):
        return ".".join(obj)


class AppendInAddr(Pipe):
    def execute(self, obj):
        return obj + ".in-addr.arpa"


class TestObservable(unittest.TestCase):
    def test_pipeline(self):
        p = Pipeline()
        s = SplitDot()
        p.add_pipe(s)
        p.add_pipe(s)
        p.add_pipe(Reverse())
        p.add_pipe(JoinWithDot())
        p.add_pipe(AppendInAddr())
        self.assertEqual(p.execute("2.45.16.56"), "56.16.45.2.in-addr.arpa")

    def test_add_del(self):
        p = Pipeline()
        r = Reverse()
        p.add_pipe(SplitDot())
        p.add_pipe(r)
        p.add_pipe(JoinWithDot())
        p.add_pipe(AppendInAddr())
        p.del_pipe(r)
        p.del_pipe(r)
        self.assertEqual(p.execute("2.45.16.56"), "2.45.16.56.in-addr.arpa")
