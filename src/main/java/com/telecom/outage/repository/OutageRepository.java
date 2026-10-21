package com.telecom.outage.repository;

import com.telecom.outage.model.Outage;
import com.telecom.outage.model.OutageSeverity;
import com.telecom.outage.model.OutageStatus;
import com.telecom.outage.model.ServiceType;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

@Repository
public class OutageRepository {
    private final Map<String, Outage> outageStore = new ConcurrentHashMap<>();
    private final AtomicLong idSequence = new AtomicLong(1000);

    public OutageRepository() {
        initSampleData();
    }

    private void initSampleData() {
        save(new Outage("OUT-1001", "Core Fiber Cut on BKC - Nariman Point Ring",
                ServiceType.BROADBAND_FIBER, OutageSeverity.CRITICAL, OutageStatus.INVESTIGATING,
                "Mumbai Metro", "TWR-MUM-104, TWR-MUM-108, TWR-MUM-115", 85000,
                "Underground Metro construction severed primary DWDM backbone fiber ring",
                "Manas Akhare (NOC Lead)", LocalDateTime.now().minusHours(1).minusMinutes(25), 180,
                "Emergency splice van dispatched. Optical bypass rerouted via secondary Western path."));

        save(new Outage("OUT-1002", "5G gNodeB Massive MIMO Sector Drop",
                ServiceType.CELLULAR_5G, OutageSeverity.MAJOR, OutageStatus.IDENTIFIED,
                "Delhi NCR", "TWR-DEL-401, TWR-DEL-402, TWR-DEL-409", 32000,
                "CPRI fronthaul link synchronization timeout following lightning surge",
                "Amitabh Sharma (RF Operations)", LocalDateTime.now().minusHours(2).minusMinutes(40), 120,
                "Baseband unit replacement initiated at Okhla primary data switch."));

        save(new Outage("OUT-1003", "VoLTE SIP Signaling Storm & Handover Glitch",
                ServiceType.VOLTE_CALLING, OutageSeverity.CRITICAL, OutageStatus.MONITORING,
                "Bangalore Circle", "TWR-BLR-012, TWR-BLR-045, TWR-BLR-088", 94000,
                "SBC capacity throttling due to peak-hour registration retry flood",
                "Priya Sundaram (Core IMS Engineer)", LocalDateTime.now().minusHours(3).minusMinutes(10), 90,
                "Session border controller rate-limit rule updated. Load shedding stabilized."));

        save(new Outage("OUT-1004", "4G LTE eNodeB Power Grid Blackout",
                ServiceType.CELLULAR_4G, OutageSeverity.MINOR, OutageStatus.IDENTIFIED,
                "Pune Circle", "TWR-PUN-203, TWR-PUN-205", 14500,
                "MSEDCL regional substation transformer overhaul; battery backup holding",
                "Rohan Kulkarni (Field Engineer)", LocalDateTime.now().minusMinutes(50), 240,
                "Mobile diesel generator unit arrived on site; fuel level adequate for 12 hours."));

        save(new Outage("OUT-1005", "Enterprise MPLS Leased Line Gateway Reset",
                ServiceType.ENTERPRISE_LEASED_LINE, OutageSeverity.MAJOR, OutageStatus.RESOLVED,
                "Hyderabad Cyberabad", "TWR-HYD-501, TWR-HYD-502", 18200,
                "BGP route flap following core router memory buffer congestion",
                "Karthik Raju (Enterprise TAC)", LocalDateTime.now().minusHours(5), 60,
                "BGP dampening configured and memory defragmented; traffic running normally."));
    }

    public List<Outage> findAll() {
        List<Outage> list = new ArrayList<>(outageStore.values());
        list.sort((a, b) -> b.getReportedAt().compareTo(a.getReportedAt()));
        return list;
    }

    public Optional<Outage> findById(String id) {
        return Optional.ofNullable(outageStore.get(id));
    }

    public synchronized Outage save(Outage outage) {
        if (outage.getId() == null || outage.getId().isBlank()) {
            outage.setId("OUT-" + idSequence.incrementAndGet());
        }
        if (outage.getReportedAt() == null) {
            outage.setReportedAt(LocalDateTime.now());
        }
        outageStore.put(outage.getId(), outage);
        return outage;
    }

    public boolean deleteById(String id) {
        return outageStore.remove(id) != null;
    }

    public long count() {
        return outageStore.size();
    }
}
