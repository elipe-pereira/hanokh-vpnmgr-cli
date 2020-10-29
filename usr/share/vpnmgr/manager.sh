#!/bin/bash

# Eli F Pereira - Software & Redes - Desenvolvimento de aplicacoes web, Servicos de Rede, Seguranca e Tecnologia
# manager.sh - Script que gera um novo certificado raiz e também o certificado do usuario
# e envia o certificado por email se o cliente de e-mails estiver
# configurado no servidor

source "/usr/lib/vpnmgr/libvpnmgr.sh"

case "$1" in
  --server-openvpn) create_server_openvpn
    ;;
  --client-openvpn) client_openvpn
    ;;
   --list-instances-openvpn) list_instances_openvpn
   ;;
   --list-certificates-openvpn) list_certificates_openvpn
   ;;
   --list-revogated-openvpn) list_revogated_openvpn
   ;;
   --mail-client-openvpn) mail_client_openvpn
   ;;
   --revoke-client-openvpn) revoke_client_openvpn
   ;;
   --server-ipsec) create_ipsec_server
   ;;
   --help) HELP
   ;;
   *) HELP
   ;;
esac
