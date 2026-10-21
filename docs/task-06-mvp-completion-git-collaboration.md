# Task 6: MVP Completion and Git Collaboration
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Functional MVP Completion Verification
The complete MVP scope for the Telecom Service Outage Dashboard was finalized, fulfilling all required modules:
1. **Data/Event Entry:** Modal form with validation for logging incidents directly into the NOC queue.
2. **Searchable Dashboard:** Sub-second client-side and server-side filtering across IDs, titles, causes, and circles.
3. **Summary Indicators:** Dynamic KPI cards for Active Incidents, Critical P1 Alerts, Affected Subscribers, MTTR, and SLA Compliance.
4. **Status Drill-Down:** Deep diagnostic modal showing cell towers, outage root-cause analysis, and lifecycle status transition selector.
5. **Alert / Exception View:** Prominent emergency alert card highlighting unmitigated P1 critical carrier faults.

---

## 2. Second Feature Branch & Intentional Conflict Creation
To demonstrate production-grade Git collaboration, a second feature branch `feature/alert-management` was established to configure alert thresholds. A concurrent change was introduced to the same file (`application.properties`) on the `develop` integration branch.

### Step 2.1: Commit on `feature/alert-management`
```bash
$ git checkout -b feature/alert-management
Switched to a new branch 'feature/alert-management'

# Configured 25,000 subscriber threshold & emergency matrix channel
$ git add src/main/resources/application.properties
$ git commit -m "feat(alert-management): configure emergency matrix escalation channel and 25k threshold"
[feature/alert-management 1a04418] feat(alert-management): configure emergency matrix escalation channel and 25k threshold
 1 file changed, 5 insertions(+)
```

### Step 2.2: Concurrent Commit on `develop`
```bash
$ git checkout develop
Switched to branch 'develop'

# Concurrently configured 20,000 threshold & slack dispatch channel
$ git add src/main/resources/application.properties
$ git commit -m "feat(config): configure slack dispatch channel with 20k threshold on develop"
[develop ceb86ae] feat(config): configure slack dispatch channel with 20k threshold on develop
 1 file changed, 5 insertions(+)
```

---

## 3. Merge Conflict Trigger and Evidence
When attempting to merge `feature/alert-management` into `develop`, Git detected conflicting modifications on lines 11–17:

```bash
$ git merge feature/alert-management
Auto-merging src/main/resources/application.properties
CONFLICT (content): Merge conflict in src/main/resources/application.properties
Automatic merge failed; fix conflicts and then commit the result.
```

### Raw Conflict Markers (`git diff`):
```diff
diff --cc src/main/resources/application.properties
index 8c0aff0,aceab95..0000000
--- a/src/main/resources/application.properties
+++ b/src/main/resources/application.properties
@@@ -9,7 -9,7 +9,14 @@@ management.endpoint.health.show-details
  logging.level.com.telecom.outage=INFO
  logging.level.org.springframework.web=INFO
  
++<<<<<<< HEAD
 +# Alert Threshold Configuration (Develop Branch Integration)
 +telecom.alert.critical-threshold=20000
 +telecom.alert.escalation-channel=noc-slack-ops-dispatch
 +telecom.alert.monitoring-interval-seconds=30
++=======
+ # Alert Threshold Configuration (Feature Alert Management Branch)
+ telecom.alert.critical-threshold=25000
+ telecom.alert.escalation-channel=noc-emergency-matrix
+ telecom.alert.auto-escalate=true
++>>>>>>> feature/alert-management
```

---

## 4. Conflict Resolution Strategy & Execution
The conflict was resolved through architectural harmonization:
- The stricter threshold of `20000` subscribers from `develop` was retained.
- The dual escalation channels (`noc-slack-ops-dispatch,noc-emergency-matrix`) were merged to ensure redundancy.
- Both `monitoring-interval-seconds=30` and `auto-escalate=true` flags were included.

### Resolved Content (`application.properties`):
```properties
# Resolved & Unified Alert Configuration (Harmonized Post-Conflict)
telecom.alert.critical-threshold=20000
telecom.alert.escalation-channel=noc-slack-ops-dispatch,noc-emergency-matrix
telecom.alert.monitoring-interval-seconds=30
telecom.alert.auto-escalate=true
```

### Staging and Committing Resolution:
```bash
$ git add src/main/resources/application.properties
$ git commit -m "fix(merge): resolve configuration conflict between develop and feature/alert-management"
[develop d5ef0bd] fix(merge): resolve configuration conflict between develop and feature/alert-management
```

---

## 5. Release Tagging and Production Baseline
The stabilized `develop` branch was merged into `main` and tagged as official MVP release `v1.0.0-mvp`:

```bash
$ git checkout main
Switched to branch 'main'

$ git merge --no-ff develop -m "release: merge develop into main for MVP v1.0.0 release baseline"
Merge made by the 'ort' strategy.

$ git tag -a v1.0.0-mvp -m "Release MVP v1.0.0: Ansible-Provisioned Telecom Service Outage Dashboard"
$ git tag -l -n3
v1.0.0-mvp      Release MVP v1.0.0: Ansible-Provisioned Telecom Service Outage Dashboard
```

### Complete Git Network Graph:
```text
*   6077bc0 (HEAD -> main, tag: v1.0.0-mvp) release: merge develop into main for MVP v1.0.0 release baseline
|\  
| *   d5ef0bd (develop) fix(merge): resolve configuration conflict between develop and feature/alert-management
| |\  
| | * 1a04418 (feature/alert-management) feat(alert-management): configure emergency matrix escalation channel and 25k threshold
| * | ceb86ae feat(config): configure slack dispatch channel with 20k threshold on develop
| |/  
| *   3e722b6 Merge pull request #1 from feature/outage-reporting - SLA telemetry and reporting core
| |\  
| | * c171078 (feature/outage-reporting) feat(outage-reporting): add real-time SLA countdown telemetry and breach detection indicators
| |/  
| * cd49244 feat(core): setup application architecture, domain models, services, and infrastructure manifests
|/  
* a229702 chore(repo): initialize Telecom Outage Dashboard repository skeleton with Maven, .gitignore, and issue templates
```
