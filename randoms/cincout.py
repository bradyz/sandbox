import sys


class Wrapper():
    def __init__(self, stream):
        self.stream = stream

    def __lshift__(self, string):
        self.stream.write(string)
        return self

cout = Wrapper(sys.stdout)
cout << "hello world" << "\n" << "123"
