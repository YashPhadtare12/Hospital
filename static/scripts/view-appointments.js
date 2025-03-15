function searchAppointments() {
    const searchTerm = document.getElementById("search").value.toLowerCase();
    const rows = document.querySelectorAll("#appointment-table tbody tr");
  
    rows.forEach((row) => {
      const patientName = row.querySelector("td[data-label='Patient Name']").textContent.toLowerCase();
      if (patientName.includes(searchTerm)) {
        row.style.display = "";
      } else {
        row.style.display = "none";
      }
    });
  }
  
  function exportAppointments() {
    const rows = document.querySelectorAll("#appointment-table tbody tr");
    let csvContent = "Patient Name,Doctor,Date,Time,Status\n";
  
    rows.forEach((row) => {
      const patientName = row.querySelector("td[data-label='Patient Name']").textContent;
      const doctor = row.querySelector("td[data-label='Doctor']").textContent;
      const date = row.querySelector("td[data-label='Date']").textContent;
      const time = row.querySelector("td[data-label='Time']").textContent;
      const status = row.querySelector("td[data-label='Status']").textContent;
      csvContent += `${patientName},${doctor},${date},${time},${status}\n`;
    });
  
    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "appointments.csv";
    a.click();
    URL.revokeObjectURL(url);
  }