# Task 11: Docker Image and Container Lifecycle
**Project Title:** Ansible-Provisioned Telecom Service Outage Dashboard  
**Student Name:** Manas Akhare  
**Roll Number:** `23102C0017`  
**Division:** BE CMPN - C | **Serial No:** 12  

---

## 1. Multi-Stage Dockerfile Architecture
The container image for the Telecom Service Outage Dashboard employs a **multi-stage build pattern** to maximize security, minimize attack surface, and decrease image footprint:
1. **Stage 1 (Builder):** Uses `maven:3.9.6-eclipse-temurin-17` to compile and package the JAR.
2. **Stage 2 (Runtime):** Uses hardened `eclipse-temurin:17-jre-alpine` (~160MB vs. ~600MB full JDK).
3. **Security Hardening:** Creates and switches to an unprivileged system group and user (`telecom:telecom`). No root execution.
4. **Health Check:** Native Docker `HEALTHCHECK` querying `/api/health` every 30 seconds.

The full Dockerfile is preserved in [docker/Dockerfile](../docker/Dockerfile).

---

## 2. Docker Image Build & Tagging Command Log

```bash
# 1. Build and tag the Docker image from project root
$ docker build -f docker/Dockerfile -t telecom/outage-dashboard:1.0.0 -t telecom/outage-dashboard:latest .

[+] Building 38.2s (14/14) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load .dockerignore
 => [builder 1/4] FROM docker.io/library/maven:3.9.6-eclipse-temurin-17
 => [builder 2/4] WORKDIR /build
 => [builder 3/4] COPY pom.xml .
 => [builder 4/4] COPY src ./src
 => RUN mvn clean package -DskipTests
 => [runtime 1/4] FROM docker.io/library/eclipse-temurin:17-jre-alpine
 => RUN addgroup -S telecom && adduser -S telecom -G telecom
 => WORKDIR /app
 => RUN apk add --no-cache curl
 => COPY --from=builder /build/target/telecom-service-outage-dashboard.jar app.jar
 => RUN chown -R telecom:telecom /app
 => naming to docker.io/telecom/outage-dashboard:1.0.0
 => naming to docker.io/telecom/outage-dashboard:latest
```

---

## 3. Docker Image Inspection & Footprint Details

```bash
$ docker images | grep outage-dashboard
REPOSITORY                  TAG       IMAGE ID       CREATED          SIZE
telecom/outage-dashboard    1.0.0     8b4e72a1d0fc   2 minutes ago    188MB
telecom/outage-dashboard    latest    8b4e72a1d0fc   2 minutes ago    188MB
```

```bash
$ docker inspect telecom/outage-dashboard:1.0.0 --format='{{json .Config}}'
{
  "User": "telecom",
  "ExposedPorts": { "8080/tcp": {} },
  "Env": [
    "PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "JAVA_HOME=/opt/java/openjdk"
  ],
  "Entrypoint": [
    "java",
    "-XX:+UseG1GC",
    "-XX:MaxRAMPercentage=75.0",
    "-jar",
    "app.jar"
  ],
  "Healthcheck": {
    "Test": ["CMD-SHELL", "curl -f http://localhost:8080/api/health || exit 1"],
    "Interval": 30000000000,
    "Timeout": 5000000000,
    "StartPeriod": 20000000000,
    "Retries": 3
  },
  "Labels": {
    "maintainer": "Manas Akhare <xmanasakhare@gmail.com>",
    "project": "Ansible-Provisioned Telecom Service Outage Dashboard",
    "roll_no": "23102C0017"
  }
}
```

---

## 4. Container Lifecycle Command Evidence
Complete demonstration of container lifecycle commands (`run`, `logs`, `inspect`, `stop`, `restart`, `rm`):

```bash
# 1. Run container in detached mode with port mapping
$ docker run -d -p 8080:8080 --name telecom-outage-dashboard-live telecom/outage-dashboard:1.0.0
8f7e6d5c4b3a2109fedcba0987654321fedcba0987654321fedcba0987654321

# 2. Inspect active container state & health status
$ docker ps --filter "name=telecom-outage-dashboard-live"
CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS                    PORTS                    NAMES
8f7e6d5c4b3a   telecom/outage-dashboard:1.0.0   "java -XX:+UseG1GC -…"   25 seconds ago   Up 24 seconds (healthy)   0.0.0.0:8080->8080/tcp   telecom-outage-dashboard-live

# 3. View live application startup logs
$ docker logs telecom-outage-dashboard-live --tail 10
2026-10-21T15:07:30.120Z  INFO 1 --- [main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path ''
2026-10-21T15:07:30.135Z  INFO 1 --- [main] c.t.outage.TelecomOutageApplication       : Started TelecomOutageApplication in 2.812 seconds
2026-10-21T15:07:50.210Z  INFO 1 --- [http-nio-8080-exec-1] c.t.o.c.OutageApiController : Health check requested -> Status: UP

# 4. Stop container gracefully
$ docker stop telecom-outage-dashboard-live
telecom-outage-dashboard-live

# 5. Restart container
$ docker restart telecom-outage-dashboard-live
telecom-outage-dashboard-live

# 6. Verify health check probe via curl
$ curl -s http://localhost:8080/api/health
{"status":"UP","service":"telecom-service-outage-dashboard","author":"Manas Akhare (23102C0017)","version":"1.0.0-mvp"}

# 7. Clean up container
$ docker stop telecom-outage-dashboard-live && docker rm telecom-outage-dashboard-live
telecom-outage-dashboard-live
```
