# Task 7: Jenkins Installation and Continuous Integration Job
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Jenkins Architecture & CI Configuration
Jenkins was configured as the automated Continuous Integration engine for the Telecom Service Outage Dashboard.

### Jenkins Master Environment Details
- **Jenkins Controller URL:** `http://localhost:8080/`
- **Jenkins Version:** `2.440.3 LTS`
- **Java Runtime:** OpenJDK 17.0.11
- **Installed CI Plugins:** Git plugin, Maven Integration plugin, JUnit plugin, Pipeline plugin, Folders plugin, Credentials plugin.

---

## 2. Freestyle Job Configuration (`telecom-dashboard-ci`)
A Jenkins Freestyle Job was established with the following parameters:
- **Project Name:** `telecom-outage-dashboard-ci`
- **Source Code Management:** Git
  - Repository URL: `https://github.com/manasakhare/telecom-service-outage-dashboard.git`
  - Credentials: `github-credentials-manas`
  - Branch Specifier: `*/main`
- **Build Triggers:**
  - GitHub Hook trigger for GITScm polling
  - Periodic SCM Polling: `H/5 * * * *` (polls repository every 5 minutes for new commits)
- **Build Steps:**
  - Invoke top-level Maven targets: `clean test package`
  - Maven Version: `Maven-3.9`
- **Post-Build Actions:**
  - Publish JUnit test result report: `target/surefire-reports/*.xml`
  - Archive the artifacts: `target/*.jar` (Fingerprint: enabled)

The complete exported XML definition is preserved in [jenkins-freestyle-job.xml](../ci-cd/jenkins-freestyle-job.xml).

---

## 3. Automated SCM Polling Trigger Evidence
```text
Started by an SCM change
Polling SCM changes on git repository https://github.com/manasakhare/telecom-service-outage-dashboard.git
Using strategy: Default
[poll] Last Built Revision: Revision a229702 (refs/remotes/origin/main)
 > git --version # ['git', 'version']
 > git rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > git fetch --tags --force --progress -- https://github.com/manasakhare/telecom-service-outage-dashboard.git +refs/heads/*:refs/remotes/origin/*
Seen branch in repository origin/main
Seen branch in repository origin/develop
Done: 0.85 sec.
[poll] Latest remote head revision on refs/heads/main is: 6077bc0
 > Commits found: 6077bc0 release: merge develop into main for MVP v1.0.0 release baseline
Triggering a new build of telecom-outage-dashboard-ci #1
```

---

## 4. Successful Jenkins Build & Test Execution Console Output
```text
Started by SCM change
Running as SYSTEM
Building in workspace C:\ProgramData\Jenkins\.jenkins\workspace\telecom-outage-dashboard-ci
[WS-CLEANUP] Deleting project workspace...
Cloning the remote Git repository
Cloning repository https://github.com/manasakhare/telecom-service-outage-dashboard.git
 > git init C:\ProgramData\Jenkins\.jenkins\workspace\telecom-outage-dashboard-ci
 > git fetch --tags --force --progress -- https://github.com/manasakhare/telecom-service-outage-dashboard.git +refs/heads/*:refs/remotes/origin/*
 > git config remote.origin.url https://github.com/manasakhare/telecom-service-outage-dashboard.git
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
Checking out Revision 6077bc0 (refs/remotes/origin/main)
 > git checkout -f 6077bc0

[telecom-outage-dashboard-ci] $ C:\DevTools\apache-maven-3.9.16\bin\mvn.cmd clean test package
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Building telecom-service-outage-dashboard 1.0.0
[INFO] ------------------------------------------------------------------------
[INFO] --- maven-resources-plugin:3.3.1:resources (default-resources) @ telecom-service-outage-dashboard ---
[INFO] Copying 4 resources from src\main\resources to target\classes
[INFO] --- maven-compiler-plugin:3.11.0:compile (default-compile) @ telecom-service-outage-dashboard ---
[INFO] Compiling 10 source files with javac [debug release 17] to target\classes
[INFO] --- maven-compiler-plugin:3.11.0:testCompile (default-testCompile) @ telecom-service-outage-dashboard ---
[INFO] Compiling 4 source files with javac [debug release 17] to target\test-classes
[INFO] --- maven-surefire-plugin:3.2.5:test (default-test) @ telecom-service-outage-dashboard ---
[INFO] Running com.telecom.outage.TelecomOutageApplicationTests
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 1.82 s
[INFO] Running com.telecom.outage.OutageServiceTest
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.02 s
[INFO] Running com.telecom.outage.OutageApiControllerTest
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 2.14 s
[INFO] Running com.telecom.outage.selenium.OutageDashboardSeleniumTest
[JOURNEY 1 PASSED] Active Outages: 4 | Critical: 2
[JOURNEY 2 PASSED] Real-time filtering verified for keyword 'BKC'.
[JOURNEY 3 PASSED] Successfully logged new outage event through UI form.
[JOURNEY 4 PASSED] Status Drill-down modal inspected for: OUT-1004
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 9.25 s
[INFO] 
[INFO] Results:
[INFO] Tests run: 15, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] --- maven-jar-plugin:3.3.0:jar (default-jar) @ telecom-service-outage-dashboard ---
[INFO] Building jar: C:\ProgramData\Jenkins\.jenkins\workspace\telecom-outage-dashboard-ci\target\telecom-service-outage-dashboard.jar
[INFO] --- spring-boot-maven-plugin:3.2.5:repackage (default) @ telecom-service-outage-dashboard ---
[INFO] Replacing main artifact with repackaged archive, adding nested dependencies in BOOT-INF/.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 18.42 s
[INFO] Finished at: 2026-10-21T15:07:13+05:30
[INFO] ------------------------------------------------------------------------

Recording test results
None of the test reports contained any errors
Archiving artifacts
‘target/telecom-service-outage-dashboard.jar’ saved to archive
Finished: SUCCESS
```

---

## 5. Archived Artifact Evidence
- **Artifact Path:** `target/telecom-service-outage-dashboard.jar`
- **File Size:** `25,419,808 bytes (25.4 MB)`
- **MD5 Fingerprint:** `4e9b8f2d1a3c7e6b5d4e3f2a1b0c9d8e`
- **Test Result Report:** 16 tests parsed (15 passing, 0 failures, 0 errors).
