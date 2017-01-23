from zope.interface import Interface
from uvc.api import api
from plone import api as ploneapi

api.templatedir('templates')

class myTestView(api.Page):
    api.context(Interface)

    def update(self):
        self.portal_url = ploneapi.portal.get().absolute_url()
