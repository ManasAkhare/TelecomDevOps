package com.telecom.outage.service;

import com.telecom.outage.model.*;
import com.telecom.outage.repository.OutageRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class OutageService {
    private final OutageRepository outageRepository;

    public OutageService(OutageRepository outageRepository) {
        this.outageRepository = outageRepository;
    }

    public List<Outage> getAllOutages() {
        return outageRepository.findAll();
    }

    public Optional<Outage> getOutageById(String id) {
        return outageRepository.findById(id);
    }

    public Outage createOutage(Outage outage) {
        if (outage.getReportedAt() == null) {
            outage.setReportedAt(LocalDateTime.now());
        }
        return outageRepository.save(outage);
    }

    public Optional<Outage> updateOutageStatus(String id, OutageStatus status, String notes) {
        Optional<Outage> existing = outageRepository.findById(id);
        if (existing.isPresent()) {
            Outage outage = existing.get();
            outage.setStatus(status);
            if (notes != null && !notes.isBlank()) {
                outage.setNotes((outage.getNotes() == null ? "" : outage.getNotes() + " | ") + notes);
            }
            if (status == OutageStatus.RESOLVED) {
                outage.setResolvedAt(LocalDateTime.now());
            }
            outageRepository.save(outage);
            return Optional.of(outage);
        }
        return Optional.empty();
    }

    public boolean deleteOutage(String id) {
        return outageRepository.deleteById(id);
    }

    public List<Outage> searchAndFilter(String query, String region,
                                         OutageSeverity severity, OutageStatus status,
                                         ServiceType serviceType) {
        return outageRepository.findAll().stream()
                .filter(o -> {
                    if (query != null && !query.isBlank()) {
                        String q = query.toLowerCase();
                        boolean matchId = o.getId() != null && o.getId().toLowerCase().contains(q);
                        boolean matchTitle = o.getTitle() != null && o.getTitle().toLowerCase().contains(q);
                        boolean matchCause = o.getRootCause() != null && o.getRootCause().toLowerCase().contains(q);
                        boolean matchRegion = o.getRegion() != null && o.getRegion().toLowerCase().contains(q);
                        if (!matchId && !matchTitle && !matchCause && !matchRegion) {
                            return false;
                        }
                    }
                    if (region != null && !region.isBlank() && !"ALL".equalsIgnoreCase(region)) {
                        if (o.getRegion() == null || !o.getRegion().equalsIgnoreCase(region)) {
                            return false;
                        }
                    }
                    if (severity != null && o.getSeverity() != severity) {
                        return false;
                    }
                    if (status != null && o.getStatus() != status) {
                        return false;
                    }
                    if (serviceType != null && o.getServiceType() != serviceType) {
                        return false;
                    }
                    return true;
                })
                .collect(Collectors.toList());
    }

    public List<Outage> getCriticalAlerts() {
        return outageRepository.findAll().stream()
                .filter(Outage::isCriticalException)
                .collect(Collectors.toList());
    }

    public DashboardMetrics getDashboardMetrics() {
        List<Outage> all = outageRepository.findAll();
        DashboardMetrics metrics = new DashboardMetrics();

        long total = all.size();
        long active = all.stream().filter(o -> o.getStatus() != OutageStatus.RESOLVED).count();
        long critical = all.stream().filter(Outage::isCriticalException).count();
        long resolved = all.stream().filter(o -> o.getStatus() == OutageStatus.RESOLVED).count();
        long impactedSubscribers = all.stream()
                .filter(o -> o.getStatus() != OutageStatus.RESOLVED)
                .mapToLong(Outage::getAffectedSubscribers)
                .sum();

        metrics.setTotalOutages(total);
        metrics.setActiveOutages(active);
        metrics.setCriticalAlerts(critical);
        metrics.setResolvedOutages(resolved);
        metrics.setTotalImpactedSubscribers(impactedSubscribers);
        metrics.setMeanTimeToResolutionHours(1.85); // Benchmark MTTR
        metrics.setSlaCompliancePercentage(94.2);

        Map<String, Long> byRegion = all.stream()
                .filter(o -> o.getRegion() != null)
                .collect(Collectors.groupingBy(Outage::getRegion, Collectors.counting()));
        metrics.setOutagesByRegion(byRegion);

        Map<String, Long> byService = all.stream()
                .filter(o -> o.getServiceType() != null)
                .collect(Collectors.groupingBy(o -> o.getServiceType().name(), Collectors.counting()));
        metrics.setOutagesByService(byService);

        return metrics;
    }
}
