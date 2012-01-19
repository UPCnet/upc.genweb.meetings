# -*- coding: utf-8 -*-
def meeting_created(meeting, event):
    assert meeting == event.object # At least normally, see below
    host = meeting.MailHost
    
    from Products.CMFCore.utils import getToolByName
    LanguageTool=getToolByName(meeting, 'portal_languages')
    lang = LanguageTool.getLanguageCookie() or 'ca'    
    au = getToolByName(meeting, 'acl_users')
    owner = au.getUserById(meeting.owner_info()['id'])
    from_email = ''
    if owner:
      if 'ldapUPC' in owner._propertysheets.keys():
        ps = owner.getPropertysheet('ldapUPC')
        if 'email' in ps._properties.keys():
            from_email = ps.getProperty('email')
    if from_email: 
        for user in meeting.getUsersList():
            if user[2]:
                body_text = {'ca':"Aquesta és una notificació automàtica per comunicar-li que ha estat convidat a la reunió '%s'. pot trobar més detalls en aquest enllaç\n\n%s",
                             'es':"Esto es una notificación automática para comunicar-le que ha sido invitado a la reunió '%s'. Puede consultar los detalles en el enlace siguiente \n\n%s",
                             'en':"This is an automated notification to let you know that you have been invited to the meeting '%s'. You can see the details in the following link \n\n%s"}
                subject_text = {'ca':"Invitació a reunió",
                                'es':"Invitación a reunion",
                                'en':"Meeting invitation"}                             
                mail_text =  body_text[lang] % ( meeting.Title(),
                                                 meeting.absolute_url(),
                                                )
                result = host.secureSend(mail_text, 
                                         user[2].encode('UTF-8'), 
                                         from_email.encode('UTF-8'), 
                                         subject=subject_text[lang], 
                                         subtype='plain', 
                                         charset='UTF-8', 
                                         debug=False, 
                                         )

def meeting_edited(meeting, event):
    assert meeting == event.object # At least normally, see below
    host = meeting.MailHost
    
    from Products.CMFCore.utils import getToolByName
    LanguageTool=getToolByName(meeting, 'portal_languages')
    lang = LanguageTool.getLanguageCookie() or 'ca'
    au = getToolByName(meeting, 'acl_users')
    owner = au.getUserById(meeting.owner_info()['id'])
    from_email = ''
    if owner:
      if 'ldapUPC' in owner._propertysheets.keys():
        ps = owner.getPropertysheet('ldapUPC')
        if 'email' in ps._properties.keys():
            from_email = ps.getProperty('email')
    if from_email:   
        for user in meeting.getUsersList():
            if user[2]:
                body_text = {'ca':"Això és una notificació automàtica per comunicar-li que s'han produit canvis a la reunió '%s' a la que està convidat/ada. Pots consultar els detalls en el següent enllaç\n\n%s",
                             'es':"Esto es una notificación automática para comunicar-le que se han producido cambios en la reunió '%s' a la que esta invitado/ada. Puede consultar los detalles en el enlace siguiente \n\n%s",
                             'en':"This is an automated notification to let you know that the meeting '%s' to which you're invited has been modified. You can see the details in the following link \n\n%s"}
                subject_text = {'ca':"Invitació a reunió",
                                'es':"Invitación a reunion",
                                'en':"Meeting invitation"}                             
                mail_text =  body_text[lang] % ( meeting.Title(),
                                                 meeting.absolute_url(),
                                                )
                result = host.secureSend(mail_text, 
                                         user[2].encode('UTF-8'), 
                                         from_email.encode('UTF-8'), 
                                         subject=subject_text[lang], 
                                         subtype='plain', 
                                         charset='UTF-8', 
                                         debug=False, 
                                         )


