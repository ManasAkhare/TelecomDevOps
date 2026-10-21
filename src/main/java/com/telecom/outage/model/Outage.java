package com.telecom.outage.model;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Outage {
    private String id;

    @NotBlank(message = "Incident title is required")
    private String title;

    @NotNull(message = "Service type is required")
    private ServiceType serviceType;

    @NotNull(message = "Severity is required")
    private OutageSeverity severity;

    @NotNull(message = "Status is required")
    private OutageStatus status;

    @NotBlank(message = "Telecom Circle/Region is required")
    private String region;

    private String impactedTowers;

    @Min(value = 0, message = "Affected subscribers must be positive")
    private long affectedSubscribers;

    private String rootCause;
    private String reportedBy;
    private LocalDateTime reportedAt;
    private LocalDateTime resolvedAt;
    private int slaTargetMinutes;
    private String notes;

    public Outage() {
        this.reportedAt = LocalDateTime.now();
        this.serviceType = ServiceType.CELLULAR_5G;
        this.severity = OutageSeverity.MAJOR;
        this.status = OutageStatus.INVESTIGATING;
        this.slaTargetMinutes = 120; // Default 2 hours SLA
    }

    public Outage(String id, String title, ServiceType serviceType, OutageSeverity severity,
                  OutageStatus status, String region, String impactedTowers,
                  long affectedSubscribers, String rootCause, String reportedBy,
                  LocalDateTime reportedAt, int slaTargetMinutes, String notes) {
        this.id = id;
        this.title = title;
        this.serviceType = serviceType;
        this.severity = severity;
        this.status = status;
        this.region = region;
        this.impactedTowers = impactedTowers;
        this.affectedSubscribers = affectedSubscribers;
        this.rootCause = rootCause;
        this.reportedBy = reportedBy;
        this.reportedAt = reportedAt;
        this.slaTargetMinutes = slaTargetMinutes;
        this.notes = notes;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public ServiceType getServiceType() { return serviceType; }
    public void setServiceType(ServiceType serviceType) { this.serviceType = serviceType; }

    public OutageSeverity getSeverity() { return severity; }
    public void setSeverity(OutageSeverity severity) { this.severity = severity; }

    public OutageStatus getStatus() { return status; }
    public void setStatus(OutageStatus status) { this.status = status; }

    public String getRegion() { return region; }
    public void setRegion(String region) { this.region = region; }

    public String getImpactedTowers() { return impactedTowers; }
    public void setImpactedTowers(String impactedTowers) { this.impactedTowers = impactedTowers; }

    public long getAffectedSubscribers() { return affectedSubscribers; }
    public void setAffectedSubscribers(long affectedSubscribers) { this.affectedSubscribers = affectedSubscribers; }

    public String getRootCause() { return rootCause; }
    public void setRootCause(String rootCause) { this.rootCause = rootCause; }

    public String getReportedBy() { return reportedBy; }
    public void setReportedBy(String reportedBy) { this.reportedBy = reportedBy; }

    public LocalDateTime getReportedAt() { return reportedAt; }
    public void setReportedAt(LocalDateTime reportedAt) { this.reportedAt = reportedAt; }

    public LocalDateTime getResolvedAt() { return resolvedAt; }
    public void setResolvedAt(LocalDateTime resolvedAt) { this.resolvedAt = resolvedAt; }

    public int getSlaTargetMinutes() { return slaTargetMinutes; }
    public void setSlaTargetMinutes(int slaTargetMinutes) { this.slaTargetMinutes = slaTargetMinutes; }

    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }

    public String getFormattedReportedAt() {
        if (reportedAt == null) return "N/A";
        return reportedAt.format(DateTimeFormatter.ofPattern("dd-MMM-yyyy HH:mm:ss"));
    }

    public boolean isCriticalException() {
        return severity == OutageSeverity.CRITICAL && status != OutageStatus.RESOLVED;
    }

    public boolean isHighImpact() {
        return affectedSubscribers >= 25000;
    }
}
