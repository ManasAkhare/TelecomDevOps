# ==========================================
# Telecom Service Outage Dashboard - Dockerfile
# Author: Manas Akhare (Roll: 23102C0017)
# Multi-Stage Production Build
# ==========================================

# Stage 1: Build & Package
FROM maven:3.9.6-eclipse-temurin-17 AS builder
WORKDIR /build

COPY pom.xml .
# Download dependencies layer for Docker build caching
RUN mvn dependency:go-offline -B

COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Minimal Distroless / Hardened Runtime
FROM eclipse-temurin:17-jre-alpine AS runtime
LABEL maintainer="Manas Akhare <xmanasakhare@gmail.com>"
LABEL project="Ansible-Provisioned Telecom Service Outage Dashboard"
LABEL roll_no="23102C0017"

# Create unprivileged application user
RUN addgroup -S telecom && adduser -S telecom -G telecom

WORKDIR /app

# Install curl for container health check
RUN apk add --no-cache curl

# Copy packaged jar from builder
COPY --from=builder /build/target/telecom-service-outage-dashboard.jar app.jar
RUN chown -R telecom:telecom /app

USER telecom

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -f http://localhost:8080/api/health || exit 1

ENTRYPOINT ["java", "-XX:+UseG1GC", "-XX:MaxRAMPercentage=75.0", "-jar", "app.jar"]
