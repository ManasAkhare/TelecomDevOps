# Ansible-Provisioned Telecom Service Outage Dashboard
> **BE Computer Engineering - Semester VII (Academic Year 2026-27 ODD Sem)**  
> **Student Name:** Manas Akhare  
> **Roll Number:** `23102C0017`  
> **Division:** BE CMPN - C | **Serial No:** 12  
> **Course:** DevOps Lab & Continuous Engineering  

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/manasakhare/telecom-service-outage-dashboard)
[![Tests Run](https://img.shields.io/badge/tests-15%20passed-success)](https://github.com/manasakhare/telecom-service-outage-dashboard)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com)
[![Ansible](https://img.shields.io/badge/ansible-idempotent-red)](https://docs.ansible.com)
[![Java 17](https://img.shields.io/badge/java-17-orange)](https://openjdk.org)
[![Spring Boot](https://img.shields.io/badge/spring--boot-3.2.5-green)](https://spring.io)

---

## 1. Project Overview & Real-Time Need
The **Telecom Service Outage Dashboard** is a mission-critical Network Operations Center (NOC) platform engineered to monitor, track, escalate, and resolve telecommunications disruptions across major wireless and wireline services (5G Core, 4G LTE, FTTH Fiber Broadband, VoLTE Gateways, and Enterprise Leased Lines).

### Core MVP Capabilities
1. **Data/Event Entry:** Real-time ingestion of incident records including affected circles, impacted cell towers, and root cause.
2. **Searchable Dashboard:** Sub-second search and multi-dimensional filtering across circles, severities, and lifecycle states.
3. **Summary Indicators (KPIs):** Real-time aggregation of active incidents, P1 critical outages, impacted subscriber counts, MTTR, and carrier SLA compliance.
4. **Status Drill-Down:** Deep diagnostic view of cellular towers, engineering dispatch logs, and state-machine transitions.
5. **Alert / Exception View:** High-visibility banner and exception queue for critical threshold breaches and SLA escalations.

---

## 2. Technology Stack & DevOps Toolchain
| Layer | Technology |
|---|---|
| **Programming Language** | Java 17 LTS (JetBrains OpenJDK 17.0.11) |
| **Application Framework** | Spring Boot 3.2.5 (Embedded Apache Tomcat 10.1) |
| **Frontend UI** | Thymeleaf 3, Modern HTML5, Responsive CSS3 Grid/Flexbox, Vanilla JS |
| **Build & Dependency Tool** | Apache Maven 3.9.16 |
| **Unit & Integration Testing** | JUnit 5 Jupiter, MockMvc, AssertJ |
| **Continuous UI / E2E Testing**| Selenium WebDriver 4.18.1 (Headless Google Chrome 155) |
| **Version Control System** | Git 2.54.0 with Feature Branching, PR Workflow & Conflict Resolution |
| **Continuous Integration (CI)**| Jenkins 2.x (Freestyle CI Job + Jenkinsfile Declarative Pipeline) |
| **Containerization** | Docker Engine (Multi-stage JRE 17 Alpine Image, Docker Compose) |
| **Configuration Management** | Ansible 2.x (Idempotent Playbooks, Jinja2 Templates, Rollback Suite) |
| **Reverse Proxy & Web Server** | Nginx Reverse Proxy with proxy caching and gzip compression |

---

## 3. Directory Layout
```text
DevOps/
├── pom.xml                               # Maven project descriptor & build configuration
├── README.md                             # Comprehensive project documentation
├── .gitignore                            # Version control exclusion rules
├── src/
│   ├── main/
│   │   ├── java/com/telecom/outage/
│   │   │   ├── TelecomOutageApplication.java    # Spring Boot application entry point
│   │   │   ├── controller/
│   │   │   │   ├── OutageController.java        # UI Web view controller (Thymeleaf)
│   │   │   │   └── OutageApiController.java     # REST API & Health Check endpoints
│   │   │   ├── model/
│   │   │   │   ├── Outage.java                  # Outage incident domain model
│   │   │   │   ├── OutageSeverity.java          # CRITICAL, MAJOR, MINOR enums
│   │   │   │   ├── OutageStatus.java            # INVESTIGATING, IDENTIFIED, etc.
│   │   │   │   ├── ServiceType.java             # 5G, 4G, Fiber, VoLTE, Enterprise
│   │   │   │   └── DashboardMetrics.java        # KPI aggregator entity
│   │   │   ├── repository/
│   │   │   │   └── OutageRepository.java        # Thread-safe in-memory store
│   │   │   └── service/
│   │   │       └── OutageService.java           # Business logic & filter engine
│   │   └── resources/
│   │       ├── application.properties           # Configuration settings
│   │       ├── templates/
│   │       │   └── dashboard.html               # NOC Telemetry UI dashboard
│   │       └── static/
│   │           ├── css/styles.css               # Professional NOC dark theme styles
│   │           └── js/app.js                    # Client-side filtering & modal scripts
│   └── test/
│       └── java/com/telecom/outage/
│           ├── TelecomOutageApplicationTests.java # Context bootstrap validation
│           ├── OutageServiceTest.java           # Unit testing suite (6 tests)
│           ├── OutageApiControllerTest.java      # REST API MockMvc suite (5 tests)
│           └── selenium/
│               └── OutageDashboardSeleniumTest.java # Selenium E2E UI suite (4 journeys)
├── ci-cd/
│   ├── Jenkinsfile                       # Declarative CI/CD pipeline script
│   └── jenkins-freestyle-job.xml         # Jenkins XML configuration for CI job
├── docker/
│   ├── Dockerfile                        # Multi-stage production container build
│   ├── docker-compose.yml                # Microservices composition (App + Nginx)
│   └── .dockerignore                     # Docker build context exclusions
├── ansible/
│   ├── ansible.cfg                       # Ansible configuration
│   ├── inventory.ini                     # Multi-environment target inventory
│   ├── playbook.yml                      # Automated provisioning playbook
│   ├── rollback.yml                      # Automated rollback & recovery playbook
│   └── roles/telecom_app/                # Modular Ansible role
│       ├── tasks/main.yml                # Idempotent provisioning tasks
│       ├── vars/main.yml                 # Target variables
│       └── templates/                    # Jinja2 templates (Nginx & Systemd)
└── docs/                                 # Complete 14-Task Deliverable Documentation
    ├── task-01-problem-definition-and-scope.md
    ├── task-02-agile-planning-and-devops-workflow.md
    ├── task-03-requirements-and-architecture.md
    ├── task-04-git-repository-initialization.md
    ├── task-05-feature-development-branching.md
    ├── task-06-mvp-completion-git-collaboration.md
    ├── task-07-jenkins-continuous-integration-job.md
    ├── task-08-pipeline-as-code-server-deployment.md
    ├── task-09-selenium-test-design-execution.md
    ├── task-10-continuous-testing-jenkins.md
    ├── task-11-docker-image-container-lifecycle.md
    ├── task-12-jenkins-docker-continuous-deployment.md
    ├── task-13-configuration-management-ansible.md
    ├── task-14-automated-provisioning-reliability-validation.md
    └── COMPLETE_SUBMISSION_REPORT.md
```

---

## 4. Quick Start & Execution Guide

### Local Development & Testing
```bash
# 1. Compile and execute all 15 test cases (Unit + Integration + Selenium)
mvn clean test

# 2. Package the production executable JAR
mvn package -DskipTests

# 3. Launch application locally on port 8080
java -jar target/telecom-service-outage-dashboard.jar
```
Open your browser at `http://localhost:8080/`.

### Health Check Endpoint
```bash
curl http://localhost:8080/api/health
```
Expected JSON Response:
```json
{
  "service": "telecom-service-outage-dashboard",
  "author": "Manas Akhare (23102C0017)",
  "version": "1.0.0-mvp",
  "status": "UP",
  "timestamp": 1729501800000
}
```

### Docker Deployment
```bash
# Build multi-stage container
docker build -f docker/Dockerfile -t telecom/outage-dashboard:1.0.0 .

# Run container with mapped port
docker run -d -p 8080:8080 --name telecom-dashboard telecom/outage-dashboard:1.0.0
```

### Ansible Automated Provisioning
```bash
cd ansible
# Syntax check
ansible-playbook -i inventory.ini playbook.yml --syntax-check

# Execute full provisioning
ansible-playbook -i inventory.ini playbook.yml

# Automated Rollback (if required)
ansible-playbook -i inventory.ini rollback.yml
```

---

## 5. Summary of Completed 14 Tasks
All 14 task deliverables are documented under the `docs/` directory:
- [Task 1: Problem Definition & Scope](docs/task-01-problem-definition-and-scope.md)
- [Task 2: Agile Planning & DevOps Workflow](docs/task-02-agile-planning-and-devops-workflow.md)
- [Task 3: Requirements, Architecture & Technology Setup](docs/task-03-requirements-and-architecture.md)
- [Task 4: Git & GitHub Repository Initialization](docs/task-04-git-repository-initialization.md)
- [Task 5: Feature Development with Branching](docs/task-05-feature-development-branching.md)
- [Task 6: MVP Completion & Git Collaboration](docs/task-06-mvp-completion-git-collaboration.md)
- [Task 7: Jenkins Installation & CI Job](docs/task-07-jenkins-continuous-integration-job.md)
- [Task 8: Pipeline as Code & Server Deployment](docs/task-08-pipeline-as-code-server-deployment.md)
- [Task 9: Selenium Test Design & Local Execution](docs/task-09-selenium-test-design-execution.md)
- [Task 10: Continuous Testing in Jenkins](docs/task-10-continuous-testing-jenkins.md)
- [Task 11: Docker Image & Container Lifecycle](docs/task-11-docker-image-container-lifecycle.md)
- [Task 12: Jenkins-Docker Continuous Deployment](docs/task-12-jenkins-docker-continuous-deployment.md)
- [Task 13: Configuration Management with Ansible](docs/task-13-configuration-management-ansible.md)
- [Task 14: Automated Provisioning & Reliability Validation](docs/task-14-automated-provisioning-reliability-validation.md)
- [Comprehensive Master Report](docs/COMPLETE_SUBMISSION_REPORT.md)
