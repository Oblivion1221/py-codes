class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print ('g')
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        print ('s')
        return self._path

    __repr__ = __str__

    def __call__(self, name):
        print ('c')
        return Chain('%s/%s' % (self._path, name))

print (Chain().status.users('me').repos)
