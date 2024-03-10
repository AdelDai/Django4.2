class FourDigitYearConverter:
    regex = '[1-9][0-9]*'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value