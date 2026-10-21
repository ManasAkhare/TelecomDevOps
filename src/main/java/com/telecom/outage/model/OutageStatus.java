package com.telecom.outage.model;

public enum OutageStatus {
    INVESTIGATING("Investigating", "primary"),
    IDENTIFIED("Identified", "warning"),
    MONITORING("Monitoring", "info"),
    RESOLVED("Resolved", "success");

    private final String label;
    private final String badgeColor;

    OutageStatus(String label, String badgeColor) {
        this.label = label;
        this.badgeColor = badgeColor;
    }

    public String getLabel() {
        return label;
    }

    public String getBadgeColor() {
        return badgeColor;
    }
}
