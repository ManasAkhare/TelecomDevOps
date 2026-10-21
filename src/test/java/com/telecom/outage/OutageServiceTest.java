package com.telecom.outage;

import com.telecom.outage.model.*;
import com.telecom.outage.repository.OutageRepository;
import com.telecom.outage.service.OutageService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Telecom Outage Service Unit Test Suite")
class OutageServiceTest {

    private OutageRepository repository;
    private OutageService outageService;

    @BeforeEach
    void setUp() {
        repository = new OutageRepository();
        outageService = new OutageService(repository);
    }

    @Test
    @DisplayName("Test 1: Verify Initial Preloaded Sample Outages")
    void testInitialOutagesExist() {
        List<Outage> list = outageService.getAllOutages();
        assertNotNull(list);
        assertTrue(list.size() >= 5, "Repository should contain initial sample data");
    }

    @Test
    @DisplayName("Test 2: Create New Telecom Outage Event")
    void testCreateOutage() {
        Outage outage = new Outage();
        outage.setTitle("Subsea Cable Fault Southern Link");
        outage.setServiceType(ServiceType.BROADBAND_FIBER);
        outage.setSeverity(OutageSeverity.CRITICAL);
        outage.setStatus(OutageStatus.INVESTIGATING);
        outage.setRegion("Chennai Circle");
        outage.setAffectedSubscribers(45000);
        outage.setRootCause("Shallow water anchor drag severed SMW-4 cable");
        outage.setReportedBy("Manas Akhare");

        Outage created = outageService.createOutage(outage);

        assertNotNull(created.getId());
        assertTrue(created.getId().startsWith("OUT-"));
        assertEquals("Subsea Cable Fault Southern Link", created.getTitle());

        Optional<Outage> fetched = outageService.getOutageById(created.getId());
        assertTrue(fetched.isPresent());
        assertEquals("Chennai Circle", fetched.get().getRegion());
    }

    @Test
    @DisplayName("Test 3: Search Outages by Keyword and Region")
    void testSearchAndFilter() {
        List<Outage> results = outageService.searchAndFilter("BKC", null, null, null, null);
        assertFalse(results.isEmpty());
        assertTrue(results.get(0).getTitle().contains("BKC"));

        List<Outage> mumbaiResults = outageService.searchAndFilter(null, "Mumbai Metro", null, null, null);
        assertFalse(mumbaiResults.isEmpty());
        assertEquals("Mumbai Metro", mumbaiResults.get(0).getRegion());
    }

    @Test
    @DisplayName("Test 4: Update Outage Status and Transition to Resolved")
    void testUpdateOutageStatus() {
        Optional<Outage> updated = outageService.updateOutageStatus("OUT-1001", OutageStatus.RESOLVED, "Splicing complete.");
        assertTrue(updated.isPresent());
        assertEquals(OutageStatus.RESOLVED, updated.get().getStatus());
        assertNotNull(updated.get().getResolvedAt());
    }

    @Test
    @DisplayName("Test 5: Verify Critical Alert Exception Filter")
    void testCriticalAlertExceptions() {
        List<Outage> alerts = outageService.getCriticalAlerts();
        assertNotNull(alerts);
        for (Outage a : alerts) {
            assertEquals(OutageSeverity.CRITICAL, a.getSeverity());
            assertNotEquals(OutageStatus.RESOLVED, a.getStatus());
        }
    }

    @Test
    @DisplayName("Test 6: Verify Dashboard KPI Metrics Aggregation")
    void testDashboardMetricsCalculation() {
        DashboardMetrics metrics = outageService.getDashboardMetrics();
        assertNotNull(metrics);
        assertTrue(metrics.getTotalOutages() >= 5);
        assertTrue(metrics.getActiveOutages() >= 1);
        assertTrue(metrics.getTotalImpactedSubscribers() > 0);
        assertTrue(metrics.getSlaCompliancePercentage() > 80.0);
    }
}
