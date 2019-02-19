import unittest

from isfreemail import is_free_mail


class TestFreeMailServers(unittest.TestCase):
    def test_gmail(self):
        self.assertTrue(is_free_mail('xyz@gmail.com'))

    def test_mail_ru(self):
        self.assertTrue(is_free_mail('piotr.vasilievici@mail.ru'))

    def test_email_ro(self):
        self.assertTrue(is_free_mail('brancusi@email.ro'))

    def test_hotmail(self):
        self.assertTrue(is_free_mail('some.dude@hotmail.com'))

    def test_plus_address(self):
        self.assertTrue(is_free_mail('some+dude@mail.nu'))


class TestBusinessMailServers(unittest.TestCase):
    def test_google(self):
        self.assertFalse(is_free_mail('this.one.for.harvesters@google.com'))

    def test_microsoft(self):
        self.assertFalse(is_free_mail('this-one-for-harvesters@microsoft.com'))

    def test_hosterion(self):
        self.assertFalse(is_free_mail('thisoneforharvesters@hosterion.ro'))

    def test_fleio(self):
        self.assertFalse(is_free_mail('getharvesters@fleio.com'))


class TestInvalidAddresses(unittest.TestCase):
    def test_no_at(self):
        self.assertFalse(is_free_mail('someinvalidemail'))

    def test_mutliple_at(self):
        self.assertFalse(is_free_mail('sosxs33me@inv@alid@email'))
