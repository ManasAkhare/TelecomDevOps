package com.telecom.outage.controller;

import com.telecom.outage.model.*;
import com.telecom.outage.service.OutageService;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.List;

@Controller
public class OutageController {

    private final OutageService outageService;

    public OutageController(OutageService outageService) {
        this.outageService = outageService;
    }

    @GetMapping("/")
    public String index(
            @RequestParam(required = false) String search,
            @RequestParam(required = false) String region,
            @RequestParam(required = false) OutageSeverity severity,
            @RequestParam(required = false) OutageStatus status,
            @RequestParam(required = false) ServiceType serviceType,
            Model model) {

        List<Outage> outages = outageService.searchAndFilter(search, region, severity, status, serviceType);
        DashboardMetrics metrics = outageService.getDashboardMetrics();
        List<Outage> criticalAlerts = outageService.getCriticalAlerts();

        model.addAttribute("outages", outages);
        model.addAttribute("metrics", metrics);
        model.addAttribute("criticalAlerts", criticalAlerts);
        model.addAttribute("newOutage", new Outage());
        model.addAttribute("serviceTypes", ServiceType.values());
        model.addAttribute("severities", OutageSeverity.values());
        model.addAttribute("statuses", OutageStatus.values());
        model.addAttribute("currentSearch", search != null ? search : "");
        model.addAttribute("currentRegion", region != null ? region : "");
        model.addAttribute("currentSeverity", severity);
        model.addAttribute("currentStatus", status);

        return "dashboard";
    }

    @PostMapping("/outages/create")
    public String createOutage(@Valid @ModelAttribute("newOutage") Outage outage,
                               BindingResult bindingResult,
                               RedirectAttributes redirectAttributes,
                               Model model) {
        if (bindingResult.hasErrors()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Validation failed! Please provide all required fields.");
            return "redirect:/";
        }
        outageService.createOutage(outage);
        redirectAttributes.addFlashAttribute("successMessage", "Incident " + outage.getId() + " logged successfully into NOC Dispatch.");
        return "redirect:/";
    }

    @PostMapping("/outages/{id}/update-status")
    public String updateStatus(@PathVariable String id,
                               @RequestParam OutageStatus status,
                               @RequestParam(required = false) String notes,
                               RedirectAttributes redirectAttributes) {
        outageService.updateOutageStatus(id, status, notes);
        redirectAttributes.addFlashAttribute("successMessage", "Outage " + id + " status transitioned to " + status.getLabel() + ".");
        return "redirect:/";
    }

    @PostMapping("/outages/{id}/delete")
    public String deleteOutage(@PathVariable String id, RedirectAttributes redirectAttributes) {
        outageService.deleteOutage(id);
        redirectAttributes.addFlashAttribute("successMessage", "Incident " + id + " has been archived.");
        return "redirect:/";
    }
}
