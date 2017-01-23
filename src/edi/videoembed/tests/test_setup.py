# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from edi.videoembed.testing import EDI_VIDEOEMBED_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that edi.videoembed is properly installed."""

    layer = EDI_VIDEOEMBED_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edi.videoembed is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edi.videoembed'))

    def test_browserlayer(self):
        """Test that IEdiVideoembedLayer is registered."""
        from edi.videoembed.interfaces import (
            IEdiVideoembedLayer)
        from plone.browserlayer import utils
        self.assertIn(IEdiVideoembedLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_VIDEOEMBED_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['edi.videoembed'])

    def test_product_uninstalled(self):
        """Test if edi.videoembed is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edi.videoembed'))

    def test_browserlayer_removed(self):
        """Test that IEdiVideoembedLayer is removed."""
        from edi.videoembed.interfaces import \
            IEdiVideoembedLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEdiVideoembedLayer, utils.registered_layers())
