package com.telecom.outage.controller;

import com.telecom.outage.model.*;
import com.telecom.outage.service.OutageService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class OutageApiController {

    private final OutageService outageService;

    public OutageApiController(OutageService outageService) {
        this.outageService = outageService;
    }

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> health() {
        Map<String, Object> resp = new HashMap<>();
        resp.put("status", "UP");
        resp.put("service", "telecom-service-outage-dashboard");
        resp.put("version", "1.0.0-mvp");
        resp.put("author", "Manas Akhare (23102C0017)");
        resp.put("timestamp", System.currentTimeMillis());
        return ResponseEntity.ok(resp);
    }

    @GetMapping("/outages")
    public ResponseEntity<List<Outage>> listOutages(
            @RequestParam(required = false) String search,
            @RequestParam(required = false) String region,
            @RequestParam(required = false) OutageSeverity severity,
            @RequestParam(required = false) OutageStatus status,
            @RequestParam(required = false) ServiceType serviceType) {
        return ResponseEntity.ok(outageService.searchAndFilter(search, region, severity, status, serviceType));
    }

    @GetMapping("/outages/{id}")
    public ResponseEntity<Outage> getOutage(@PathVariable String id) {
        return outageService.getOutageById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/outages")
    public ResponseEntity<Outage> createOutage(@Valid @RequestBody Outage outage) {
        Outage created = outageService.createOutage(outage);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @PutMapping("/outages/{id}/status")
    public ResponseEntity<Outage> updateStatus(@PathVariable String id,
                                               @RequestParam OutageStatus status,
                                               @RequestParam(required = false) String notes) {
        return outageService.updateOutageStatus(id, status, notes)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/outages/{id}")
    public ResponseEntity<Map<String, String>> deleteOutage(@PathVariable String id) {
        boolean removed = outageService.deleteOutage(id);
        if (removed) {
            Map<String, String> resp = new HashMap<>();
            resp.put("message", "Outage " + id + " successfully deleted.");
            return ResponseEntity.ok(resp);
        }
        return ResponseEntity.notFound().build();
    }

    @GetMapping("/metrics")
    public ResponseEntity<DashboardMetrics> getMetrics() {
        return ResponseEntity.ok(outageService.getDashboardMetrics());
    }

    @GetMapping("/alerts")
    public ResponseEntity<List<Outage>> getCriticalAlerts() {
        return ResponseEntity.ok(outageService.getCriticalAlerts());
    }
}
