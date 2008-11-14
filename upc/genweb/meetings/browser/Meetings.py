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
        au = getToolByName(self, 'acl_users')
        ldap_plugins = [item[1] for item in au.items() if item[1].meta_type=="Plone LDAP plugin"]
        if ldap_plugins:
            LDAP = ldap_plugins[0]
            ldap_users = LDAP.acl_users.searchUsers(cn=filter,ou='users',dc='upc')
        else:
            ldap_users = []
        if ldap_users:
            if ldap_users[0]['dn']=='Too many results for this query':
                return {'result':'error','type':'too_many'}
            else:
                #filtered_user_ids = [dict(value=u['cn'],text='%s %s' % (u['sn'],'mail' in u.keys() and '['+u['mail']+']' or '')) for u in ldap_users]
                filtered_user_ids = [dict(value=u['cn'],text=u['sn']) for u in ldap_users]
                return {'result':'success','users':filtered_user_ids}                
        else:
            return {'result':'error','type':'no_results'}
        


