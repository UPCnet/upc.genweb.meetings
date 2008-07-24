# -*- coding: utf-8 -*-
def meeting_created(meeting, event):
    assert meeting == event.object # At least normally, see below
    host = meeting.MailHost
    
    import pdb;pdb.set_trace()
    from Products.CMFCore.utils import getToolByName
    au = getToolByName(meeting, 'acl_users')
    owner = au.getUserById(meeting.owner_info()['id'])
    from_email = ''
    if 'LDAP' in owner._propertysheets.keys():
        ps = owner.getPropertysheet('LDAP')
        if 'email' in ps._properties.keys():
            from_email = ps.getProperty('email')
    if from_email:   
        for user in meeting.getUsersList():
            if user[2]:
                mail_text = """From:%s
To: %s
Subject: Invitació a reunió
Content-Type: text/plain; charset=UTF-8

Aquesta és una notificació automàtica per comunicar-li que ha estat convidat a la reunió %s. pot trobar més detalls en aquest enllaç 

%s
""" % (from_email.encode('UTF-8'),
       user[2].encode('UTF-8'),
       meeting.Title(),
       meeting.absolute_url()                      )

                host.send(mail_text)

def meeting_edited(meeting, event):
    assert meeting == event.object # At least normally, see below
    host = meeting.MailHost
    
    import pdb;pdb.set_trace()
    from Products.CMFCore.utils import getToolByName
    au = getToolByName(meeting, 'acl_users')
    owner = au.getUserById(meeting.owner_info()['id'])
    from_email = ''
    if 'LDAP' in owner._propertysheets.keys():
        ps = owner.getPropertysheet('LDAP')
        if 'email' in ps._properties.keys():
            from_email = ps.getProperty('email')
    if from_email:   
        for user in meeting.getUsersList():
            if user[2]:
                mail_text = """From:%s
To: %s
Subject: Invitació a reunió
Content-Type: text/plain; charset=UTF-8

Aquesta és una notificació automàtica per comunicar-li que s'han produit canvis en la reunió %s a la qual esta convidat/ada.Pot consultar els detalls en aquest enllaç 

%s
""" % (from_email.encode('UTF-8'),
       user[2].encode('UTF-8'),
       meeting.Title(),
       meeting.absolute_url()                      )

                host.send(mail_text)

