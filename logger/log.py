
# class new creaes a new log for output
class New:
    def __init__(self, err_type, message):
        self._error_types = 'error', 'warning', 'log'
        try:
            self._check_type(err_type)
        except TypeError:
            print('Invalid error of type: ' + err_type + '\n')
        err_type = err_type.upper()
        self._type = err_type
        self._message = message

    def _check_type(self, err_type):
        for t in self._error_types:
            if err_type == t:
                return
        raise TypeError

    def print(self):
        print('[' + self._type + ']: ' + self._message + '\n')
        if self._type == 'ERROR':
            print('exiting...\n')
