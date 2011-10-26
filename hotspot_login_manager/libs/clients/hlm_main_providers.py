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
# Description: Main program for listing the available providers.
#


#-----------------------------------------------------------------------------
import sys
#
from hotspot_login_manager.libs.daemon import hlm_auth_plugins


#-----------------------------------------------------------------------------
def main(args):
    providers = hlm_auth_plugins.getSupportedProviders()
    providers.sort()

    print(_('Available service providers:'))
    for provider in providers:
        print('    ' + provider)

    sys.exit(0)


#-----------------------------------------------------------------------------
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
