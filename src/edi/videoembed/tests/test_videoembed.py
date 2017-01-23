# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from edi.videoembed.interfaces import IVideoembed
from edi.videoembed.testing import EDI_VIDEOEMBED_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class VideoembedIntegrationTest(unittest.TestCase):

    layer = EDI_VIDEOEMBED_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Videoembed')
        schema = fti.lookupSchema()
        self.assertEqual(IVideoembed, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Videoembed')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Videoembed')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IVideoembed.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Videoembed',
            id='Videoembed',
        )
        self.assertTrue(IVideoembed.providedBy(obj))
