# -*- coding: utf-8 -*-
"""
Generates the Academic Exhibition Poster for:
Ansible-Provisioned Telecom Service Outage Dashboard
Student: Manas Akhare | Roll No: 23102C0017 | BE CMPN C
Outputs: poster.html, Telecom_Outage_Dashboard_Poster.pdf, Telecom_Outage_Dashboard_Poster.png
"""

import os
import subprocess

poster_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Academic Poster - Telecom Service Outage Dashboard</title>
    <style>
        @page {
            size: A2 portrait;
            margin: 0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
            background: #090d16;
            color: #f1f5f9;
            width: 1400px;
            min-height: 1980px;
            margin: 0 auto;
            padding: 30px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        /* Top Header Banner */
        .poster-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0369a1 100%);
            border: 2px solid #0284c7;
            border-radius: 16px;
            padding: 30px 40px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header-left {
            max-width: 880px;
        }

        .dept-title {
            font-size: 13pt;
            font-weight: 700;
            color: #38bdf8;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 8px;
        }

        .main-title {
            font-size: 28pt;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 8px;
            text-shadow: 0 2px 10px rgba(2, 132, 199, 0.5);
        }

        .subtitle {
            font-size: 13pt;
            color: #cbd5e1;
            font-weight: 500;
        }

        .header-right {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid #38bdf8;
            border-radius: 12px;
            padding: 18px 24px;
            text-align: right;
        }

        .student-name {
            font-size: 16pt;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 4px;
        }

        .student-meta {
            font-size: 11pt;
            color: #94a3b8;
            line-height: 1.5;
        }

        .meta-highlight {
            color: #38bdf8;
            font-weight: 700;
        }

        /* Metric Highlights Ribbon */
        .metrics-ribbon {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 16px;
        }

        .ribbon-card {
            background: #131b2e;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 16px 20px;
            text-align: center;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3);
            border-top: 4px solid #0284c7;
        }

        .ribbon-val {
            font-size: 26pt;
            font-weight: 900;
            color: #38bdf8;
            font-family: 'Consolas', monospace;
            line-height: 1.1;
        }

        .ribbon-lbl {
            font-size: 9.5pt;
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            margin-top: 6px;
            letter-spacing: 0.5px;
        }

        /* 3-Column Poster Layout */
        .poster-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            flex: 1;
        }

        .col {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .card {
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 14px;
            padding: 22px 24px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid #1f2937;
            padding-bottom: 10px;
        }

        .card-icon {
            font-size: 16pt;
        }

        .card-title {
            font-size: 13pt;
            font-weight: 800;
            color: #38bdf8;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .card-content {
            font-size: 10pt;
            color: #cbd5e1;
            line-height: 1.55;
            text-align: justify;
        }

        /* Badges & Tags */
        .tech-pill-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 6px;
        }

        .tech-pill {
            background: #1e293b;
            color: #e2e8f0;
            border: 1px solid #334155;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 8.5pt;
            font-weight: 600;
        }

        .tech-pill.active {
            background: rgba(2, 132, 199, 0.2);
            color: #38bdf8;
            border-color: #0284c7;
        }

        /* Flow diagram box */
        .diagram-box {
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 12px;
            margin-top: 4px;
        }

        .flow-step {
            background: #1e293b;
            border-left: 4px solid #0284c7;
            padding: 8px 12px;
            border-radius: 4px;
            margin-bottom: 8px;
            font-size: 9pt;
        }
        .flow-step:last-child {
            margin-bottom: 0;
        }

        .flow-step strong {
            color: #38bdf8;
        }

        /* Comparison Table */
        .mini-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 8.5pt;
            margin-top: 6px;
        }

        .mini-table th {
            background: #1f2937;
            color: #93c5fd;
            padding: 6px 8px;
            text-align: left;
            border: 1px solid #374151;
        }

        .mini-table td {
            padding: 6px 8px;
            border: 1px solid #374151;
            color: #e5e7eb;
        }

        .mini-table tr:nth-child(even) {
            background: #161f30;
        }

        .highlight-green {
            color: #4ade80;
            font-weight: 700;
        }

        .highlight-red {
            color: #f87171;
            font-weight: 700;
        }

        /* Poster Footer */
        .poster-footer {
            background: #0d1527;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 16px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 9.5pt;
            color: #94a3b8;
        }

        .footer-left strong {
            color: #f8fafc;
        }
        .footer-right {
            font-family: 'Consolas', monospace;
            color: #38bdf8;
        }
    </style>
</head>
<body>

    <!-- Header Banner -->
    <header class="poster-header">
        <div class="header-left">
            <div class="dept-title">University Dept. of Computer Engineering &bull; BE Semester VII Capstone</div>
            <h1 class="main-title">Ansible-Provisioned Telecom Service Outage Dashboard</h1>
            <div class="subtitle">A Resilient, Containerized NOC Observability Platform with Git Flow, Continuous Testing, Jenkins CI/CD &amp; Idempotent Infrastructure</div>
        </div>
        <div class="header-right">
            <div class="student-name">Manas Akhare</div>
            <div class="student-meta">Roll Number: <span class="meta-highlight">23102C0017</span></div>
            <div class="student-meta">Class: <span class="meta-highlight">BE - VII (CMPN - C)</span> &bull; Sr No: 12</div>
            <div class="student-meta">Academic Year: <span class="meta-highlight">2026-2027</span></div>
        </div>
    </header>

    <!-- Key Metrics Ribbon -->
    <section class="metrics-ribbon">
        <div class="ribbon-card">
            <div class="ribbon-val">15 / 15</div>
            <div class="ribbon-lbl">Tests Passed (100%)</div>
        </div>
        <div class="ribbon-card" style="border-top-color: #10b981;">
            <div class="ribbon-val" style="color: #34d399;">1.85h</div>
            <div class="ribbon-lbl">Optimized MTTR</div>
        </div>
        <div class="ribbon-card" style="border-top-color: #f59e0b;">
            <div class="ribbon-val" style="color: #fbbf24;">188 MB</div>
            <div class="ribbon-lbl">Alpine JRE Image</div>
        </div>
        <div class="ribbon-card" style="border-top-color: #8b5cf6;">
            <div class="ribbon-val" style="color: #a78bfa;">0 Drift</div>
            <div class="ribbon-lbl">Idempotency (changed=0)</div>
        </div>
        <div class="ribbon-card" style="border-top-color: #ef4444;">
            <div class="ribbon-val" style="color: #f87171;">&lt; 8 sec</div>
            <div class="ribbon-lbl">Automated Rollback</div>
        </div>
    </section>

    <!-- 3-Column Main Body -->
    <main class="poster-grid">
        
        <!-- Column 1: Problem & Architecture -->
        <div class="col">
            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#9888;</span>
                    <h2 class="card-title">1. Problem &amp; Telecom Need</h2>
                </div>
                <div class="card-content">
                    <p>Telecom providers manage millions of active subscribers across 5G SA/NSA, 4G LTE, and DWDM fiber backbones. Incidents such as civic fiber excavations or baseband surges cause catastrophic regional drops in circles like Mumbai and Delhi.</p>
                    <p style="margin-top: 6px;"><strong>Existing Bottlenecks:</strong> Siloed alarm systems, 45-min incident ingestion lag, manual SSH deployments prone to configuration drift, and lack of automated quality gates.</p>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#127959;</span>
                    <h2 class="card-title">2. Multi-Tier Architecture</h2>
                </div>
                <div class="card-content">
                    <div class="diagram-box">
                        <div class="flow-step"><strong>Tier 1: Presentation &amp; Ingress</strong><br>Nginx Reverse Proxy (Port 80) &bull; Gzip &bull; Forwarding to Spring Boot</div>
                        <div class="flow-step"><strong>Tier 2: Business Logic &amp; REST</strong><br>Java 17 &bull; Spring Boot 3.2.5 &bull; Embedded Tomcat 10.1 on Port 8085</div>
                        <div class="flow-step"><strong>Tier 3: CI/CD &amp; Testing Quality Gate</strong><br>Jenkins Pipeline as Code &bull; Selenium E2E &bull; JUnit 5 &bull; Maven</div>
                        <div class="flow-step"><strong>Tier 4: Infrastructure &amp; SRE</strong><br>Docker Alpine Container &bull; Ansible Playbooks &bull; Systemd Unit</div>
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#128736;</span>
                    <h2 class="card-title">3. Technology Stack</h2>
                </div>
                <div class="card-content">
                    <div class="tech-pill-container">
                        <span class="tech-pill active">Java 17 LTS</span>
                        <span class="tech-pill active">Spring Boot 3.2</span>
                        <span class="tech-pill active">Thymeleaf 3</span>
                        <span class="tech-pill active">Maven 3.9</span>
                        <span class="tech-pill active">Selenium 4.18</span>
                        <span class="tech-pill active">Headless Chrome</span>
                        <span class="tech-pill active">Jenkins CI/CD</span>
                        <span class="tech-pill active">Docker Alpine</span>
                        <span class="tech-pill active">Ansible 2.x</span>
                        <span class="tech-pill active">Nginx 1.24</span>
                        <span class="tech-pill active">Systemd</span>
                        <span class="tech-pill active">Git Flow</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Column 2: Dashboard MVP & CI/CD Pipeline -->
        <div class="col">
            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#128187;</span>
                    <h2 class="card-title">4. Core Dashboard Capabilities</h2>
                </div>
                <div class="card-content">
                    <div class="diagram-box">
                        <div class="flow-step"><strong>1. Data/Event Entry Modal:</strong> Ingests incident title, circle, towers, affected subscribers, and root cause.</div>
                        <div class="flow-step"><strong>2. Searchable Dashboard:</strong> Real-time sub-second search and multi-attribute circle dropdown filtering.</div>
                        <div class="flow-step"><strong>3. Summary Indicators:</strong> Dynamic KPI telemetry for active outages, MTTR, and SLA adherence.</div>
                        <div class="flow-step"><strong>4. Status Drill-Down:</strong> Detailed modal showing cell towers, SLA countdown, and lifecycle state transitions.</div>
                        <div class="flow-step"><strong>5. Critical Exception Alert View:</strong> High-priority banner isolating active P1 carrier faults (&ge;25k users).</div>
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#128300;</span>
                    <h2 class="card-title">5. Testing Pyramid &amp; Selenium</h2>
                </div>
                <div class="card-content">
                    <p>Automated test suite executing across all three pyramid tiers:</p>
                    <ul style="margin: 6px 0 8px 18px;">
                        <li><strong>6 Unit Tests:</strong> OutageService business logic &amp; SLA calculations.</li>
                        <li><strong>5 MockMvc Tests:</strong> REST endpoint contract validation (200 OK).</li>
                        <li><strong>4 Selenium E2E Journeys:</strong> Navigation, Search, Ingestion, Drill-down in headless Chrome 155.</li>
                        <li><strong>Failure Screenshot Watcher:</strong> Automatically captures PNG on failure.</li>
                    </ul>
                    <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; padding: 6px 12px; border-radius: 6px; font-size: 8.5pt; color: #34d399; font-weight: 600;">
                        &#10004; 15 Tests Executed &bull; 0 Failures &bull; 0 Errors &bull; 19.6s Total Time
                    </div>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#9881;</span>
                    <h2 class="card-title">6. Git Flow &amp; Conflict Resolution</h2>
                </div>
                <div class="card-content">
                    <p>Implemented enterprise Git Flow with Pull Request peer reviews:</p>
                    <div class="diagram-box">
                        <div class="flow-step"><code>feature/outage-reporting</code> &rarr; PR #1 merged to <code>develop</code></div>
                        <div class="flow-step"><code>feature/alert-management</code> &rarr; Intentional conflict on <code>application.properties</code></div>
                        <div class="flow-step">Harmonious resolution committed &bull; Tagged <code>v1.0.0-mvp</code></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Column 3: Docker, Ansible & SRE Results -->
        <div class="col">
            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#128011;</span>
                    <h2 class="card-title">7. Multi-Stage Docker Build</h2>
                </div>
                <div class="card-content">
                    <p>Eliminates image bloat and eliminates attack surfaces:</p>
                    <ul style="margin: 6px 0 8px 18px;">
                        <li><strong>Stage 1 (Builder):</strong> Maven 3.9 + JDK 17 with dependency layer caching to package the 25.4 MB executable JAR.</li>
                        <li><strong>Stage 2 (Runtime):</strong> Minimal Alpine JRE 17 copying only the JAR.</li>
                        <li><strong>Security Hardened:</strong> Runs under unprivileged user <code>telecom</code>.</li>
                        <li><strong>Result:</strong> Image size reduced from 600 MB to <strong>188 MB (68% saving)</strong>.</li>
                    </ul>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#128225;</span>
                    <h2 class="card-title">8. Ansible IaC &amp; Idempotency</h2>
                </div>
                <div class="card-content">
                    <p>Codified server provisioning across 16 discrete tasks:</p>
                    <ul style="margin: 6px 0 8px 18px;">
                        <li>Installs OpenJDK 17, Nginx, UFW, Curl.</li>
                        <li>Renders Systemd supervisor unit &amp; Nginx proxy templates.</li>
                        <li><strong>Idempotency Proof:</strong> Run 1: <code>changed=13</code> &rarr; Run 2: <strong class="highlight-green">changed=0</strong>.</li>
                        <li><strong>Automated Rollback:</strong> <code>rollback.yml</code> restores backup in <strong class="highlight-green">&lt; 8 seconds</strong>.</li>
                    </ul>
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-icon">&#128200;</span>
                    <h2 class="card-title">9. Operational Impact</h2>
                </div>
                <div class="card-content">
                    <table class="mini-table">
                        <thead>
                            <tr>
                                <th>Operational Metric</th>
                                <th>Manual Legacy</th>
                                <th>Our DevOps Solution</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Mean Time to Recovery</td>
                                <td class="highlight-red">4.2 hours</td>
                                <td class="highlight-green">1.85 hours (-56%)</td>
                            </tr>
                            <tr>
                                <td>Server Deployment</td>
                                <td class="highlight-red">45 mins (SSH)</td>
                                <td class="highlight-green">&lt; 3 mins (Ansible)</td>
                            </tr>
                            <tr>
                                <td>Rollback Duration</td>
                                <td class="highlight-red">30-60 mins</td>
                                <td class="highlight-green">&lt; 8 seconds</td>
                            </tr>
                            <tr>
                                <td>Testing Coverage</td>
                                <td class="highlight-red">Manual sample</td>
                                <td class="highlight-green">100% Automated</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="poster-footer">
        <div class="footer-left">
            <strong>Ansible-Provisioned Telecom Service Outage Dashboard</strong> &bull; Student: <strong>Manas Akhare</strong> (Roll: 23102C0017) &bull; Department of Computer Engineering
        </div>
        <div class="footer-right">
            HTTP Status: 200 UP &bull; http://localhost:8085/api/health
        </div>
    </footer>

</body>
</html>
"""

# Write poster HTML
poster_html_path = os.path.abspath("Telecom_Outage_Dashboard_Poster.html")
with open(poster_html_path, "w", encoding="utf-8") as f:
    f.write(poster_html)
print(f"Generated Poster HTML: {poster_html_path}")

# Compile into PDF
poster_pdf_path = os.path.abspath("Telecom_Outage_Dashboard_Poster.pdf")
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_exe):
    chrome_exe = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

print("Compiling Poster PDF...")
cmd_pdf = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={poster_pdf_path}",
    poster_html_path
]
subprocess.run(cmd_pdf, capture_output=True, text=True)
if os.path.exists(poster_pdf_path):
    print(f"SUCCESS: Poster PDF created: {poster_pdf_path} ({os.path.getsize(poster_pdf_path)} bytes)")

# Compile into high-res PNG image screenshot
poster_png_path = os.path.abspath("Telecom_Outage_Dashboard_Poster.png")
print("Compiling Poster high-resolution PNG image...")
cmd_png = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--window-size=1460,2060",
    f"--screenshot={poster_png_path}",
    poster_html_path
]
subprocess.run(cmd_png, capture_output=True, text=True)
if os.path.exists(poster_png_path):
    print(f"SUCCESS: Poster PNG image created: {poster_png_path} ({os.path.getsize(poster_png_path)} bytes)")
