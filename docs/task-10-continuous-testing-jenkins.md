# Task 10: Continuous Testing in Jenkins
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Jenkins Continuous Testing Integration
The Selenium WebDriver test suite was integrated as a mandatory automated quality gate in the Jenkins CI/CD pipeline:
- **XML Test Report Ingestion:** Jenkins parses `target/surefire-reports/*.xml` using the JUnit Test Result Archiver.
- **Strict Quality Gate:** If any unit or Selenium test fails, the build status is marked as `FAILURE` and downstream deployment stages (Docker build and Ansible server provisioning) are blocked automatically.

---

## 2. Deliberately Introduced Defect Scenario
To validate that the pipeline strictly prevents defective code from reaching staging/production environments, a defect was deliberately introduced:
- **Defect Injection:** In `dashboard.html`, the element ID for `#searchInput` was altered to `#brokenSearchField`.
- **Expected Consequence:** Journey 2 in `OutageDashboardSeleniumTest` (`testSearchAndFilterOutages`) will fail with `NoSuchElementException: Unable to locate element: #searchInput`.
- **Pipeline Behavior:** The Jenkins pipeline must halt at Stage 3, record test failure telemetry, and refuse to package or deploy the application.

---

## 3. Failed Pipeline Evidence (Build #2 Log)
```text
[Pipeline] stage
[Pipeline] { (3. Continuous Testing: Selenium E2E)
--> Stage 3: Executing Headless Selenium WebDriver User Journey Tests...
[telecom-service-outage-dashboard] $ mvn test -Dtest=OutageDashboardSeleniumTest
[INFO] Running com.telecom.outage.selenium.OutageDashboardSeleniumTest
[JOURNEY 1 PASSED] Active Outages: 4 | Critical: 2
[ERROR]   OutageDashboardSeleniumTest.testSearchAndFilterOutages:98 » NoSuchElement no such element: Unable to locate element: {"method":"css selector","selector":"#searchInput"}
[INFO] Tests run: 4, Failures: 0, Errors: 1, Skipped: 0, Time elapsed: 6.812 s <<< FAILURE!
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[Pipeline] junit
Recording test results
[JUnit] Processing target/surefire-reports/TEST-com.telecom.outage.selenium.OutageDashboardSeleniumTest.xml
[JUnit] Test result: 1 test failed (testSearchAndFilterOutages).
--> CRITICAL: Selenium Test Suite Failed! Halting deployment pipeline to safeguard production SLA.
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage (4. Package Artifact) - SKIPPED DUE TO QUALITY GATE
[Pipeline] stage (5. Docker Image Build) - SKIPPED DUE TO QUALITY GATE
[Pipeline] stage (6. Ansible Target Provisioning) - SKIPPED DUE TO QUALITY GATE
==========================================================
 PIPELINE FAILED: Rollback Playbook Trigger Recommended
 Notification dispatched to: xmanasakhare@gmail.com
==========================================================
ERROR: script returned exit code 1
Finished: FAILURE
```

---

## 4. Defect Correction & Git Commit
The issue was identified from the failure report and corrected:
- The element ID was restored to `#searchInput`.
- Added defensive `WebDriverWait` check in the Selenium test script.

```bash
$ git add src/main/resources/templates/dashboard.html
$ git commit -m "fix(ui): restore correct element id #searchInput and resolve Selenium journey failure"
[develop 81a94b2] fix(ui): restore correct element id #searchInput and resolve Selenium journey failure
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git push origin develop
```

---

## 5. Successful Jenkins Rerun Evidence (Build #3 Log)
Following the bug fix commit, the Jenkins pipeline was re-triggered via SCM polling:

```text
Started by SCM change (commit 81a94b2 by Manas Akhare)
[Pipeline] { (2. Maven Compile & Unit Test)
[INFO] Tests run: 12, Failures: 0, Errors: 0, Skipped: 0
[Pipeline] }
[Pipeline] { (3. Continuous Testing: Selenium E2E)
--> Stage 3: Executing Headless Selenium WebDriver User Journey Tests...
[JOURNEY 1 PASSED] Active Outages: 4 | Critical: 2
[JOURNEY 2 PASSED] Real-time filtering verified for keyword 'BKC'.
[JOURNEY 3 PASSED] Successfully logged new outage event through UI form.
[JOURNEY 4 PASSED] Status Drill-down modal inspected for: OUT-1004
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
[JUnit] Recording test results: 0 test failures, 16 tests passing.
[Pipeline] }
[Pipeline] { (4. Package Artifact)
[INFO] Building jar: target/telecom-service-outage-dashboard.jar
[INFO] BUILD SUCCESS
[Pipeline] }
[Pipeline] { (5. Docker Image Build & Tag)
Successfully built telecom/outage-dashboard:3
[Pipeline] }
[Pipeline] { (6. Ansible Target Provisioning & Deployment)
localhost                  : ok=14   changed=1    unreachable=0    failed=0
[Pipeline] }
[Pipeline] { (7. Health-Check & Smoke Validation)
HTTP/1.1 200 OK {"status":"UP","service":"telecom-service-outage-dashboard","author":"Manas Akhare (23102C0017)"}
[Pipeline] }
==========================================================
 PIPELINE SUCCEEDED: Telecom Service Outage Dashboard
 Student: Manas Akhare (Roll: 23102C0017)
 Deployed to: production on Port: 8080
==========================================================
Finished: SUCCESS
```
The automated pipeline proved that defective code cannot penetrate past the testing phase, validating continuous testing robustness.
