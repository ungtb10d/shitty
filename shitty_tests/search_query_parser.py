#!/usr/bin/env python
# License: GPLv3 Copyright: 2022, ungtb10d <kovid at ungtb10d.net>


from . import BaseTest


class TestSQP(BaseTest):

    def test_search_query_parser(self):
        from shitty.search_query_parser import search, ParseException
        locations = 'id'
        universal_set = {1, 2, 3, 4, 5}

        def get_matches(location, query, candidates):
            return {x for x in candidates if query == str(x)}

        def t(q, expected=set()):
            actual = search(q, locations, universal_set, get_matches)
            self.ae(actual, expected)

        t('id:1', {1})
        t('id:"1"', {1})
        t('id:1 and id:1', {1})
        t('id:1 or id:2', {1, 2})
        t('id:1 and id:2')
        t('not id:1', universal_set - {1})
        t('(id:1 or id:2) and id:1', {1})
        self.assertRaises(ParseException, t, '1')
        self.assertRaises(ParseException, t, '"id:1"')
