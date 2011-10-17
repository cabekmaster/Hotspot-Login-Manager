# -*- coding:utf-8 -*-
#
# hotspot-login-manager
# https://github.com/syam44/Hotspot-Login-Manager
#
# Distributed under the GNU General Public License version 3
# https://www.gnu.org/copyleft/gpl.html
#
# Authors: syam (aks92@free.fr)
#
# Description: User notification daemon.
#


#-----------------------------------------------------------------------------
import os
import subprocess
#
from hotspot_login_manager.libs.core import hlm_application


#-----------------------------------------------------------------------------
#
# Filesystem path for the notification backends
#
_notifierBackendsPath = hlm_application.getPath() + '/notifiers'


#-----------------------------------------------------------------------------
class NotificationBackend(object):
    ''' Notification backend wrapper.
    '''
    def __init__(self, backend):
        # Check that the backend is actually supported.
        if backend in getAvailableBackends():
            self.__backend = _backendFullPath(backend)
        else:
            self.__backend = None


    def notify(self, message):
        ''' Send a notification message to the user through the backend program.
            Return a boolean indicating success.
        '''
        try:
            if self.__backend != None:
                subprocess.check_call([self.__backend, message])
                return True
        except:
            pass
        return False


#-----------------------------------------------------------------------------
def getAvailableBackends():
    ''' List all available notification backends.
    '''
    if getAvailableBackends.__cache == None:
        getAvailableBackends.__cache = []
        try:
            entries = os.listdir(_notifierBackendsPath + '/')
            for backend in entries:
                if _isValidBackend(backend):
                    getAvailableBackends.__cache.append(backend)
        except:
            pass
        getAvailableBackends.__cache.sort()
    return getAvailableBackends.__cache

#
# Use function attribute to cache the results
#
getAvailableBackends.__cache = None


#-----------------------------------------------------------------------------
def _backendFullPath(backend):
    ''' Return the full path of a specific notification backend.
    '''
    return os.path.realpath(_notifierBackendsPath + '/' + backend)


#-----------------------------------------------------------------------------
def _isValidBackend(backend):
    ''' Determine whether a particular notification backend is callable from
        the current user session context.
    '''
    try:
        backendPath = _backendFullPath(backend)
        if os.path.isfile(backendPath):
            subprocess.check_call([backendPath])
            return True
    except:
        pass
    return False


#-----------------------------------------------------------------------------
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
