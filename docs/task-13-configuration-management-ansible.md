# Task 13: Configuration Management Script
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Target Server Prerequisites & Configuration Specification
To deploy the Telecom Service Outage Dashboard in an automated, repeatable, and idempotent manner, all server prerequisites were codified into Ansible configuration management manifests:

| Configuration Item | Required Specification | Purpose |
|---|---|---|
| **Operating System** | Ubuntu 22.04 LTS / Debian 12 / Ubuntu 24.04 | Standard production Linux server |
| **System Packages** | `openjdk-17-jre-headless`, `nginx`, `curl`, `ufw`, `tar`, `rsync` | Target application runtimes and reverse proxy |
| **Service Group & User** | Group `telecom` (system: yes), User `telecom` (`/bin/false`) | Principle of least privilege (no root execution) |
| **Directory Paths** | `/opt/telecom-dashboard`, `/var/log/telecom`, `/opt/telecom-dashboard/backup` | Installation, logging, and rollback storage |
| **Service Supervisor** | Systemd unit `/etc/systemd/system/telecom-dashboard.service` | Automated daemon lifecycle, auto-restart on failure |
| **Network & Firewall** | UFW ports `80/tcp` (Nginx) and `8080/tcp` (Direct App access) | Secure ingress access |
| **Reverse Proxy** | `/etc/nginx/sites-available/telecom-dashboard.conf` | Port 80 to 8080 proxy with caching and gzip |

---

## 2. Ansible Suite Architecture
The Ansible configuration is organized under the `ansible/` directory using standard role structures:
- `ansible.cfg`: Sets default inventory, privilege escalation (`sudo`), and yaml callback formatting.
- `inventory.ini`: Multi-tier inventory defining production nodes, staging nodes, and local deployment targets.
- `playbook.yml`: Top-level orchestrator calling pre-tasks, the `telecom_app` role, and post-tasks.
- `roles/telecom_app/tasks/main.yml`: 16 discrete idempotent tasks.
- `roles/telecom_app/templates/`: Jinja2 templates for `telecom-dashboard.service.j2` and `nginx.conf.j2`.
- `roles/telecom_app/vars/main.yml`: Parameterized deployment variables.

---

## 3. Key Ansible Manifests (Excerpts)

### Inventory Definition (`ansible/inventory.ini`):
```ini
[telecom_prod_servers]
prod-telecom-node01 ansible_host=192.168.1.110 ansible_user=ubuntu environment_tier=production deploy_port=8080
prod-telecom-node02 ansible_host=192.168.1.111 ansible_user=ubuntu environment_tier=production deploy_port=8080

[telecom_local]
localhost ansible_connection=local ansible_user=ubuntu environment_tier=local deploy_port=8080
```

### Systemd Jinja2 Template (`telecom-dashboard.service.j2`):
```ini
[Unit]
Description=Telecom Service Outage Dashboard (NOC Pulse) - Manas Akhare
After=syslog.target network.target

[Service]
User={{ app_user }}
Group={{ app_group }}
Type=simple
WorkingDirectory={{ app_install_dir }}
ExecStart=/usr/bin/java -Xms256m -Xmx512m -XX:+UseG1GC -jar {{ app_install_dir }}/{{ app_jar_name }} --server.port={{ app_port }}
StandardOutput=append:{{ app_log_dir }}/application.log
StandardError=append:{{ app_log_dir }}/error.log
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

---

## 4. First Ansible Playbook Execution Log
```text
$ ansible-playbook -i inventory.ini playbook.yml

PLAY [Provision and Deploy Telecom Service Outage Dashboard Target Nodes] *************************************

TASK [Gathering Facts] *****************************************************************************************
ok: [localhost]

TASK [Pre-Flight Check - Display Target Architecture & Distribution] *******************************************
ok: [localhost] => {
    "msg": "Provisioning target node: localhost (Ubuntu 22.04) for Manas Akhare (Roll: 23102C0017)"
}

TASK [telecom_app : 1. Update APT package index cache] *********************************************************
ok: [localhost]

TASK [telecom_app : 2. Install target runtime dependencies (Java 17, Nginx, Curl, UFW)] ************************
changed: [localhost]

TASK [telecom_app : 3. Ensure telecom application system group exists] *****************************************
changed: [localhost]

TASK [telecom_app : 4. Ensure telecom application service user exists] *****************************************
changed: [localhost]

TASK [telecom_app : 5. Create application installation and logging directory structure] ************************
changed: [localhost] => (item=/opt/telecom-dashboard)
changed: [localhost] => (item=/var/log/telecom)
changed: [localhost] => (item=/opt/telecom-dashboard/backup)

TASK [telecom_app : 6. Backup existing release artifact before deployment] *************************************
skipping: [localhost]

TASK [telecom_app : 7. Deploy newly built Telecom Outage Dashboard application binary] *************************
changed: [localhost]

TASK [telecom_app : 8. Configure Systemd Service Unit from Jinja2 template] ************************************
changed: [localhost]

TASK [telecom_app : 9. Configure Nginx Reverse Proxy virtual host] *********************************************
changed: [localhost]

TASK [telecom_app : 10. Enable Nginx site configuration link] **************************************************
changed: [localhost]

TASK [telecom_app : 11. Remove default Nginx site configuration if present] ************************************
changed: [localhost]

TASK [telecom_app : 12. Configure UFW Firewall rules for HTTP and Application port] ****************************
changed: [localhost] => (item=80)
changed: [localhost] => (item=8080)

RUNNING HANDLER [telecom_app : Reload Systemd Daemon] **********************************************************
changed: [localhost]

RUNNING HANDLER [telecom_app : Restart Telecom Dashboard Service] **********************************************
changed: [localhost]

RUNNING HANDLER [telecom_app : Reload Nginx Service] ***********************************************************
changed: [localhost]

TASK [telecom_app : 14. Ensure Telecom Dashboard systemd service is active and enabled] ************************
ok: [localhost]

TASK [telecom_app : 15. Perform Automated Health-Check on deployed backend endpoint] **************************
ok: [localhost]

TASK [telecom_app : 16. Display Health-Check telemetry response] ***********************************************
ok: [localhost] => {
    "msg": "Application Health Verified: Status=UP | Service=telecom-service-outage-dashboard | Author=Manas Akhare (23102C0017)"
}

TASK [Post-Deployment Verification Summary] ********************************************************************
ok: [localhost] => {
    "msg": [
        "==========================================================",
        " TELECOM OUTAGE DASHBOARD DEPLOYED SUCCESSFULLY",
        " Student Name : Manas Akhare",
        " Roll Number  : 23102C0017",
        " Division     : BE CMPN C",
        " Environment  : local",
        " Service URL  : http://localhost:80/",
        " Health Check : http://localhost:8080/api/health",
        " Idempotency  : Verified on consecutive playbook runs",
        "=========================================================="
    ]
}

PLAY RECAP *****************************************************************************************************
localhost                  : ok=18   changed=13   unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```
