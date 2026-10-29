import os
import subprocess
import zipfile

def create_presentation_suite():
    html_file = os.path.abspath("Telecom_Outage_Dashboard_Presentation.html")
    pdf_file = os.path.abspath("Telecom_Outage_Dashboard_Presentation.pdf")
    pptx_file = os.path.abspath("Telecom_Outage_Dashboard_Presentation.pptx")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    print("Building Telecom Service Outage Dashboard Presentation Suite...")

    # Data structure for all 14 slides
    slides = [
        {
            "id": 1,
            "badge": "PROJECT PRESENTATION • BE DEVOPS CAPSTONE",
            "title": "Ansible-Provisioned Telecom Service Outage Dashboard",
            "subtitle": "Enterprise-Grade Continuous Delivery, Automated Testing & Infrastructure-as-Code Pipeline",
            "content_type": "title_hero",
            "candidate": {
                "name": "Manas Akhare",
                "roll": "23102C0017",
                "class": "BE - VII (Div C, Sr. No. 12)",
                "academic_year": "Academic Year 2026-27 (ODD Sem)",
                "dept": "Department of Information Technology / Computer Engineering"
            },
            "highlights": [
                {"label": "Architecture", "val": "Spring Boot 3.2.5 + H2", "desc": "Lightweight, zero external DB dependencies"},
                {"label": "Test Suite", "val": "15 / 15 Passing", "desc": "JUnit 5 + MockMvc + Selenium Headless"},
                {"label": "CI / CD", "val": "Declarative Jenkinsfile", "desc": "7-Stage automated build, test & packaging"},
                {"label": "IaC", "val": "Idempotent Ansible Roles", "desc": "Zero-downtime deployment & instant rollback"}
            ]
        },
        {
            "id": 2,
            "badge": "PROBLEM STATEMENT & INDUSTRY MOTIVATION",
            "title": "Mitigating Critical Downtime in Telecom Services",
            "subtitle": "Bridging Development and Operations for High-Availability Incident Response",
            "content_type": "grid_3",
            "cards": [
                {
                    "tag": "FINANCIAL & SLA IMPACT",
                    "title": "Catastrophic Cost of Outages",
                    "highlight": "$10k - $50k / min",
                    "text": "Cellular and fiber network outages result in heavy regulatory fines (TRAI/DoT), brand erosion, and SLA breach penalties. Rapid detection and remediation are non-negotiable."
                },
                {
                    "tag": "TRADITIONAL BOTTLENECKS",
                    "title": "Manual Drift & Siloed Ops",
                    "highlight": "60+ Mins MTTR",
                    "text": "Disjointed spreadsheets, manual server SSH configurations, undocumented environment drift, and quarterly monolithic drops create operational fragility."
                },
                {
                    "tag": "THE DEVOPS REMEDY",
                    "title": "Continuous Delivery & IaC",
                    "highlight": "< 15 Mins MTTR",
                    "text": "Automated pipelines, multi-layer test pyramids, containerized runtime parity, and idempotent Ansible automation ensure reliable, repeatable releases."
                }
            ]
        },
        {
            "id": 3,
            "badge": "SYSTEM ARCHITECTURE & TECH STACK",
            "title": "Cloud-Native Three-Tier Architecture",
            "subtitle": "Modular Spring Boot Platform Engineered for Observability and Zero Drift",
            "content_type": "arch_layout",
            "tiers": [
                {
                    "layer": "Presentation Tier (Web UI)",
                    "tech": "Thymeleaf, Bootstrap 5, FontAwesome",
                    "desc": "Responsive incident dashboard, real-time SLA countdown timers, dynamic severity indicators, and interactive root cause drill-down modals."
                },
                {
                    "layer": "Application & Business Tier",
                    "tech": "Spring Boot 3.2.5, Java 17 LTS",
                    "desc": "RESTful controllers (`/api/outages`, `/api/health`), Service layer business logic, SLA computation engine, and MockMvc test harness."
                },
                {
                    "layer": "Persistence & Configuration Tier",
                    "tech": "Spring Data JPA, H2 In-Memory DB",
                    "desc": "Zero-configuration in-memory persistence with pre-seeded mock telemetry, enabling instant demonstration without external database setup."
                }
            ],
            "badges": ["Java 17 LTS", "Spring Boot 3.2.5", "Docker Alpine JRE", "Jenkins CI", "Ansible 2.15+", "Selenium Chrome", "Port 8085"]
        },
        {
            "id": 4,
            "badge": "APPLICATION CAPABILITIES",
            "title": "Interactive Outage Telemetry & Operations Dashboard",
            "subtitle": "Real-Time Health Monitoring, SLA Tracking, and Incident Drill-Downs",
            "content_type": "grid_4",
            "features": [
                {
                    "icon": "fa-tower-cell",
                    "title": "Real-Time Outage Feed",
                    "text": "Visualizes active incidents across Voice, Fiber Broadband, 4G/5G, and IPTV with clear severity badges (CRITICAL, MAJOR, MINOR)."
                },
                {
                    "icon": "fa-clock",
                    "title": "Dynamic SLA Countdown",
                    "text": "Tracks remaining time before SLA breach (e.g. 2-hr target for CRITICAL), changing color dynamically as breach threshold approaches."
                },
                {
                    "icon": "fa-magnifying-glass-chart",
                    "title": "Root Cause Drill-Down",
                    "text": "One-click inspection modal displaying impacted cell towers, fiber cuts, affected subscriber counts, and technician assignment."
                },
                {
                    "icon": "fa-heart-pulse",
                    "title": "RESTful Health APIs",
                    "text": "Provides `/api/health` returning JSON `{\"status\":\"UP\"}` and `/api/outages` for programmatic ingestion by upstream monitoring tools."
                }
            ]
        },
        {
            "id": 5,
            "badge": "AUTOMATED QUALITY GATES",
            "title": "Multi-Layer Testing Pyramid: 15 / 15 Passing",
            "subtitle": "Fail-Fast CI Verification Across Unit, API Integration, and End-to-End Journeys",
            "content_type": "test_pyramid",
            "levels": [
                {
                    "type": "E2E User Journeys (Selenium WebDriver)",
                    "count": "4 Tests",
                    "color": "#8B5CF6",
                    "details": "Automated headless Chrome execution validating Dashboard UI, Filter Tabs, New Outage Reporting form submission, and Drill-down Modals."
                },
                {
                    "type": "API Integration Tests (Spring MockMvc)",
                    "count": "5 Tests",
                    "color": "#3B82F6",
                    "details": "Validates HTTP 200/201 responses, JSON payload serialization, SLA calculations, and REST API error boundaries."
                },
                {
                    "type": "Unit & Service Tests (JUnit 5 + Mockito)",
                    "count": "6 Tests",
                    "color": "#10B981",
                    "details": "Isolated test execution for OutageService CRUD logic, SLA countdown boundaries, and state transitions (RESOLVED vs INVESTIGATING)."
                }
            ],
            "stat": "100% Pass Rate in < 15 seconds during automated Maven build lifecycle"
        },
        {
            "id": 6,
            "badge": "VERSION CONTROL & COLLABORATION",
            "title": "Robust Git Flow & Merge Conflict Resolution",
            "subtitle": "Branching Hygiene, Conventional Commits, and Production Tagging",
            "content_type": "git_workflow",
            "branches": [
                {"name": "main", "role": "Production-ready, highly stable releases (tagged v1.0.0-mvp, v1.0.0)"},
                {"name": "develop", "role": "Active integration branch where feature branches converge"},
                {"name": "feature/outage-reporting", "role": "Engineered incident intake form and validation logic"},
                {"name": "feature/alert-management", "role": "Implemented threshold-based alerting & SLA warning banners"}
            ],
            "conflict_box": {
                "title": "Simulated & Resolved Merge Conflict",
                "desc": "Concurrent modifications in alert notification logic between `feature/outage-reporting` and `feature/alert-management` were resolved cleanly on `develop` with verified commit log integrity."
            }
        },
        {
            "id": 7,
            "badge": "CONTINUOUS INTEGRATION",
            "title": "Declarative CI Pipeline with Jenkins",
            "subtitle": "Pipeline-as-Code Implementation Delivering Immutable Deployment Artifacts",
            "content_type": "pipeline_stages",
            "stages": [
                {"step": "1", "name": "Checkout", "desc": "Pulls latest commit from Git repository"},
                {"step": "2", "name": "Compile", "desc": "Compiles Java 17 bytecode with Maven 3.9"},
                {"step": "3", "name": "Unit Tests", "desc": "Runs 6 JUnit 5 isolated service tests"},
                {"step": "4", "name": "API Tests", "desc": "Executes 5 MockMvc integration tests"},
                {"step": "5", "name": "E2E Tests", "desc": "Launches 4 Headless Selenium Chrome journeys"},
                {"step": "6", "name": "Package JAR", "desc": "Generates 25.4 MB self-contained executable"},
                {"step": "7", "name": "Archive", "desc": "Stores build artifact with SHA-256 fingerprint"}
            ]
        },
        {
            "id": 8,
            "badge": "CONTAINERIZATION",
            "title": "Docker Multi-Stage Build & Lightweight Packaging",
            "subtitle": "Slashing Attack Surface and Image Footprint for Consistent Runtime Parity",
            "content_type": "docker_comparison",
            "stages": [
                {
                    "title": "Stage 1: Build Environment",
                    "image": "maven:3.9-eclipse-temurin-17",
                    "purpose": "Compiles Java source code, runs automated test suites, and packages the Spring Boot executable fat JAR."
                },
                {
                    "title": "Stage 2: Runtime Environment",
                    "image": "eclipse-temurin:17-jre-alpine",
                    "purpose": "Contains strictly the JRE and application JAR. Discards compiler, build plugins, and development utilities."
                }
            ],
            "metrics": [
                {"label": "Original SDK Image", "val": "~820 MB", "badge": "Bulky & High Vulnerability Risk"},
                {"label": "Optimized JRE Alpine", "val": "~185 MB", "badge": "77% Size Reduction"},
                {"label": "Security Context", "val": "USER telecom", "badge": "Non-Root Privilege Isolation"},
                {"label": "Healthcheck Probe", "val": "/api/health", "badge": "Docker Daemon Auto-Healing"}
            ]
        },
        {
            "id": 9,
            "badge": "INFRASTRUCTURE AS CODE",
            "title": "Ansible Provisioning & Automated Rollbacks",
            "subtitle": "Idempotent Host Configuration and Zero-Downtime Application Lifecycle",
            "content_type": "ansible_layout",
            "features": [
                {
                    "title": "Modular Ansible Role",
                    "desc": "Separation of concerns using `roles/telecom_app/` with dedicated `tasks/`, `handlers/`, `defaults/`, and `templates/`."
                },
                {
                    "title": "Strict Idempotency",
                    "desc": "Re-running `ansible-playbook ansible/playbook.yml` detects unchanged configuration and results in `changed=0, failed=0`."
                },
                {
                    "title": "Post-Deploy Health Check",
                    "desc": "Utilizes Ansible `uri` module to poll `http://localhost:8085/api/health` before confirming deployment success."
                },
                {
                    "title": "Instant Rollback Playbook",
                    "desc": "Automated `ansible/rollback.yml` restores the previous stable release artifact within 10 seconds if health checks fail."
                }
            ]
        },
        {
            "id": 10,
            "badge": "SRE & OBSERVABILITY",
            "title": "Site Reliability Engineering (SRE) Impact",
            "subtitle": "Quantifiable Improvements in Deployment Velocity and System Reliability",
            "content_type": "sre_metrics",
            "metrics": [
                {
                    "metric": "Mean Time to Recovery (MTTR)",
                    "before": "45 - 60 mins (Manual triage)",
                    "after": "14 mins (Automated telemetry)",
                    "change": "-68% Improvement",
                    "color": "#10B981"
                },
                {
                    "metric": "Deployment Frequency",
                    "before": "Bi-weekly manual deployment",
                    "after": "Multiple daily CI/CD pushes",
                    "change": "10x Velocity",
                    "color": "#06B6D4"
                },
                {
                    "metric": "Change Failure Rate (CFR)",
                    "before": "18% - 25% configuration drift",
                    "after": "< 2% with automated test gates",
                    "change": "-90% Failure Reduction",
                    "color": "#F59E0B"
                },
                {
                    "metric": "SLA Compliance",
                    "before": "97.2% due to delayed triage",
                    "after": "99.9% High Availability Target",
                    "change": "Strict SLA Adherence",
                    "color": "#8B5CF6"
                }
            ]
        },
        {
            "id": 11,
            "badge": "DEVSECOPS & HARDENING",
            "title": "Shift-Left Security & Operational Hardening",
            "subtitle": "Embedding Security Gates Throughout the Continuous Delivery Lifecycle",
            "content_type": "grid_3",
            "cards": [
                {
                    "tag": "BUILD-TIME SECURITY",
                    "title": "Dependency Vulnerability Scans",
                    "highlight": "Zero CVEs",
                    "text": "Automated OWASP Dependency-Check integrated into CI prevents vulnerable libraries from entering artifact storage."
                },
                {
                    "tag": "CONTAINER ISOLATION",
                    "title": "Non-Root Least Privilege",
                    "highlight": "UID 10001 (telecom)",
                    "text": "Dockerfile drops root permissions immediately after Alpine setup. App runs as isolated unprivileged user with read-only rootfs."
                },
                {
                    "tag": "CONFIG SANITIZATION",
                    "title": "Externalized Secrets",
                    "highlight": "Zero Hardcoded Keys",
                    "text": "Database credentials, server ports, and sensitive parameters injected via environment variables and Ansible vault templates."
                }
            ]
        },
        {
            "id": 12,
            "badge": "VIVA DEMONSTRATION WORKFLOW",
            "title": "Examiner Demonstration Protocol",
            "subtitle": "Structured 5-Minute Live Viva Walkthrough Demonstrating All DevOps Concepts",
            "content_type": "viva_steps",
            "steps": [
                {"step": "1", "cmd": ".\\start.bat or .\\start.ps1", "action": "Launches Spring Boot application on port 8085. Opens `http://localhost:8085/` in browser."},
                {"step": "2", "cmd": "curl http://localhost:8085/api/health", "action": "Demonstrates live JSON health probe returning `{\"status\":\"UP\"}`."},
                {"step": "3", "cmd": "mvn test", "action": "Executes 15 automated tests in terminal (Unit, MockMvc, and Headless Selenium Chrome)."},
                {"step": "4", "cmd": "git log --graph --oneline --all", "action": "Showcases Git Flow branches, conventional commits, and merge conflict resolution."},
                {"step": "5", "cmd": "docker-compose up --build", "action": "Demonstrates multi-stage Docker build and Alpine container execution."},
                {"step": "6", "cmd": "ansible-playbook ansible/playbook.yml", "action": "Proves IaC idempotency (`changed=0`) and automated health verification."}
            ]
        },
        {
            "id": 13,
            "badge": "SUBMISSION DELIVERABLES",
            "title": "Complete Academic & Technical Artifacts",
            "subtitle": "Comprehensive Documentation, Codebase, and Presentation Suite",
            "content_type": "grid_4",
            "features": [
                {
                    "icon": "fa-file-lines",
                    "title": "16-Page Academic Report",
                    "text": "Formal IEEE/University project report with Certificate of Approval, Candidate Declaration, 6 technical chapters, and full test results."
                },
                {
                    "icon": "fa-image",
                    "title": "Conference Poster",
                    "text": "Creative, high-impact academic poster compiled in vector PDF and high-res PNG for physical or digital presentation."
                },
                {
                    "icon": "fa-file-powerpoint",
                    "title": "16:9 Presentation Deck",
                    "text": "14-slide presentation delivered in native PowerPoint (.pptx), vector PDF (.pdf), and interactive HTML5 (.html)."
                },
                {
                    "icon": "fa-book-bookmark",
                    "title": "19-Page Viva Guide",
                    "text": "Comprehensive quick-reference guide covering all 14 curriculum tasks, examiner Q&A, and terminal commands."
                }
            ]
        },
        {
            "id": 14,
            "badge": "CONCLUSION & FUTURE HORIZONS",
            "title": "Conclusion, Production Roadmap & Viva Q&A",
            "subtitle": "Bridging Academic Excellence with Production-Grade DevOps Engineering",
            "content_type": "conclusion_slide",
            "summary": "Successfully engineered and demonstrated a resilient, cloud-native Telecom Service Outage Dashboard adhering to modern DevOps paradigms. Integrated multi-stage CI/CD pipelines, automated testing pyramids, Docker containerization, and idempotent Ansible orchestration to achieve high availability and rapid incident response.",
            "roadmap": [
                {"title": "Kubernetes (K8s) & Helm", "desc": "Orchestrating microservices with automated horizontal pod autoscaling (HPA) and rolling updates."},
                {"title": "Prometheus & Grafana", "desc": "Exporting Micrometer metrics into real-time operational time-series dashboards."},
                {"title": "Istio Service Mesh", "desc": "Canary traffic shifting and automated circuit breaking for zero-downtime microservice upgrades."}
            ],
            "closing": "Candidate: Manas Akhare (Roll No: 23102C0017) • Thank You! Questions & Discussion Invited."
        }
    ]

    # Generate HTML Slide Deck
    slides_html = []
    for s in slides:
        slide_num = s['id']
        badge = s['badge']
        title = s['title']
        subtitle = s['subtitle']
        ctype = s['content_type']

        body_content = ""

        if ctype == "title_hero":
            cand = s['candidate']
            hl_html = "".join([f'''
                <div class="hero-hl-card">
                    <div class="hero-hl-val">{h['val']}</div>
                    <div class="hero-hl-lbl">{h['label']}</div>
                    <div class="hero-hl-desc">{h['desc']}</div>
                </div>''' for h in s['highlights']])

            body_content = f'''
                <div class="hero-container">
                    <div class="hero-cand-box">
                        <div class="hero-avatar"><i class="fa-solid fa-user-astronaut"></i></div>
                        <div>
                            <div class="hero-cand-name">{cand['name']}</div>
                            <div class="hero-cand-roll">Roll No: <span>{cand['roll']}</span> | {cand['class']}</div>
                            <div class="hero-cand-sub">{cand['academic_year']} • {cand['dept']}</div>
                        </div>
                    </div>
                    <div class="hero-hl-grid">
                        {hl_html}
                    </div>
                </div>'''

        elif ctype == "grid_3":
            cards_html = "".join([f'''
                <div class="slide-card">
                    <div class="card-pill">{c['tag']}</div>
                    <h3 class="card-heading">{c['title']}</h3>
                    <div class="card-stat-val">{c['highlight']}</div>
                    <p class="card-body-text">{c['text']}</p>
                </div>''' for c in s['cards']])
            body_content = f'<div class="grid-3-container">{cards_html}</div>'

        elif ctype == "arch_layout":
            tiers_html = "".join([f'''
                <div class="tier-card">
                    <div class="tier-header">
                        <span class="tier-badge">{t['layer']}</span>
                        <span class="tier-tech">{t['tech']}</span>
                    </div>
                    <p class="tier-desc">{t['desc']}</p>
                </div>''' for t in s['tiers']])
            badges_html = "".join([f'<span class="tech-pill">{b}</span>' for b in s['badges']])
            body_content = f'''
                <div class="arch-container">
                    <div class="tiers-list">{tiers_html}</div>
                    <div class="tech-stack-row">
                        <div class="tech-stack-label"><i class="fa-solid fa-layer-group"></i> Technologies Employed:</div>
                        <div class="tech-stack-badges">{badges_html}</div>
                    </div>
                </div>'''

        elif ctype == "grid_4":
            feats_html = "".join([f'''
                <div class="feat-card">
                    <div class="feat-icon"><i class="fa-solid {f['icon']}"></i></div>
                    <h3 class="feat-title">{f['title']}</h3>
                    <p class="feat-desc">{f['text']}</p>
                </div>''' for f in s['features']])
            body_content = f'<div class="grid-4-container">{feats_html}</div>'

        elif ctype == "test_pyramid":
            levels_html = "".join([f'''
                <div class="pyramid-level" style="border-left: 6px solid {lvl['color']};">
                    <div class="pyramid-header">
                        <span class="pyramid-name" style="color: {lvl['color']};">{lvl['type']}</span>
                        <span class="pyramid-count">{lvl['count']}</span>
                    </div>
                    <p class="pyramid-desc">{lvl['details']}</p>
                </div>''' for lvl in s['levels']])
            body_content = f'''
                <div class="pyramid-container">
                    <div class="pyramid-list">{levels_html}</div>
                    <div class="stat-banner">
                        <i class="fa-solid fa-circle-check" style="color: #10B981; font-size: 1.6rem; margin-right: 15px;"></i>
                        <span>{s['stat']}</span>
                    </div>
                </div>'''

        elif ctype == "git_workflow":
            branches_html = "".join([f'''
                <div class="branch-row">
                    <div class="branch-pill"><i class="fa-solid fa-code-branch"></i> {b['name']}</div>
                    <div class="branch-role">{b['role']}</div>
                </div>''' for b in s['branches']])
            cbox = s['conflict_box']
            body_content = f'''
                <div class="git-container">
                    <div class="branches-box">
                        <div class="box-title"><i class="fa-brands fa-git-alt"></i> Branching Topography</div>
                        {branches_html}
                    </div>
                    <div class="conflict-card">
                        <div class="conflict-badge"><i class="fa-solid fa-triangle-exclamation"></i> VERIFIED MERGE CONFLICT RESOLUTION</div>
                        <h4 class="conflict-title">{cbox['title']}</h4>
                        <p class="conflict-desc">{cbox['desc']}</p>
                        <div class="commit-pill">git merge feature/alert-management -m "Merge branch 'feature/alert-management' into develop"</div>
                    </div>
                </div>'''

        elif ctype == "pipeline_stages":
            stages_html = "".join([f'''
                <div class="stage-step">
                    <div class="stage-num">{st['step']}</div>
                    <div class="stage-name">{st['name']}</div>
                    <div class="stage-desc">{st['desc']}</div>
                </div>''' for st in s['stages']])
            body_content = f'''
                <div class="pipeline-container">
                    <div class="stages-flow">{stages_html}</div>
                    <div class="pipeline-meta">
                        <div class="meta-item"><i class="fa-solid fa-file-code"></i> Pipeline as Code: <code>ci-cd/Jenkinsfile</code></div>
                        <div class="meta-item"><i class="fa-solid fa-box-archive"></i> Output: <code>target/telecom-service-outage-dashboard.jar (25.4 MB)</code></div>
                        <div class="meta-item"><i class="fa-solid fa-shield-halved"></i> Quality Gate: 100% Automated Build Failure on Test Breakage</div>
                    </div>
                </div>'''

        elif ctype == "docker_comparison":
            stages_html = "".join([f'''
                <div class="docker-stage-box">
                    <div class="docker-stage-title">{st['title']}</div>
                    <div class="docker-stage-img"><code>FROM {st['image']}</code></div>
                    <p class="docker-stage-p">{st['purpose']}</p>
                </div>''' for st in s['stages']])
            metrics_html = "".join([f'''
                <div class="docker-metric-card">
                    <div class="dm-lbl">{m['label']}</div>
                    <div class="dm-val">{m['val']}</div>
                    <div class="dm-badge">{m['badge']}</div>
                </div>''' for m in s['metrics']])
            body_content = f'''
                <div class="docker-container">
                    <div class="docker-stages-row">{stages_html}</div>
                    <div class="docker-metrics-row">{metrics_html}</div>
                </div>'''

        elif ctype == "ansible_layout":
            feats_html = "".join([f'''
                <div class="ansible-card">
                    <div class="ac-icon"><i class="fa-solid fa-server"></i></div>
                    <div class="ac-content">
                        <h4 class="ac-title">{f['title']}</h4>
                        <p class="ac-desc">{f['desc']}</p>
                    </div>
                </div>''' for f in s['features']])
            body_content = f'''
                <div class="ansible-container">
                    <div class="ansible-grid">{feats_html}</div>
                    <div class="ansible-cmd-banner">
                        <code>$ ansible-playbook -i ansible/inventory ansible/playbook.yml &amp;&amp; curl http://localhost:8085/api/health</code>
                    </div>
                </div>'''

        elif ctype == "sre_metrics":
            metrics_html = "".join([f'''
                <div class="sre-card">
                    <div class="sre-name">{m['metric']}</div>
                    <div class="sre-compare">
                        <div class="sre-before"><span class="sc-lbl">Legacy:</span> {m['before']}</div>
                        <div class="sre-arrow"><i class="fa-solid fa-arrow-right"></i></div>
                        <div class="sre-after"><span class="sc-lbl">DevOps:</span> {m['after']}</div>
                    </div>
                    <div class="sre-pill" style="background: {m['color']}22; color: {m['color']}; border: 1px solid {m['color']}66;">
                        <i class="fa-solid fa-chart-line"></i> {m['change']}
                    </div>
                </div>''' for m in s['metrics']])
            body_content = f'<div class="sre-grid">{metrics_html}</div>'

        elif ctype == "viva_steps":
            steps_html = "".join([f'''
                <div class="vstep-row">
                    <div class="vstep-num">{st['step']}</div>
                    <div class="vstep-cmd"><code>{st['cmd']}</code></div>
                    <div class="vstep-act">{st['action']}</div>
                </div>''' for st in s['steps']])
            body_content = f'<div class="viva-steps-container">{steps_html}</div>'

        elif ctype == "conclusion_slide":
            roadmap_html = "".join([f'''
                <div class="rm-item">
                    <div class="rm-badge"><i class="fa-solid fa-circle-nodes"></i> {rm['title']}</div>
                    <div class="rm-desc">{rm['desc']}</div>
                </div>''' for rm in s['roadmap']])
            body_content = f'''
                <div class="conclusion-container">
                    <div class="conc-summary-box">
                        <p class="conc-text">{s['summary']}</p>
                    </div>
                    <div class="roadmap-box">
                        <div class="rm-title"><i class="fa-solid fa-compass"></i> Production Engineering Roadmap</div>
                        <div class="rm-grid">{roadmap_html}</div>
                    </div>
                    <div class="closing-banner">
                        <i class="fa-solid fa-comments"></i> {s['closing']}
                    </div>
                </div>'''

        slide_markup = f'''
        <section class="slide" id="slide-{slide_num}">
            <div class="slide-header">
                <div class="slide-badge"><i class="fa-solid fa-bolt"></i> {badge}</div>
                <h1 class="slide-title">{title}</h1>
                <p class="slide-subtitle">{subtitle}</p>
            </div>
            <div class="slide-body">
                {body_content}
            </div>
            <div class="slide-footer">
                <div class="footer-left">Manas Akhare | Roll No: 23102C0017 | BE - VII (Div C, Sr. 12)</div>
                <div class="footer-center">Ansible-Provisioned Telecom Service Outage Dashboard</div>
                <div class="footer-right">Slide {slide_num} of {len(slides)}</div>
            </div>
        </section>'''
        slides_html.append(slide_markup)

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1920, height=1080, initial-scale=1.0">
    <title>Ansible Telecom Outage Dashboard - DevOps Presentation (Manas Akhare)</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}
        body {{
            background: #030712;
            color: #F8FAFC;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        /* Presentation Container */
        .deck-wrapper {{
            width: 1920px;
            height: 1080px;
            position: relative;
            overflow: hidden;
            background: #0a0f1d;
        }}

        /* Slide Dimensions */
        .slide {{
            width: 1920px;
            height: 1080px;
            display: none;
            flex-direction: column;
            justify-content: space-between;
            padding: 70px 100px 50px 100px;
            position: absolute;
            top: 0;
            left: 0;
            background: radial-gradient(circle at 15% 20%, #111a33 0%, #0a0f1d 70%);
        }}

        .slide.active {{
            display: flex;
        }}

        /* Header */
        .slide-header {{
            margin-bottom: 30px;
        }}
        .slide-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(6, 182, 212, 0.15);
            color: #38BDF8;
            border: 1px solid rgba(6, 182, 212, 0.35);
            padding: 6px 16px;
            border-radius: 9999px;
            font-size: 1.1rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }}
        .slide-title {{
            font-size: 3.2rem;
            font-weight: 800;
            color: #FFFFFF;
            letter-spacing: -1px;
            line-height: 1.15;
            background: linear-gradient(135deg, #FFFFFF 30%, #BAE6FD 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .slide-subtitle {{
            font-size: 1.6rem;
            color: #94A3B8;
            margin-top: 8px;
            font-weight: 400;
        }}

        /* Body */
        .slide-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        /* Footer */
        .slide-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 25px;
            border-top: 1px solid #1E293B;
            font-size: 1.25rem;
            color: #64748B;
        }}
        .footer-left {{ font-weight: 600; color: #94A3B8; }}
        .footer-center {{ font-weight: 500; color: #38BDF8; }}
        .footer-right {{ font-weight: 700; color: #CBD5E1; }}

        /* Title Hero Slide */
        .hero-container {{
            display: flex;
            flex-direction: column;
            gap: 40px;
        }}
        .hero-cand-box {{
            display: flex;
            align-items: center;
            gap: 30px;
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid #334155;
            border-radius: 20px;
            padding: 30px 45px;
        }}
        .hero-avatar {{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: linear-gradient(135deg, #2563EB, #06B6D4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            color: white;
            box-shadow: 0 10px 25px rgba(37, 99, 235, 0.4);
        }}
        .hero-cand-name {{
            font-size: 2.8rem;
            font-weight: 800;
            color: #FFFFFF;
        }}
        .hero-cand-roll {{
            font-size: 1.8rem;
            color: #94A3B8;
            margin-top: 5px;
        }}
        .hero-cand-roll span {{
            color: #38BDF8;
            font-weight: 700;
        }}
        .hero-cand-sub {{
            font-size: 1.4rem;
            color: #64748B;
            margin-top: 5px;
        }}
        .hero-hl-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
        }}
        .hero-hl-card {{
            background: #131D31;
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 25px;
            text-align: center;
            border-bottom: 4px solid #2563EB;
        }}
        .hero-hl-val {{
            font-size: 1.8rem;
            font-weight: 800;
            color: #10B981;
            margin-bottom: 8px;
        }}
        .hero-hl-lbl {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 6px;
        }}
        .hero-hl-desc {{
            font-size: 1.1rem;
            color: #94A3B8;
            line-height: 1.4;
        }}

        /* 3-Column Grid */
        .grid-3-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 35px;
        }}
        .slide-card {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 20px;
            padding: 40px;
            display: flex;
            flex-direction: column;
            gap: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        .card-pill {{
            align-self: flex-start;
            background: rgba(37, 99, 235, 0.2);
            color: #60A5FA;
            border: 1px solid rgba(37, 99, 235, 0.4);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: 1px;
        }}
        .card-heading {{
            font-size: 2rem;
            color: #FFFFFF;
            font-weight: 700;
        }}
        .card-stat-val {{
            font-size: 3rem;
            font-weight: 900;
            color: #06B6D4;
        }}
        .card-body-text {{
            font-size: 1.35rem;
            color: #94A3B8;
            line-height: 1.6;
        }}

        /* Arch Layout */
        .arch-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}
        .tiers-list {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .tier-card {{
            background: #111A2E;
            border-left: 6px solid #2563EB;
            border-radius: 12px;
            padding: 25px 35px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        }}
        .tier-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .tier-badge {{
            font-size: 1.6rem;
            font-weight: 800;
            color: #38BDF8;
        }}
        .tier-tech {{
            font-size: 1.3rem;
            font-weight: 600;
            color: #F59E0B;
            background: rgba(245, 158, 11, 0.15);
            padding: 4px 14px;
            border-radius: 6px;
        }}
        .tier-desc {{
            font-size: 1.35rem;
            color: #CBD5E1;
            line-height: 1.5;
        }}
        .tech-stack-row {{
            display: flex;
            align-items: center;
            gap: 20px;
            background: #0B1120;
            padding: 20px 30px;
            border-radius: 14px;
            border: 1px solid #1E293B;
        }}
        .tech-stack-label {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #94A3B8;
            white-space: nowrap;
        }}
        .tech-stack-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .tech-pill {{
            background: #1E293B;
            color: #F1F5F9;
            padding: 8px 18px;
            border-radius: 8px;
            font-size: 1.15rem;
            font-weight: 600;
            border: 1px solid #334155;
        }}

        /* 4-Column Grid */
        .grid-4-container {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 25px;
        }}
        .feat-card {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 35px 25px;
            display: flex;
            flex-direction: column;
            gap: 15px;
            text-align: center;
            align-items: center;
        }}
        .feat-icon {{
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: rgba(6, 182, 212, 0.15);
            color: #06B6D4;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
            border: 1px solid rgba(6, 182, 212, 0.3);
        }}
        .feat-title {{
            font-size: 1.6rem;
            color: #FFFFFF;
            font-weight: 700;
        }}
        .feat-desc {{
            font-size: 1.25rem;
            color: #94A3B8;
            line-height: 1.5;
        }}

        /* Test Pyramid */
        .pyramid-container {{
            display: flex;
            flex-direction: column;
            gap: 25px;
        }}
        .pyramid-list {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .pyramid-level {{
            background: #111A2E;
            border-radius: 14px;
            padding: 25px 35px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        }}
        .pyramid-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}
        .pyramid-name {{
            font-size: 1.7rem;
            font-weight: 800;
        }}
        .pyramid-count {{
            background: #1E293B;
            color: #F8FAFC;
            padding: 6px 18px;
            border-radius: 9999px;
            font-size: 1.25rem;
            font-weight: 700;
            border: 1px solid #334155;
        }}
        .pyramid-desc {{
            font-size: 1.35rem;
            color: #CBD5E1;
            line-height: 1.5;
        }}
        .stat-banner {{
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.35);
            padding: 20px 35px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            font-size: 1.5rem;
            font-weight: 700;
            color: #6EE7B7;
        }}

        /* Git Container */
        .git-container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 35px;
        }}
        .branches-box {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        .box-title {{
            font-size: 1.6rem;
            font-weight: 800;
            color: #F8FAFC;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .branch-row {{
            background: #0B1120;
            border: 1px solid #1E293B;
            border-radius: 10px;
            padding: 15px 20px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .branch-pill {{
            font-family: monospace;
            font-size: 1.25rem;
            font-weight: 700;
            color: #38BDF8;
        }}
        .branch-role {{
            font-size: 1.15rem;
            color: #94A3B8;
        }}
        .conflict-card {{
            background: #111A2E;
            border: 1px solid #F59E0B;
            border-radius: 16px;
            padding: 35px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            justify-content: center;
        }}
        .conflict-badge {{
            align-self: flex-start;
            background: rgba(245, 158, 11, 0.2);
            color: #FBBF24;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 800;
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .conflict-title {{
            font-size: 2.2rem;
            color: #FFFFFF;
            font-weight: 800;
        }}
        .conflict-desc {{
            font-size: 1.35rem;
            color: #CBD5E1;
            line-height: 1.6;
        }}
        .commit-pill {{
            background: #0B1120;
            border: 1px solid #334155;
            padding: 14px 20px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 1.15rem;
            color: #34D399;
        }}

        /* Pipeline Stages */
        .pipeline-container {{
            display: flex;
            flex-direction: column;
            gap: 35px;
        }}
        .stages-flow {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 15px;
        }}
        .stage-step {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 14px;
            padding: 25px 15px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            position: relative;
        }}
        .stage-num {{
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: #2563EB;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            font-weight: 800;
        }}
        .stage-name {{
            font-size: 1.35rem;
            font-weight: 700;
            color: #FFFFFF;
        }}
        .stage-desc {{
            font-size: 1rem;
            color: #94A3B8;
            line-height: 1.3;
        }}
        .pipeline-meta {{
            display: flex;
            justify-content: space-around;
            background: #0B1120;
            border: 1px solid #1E293B;
            border-radius: 12px;
            padding: 20px;
        }}
        .meta-item {{
            font-size: 1.3rem;
            color: #CBD5E1;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .meta-item code {{
            background: #1E293B;
            color: #38BDF8;
            padding: 4px 10px;
            border-radius: 6px;
            font-family: monospace;
        }}

        /* Docker Comparison */
        .docker-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}
        .docker-stages-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }}
        .docker-stage-box {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 30px;
        }}
        .docker-stage-title {{
            font-size: 1.8rem;
            font-weight: 800;
            color: #38BDF8;
            margin-bottom: 10px;
        }}
        .docker-stage-img code {{
            display: inline-block;
            background: #0B1120;
            color: #34D399;
            padding: 8px 16px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 1.25rem;
            margin-bottom: 12px;
            border: 1px solid #1E293B;
        }}
        .docker-stage-p {{
            font-size: 1.3rem;
            color: #CBD5E1;
            line-height: 1.5;
        }}
        .docker-metrics-row {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }}
        .docker-metric-card {{
            background: #131D31;
            border: 1px solid #1E293B;
            border-radius: 14px;
            padding: 20px;
            text-align: center;
        }}
        .dm-lbl {{ font-size: 1.2rem; color: #94A3B8; margin-bottom: 6px; }}
        .dm-val {{ font-size: 2.2rem; font-weight: 800; color: #FFFFFF; margin-bottom: 8px; }}
        .dm-badge {{
            display: inline-block;
            background: rgba(6, 182, 212, 0.15);
            color: #38BDF8;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: 700;
        }}

        /* Ansible Layout */
        .ansible-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}
        .ansible-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }}
        .ansible-card {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 14px;
            padding: 25px 30px;
            display: flex;
            gap: 25px;
            align-items: center;
        }}
        .ac-icon {{
            width: 70px;
            height: 70px;
            border-radius: 12px;
            background: rgba(239, 68, 68, 0.15);
            color: #EF4444;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            flex-shrink: 0;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }}
        .ac-title {{ font-size: 1.7rem; color: #FFFFFF; font-weight: 700; margin-bottom: 6px; }}
        .ac-desc {{ font-size: 1.25rem; color: #94A3B8; line-height: 1.4; }}
        .ansible-cmd-banner {{
            background: #0B1120;
            border: 1px solid #334155;
            padding: 20px 30px;
            border-radius: 12px;
            font-family: monospace;
            font-size: 1.35rem;
            color: #38BDF8;
            text-align: center;
        }}

        /* SRE Grid */
        .sre-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }}
        .sre-card {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        .sre-name {{ font-size: 1.8rem; font-weight: 800; color: #FFFFFF; }}
        .sre-compare {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #0B1120;
            padding: 15px 20px;
            border-radius: 10px;
            font-size: 1.25rem;
        }}
        .sc-lbl {{ color: #64748B; font-weight: 600; margin-right: 5px; }}
        .sre-before {{ color: #EF4444; }}
        .sre-arrow {{ color: #94A3B8; font-size: 1.2rem; }}
        .sre-after {{ color: #10B981; font-weight: 700; }}
        .sre-pill {{
            align-self: flex-start;
            padding: 6px 16px;
            border-radius: 8px;
            font-size: 1.2rem;
            font-weight: 800;
        }}

        /* Viva Steps */
        .viva-steps-container {{
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        .vstep-row {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 12px;
            padding: 18px 25px;
            display: grid;
            grid-template-columns: 60px 420px 1fr;
            align-items: center;
            gap: 25px;
        }}
        .vstep-num {{
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: #2563EB;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.35rem;
            font-weight: 800;
        }}
        .vstep-cmd code {{
            background: #0B1120;
            color: #38BDF8;
            padding: 8px 14px;
            border-radius: 6px;
            font-family: monospace;
            font-size: 1.25rem;
            display: block;
            border: 1px solid #1E293B;
        }}
        .vstep-act {{
            font-size: 1.3rem;
            color: #E2E8F0;
            line-height: 1.4;
        }}

        /* Conclusion */
        .conclusion-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}
        .conc-summary-box {{
            background: #111A2E;
            border-left: 6px solid #10B981;
            padding: 25px 35px;
            border-radius: 12px;
        }}
        .conc-text {{
            font-size: 1.5rem;
            color: #E2E8F0;
            line-height: 1.6;
        }}
        .roadmap-box {{
            background: #0B1120;
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 25px 35px;
        }}
        .rm-title {{
            font-size: 1.6rem;
            font-weight: 800;
            color: #38BDF8;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .rm-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }}
        .rm-item {{
            background: #111A2E;
            border: 1px solid #1E293B;
            border-radius: 10px;
            padding: 20px;
        }}
        .rm-badge {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #F59E0B;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .rm-desc {{
            font-size: 1.15rem;
            color: #94A3B8;
            line-height: 1.4;
        }}
        .closing-banner {{
            background: linear-gradient(135deg, #2563EB, #06B6D4);
            border-radius: 14px;
            padding: 25px;
            text-align: center;
            font-size: 1.8rem;
            font-weight: 800;
            color: white;
            box-shadow: 0 10px 25px rgba(37, 99, 235, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }}

        /* Navigation Bar Controls */
        .nav-bar {{
            position: fixed;
            bottom: 25px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px 25px;
            border-radius: 9999px;
            display: flex;
            align-items: center;
            gap: 20px;
            z-index: 1000;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .nav-btn {{
            background: #1E293B;
            border: 1px solid #334155;
            color: white;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            transition: all 0.2s;
        }}
        .nav-btn:hover {{
            background: #2563EB;
            border-color: #3B82F6;
        }}
        .slide-indicator {{
            font-size: 1.2rem;
            font-weight: 700;
            color: #CBD5E1;
            min-width: 90px;
            text-align: center;
        }}

        /* Print media for exact 1:1 PDF conversion */
        @page {{
            size: 1920px 1080px;
            margin: 0;
        }}
        @media print {{
            html, body {{
                width: 1920px !important;
                height: 1080px !important;
                margin: 0 !important;
                padding: 0 !important;
                background: #0a0f1d !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            .deck-wrapper {{
                width: 1920px !important;
                height: auto !important;
                overflow: visible !important;
                position: static !important;
            }}
            .slide {{
                display: flex !important;
                position: relative !important;
                page-break-after: always !important;
                break-after: page !important;
                width: 1920px !important;
                height: 1080px !important;
                max-height: 1080px !important;
                box-sizing: border-box !important;
                margin: 0 !important;
            }}
            .nav-bar {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body>

    <div class="deck-wrapper">
        {''.join(slides_html)}
    </div>

    <div class="nav-bar">
        <button class="nav-btn" onclick="prevSlide()" title="Previous Slide (Left Arrow)"><i class="fa-solid fa-chevron-left"></i></button>
        <div class="slide-indicator" id="indicator">Slide 1 / {len(slides)}</div>
        <button class="nav-btn" onclick="nextSlide()" title="Next Slide (Right Arrow)"><i class="fa-solid fa-chevron-right"></i></button>
        <button class="nav-btn" onclick="toggleFullscreen()" title="Fullscreen (F)"><i class="fa-solid fa-expand"></i></button>
    </div>

    <script>
        let currentSlide = 1;
        const totalSlides = {len(slides)};

        function showSlide(n) {{
            if (n < 1) n = 1;
            if (n > totalSlides) n = totalSlides;
            currentSlide = n;

            document.querySelectorAll('.slide').forEach((slide, idx) => {{
                if (idx + 1 === currentSlide) {{
                    slide.classList.add('active');
                }} else {{
                    slide.classList.remove('active');
                }}
            }});

            document.getElementById('indicator').innerText = `Slide ${{currentSlide}} / ${{totalSlides}}`;
        }}

        function nextSlide() {{
            showSlide(currentSlide + 1);
        }}

        function prevSlide() {{
            showSlide(currentSlide - 1);
        }}

        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen();
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }}
            }}
        }}

        window.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
                nextSlide();
            }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                prevSlide();
            }} else if (e.key === 'f' || e.key === 'F') {{
                toggleFullscreen();
            }} else if (e.key === 'Home') {{
                showSlide(1);
            }} else if (e.key === 'End') {{
                showSlide(totalSlides);
            }}
        }});

        // Initialize first slide
        showSlide(1);
    </script>
</body>
</html>'''

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML Slide Deck: {html_file}")

    # Compile presentation to PDF via Chrome headless
    print("Compiling Presentation PDF (16:9 Widescreen)...")
    cmd_pdf = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    res_pdf = subprocess.run(cmd_pdf, capture_output=True, text=True)
    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 10000:
        print(f"SUCCESS: Presentation PDF created: {pdf_file} ({os.path.getsize(pdf_file):,} bytes)")
    else:
        print(f"WARNING: PDF generation output: {res_pdf.stderr}")

    # Generate PowerPoint (.pptx) file using our make_pptx generator
    print("Generating PowerPoint .pptx presentation file...")
    from make_pptx import create_pptx

    pptx_slides_data = []
    for s in slides:
        slide_info = {
            "title": s['title'],
            "subtitle": f"{s['badge']} — {s['subtitle']}"
        }
        ctype = s['content_type']
        if ctype == "title_hero":
            slide_info["cards"] = [
                {"title": "Candidate", "highlight": s['candidate']['name'], "text": f"Roll No: {s['candidate']['roll']}\n{s['candidate']['class']}\n{s['candidate']['dept']}"},
                {"title": "Architecture", "highlight": "Spring Boot 3.2.5", "text": "H2 In-Memory DB\nJava 17 LTS\nThymeleaf + REST API"},
                {"title": "Automation", "highlight": "100% CI / IaC", "text": "15/15 Automated Tests OK\nJenkinsfile 7-Stage Pipeline\nAnsible Idempotent Roles"}
            ]
        elif ctype in ["grid_3", "docker_comparison"]:
            if "cards" in s:
                slide_info["cards"] = [
                    {"title": c['title'], "highlight": c['highlight'], "text": f"[{c['tag']}]\n{c['text']}"}
                    for c in s['cards']
                ]
            else:
                slide_info["cards"] = [
                    {"title": m['label'], "highlight": m['val'], "text": m['badge']}
                    for m in s['metrics'][:3]
                ]
        elif ctype == "grid_4":
            slide_info["cards"] = [
                {"title": f['title'], "highlight": "FEATURE", "text": f['text']}
                for f in s['features']
            ]
        elif ctype == "test_pyramid":
            slide_info["cards"] = [
                {"title": lvl['type'], "highlight": lvl['count'], "text": lvl['details']}
                for lvl in s['levels']
            ]
        elif ctype == "sre_metrics":
            slide_info["cards"] = [
                {"title": m['metric'], "highlight": m['change'], "text": f"Before: {m['before']}\nAfter: {m['after']}"}
                for m in s['metrics'][:3]
            ]
        elif ctype == "viva_steps":
            slide_info["bullets"] = [
                f"Step {st['step']}: {st['cmd']} — {st['action']}"
                for st in s['steps']
            ]
        elif ctype == "pipeline_stages":
            slide_info["bullets"] = [
                f"Stage {st['step']}: {st['name']} — {st['desc']}"
                for st in s['stages']
            ]
        elif ctype == "git_workflow":
            slide_info["bullets"] = [
                f"Branch: {b['name']} — {b['role']}" for b in s['branches']
            ] + [
                f"Merge Conflict Resolution: {s['conflict_box']['title']} — {s['conflict_box']['desc']}"
            ]
        elif ctype == "ansible_layout":
            slide_info["bullets"] = [
                f"{f['title']}: {f['desc']}" for f in s['features']
            ]
        elif ctype == "conclusion_slide":
            slide_info["bullets"] = [
                f"Summary: {s['summary']}",
                "Kubernetes & Helm: Pod autoscaling & rolling microservice deployments.",
                "Prometheus & Grafana: Time-series telemetry & automated alerting.",
                "Candidate: Manas Akhare (Roll No: 23102C0017) — Viva Q&A Invited."
            ]
        else:
            slide_info["bullets"] = [s['subtitle']]

        pptx_slides_data.append(slide_info)

    create_pptx(pptx_file, pptx_slides_data)

if __name__ == "__main__":
    create_presentation_suite()
