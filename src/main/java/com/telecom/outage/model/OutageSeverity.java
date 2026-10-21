package com.telecom.outage.model;

public enum OutageSeverity {
    CRITICAL("Critical - P1", "danger"),
    MAJOR("Major - P2", "warning"),
    MINOR("Minor - P3", "info");

    private final String label;
    private final String badgeColor;

    OutageSeverity(String label, String badgeColor) {
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
