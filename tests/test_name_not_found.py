from errors import NameNotFoundError
from tests import BaseTestCase


class NameNotFoundTestCase(BaseTestCase):
    def test_record_not_found(self):
        self.assertHasError('{Person p;}', NameNotFoundError)
        self.assertHasError('record Person {Address a;}', NameNotFoundError)

    def test_function_not_found(self):
        self.assertHasError('{foo();}', NameNotFoundError)