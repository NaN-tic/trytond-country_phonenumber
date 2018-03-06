# This file is part country_phonenumber module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import country


def register():
    Pool.register(
        country.Country,
        country.LoadCountryPhonenumberStart,
        module='country_phonenumber', type_='model')
    Pool.register(
        country.LoadCountryPhonenumber,
        module='country_phonenumber', type_='wizard')
