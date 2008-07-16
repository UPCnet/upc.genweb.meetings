# -*- coding: utf-8 -*-
#
# File: Meeting.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0-beta11
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from upc.genweb.meetings.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='date',
        widget=DateTimeField._properties['widget'](
            label='Date',
            label_msgid='meetings_label_date',
            i18n_domain='meetings',
        ),
    ),
    LinesField(
        name='atendees',
        widget=LinesField._properties['widget'](
            label='Atendees',
            label_msgid='meetings_label_atendees',
            i18n_domain='meetings',
        ),
    ),
    TextField(
        name='agenda',
        widget=TextAreaWidget(
            label='Agenda',
            label_msgid='meetings_label_agenda',
            i18n_domain='meetings',
        ),
    ),
    TextField(
        name='acta',
        widget=TextAreaWidget(
            label='Acta',
            label_msgid='meetings_label_acta',
            i18n_domain='meetings',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Meeting_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Meeting(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IMeeting)

    meta_type = 'Meeting'
    _at_rename_after_creation = True

    schema = Meeting_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Meeting, PROJECTNAME)
# end of class Meeting

##code-section module-footer #fill in your manual code here
##/code-section module-footer



