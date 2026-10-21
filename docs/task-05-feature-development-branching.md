# Task 5: Feature Development with Branching
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Feature 1 Specification: Outage SLA Countdown & Breach Telemetry
The first core feature branch was established to implement the **Outage SLA Countdown and Automated Breach Detection Mechanism** in the domain layer. 

### Key Capabilities Implemented:
- Calculation of dynamic elapsed incident time vs. carrier SLA threshold (`getRemainingSlaMinutes()`).
- Automated boolean flag detecting SLA threshold breach (`isSlaBreached()`).
- High-impact subscriber breach flag (`isHighImpact()`) for incidents impacting \(\ge 25,000\) subscribers.

---

## 2. Feature Branching Execution Log

```bash
# 1. Ensure develop branch is up to date and create feature branch
$ git checkout develop
Switched to branch 'develop'

$ git checkout -b feature/outage-reporting
Switched to a new branch 'feature/outage-reporting'

# 2. Implement the SLA telemetry enhancements in src/main/java/com/telecom/outage/model/Outage.java
$ git status
On branch feature/outage-reporting
Changes not staged for commit:
  modified:   src/main/java/com/telecom/outage/model/Outage.java

# 3. Stage changes and commit using conventional commits
$ git add src/main/java/com/telecom/outage/model/Outage.java
$ git commit -m "feat(outage-reporting): add real-time SLA countdown telemetry and breach detection indicators"
[feature/outage-reporting c171078] feat(outage-reporting): add real-time SLA countdown telemetry and breach detection indicators
 1 file changed, 13 insertions(+)
```

---

## 3. Pull Request Simulation & Code Review Comments

### Pull Request Metadata
- **PR Title:** `[PR #1]: SLA Telemetry and Real-Time Breach Detection Core`
- **Source Branch:** `feature/outage-reporting`
- **Target Branch:** `develop`
- **Author:** `Manas Akhare (23102C0017)`
- **Reviewer:** `Senior NOC Architect / Tech Lead`
- **Status:** **APPROVED & MERGED**

### Code Review Log
> **Reviewer Comment (Line 120, `Outage.java`):**  
> *"Good implementation of `Duration.between`. Ensure `Math.max(0, ...)` is used so remaining SLA does not return negative values once an incident breaches the threshold."*  
>  
> **Author Reply (Manas Akhare):**  
> *"Confirmed. `Math.max(0, slaTargetMinutes - elapsedMinutes)` prevents negative counters and accurately preserves SLA breach status until transitioned to RESOLVED."*  
>  
> **Reviewer Decision:**  
> *"Unit tests in `OutageServiceTest` verify positive elapsed durations and threshold handling. Clean implementation, approving for merge."*

---

## 4. Merge Evidence into `develop`

```bash
# 4. Switch back to develop branch and execute non-fast-forward merge
$ git checkout develop
Switched to branch 'develop'

$ git merge --no-ff feature/outage-reporting -m "Merge pull request #1 from feature/outage-reporting - SLA telemetry and reporting core"
Merge made by the 'ort' strategy.
 src/main/java/com/telecom/outage/model/Outage.java | 13 +++++++++++++
 1 file changed, 13 insertions(+)

# 5. Review branch log
$ git log -n 3 --oneline
3e722b6 Merge pull request #1 from feature/outage-reporting - SLA telemetry and reporting core
c171078 feat(outage-reporting): add real-time SLA countdown telemetry and breach detection indicators
cd49244 feat(core): setup application architecture, domain models, services, and infrastructure manifests
```
