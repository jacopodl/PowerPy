from powerpy.synchronize import synchronized, synchronize_ensure, synchronize_release


class Pipe:
    def execute(self, obj):
        raise NotImplementedError()


class Pipeline:
    def __init__(self):
        self.pipeline = []

    @synchronized
    def add_pipe(self, pipe):
        if pipe not in self.pipeline:
            self.pipeline.append(pipe)

    @synchronized
    def del_pipe(self, pipe):
        if pipe in self.pipeline:
            self.pipeline.remove(pipe)

    def execute(self, obj):
        try:
            synchronize_ensure(self)
            pipes = list(self.pipeline)
        finally:
            synchronize_release(self)
        data = obj
        for pipe in pipes:
            data = pipe.execute(data)
        return data
