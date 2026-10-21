package com.telecom.outage;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
@DisplayName("Telecom Outage REST API Integration Test Suite")
class OutageApiControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    @DisplayName("API Test 1: Health Endpoint Returns UP Status")
    void testHealthEndpoint() throws Exception {
        mockMvc.perform(get("/api/health"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.status", is("UP")))
                .andExpect(jsonPath("$.author", containsString("Manas Akhare")));
    }

    @Test
    @DisplayName("API Test 2: List Outages Returns JSON Array")
    void testListOutages() throws Exception {
        mockMvc.perform(get("/api/outages"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(greaterThanOrEqualTo(5))))
                .andExpect(jsonPath("$[0].id", notNullValue()));
    }

    @Test
    @DisplayName("API Test 3: Get Outage By ID Returns Correct Incident")
    void testGetOutageById() throws Exception {
        mockMvc.perform(get("/api/outages/OUT-1001"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id", is("OUT-1001")))
                .andExpect(jsonPath("$.region", is("Mumbai Metro")));
    }

    @Test
    @DisplayName("API Test 4: Dashboard Metrics Endpoint Aggregates Data")
    void testGetMetrics() throws Exception {
        mockMvc.perform(get("/api/metrics"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.totalOutages", greaterThanOrEqualTo(5)))
                .andExpect(jsonPath("$.activeOutages", greaterThan(0)));
    }

    @Test
    @DisplayName("API Test 5: Critical Alerts Endpoint Filters High Severity Outages")
    void testGetCriticalAlerts() throws Exception {
        mockMvc.perform(get("/api/alerts"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].severity", is("CRITICAL")));
    }
}
