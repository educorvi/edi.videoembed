# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
import random
from edi.videoembed import _
from five import grok
from zope import schema
from zope.interface import Interface
from DateTime import DateTime
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema.interfaces import IContextAwareDefaultFactory
from Products.CMFCore.utils import getToolByName
from plone.namedfile.field import NamedBlobImage
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.textfield import RichText
from plone.supermodel import directives

formatVocabulary = SimpleVocabulary.fromItems((
    (u"4:3", "embed-responsive-4by3"),
    (u"16:9", "embed-responsive-16by9")))

@grok.provider(IContextAwareDefaultFactory)
def genWebcode(context):
    aktuell=unicode(DateTime()).split(' ')[0]
    neujahr='%s/01/01' %str(DateTime()).split(' ')[0][:4]
    konstante=unicode(aktuell[2:4])
    zufallszahl=unicode(random.randint(100000, 999999))
    code=konstante+zufallszahl
    pcat=getToolByName(context,'portal_catalog')
    results = pcat(Webcode=code, created={"query":[neujahr,aktuell],"range":"minmax"})
    while results:
        zufallszahl=unicode(random.randint(100000, 999999))
        code=konstante+zufallszahl
        results = pcat(Webcode=code, created={"query":[neujahr,aktuell],"range":"minmax"})
    return code

class IEdiVideoembedLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IVideoembed(Interface):

    directives.fieldset('settings',
                        label=u'Einstellungen',
                        fields=(u'videoformat',u'showtitle',u'showdescription',),
    )

    title = schema.TextLine(
        title=u'Titel',
        required=True,
    )

    description = schema.Text(
        title=u'Beschreibung',
        required=False,
    )

    textbefore = RichText(title = u'Text vor Einblendung des Videos',
                          required = False)

    src = schema.TextLine(title = u'Quell-URL für YouTube Videos oder MP4-Dateien',
            description = u'Bitte kopieren Sie die Internetadresse Ihres YouTube Videos\
                            oder ihrer MP4-Datei und fügen diese hier ein.',
            required = False)

    embed = schema.Text(title = u'Alternativ: Einfügen von "Embed-Code"',
            description = u'Alternativ können Sie hier den Embed-Code einfügen,\
                            den Sie von Ihrem Videodienst (z.B.: Movingimage24, Vimeo, Kaltura...)\
                            zur Verfügung gestellt bekommen.',
            required = False)

    caption = schema.TextLine(title = u'(Bild-) Unterschrift unter das Video',
                         required = False)

    textafter = RichText(title = u'Text nach Einblendung des Videos',
                          required = False)

    videoformat = schema.Choice(title = u'Bildschirmformat des Videos',
                           default = u"embed-responsive-16by9",
                           vocabulary = formatVocabulary,
                           required = True)

    poster = NamedBlobImage(title=u"Poster bzw. Titelbild für das Video",
                           required=False,
                           ) 

    showtitle = schema.Bool(title = u'Titel anzeigen',
            description = u"Hier klicken wenn der Titel in der Einzeldarstellung angezeigt werden soll.",
            default = True,
            required = False)

    showdescription = schema.Bool(title = u'Beschreibung anzeigen',
            description = u"Hier klicken wenn die Beschreibung in der Einzeldarstellung angezeigt werden soll.",
            default = True,
            required = False)

    webcode = schema.TextLine(
              title=u"Webcode",
              description=u"Der Webcode für diesen Artikel wird automatisch errechnet und angezeigt. Sie\
                          können diesen Webcode bei Bedarf jedoch jederzeit überschreiben.",
              required = True,
              defaultFactory = genWebcode,
              )
