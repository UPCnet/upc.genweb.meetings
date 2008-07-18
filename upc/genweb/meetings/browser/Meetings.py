# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_parent

class Atendees(BrowserView):
    """ Atendees List """



    def __init__(self,context, request):
        self.context = context
        self.request = request

    def getUsers(self,new_context):
        """
        """

    def getUsers(self):
        """
        """
        from Products.CMFCore.utils import getToolByName
        filter=self.request.get('filter','')
        mt = getToolByName(self, 'portal_membership')
        user_ids = mt.listMemberIds()
        filtered_user_ids = [dict(value=u,text=u) for u in user_ids if u.find(filter)>=0]
        return filtered_user_ids

