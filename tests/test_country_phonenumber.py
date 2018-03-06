# This file is part country_phonenumber module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class CountryPhonenumberTestCase(ModuleTestCase):
    'Test Country Phonenumber module'
    module = 'country_phonenumber'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            CountryPhonenumberTestCase))
    return suite
