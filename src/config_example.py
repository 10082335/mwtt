########################
# mist_conf:
# Configuration to receive webhooks from Mist Cloud and to send API
# requests to Mist Cloud
#
# apitoken:         apitoken from Mist Cloud to sent API requests
# mist_cloud:       api.mist.com if you are using US Cloud, or
#                   api.eu.mist.com if you are using EU Cloud
# server_uri:       uri where you want to receive wehbooks messages
#                   on this server.
# mist_secret:      the webhook secret configuration on the Mist Cloud
#                   to secure webhook reception
mist_conf = {
    # file deepcode ignore HardcodedNonCryptoSecret: This is just an example
    "apitoken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "mist_host": "manage.mist.com",
    "mist_secret": None,
    "server_uri": "/webhooks",
    "site_id_ignored": [],
    "approved_admins": ["user@domain.com"]
}

log_level = "INFO"
# You can create more slack / msteams channel urls depending on your needs, you just need to be sure each
# channel has a unique name
slack_conf = {
    "enabled": True,
    "default_url": "https://hooks.slack.com/services/XXXXXXXX/XXXXXXXXX/XXXXXXXXXXX4",
    "url": {
        "debug": "https://hooks.slack.com/services/XXXXXXXX/XXXXXXXXX/XXXXXXXXXXX1",
        "info": "https://hooks.slack.com/services/XXXXXXXX/XXXXXXXXX/XXXXXXXXXXX2",
        "warning": "https://hooks.slack.com/services/XXXXXXXX/XXXXXXXXX/XXXXXXXXXXX3",
        "critical": "https://hooks.slack.com/services/XXXXXXXX/XXXXXXXXX/XXXXXXXXXXX3",
    }
}

msteams_conf = {
    "enabled": True,
    "default_url": "https://outlook.office.com/webhook/xxxxxxxxxxxx/IncomingWebhook/xxxxxxxxxxx/xxxxxxxxxxx",
    "url": {
        "debug": "https://outlook.office.com/webhook/xxxxxxxxxxxx/IncomingWebhook/xxxxxxxxxxx/xxxxxxxxxxx",
        "info": "https://outlook.office.com/webhook/xxxxxxxxxxxx/IncomingWebhook/xxxxxxxxxxx/xxxxxxxxxxx",
        "warning": "https://outlook.office.com/webhook/xxxxxxxxxxxx/IncomingWebhook/xxxxxxxxxxx/xxxxxxxxxxx",
        "critical": "https://outlook.office.com/webhook/xxxxxxxxxxxx/IncomingWebhook/xxxxxxxxxxx/xxxxxxxxxxx"
    }
}

event_channels = {
    "AP_CLAIMED": "warning",
    "AP_UNCLAIMED": "warning",
    "AP_ASSIGNED": "info",
    "AP_UNASSIGNED": "info",
    "AP_CONFIG_CHANGED_BY_RRM": "debug",
    "AP_CONFIG_CHANGED_BY_USER": "info",
    "AP_CONFIG_FAILED": "critical",
    "AP_CONFIGURED": "debug",
    "AP_RECONFIGURED": "debug",
    "1026": "debug",
    "AP_RRM_ACTION": "debug",
    "AP_BEACON_STUCK": "critical",
    "AP_RESTART_BY_USER": "info",
    "AP_RESTARTED": "info",
    "AP_CONNECTED": "info",
    "AP_DISCONNECTED": "info",
    "AP_DISCONNECTED_LONG": "warning",
    "AP_UPGRADED": "info",
    "AP_UPGRADE_BY_SCHEDULE": "debug",
    "AP_UPGRADE_BY_USER": "debug",
    "AP_UPGRADE_FAILED": "critical",
    "AP_RADAR_DETECTED": "info",
    "AP_CERT_REGENERATED": "debug",
    "AP_GET_SUPPORT_FILES": "debug",

    "GW_CLAIMED": "warning",
    "GW_UNCLAIMED": "warning",
    "GW_ASSIGNED": "info",
    "GW_UNASSIGNED": "info",
    "GW_ZTP_FINISHED": "info",
    "GW_CONFIG_CHANGED_BY_USER": "info",
    "GW_CONFIG_GENERATED": "debug",
    "GW_RECONFIGURED": "debug",
    "GW_CONFIGURED": "debug",
    "GW_CONFIG_LOCK_FAILED": "warning",
    "GW_CONFIG_FAILED": "warning",
    "GW_PORT_UP": "info",
    "GW_PORT_DOWN": "info",
    "GW_CONNECTED": "info",
    "GW_DISCONNECTED": "info",
    "GW_DISCONNECTED_LONG": "warning",
    "GW_RESTARTED": "info",
    "GW_RESTARTED_BY_USER": "info",
    "GW_OSPF_NEIGHBOR_UP": "debug",
    "GW_OSPF_NEIGHBOR_DOWN": "debug",
    "GW_BGP_NEIGHBOR_STATE_CHANGED": "debug",
    "GW_VPN_PATH_DOWN": "debug",
    "GW_VPN_PATH_UP": "debug",
    "GW_VPN_PEER_UP": "debug",
    "GW_VPN_PEER_DOWN": "debug",
    "GW_CERT_REGENERATED": "debug",
    "GW_ALARM": "warning",
    "GW_UPGRADE_BY_USER": "debug",
    "GW_UPGRADED": "debug",
    "GW_UPGRADE_PENDING": "debug",
    "GW_UPGRADE_FAILED": "warning",
    "GW_CONDUCTOR_CONNECTED": "info",
    "GW_ARP_RESOLVED": "info",
    "GW_ARP_UNRESOLVED": "warning",
    "GW_DHCP_RESOLVED": "debug",
    "GW_DHCP_UNRESOLVED": "warning",
    "GW_HA_CONTROL_LINK_UP": "info",
    "GW_HA_CONTROL_LINK_DOWN": "warning",
    "GW_HA_HEALTH_WEIGHT_LOW": "warning",
    "GW_HA_HEALTH_WEIGHT_RECOVERY": "info",
    "GW_CONDUCTOR_DISCONNECTED": "warning",
    "GW_SYSTEM_SERVICE_RESTART": "warning",
    "GW_REJECTED": "critical",
    "GW_RG_STATE_CHANGED": "info",
    "GW_PORT_RG_STATE_CHANGED": "info",

    "SW_CLAIMED": "warning",
    "SW_UNCLAIMED": "warning",
    "SW_ASSIGNED": "info",
    "SW_UNASSIGNED": "info",
    "SW_ZTP_FINISHED": "info",
    "SW_CONFIG_CHANGED_BY_USER": "info",
    "SW_RECONFIGURED": "debug",
    "SW_CONFIG_GENERATED": "debug",
    "SW_CONFIGURED": "debug",
    "SW_CONFIG_LOCK_FAILED": "warning",
    "SW_CONFIG_FAILED": "warning",
    "SW_PORT_UP": "debug",
    "SW_PORT_DOWN": "debug",
    "SW_CONNECTED": "info",
    "SW_DISCONNECTED": "info",
    "SW_RESTARTED": "info",
    "SW_RESTART_BY_USER": "info",
    "SW_OSPF_NEIGHBOR_UP": "debug",
    "SW_OSPF_NEIGHBOR_DOWN": "debug",
    "SW_BGP_NEIGHBOR_STATE_CHANGED": "debug",
    'SW_ALARM': "warning",
    'SW_ALARM_CHASSIS_PARTITION': "warning",
    'SW_ALARM_CHASSIS_POE': "warning",
    'SW_ALARM_CHASSIS_PSU': "warning",
    "SW_UPGRADE_BY_USER": "debug",
    "SW_UPGRADED": "debug",
    "SW_UPGRADE_PENDING": "debug",
    "SW_UPGRADE_FAILED": "critical",
    'SW_SYSTEM_SERVICE_RESTART': "warning",
    'SW_REJECTED': "critical",
    "SW_DYNAMIC_PORT_ASSIGNED": "info",
    'SW_PORT_BPDU_BLOCKED': "warnning",
    'SW_PORT_STORM_CONTROL': "warnning",
    'SW_HANDSHAKE_ERROR': "warning",
    'SW_STP_TOPO_CHANGED': "info",
    'SW_VC_BACKUP_ELECTED': "warning",
    'SW_VC_MASTER_CHANGED': "warning",
    'SW_VC_MEMBER_ADDED': "info",
    'SW_VC_MEMBER_DELETED': "warning",
    'SW_MASTER_ON_RECOVERY': "warning",
    'SW_MEMBER_ON_RECOVERY': "warning",
    'SW_RECOVERY_SNAPSHOT_REQUESTED': "info",
    'SW_RECOVERY_SNAPSHOT_SUCCEEDED': "info",
    'SW_RECOVERY_SNAPSHOT_FAILED': "warning",
    'SW_RECOVERY_SNAPSHOT_NOTNEEDED': "warning",
    'SW_RECOVERY_SNAPSHOT_UNSUPPORTED': "info",
    "SW_DOT1XD_USER_AUTHENTICATED": "debug",
    "SW_RADIUS_SERVER_UNREACHABLE": "warning",

    "ME_CLAIMED": "warning",
    "ME_UNCLAIMED": "warning",
    "ME_ASSIGNED": "info",
    "ME_UNASSIGNED": "info",
}

updown_channels = {
    "AP_CONNECTED": "info",
    "AP_DISCONNECTED": "info",
    "AP_RESTARTED": "info",
    "GW_CONNECTED": "info",
    "GW_DISCONNECTED": "info",
    "GW_RESTARTED": "info",
    "SW_CONNECTED": "info",
    "SW_DISCONNECTED": "info",
    "SW_RESTARTED": "info"
}

alarm_channels = {
    # infrastructure
    "device_down": "warning",
    "device_restarted": "info",
    "switch_down": "warning",
    "switch_restarted": "info",
    "gateway_down": "warning",
    "device_reconnected": "info",
    "switch_reconnected": "info",
    "gateway_reconnected": "info",
    "vpn_peer_down": "warning",
    "vc_master_changed": "critical",
    "vc_backup_failed": "critical",
    "vc_member_added": "info",
    "vc_member_deleted": "critical",
    "sw_alarm_chassis_poe": "warning",
    "sw_alarm_chassis_pem": "warning",
    "sw_alarm_chassis_psu": "warning",
    "sw_alarm_chassis_partition": "warning",
    "sw_dhcp_pool_exhausted": "warning",
    "gw_dhcp_pool_exhausted": "warning",
    "sw_bgp_neighbor_state_changed": "info",
    "sw_bad_optics": "warning",
    "sw_bpdu_error": "warning",
    # security
    "secpolicy_violation": "warning",
    "bssid_spoofing": "info",
    "honeypot_ssid": "info",
    "adhoc_network": "warning",
    "rogue_ap": "critical",
    "rogue_client": "critical",
    "watched_station": "warning",
    "eap_handshake_flood": "info",
    "air_magnet_scan": "info",
    "excessive_eapol_start": "warning",
    "eapol_logoff_attack": "warning",
    "eap_dictionary_attack": "warning",
    "disassociation_flood": "warning",
    "beacon_flood": "warning",
    "essid_jack": "warning",
    "krack_attack": "warning",
    "vendor_ie_missing": "warning",
    "tkip_icv_attack": "warning",
    "repeated_auth_failures": "info",
    "eap_failure_injection": "warning",
    "eap_spoofed_success": "warning",
    "out_of_sequence": "warning",
    "zero_ssid_association": "warning",
    "monkey_jack": "warning",
    "excessive_client": "warning",
    "ssid_injection": "warning",
    # marvis
    "missing_vlan": "critical",
    "bad_cable": "critical",
    "port_flap": "warning",
    "gw_bad_cable": "critical",
    "authentication_failure": "critical",
    "dhcp_failure": "critical",
    "arp_failure": "critical",
    "dns_failure": "critical",
    "negotiation_mismatch": "critical",
    "gw_negotiation_mismatch": "critical",
    "ap_offline": "warning",
    "non_compliant": "warning",
    "ap_bad_cable": "critical",
    "health_check_failed": "warning",
}

audit_channels = {
    "approved_admins": "debug",
    "other_admins": "critical"
}

mxedge_events = {
    "ME_CONFIG_CHANGED_BY_USER": "info",
    "ME_SERVICE_STOPPED": "debug",
    "ME_SERVICE_STARTED": "debug",
    "ME_SERVICE_RESTARTED": "debug",
    "ME_SERVICE_FAILED": "critical",
    "TT_TUNNELS_LOST": "warning",
    "ME_PACKAGE_INSTALLED": "info",
    "ME_PACKAGE_UPDATE_BY_USER": "info",
    "ME_RESTARTED": "info",
    "ME_RESOURCE_USAGE": "warning"
}
