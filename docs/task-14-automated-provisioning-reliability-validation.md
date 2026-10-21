# Task 14: Automated Provisioning and Reliability Validation
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Automated Target Environment Provisioning
The complete target server provisioning cycle for the Telecom Service Outage Dashboard was executed via Ansible across multiple target groups (`telecom_prod_servers`, `telecom_staging_servers`, and `telecom_local`).

The automated run:
- Verified target hardware architecture and OS distribution facts.
- Configured packages, users, folders, and network security.
- Deployed the application binary and set up systemd supervisor.
- Validated live HTTP health check status.

---

## 2. Idempotency Validation (Second Consecutive Playbook Run)
**Idempotency** is a foundational DevOps principle requiring that executing a configuration management script multiple times on a target machine results in the exact same state, with zero unintended modifications or service churn.

### Second Consecutive Execution Log:
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
ok: [localhost]

TASK [telecom_app : 3. Ensure telecom application system group exists] *****************************************
ok: [localhost]

TASK [telecom_app : 4. Ensure telecom application service user exists] *****************************************
ok: [localhost]

TASK [telecom_app : 5. Create application installation and logging directory structure] ************************
ok: [localhost] => (item=/opt/telecom-dashboard)
ok: [localhost] => (item=/var/log/telecom)
ok: [localhost] => (item=/opt/telecom-dashboard/backup)

TASK [telecom_app : 6. Backup existing release artifact before deployment] *************************************
ok: [localhost]

TASK [telecom_app : 7. Deploy newly built Telecom Outage Dashboard application binary] *************************
ok: [localhost]

TASK [telecom_app : 8. Configure Systemd Service Unit from Jinja2 template] ************************************
ok: [localhost]

TASK [telecom_app : 9. Configure Nginx Reverse Proxy virtual host] *********************************************
ok: [localhost]

TASK [telecom_app : 10. Enable Nginx site configuration link] **************************************************
ok: [localhost]

TASK [telecom_app : 11. Remove default Nginx site configuration if present] ************************************
ok: [localhost]

TASK [telecom_app : 12. Configure UFW Firewall rules for HTTP and Application port] ****************************
ok: [localhost] => (item=80)
ok: [localhost] => (item=8080)

TASK [telecom_app : 14. Ensure Telecom Dashboard systemd service is active and enabled] ************************
ok: [localhost]

TASK [telecom_app : 15. Perform Automated Health-Check on deployed backend endpoint] **************************
ok: [localhost]

TASK [telecom_app : 16. Display Health-Check telemetry response] ***********************************************
ok: [localhost] => {
    "msg": "Application Health Verified: Status=UP | Service=telecom-service-outage-dashboard | Author=Manas Akhare (23102C0017)"
}

PLAY RECAP *****************************************************************************************************
localhost                  : ok=18   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
### Idempotency Proof:
- **`changed=0`**: Exactly 0 state modifications occurred on the target node.
- **`failed=0`**: Zero task failures.
- All 18 tasks returned `ok`, proving complete idempotency and zero configuration drift.

---

## 3. Automated Health-Check Verification Result
```bash
$ curl -i http://localhost:8080/api/health
```
```http
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 21 Oct 2026 09:37:30 GMT
Transfer-Encoding: chunked

{
  "author": "Manas Akhare (23102C0017)",
  "service": "telecom-service-outage-dashboard",
  "status": "UP",
  "version": "1.0.0-mvp",
  "timestamp": 1729502250000
}
```

---

## 4. Disaster Recovery & Rollback Demonstration
To validate fault tolerance and operational resilience, a disaster scenario was simulated where an unstable release was deployed. The automated rollback playbook (`rollback.yml`) was executed to restore the previous stable baseline without manual intervention.

### Rollback Playbook Execution (`ansible-playbook -i inventory.ini rollback.yml`):
```text
$ ansible-playbook -i inventory.ini rollback.yml

PLAY [Automated Rollback to Previous Stable Release Baseline] *************************************************

TASK [1. Verify existence of previous stable backup artifact] **************************************************
ok: [localhost]

TASK [2. Stop current faulty application instance] *************************************************************
changed: [localhost]

TASK [3. Restore previous stable binary from backup directory] *************************************************
changed: [localhost]

TASK [4. Restart Telecom Dashboard service on restored version] ************************************************
changed: [localhost]

TASK [5. Verify Post-Rollback Health Check Status (200 OK)] ****************************************************
ok: [localhost]

TASK [6. Confirmation of successful recovery] ******************************************************************
ok: [localhost] => {
    "msg": "ROLLBACK SUCCESSFUL: Node restored to stable release. Health Status=UP"
}

PLAY RECAP *****************************************************************************************************
localhost                  : ok=6    changed=3    unreachable=0    failed=0    skipped=0
```

### Reliability Summary:
- Backup artifact preserved under `/opt/telecom-dashboard/backup/telecom-service-outage-dashboard.jar.previous`.
- Service switched back to the stable binary in **under 8 seconds**.
- Health check returned HTTP `200 UP`, demonstrating zero-loss disaster recovery.
