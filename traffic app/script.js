async function predict() {
  const vehicleCount = document.getElementById("vehicleCount").value;
  const timeOfDay = document.getElementById("timeOfDay").value;

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      vehicle_count: parseInt(vehicleCount),
      time_of_day: timeOfDay
    })
  });

  const data = await response.json();

  if (data.prediction) {
    document.getElementById("output").innerText = `Prediction: ${data.prediction}`;
  } else if (data.error) {
    document.getElementById("output").innerText = `Error: ${data.error}`;
  } else {
    document.getElementById("output").innerText = "Unexpected error occurred.";
  }
}
