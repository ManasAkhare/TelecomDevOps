// Telecom Outage Dashboard Client Controller

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

// Close modal when clicking on backdrop
window.onclick = function(event) {
    if (event.target.classList.contains('modal-backdrop')) {
        event.target.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
};

// Client-side instant live filtering
function clientSideFilter() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.querySelectorAll('#outageTableBody .outage-row');
    let visibleCount = 0;

    rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        if (text.includes(query)) {
            row.style.display = '';
            visibleCount++;
        } else {
            row.style.display = 'none';
        }
    });

    const countDisplay = document.getElementById('outageCountDisplay');
    if (countDisplay) {
        countDisplay.innerText = visibleCount;
    }
}

// Open and populate Status Drill-Down Modal
function openDrillDownFromElement(element) {
    const id = element.getAttribute('data-id');
    const title = element.getAttribute('data-title');
    const region = element.getAttribute('data-region');
    const service = element.getAttribute('data-service');
    const severity = element.getAttribute('data-severity');
    const status = element.getAttribute('data-status');
    const subscribers = element.getAttribute('data-subscribers');
    const towers = element.getAttribute('data-towers');
    const cause = element.getAttribute('data-cause');
    const time = element.getAttribute('data-time');
    const notes = element.getAttribute('data-notes');

    document.getElementById('modalDrillDownId').innerText = id || 'N/A';
    document.getElementById('modalDrillDownTitle').innerText = title || 'Incident Details';
    document.getElementById('modalDrillDownRegion').innerText = region || 'N/A';
    document.getElementById('modalDrillDownService').innerText = service || 'N/A';
    document.getElementById('modalDrillDownSeverity').innerText = severity || 'N/A';
    document.getElementById('modalDrillDownStatus').innerText = status || 'N/A';
    document.getElementById('modalDrillDownSubscribers').innerText = subscribers ? Number(subscribers).toLocaleString() + ' Users' : '0';
    document.getElementById('modalDrillDownTime').innerText = time || 'N/A';
    document.getElementById('modalDrillDownCause').innerText = cause || 'Investigation ongoing.';
    document.getElementById('modalDrillDownNotes').innerText = notes || 'No field notes logged yet.';

    // Populate towers as pills
    const towerContainer = document.getElementById('modalDrillDownTowers');
    towerContainer.innerHTML = '';
    if (towers && towers.trim().length > 0) {
        const towerList = towers.split(',');
        towerList.forEach(t => {
            const span = document.createElement('span');
            span.className = 'tower-pill';
            span.innerText = t.trim();
            towerContainer.appendChild(span);
        });
    } else {
        towerContainer.innerText = 'All BSS Sectors in Circle';
    }

    // Set form action for status transition
    const form = document.getElementById('updateStatusForm');
    if (form) {
        form.action = '/outages/' + id + '/update-status';
    }

    openModal('drillDownModal');
}

console.log('Telecom Service Outage Dashboard initialized. Ready for NOC telemetry.');
