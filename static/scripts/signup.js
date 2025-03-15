function signup() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
  
    // Basic validation
    if (!name || !email || !username || !password) {
      alert("Please fill in all fields.");
      return;
    }
  
    // Send signup request to the server
    fetch("/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email, username, password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Signup successful! Please login.");
          window.location.href = "/login"; // Redirect to login page
        } else {
          alert(data.message || "Signup failed. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
      });
  }