# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import hiremi.api


class HiremiApiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=hiremi.api)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'hiremi.api:default')


HIREMI_API_FIXTURE = HiremiApiLayer()


HIREMI_API_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HIREMI_API_FIXTURE,),
    name='HiremiApiLayer:IntegrationTesting',
)


HIREMI_API_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HIREMI_API_FIXTURE,),
    name='HiremiApiLayer:FunctionalTesting',
)


HIREMI_API_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        HIREMI_API_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='HiremiApiLayer:AcceptanceTesting',
)
