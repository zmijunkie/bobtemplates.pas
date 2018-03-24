# -*- coding: utf-8 -*-


class RegEntry(object):
    def __init__(self):
        self.template = ''
        self.plonecli_alias = ''
        self.depend_on = None


def plone_pasplugin():
    reg = RegEntry()
    reg.template = 'bobtemplates.pas:plugin'
    reg.plonecli_alias = 'plone_pasplugin'
    reg.depend_on = 'plone_addon'
    return reg
