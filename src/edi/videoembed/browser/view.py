from zope.interface import Interface
from uvc.api import api
from plone import api as ploneapi

api.templatedir('templates')

class VideoEmbedView(api.Page):
    api.context(Interface)

    def update(self):
        self.portal_url = ploneapi.portal.get().absolute_url()
        self.showtitle = self.context.showtitle
        self.showdescription = self.context.showdescription
        self.src = self.context.src
        self.videotype = 'video/mp4'
        if self.src:
            if 'youtube' in self.src:
                self.videotype = 'video/youtube'
        self.embed = ''
        if not self.context.src:
            self.embed = self.context.embed
        self.textbefore = u''
        if self.context.textbefore:
            self.textbefore = self.context.textbefore.output
        self.textafter = u''
        if self.context.textafter:
            self.textafter = self.context.textafter.output
        self.caption = u''
        if self.context.caption:
            self.caption = self.context.caption
        self.videoformat = "row embed-responsive embed-responsive-16by9"
        if self.context.videoformat == "embed-responsive-4by3":
            self.videoformat = "row embed-responsive embed-responsive-4by3"

