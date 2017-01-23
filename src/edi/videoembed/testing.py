# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.videoembed


class EdiVideoembedLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=edi.videoembed)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.videoembed:default')


EDI_VIDEOEMBED_FIXTURE = EdiVideoembedLayer()


EDI_VIDEOEMBED_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_VIDEOEMBED_FIXTURE,),
    name='EdiVideoembedLayer:IntegrationTesting'
)


EDI_VIDEOEMBED_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_VIDEOEMBED_FIXTURE,),
    name='EdiVideoembedLayer:FunctionalTesting'
)


EDI_VIDEOEMBED_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_VIDEOEMBED_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='EdiVideoembedLayer:AcceptanceTesting'
)
