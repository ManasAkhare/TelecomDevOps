# Task 4: Git and GitHub Repository Initialization
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Repository Specification
- **Repository Name:** `telecom-service-outage-dashboard`
- **Upstream GitHub URL:** `https://github.com/manasakhare/telecom-service-outage-dashboard.git`
- **Default Branch:** `main`
- **Development Integration Branch:** `develop`
- **Author Identity:**
  - Name: `Manas Akhare`
  - Email: `xmanasakhare@gmail.com`

---

## 2. Branching Naming Policy & Rules
To ensure strict quality control and seamless collaboration across DevOps teams, the following branching strategy (Git Flow adaptation) is enforced:

| Branch Type | Naming Convention | Source Branch | Target Merge Branch | Purpose |
|---|---|---|---|---|
| **Production** | `main` | N/A | Tagged Releases | Clean, deployable production baselines only. |
| **Development**| `develop` | `main` | `main` | Active sprint integration baseline. |
| **Feature** | `feature/<feature-name>` | `develop` | `develop` | New functional development (e.g. `feature/outage-reporting`). |
| **Bug Fix** | `bugfix/<issue-id>` | `develop` | `develop` | Defect fixes during testing sprints. |
| **Hotfix** | `hotfix/<patch-version>` | `main` | `main` & `develop` | Critical production outage hotfixes. |
| **Release** | `release/v<X.Y.Z>` | `develop` | `main` & `develop` | Final release hardening and stabilization. |

### Protected Branch Rules:
- Direct pushes to `main` and `develop` are prohibited.
- All code changes must pass automated Maven test execution before merge.
- Every merge into `develop` requires an approved Pull Request with code review.

---

## 3. GitHub Issue & Pull Request Templates
The repository includes standardized GitHub markdown templates under `.github/`:
1. [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md): Captures affected service layer (5G/4G/Fiber), circle, reproduction steps, and severity.
2. [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md): Gathers stakeholder requirements and operational benefits for NOC workflows.
3. [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md): Enforces review checklists, linked issues, unit test verification, and documentation updates.

---

## 4. Repository Structure & Exclusions
The `.gitignore` excludes compiled classes, Maven `target/` binaries, IDE configuration files (`.idea/`, `.vscode/`), local logs, and test failure screenshots while maintaining wrapper scripts and source baselines.

---

## 5. Initial Commit Evidence
The repository was initialized and committed using conventional commit standards:

```bash
$ git init
Initialized empty Git repository in C:/Users/Admin/Downloads/DevOps/.git/

$ git checkout -b main
Switched to a new branch 'main'

$ git add pom.xml .gitignore README.md .github/
$ git commit -m "chore(repo): initialize Telecom Outage Dashboard repository skeleton with Maven, .gitignore, and issue templates"
[main (root-commit) a229702] chore(repo): initialize Telecom Outage Dashboard repository skeleton with Maven, .gitignore, and issue templates
 6 files changed, 397 insertions(+)
 create mode 100644 .github/ISSUE_TEMPLATE/bug_report.md
 create mode 100644 .github/ISSUE_TEMPLATE/feature_request.md
 create mode 100644 .github/PULL_REQUEST_TEMPLATE.md
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 pom.xml
```
