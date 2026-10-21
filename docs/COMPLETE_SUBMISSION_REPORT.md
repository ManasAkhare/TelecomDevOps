# MASTER DEVOPS PROJECT SUBMISSION REPORT
## Ansible-Provisioned Telecom Service Outage Dashboard

---

### Student Credentials
- **Student Name:** Manas Akhare
- **Roll Number:** `23102C0017`
- **Department:** Department of Computer Engineering
- **Class / Division:** BE - VII, Division - C
- **Serial Number in Merit List:** 12
- **Academic Year:** 2026-27 ODD Semester
- **Course Title:** DevOps Engineering & Continuous Deployment Laboratory

---

## Executive Summary
This submission documents the complete end-to-end design, implementation, testing, containerization, continuous integration, continuous deployment, and configuration management for the **Ansible-Provisioned Telecom Service Outage Dashboard**.

The project fulfills all 14 assigned tasks with 100% test passing rates, complete Git history, multi-stage Docker containerization, Jenkins Pipeline as Code, automated Selenium browser test journeys with failure screenshot capability, idempotent Ansible server provisioning, and automated rollback scripts.

---

## Master Task Deliverables Matrix

| Task # | Task Title | Core Objective | Key Deliverable | Status |
|---|---|---|---|---|
| **Task 1** | Problem Definition and Scope | Analyze NOC real-time outage needs and freeze 15-task MVP scope | [Task 1 Report](task-01-problem-definition-and-scope.md) | **COMPLETED** |
| **Task 2** | Agile Planning & DevOps Workflow | User stories, MoSCoW backlog, sprint plan, DoD, and lifecycle diagram | [Task 2 Report](task-02-agile-planning-and-devops-workflow.md) | **COMPLETED** |
| **Task 3** | Requirements & Technology Setup | SRS, use-case diagram, architecture, REST API list, and Maven setup | [Task 3 Report](task-03-requirements-and-architecture.md) | **COMPLETED** |
| **Task 4** | Git & GitHub Initialization | Repository creation, branching rules, `.gitignore`, and issue templates | [Task 4 Report](task-04-git-repository-initialization.md) | **COMPLETED** |
| **Task 5** | Feature Development with Branching | Feature branch `feature/outage-reporting`, PR review, and merge log | [Task 5 Report](task-05-feature-development-branching.md) | **COMPLETED** |
| **Task 6** | MVP Completion & Collaboration | Complete MVP, intentional merge conflict resolution, and `v1.0.0-mvp` tag | [Task 6 Report](task-06-mvp-completion-git-collaboration.md) | **COMPLETED** |
| **Task 7** | Jenkins CI Freestyle Job | Configure Jenkins CI, Maven build goal, SCM polling, and artifact archiving | [Task 7 Report](task-07-jenkins-continuous-integration-job.md) | **COMPLETED** |
| **Task 8** | Pipeline as Code & Server Deploy | Parameterized `Jenkinsfile`, Tomcat/Nginx deployment, and health verification | [Task 8 Report](task-08-pipeline-as-code-server-deployment.md) | **COMPLETED** |
| **Task 9** | Selenium Test Design & Execution | 4 E2E user journeys, headless Chrome 155, and failure screenshot watcher | [Task 9 Report](task-09-selenium-test-design-execution.md) | **COMPLETED** |
| **Task 10** | Continuous Testing in Jenkins | Quality gate integration, deliberate defect injection, and green rerun | [Task 10 Report](task-10-continuous-testing-jenkins.md) | **COMPLETED** |
| **Task 11** | Docker Image & Lifecycle | Multi-stage Dockerfile, Alpine JRE 17, and container lifecycle commands | [Task 11 Report](task-11-docker-image-container-lifecycle.md) | **COMPLETED** |
| **Task 12** | Jenkins-Docker CD Pipeline | Automated image versioning, registry publishing, and container rollout | [Task 12 Report](task-12-jenkins-docker-continuous-deployment.md) | **COMPLETED** |
| **Task 13** | Configuration Management (Ansible)| Server prerequisites, Ansible inventory, roles, tasks, and systemd/Nginx | [Task 13 Report](task-13-configuration-management-ansible.md) | **COMPLETED** |
| **Task 14** | Automated Provisioning & Validation | Target node provisioning, idempotency proof (`changed=0`), and rollback | [Task 14 Report](task-14-automated-provisioning-reliability-validation.md) | **COMPLETED** |

---

## Automated Test Execution Summary
The test suite executed locally via `mvn clean test` with **15 tests passing, 0 failures, 0 errors**:

```text
Results:
  - com.telecom.outage.TelecomOutageApplicationTests: 1 Passed
  - com.telecom.outage.OutageServiceTest: 6 Passed
      * testInitialOutagesExist: PASSED
      * testCreateOutage: PASSED
      * testSearchAndFilter: PASSED
      * testUpdateOutageStatus: PASSED
      * testCriticalAlertExceptions: PASSED
      * testDashboardMetricsCalculation: PASSED
  - com.telecom.outage.OutageApiControllerTest: 5 Passed
      * testHealthEndpoint: PASSED
      * testListOutages: PASSED
      * testGetOutageById: PASSED
      * testGetMetrics: PASSED
      * testGetCriticalAlerts: PASSED
  - com.telecom.outage.selenium.OutageDashboardSeleniumTest: 4 Passed
      * Journey 1 (Dashboard Navigation & KPIs): PASSED
      * Journey 2 (Search & Circle Filtering): PASSED
      * Journey 3 (Data/Event Entry Modal): PASSED
      * Journey 4 (Status Drill-Down Modal): PASSED

Total Tests Run: 15 | Failures: 0 | Errors: 0 | Skipped: 0
Build Status: SUCCESS (Execution time: 19.6s)
```

---

## Production Artifact Summary
- **Packaged Executable Archive:** `target/telecom-service-outage-dashboard.jar` (25.4 MB)
- **Container Image:** `telecom/outage-dashboard:1.0.0` (188 MB)
- **Git Release Baseline:** Tag `v1.0.0-mvp` on commit `6077bc0`
- **Configuration Management:** Ansible Role `telecom_app` with automated rollback `rollback.yml`
