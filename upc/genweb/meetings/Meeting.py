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
from Products.ATContentTypes import ATCTMessageFactory as _
from Products.ATContentTypes.lib.calendarsupport import CalendarSupportMixin

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


    TextField(
        name='description',
        allowable_content_types=('text/plain'),
        widget=TextAreaWidget(
            label="Description",
            description="Brief description of the meeting",
            label_msgid='meetings_label_description',
            description_msgid='meetings_help_description',
            i18n_domain='meetings',
        ),
        default_output_type='text/plain',
        label="Description",
    ),
    DateTimeField(
        name='startDate',
        accessor='start',
        widget=DateTimeField._properties['widget'](
            label="Meeting starts",
            description="Date and time when meeting starts",
            label_msgid='meetings_label_start',
            description_msgid='meetings_help_start',
            i18n_domain='meetings',
        ),
        label="Meeting ends",
    ),
    DateTimeField(
        name='endDate',
        accessor='end',
        widget=DateTimeField._properties['widget'](
            label="Meeting ends",
            description="Date and time when meeting ends",
            label_msgid='meetings_label_end',
            description_msgid='meetings_help_end',
            i18n_domain='meetings',
        ),
        label="Meeting ends",
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
    LinesField('eventType',
               required=False,
               searchable=True,
               languageIndependent=True,
               widget = KeywordWidget(
                        size = 6,
                        description='',
                        label = _(u'label_event_type', default=u'Event Type(s)')
                        )),   
    StringField('contactName',
                required=False,
                searchable=True,
                accessor='contact_name',
                widget = StringWidget(
                        description = '',
                        label = _(u'label_contact_name', default=u'Contact Name')
                        )),    
    StringField('contactPhone',
                required=False,
                searchable=True,
                accessor='contact_phone',
                validators= (),
                widget = StringWidget(
                        description = '',
                        label = _(u'label_contact_phone', default=u'Contact Phone')
                        )),    
    StringField('contactEmail',
                required=False,
                searchable=True,
                accessor='contact_email',
                validators = ('isEmail',),
                widget = StringWidget(
                        description = '',
                        label = _(u'label_contact_email', default=u'Contact E-mail')
                        )),   
    StringField('eventUrl',
                required=False,
                searchable=True,
                accessor='event_url',
                validators=('isURL',),
                widget = StringWidget(
                        description = _(u'help_url',
                                        default=u"Web address with more info about the event. "
                                                 "Add http:// for external links."),
                        label = _(u'label_url', default=u'Event URL')
                        )),    
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Meeting_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
Meeting_schema['eventType'].widget.visible = {'view': 'invisible','edit': 'invisible'}
Meeting_schema['contactName'].widget.visible = {'view': 'invisible','edit': 'invisible'}
Meeting_schema['contactPhone'].widget.visible = {'view': 'invisible','edit': 'invisible'}
Meeting_schema['contactEmail'].widget.visible = {'view': 'invisible','edit': 'invisible'}
Meeting_schema['eventUrl'].widget.visible = {'view': 'invisible','edit': 'invisible'}
##/code-section after-schema

class Meeting(BaseContent,  CalendarSupportMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IMeeting)

    meta_type = 'Meeting'
    _at_rename_after_creation = True

    schema = Meeting_schema

    ##code-section class-header #fill in your manual code here

    security.declarePublic('exclude_from_nav')
    def exclude_from_nav(self):
        """
        """
        value=False
        return value
    

    security.declarePublic('Description')
    def Description(self):
        """
        """
        value=self.getDescription()
        return value
    
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
            
            if 'ldapUPC' in user._propertysheets.keys():
                ps = user.getPropertysheet('ldapUPC')
                mail = ps.getProperty('email')
                fullname = ps.getProperty('fullname')    
                name = ps.getProperty('name')  
            else:
                name = ld
                mail = ld            
            ld_atendees.append((ld,name,mail))
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


registerType(Meeting, PROJECTNAME)
# end of class Meeting

##code-section module-footer #fill in your manual code here
##/code-section module-footer



