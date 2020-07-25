#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os


def main():

    parameters = ['--server-openvpn', '--client-openvpn', 'list-instances-openvpn',
                  '--list-certificates-openvpn', '--list-revogated-openvpn',
                  '--mail-client-openvpn', '--revoke-client-openvpn', 'server-ipsec',
                  '--help']

    try:
        for parameter in parameters:
            if sys.argv[1] == parameter:
                os.system("/usr/share/vpnmgr/manager.sh {}".format(parameter))
    except:
        os.system('/usr/share/vpnmgr/manager.sh --help')


if __name__ == '__main__':
    main()

