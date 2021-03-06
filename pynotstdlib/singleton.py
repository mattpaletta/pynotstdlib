class Singleton(object):
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.
    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.
    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    """

    __slots__ = ["_decorated", "_instance"]

    def __init__(self, decorated):
        self._decorated = decorated
        self._instance = None

    def Instance(self, *args, **kwargs):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        if self._instance is None:
            self._instance = self._decorated(*args, **kwargs)

        assert self._instance is not None, "Error, returning invalid class."
        return self._instance

    def __call__(self):
        if self._instance is None:
            self._instance = self._decorated(*args, **kwargs)

        assert self._instance is not None, "Error, returning invalid class."
        return self._instance

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
