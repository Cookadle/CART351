const oracleButton = document.getElementById("oracle-button");
const oracleOutput = document.getElementById("oracle-output");

oracleButton.addEventListener("click", async () => {
  oracleOutput.textContent = "Listening to the oracle...";

  try {
    const response = await fetch("/oracle");
    const data = await response.json();

    if (response.status === 200) {
      oracleOutput.innerHTML = `
        <p class="oracle-confession">"${data.text}"</p>
        <small>Echoed ${data.times_given} time(s)</small>
      `;
    } else {
      oracleOutput.textContent = data.error || "Could not reach the oracle.";
    }
  } catch (err) {
    oracleOutput.textContent = "Network error—check that Flask is running.";
  }
});