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

# additional imports from tagged value 'import'
from Products.AJAXAddRemoveWidget.AJAXAddRemoveWidget import AJAXAddRemoveWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='date',
        widget=DateTimeField._properties['widget'](
            label="Date",
            description="Meeting date and time",
            label_msgid='meetings_label_date',
            description_msgid='meetings_help_date',
            i18n_domain='meetings',
        ),
        label="Date",
    ),
    LinesField(
        name='atendees',
        widget=AJAXAddRemoveWidget(
            label="Atendees",
            allow_add=0,
            description="Search and select who is invited to the meeting. An e-mail will be sent to all the atendees.",
            label_msgid='meetings_label_atendees',
            description_msgid='meetings_help_atendees',
            i18n_domain='meetings',
        ),
        vocabulary='getUsers',
        label="Atendees",
    ),
    TextField(
        name='agenda',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Agenda",
            description="What is going to be discussed during the meeting",
            label_msgid='meetings_label_agenda',
            description_msgid='meetings_help_agenda',
            i18n_domain='meetings',
        ),
        default_output_type='text/html',
        label="Agenda",
    ),
    TextField(
        name='acta',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Acta",
            description="Briefing of the meeting once concluded",
            label_msgid='meetings_label_acta',
            description_msgid='meetings_help_acta',
            i18n_domain='meetings',
        ),
        default_output_type='text/html',
        label="Acta",
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

    security.declarePublic('getUsersList')
    def getUsersList(self):
        """
        """
        from Products.CMFCore.utils import getToolByName
        au = getToolByName(self, 'acl_users')
        
        ld_atendees = []
        for ld in self.getAtendees():
            mail = ''
            fullname = ld
            user = au.getUserById(ld)
            if 'LDAP' in user._propertysheets.keys():
                ps = user.getPropertysheet('LDAP')
                mail = ps.getProperty('email')
                fullname = ps.getProperty('fullname')
            ld_atendees.append((ld,fullname,mail))
        return ld_atendees


    ##/code-section class-header

    # Methods

    security.declarePublic('getUsers')
    def getUsers(self):
        """
        """
        from Products.CMFCore.utils import getToolByName
        au = getToolByName(self, 'acl_users')
        return DisplayList(tuple(self.getUsersList()))

    # Manually created methods




registerType(Meeting, PROJECTNAME)
# end of class Meeting

##code-section module-footer #fill in your manual code here
##/code-section module-footer



