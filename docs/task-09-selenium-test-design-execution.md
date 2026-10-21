# Task 9: Selenium Test Design and Local Execution
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Selenium Automated Test Plan
To validate end-user workflows and ensure regression prevention across automated releases, an automated Selenium WebDriver suite was constructed in Java using JUnit 5 Jupiter and Google Chrome in headless mode (`--headless=new`).

### Four Critical User Journeys Tested:
| Journey # | Target Workflow | Test Objective | Validation Criteria |
|---|---|---|---|
| **Journey 1** | Dashboard Navigation & KPI Indicators | Verify page loads, title matches NOC branding, and KPI metric values (active outages, critical alerts, impacted subscribers) render correctly. | `driver.getTitle()` equals expected title; `#kpiActiveOutages` is non-empty. |
| **Journey 2** | Real-time Search & Circle Filtering | Simulate user typing query "BKC" in `#searchInput`. Verify table filters down immediately to matching incidents. | Table body contains "OUT-1001" and "BKC". |
| **Journey 3** | Data/Event Entry & Form Submission | Click "+ Log Outage Event", fill modal form with test incident details (Title, Circle, Subscribers, Towers, Cause), and click Submit. | Form posts, page reloads, and `#successBanner` displays confirmation message. |
| **Journey 4** | Status Drill-Down Diagnostics | Click on incident row (`.outage-row`), open `#drillDownModal`, and verify tower badges and root cause text render accurately. | Modal is displayed; `#modalDrillDownId` contains valid ID; tower pills rendered. |

---

## 2. Selenium WebDriver Implementation Code
The complete implementation is preserved in [OutageDashboardSeleniumTest.java](../src/test/java/com/telecom/outage/selenium/OutageDashboardSeleniumTest.java).

Key architectural features of the test suite:
- **Spring Boot Random Port Binding:** `@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)` prevents local port conflicts by dynamically allocating an unused port.
- **Headless Chrome 155 Execution:** Configured with `--headless=new`, `--no-sandbox`, `--disable-dev-shm-usage`, and `--remote-allow-origins=*` to run headlessly in CI/CD environments.
- **Explicit Synchronization Waits:** `WebDriverWait` used with `ExpectedConditions` to avoid race conditions.

---

## 3. Automated Failure Screenshot Capture Mechanism
The test suite implements the JUnit 5 `TestWatcher` extension (`ScreenshotOnFailureExtension`). When any assertion or element lookup fails, the extension automatically intercepts the event, captures the browser viewport using `TakesScreenshot`, and writes the image to `target/screenshots/{testName}_failure.png`.

```java
public static class ScreenshotOnFailureExtension implements TestWatcher {
    @Override
    public void testFailed(ExtensionContext context, Throwable cause) {
        if (driver instanceof TakesScreenshot) {
            try {
                byte[] screenshotBytes = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
                Files.createDirectories(Paths.get("target/screenshots"));
                String filePath = "target/screenshots/" + context.getDisplayName().replaceAll("[^a-zA-Z0-9.-]", "_") + "_failure.png";
                try (FileOutputStream fos = new FileOutputStream(filePath)) {
                    fos.write(screenshotBytes);
                }
                System.err.println("[SELENIUM SCREENSHOT] Captured failure screenshot to: " + filePath);
            } catch (IOException e) {
                System.err.println("Failed to write screenshot: " + e.getMessage());
            }
        }
    }
}
```

---

## 4. Local Test Execution Report (`mvn test`)
Execution of the complete test suite via Maven produced the following console output:

```text
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.telecom.outage.OutageApiControllerTest
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 4.375 s -- in com.telecom.outage.OutageApiControllerTest
[INFO] Running com.telecom.outage.OutageServiceTest
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.015 s -- in com.telecom.outage.OutageServiceTest
[INFO] Running com.telecom.outage.selenium.OutageDashboardSeleniumTest
2026-10-21T15:06:40.030+05:30  INFO 13848 --- [telecom-service-outage-dashboard] [main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 53560 (http) with context path ''
[JOURNEY 1 PASSED] Active Outages: 4 | Critical: 2
[JOURNEY 2 PASSED] Real-time filtering verified for keyword 'BKC'.
[JOURNEY 3 PASSED] Successfully logged new outage event through UI form.
[JOURNEY 4 PASSED] Status Drill-down modal inspected for: OUT-1004
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 9.257 s -- in com.telecom.outage.selenium.OutageDashboardSeleniumTest
[INFO] 
[INFO] Results:
[INFO] 
[INFO] Tests run: 15, Failures: 0, Errors: 0, Skipped: 0
[INFO] 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  19.606 s
[INFO] Finished at: 2026-10-21T15:06:48+05:30
[INFO] ------------------------------------------------------------------------
```
All 4 user journeys and 11 unit/API tests executed with **0 failures and 0 errors**.
