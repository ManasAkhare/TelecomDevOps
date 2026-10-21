package com.telecom.outage.model;

import java.util.Map;

public class DashboardMetrics {
    private long totalOutages;
    private long activeOutages;
    private long criticalAlerts;
    private long resolvedOutages;
    private long totalImpactedSubscribers;
    private double meanTimeToResolutionHours;
    private double slaCompliancePercentage;
    private Map<String, Long> outagesByRegion;
    private Map<String, Long> outagesByService;

    public DashboardMetrics() {}

    public long getTotalOutages() { return totalOutages; }
    public void setTotalOutages(long totalOutages) { this.totalOutages = totalOutages; }

    public long getActiveOutages() { return activeOutages; }
    public void setActiveOutages(long activeOutages) { this.activeOutages = activeOutages; }

    public long getCriticalAlerts() { return criticalAlerts; }
    public void setCriticalAlerts(long criticalAlerts) { this.criticalAlerts = criticalAlerts; }

    public long getResolvedOutages() { return resolvedOutages; }
    public void setResolvedOutages(long resolvedOutages) { this.resolvedOutages = resolvedOutages; }

    public long getTotalImpactedSubscribers() { return totalImpactedSubscribers; }
    public void setTotalImpactedSubscribers(long totalImpactedSubscribers) { this.totalImpactedSubscribers = totalImpactedSubscribers; }

    public double getMeanTimeToResolutionHours() { return meanTimeToResolutionHours; }
    public void setMeanTimeToResolutionHours(double meanTimeToResolutionHours) { this.meanTimeToResolutionHours = meanTimeToResolutionHours; }

    public double getSlaCompliancePercentage() { return slaCompliancePercentage; }
    public void setSlaCompliancePercentage(double slaCompliancePercentage) { this.slaCompliancePercentage = slaCompliancePercentage; }

    public Map<String, Long> getOutagesByRegion() { return outagesByRegion; }
    public void setOutagesByRegion(Map<String, Long> outagesByRegion) { this.outagesByRegion = outagesByRegion; }

    public Map<String, Long> getOutagesByService() { return outagesByService; }
    public void setOutagesByService(Map<String, Long> outagesByService) { this.outagesByService = outagesByService; }
}
