import operator


class Uint(int):
    def __add__(self, other):
        result = operator.__add__(self, other)
        return 0 if result < 0 else result

    def __sub__(self, other):
        result = operator.__sub__(self, other)
        return 0 if result < 0 else result

    def __mul__(self, other):
        result = operator.__mul__(self, other)
        return 0 if result < 0 else result

    def __mod__(self, other):
        result = operator.__mod__(self, other)
        return 0 if result < 0 else result

    def __floordiv__(self, other):
        result = operator.__floordiv__(self, other)
        return 0 if result < 0 else result

    def __truediv__(self, other):
        result = operator.__truediv__(self, other)
        return 0 if result < 0 else result
        
