package com.telecom.outage.model;

public enum ServiceType {
    CELLULAR_5G("5G Mobile Core"),
    CELLULAR_4G("4G VoLTE / LTE"),
    BROADBAND_FIBER("FTTH Fiber Broadband"),
    VOLTE_CALLING("VoLTE Voice Gateway"),
    ENTERPRISE_LEASED_LINE("Enterprise MPLS / ILL");

    private final String displayName;

    ServiceType(String displayName) {
        this.displayName = displayName;
    }

    public String getDisplayName() {
        return displayName;
    }
}
