# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from edi.videoembed import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.namedfile.field import NamedBlobImage
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.textfield import RichText


formatVocabulary = SimpleVocabulary.fromItems((
    (u"4:3", "embed-responsive-4by3"),
    (u"16:9", "embed-responsive-16by9")))

class IEdiVideoembedLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IVideoembed(Interface):

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
            required = False)

    showdescription = schema.Bool(title = u'Beschreibung anzeigen',
            description = u"Hier klicken wenn die Beschreibung in der Einzeldarstellung angezeigt werden soll.",
            required = False)

