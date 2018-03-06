#This file is part of country_zip_es module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from csv import reader
from trytond.model import ModelView, fields
from trytond.pool import Pool, PoolMeta
from trytond.wizard import Button, StateView, Wizard, StateTransition
import os

__all__ = ['Country', 'LoadCountryPhonenumberStart', 'LoadCountryPhonenumber']


class Country:
    __metaclass__ = PoolMeta
    __name__ = 'country.country'
    phonenumber = fields.Integer('Phonenumber')


class LoadCountryPhonenumberStart(ModelView):
    'Load Country Phonenumber Start'
    __name__ = 'load.country.phonenumber.start'


class LoadCountryPhonenumber(Wizard):
    'Load Country Phonenumber'
    __name__ = "load.country.phonenumber"
    start = StateView('load.country.phonenumber.start',
        'country_phonenumber.load_country_phonenumber_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Accept', 'accept', 'tryton-ok', default=True),
            ])
    accept = StateTransition()

    @classmethod
    def __setup__(cls):
        super(LoadCountryPhonenumber, cls).__setup__()
        cls._error_messages.update({
                'error': 'CSV Import Error!',
                'read_error': 'Error reading file: %s.\nError raised: %s.',
                })

    def transition_accept(self):
        Country = Pool().get('country.country')

        delimiter = ','
        quotechar = '"'
        data = open(os.path.join(
                os.path.dirname(__file__), 'phonenumber.csv'))
        try:
            rows = reader(data, delimiter=delimiter, quotechar=quotechar)
        except TypeError, e:
            self.raise_user_error('error',
                error_description='read_error',
                error_description_args=('phonenumber.csv', e))
        rows.next()

        countries = dict((c.code, c) for c in Country.search([]))

        to_write = []
        for row in rows:
            if not row:
                continue
            country_code = row[0]
            if countries.get(country_code):
                country = countries[country_code]
                to_write.extend(([country], {'phonenumber': int(row[1])}))

        if to_write:
            Country.write(*to_write)

        return 'end'
