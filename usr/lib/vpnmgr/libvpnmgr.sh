#!/usr/bin/env bash

source "/usr/lib/vpnmgr/Common.sh"
source "/usr/lib/vpnmgr/OpenvpnServer.sh"
source "/usr/lib/vpnmgr/ClientOpenvpn.sh"
source "/usr/lib/vpnmgr/ListingsOpenvpn.sh"
source "/usr/lib/vpnmgr/RevokeOpenvpn.sh"
source "/usr/lib/vpnmgr/MailOpenvpn.sh"
source "/usr/lib/vpnmgr/IpsecServer.sh"

HELP (){
    echo
    echo "      -----------------------------Informações de ajuda----------------------------"
    echo
    echo "      --help                      -               Ajuda"
    echo
    echo "      --server-openvpn            -               Cria um certificado raiz"
    echo
    echo "      --server-ipsec (unstable - not use)"             -               "Cria um servidor ipsec"
    echo
    echo "      --client-openvpn            -               Cria um certificado de um cliente"
    echo
    echo "      --revoke-client-openvpn     -               Revoga um certificado cliente"
    echo
    echo "      --list-instances-openvpn    -               Lista instâncias VPN"
    echo
    echo "      --list-revogated-openvpn    -               Lista certificados revogados"
    echo
    echo "      --list-certificates-openvpn -               Lista certificados clientes"
    echo
    echo "      --mail-client-openvpn       -               Enviado o certificado do cliente por e-mail"
    echo
}