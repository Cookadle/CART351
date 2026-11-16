const confessionForm = document.getElementById("confession-form");
const confessionInput = document.getElementById("confession-input");
const statusMessage = document.getElementById("status-message");
const oracleButton = document.getElementById("oracle-button");
const oracleOutput = document.getElementById("oracle-output");

if (confessionForm && confessionInput) { //CHECK form and date entered
    confessionForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        //trim whitespace etc
        const text = confessionInput.value.trim();
        if (!text) {
            if (statusMessage) {
                statusMessage.textContent = "Please write a confession first.";
            }
            return;
        }


        try { //send confession json to confess
            const response = await fetch("/confess", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text }),
            });
            //parse data
            const data = await response.json();

            //confession saved and okay 
            if (response.status === 201) {
                confessionInput.value = ""; //reset text 4 next confession
                if (statusMessage) {
                    statusMessage.textContent = "Confession whispered to thy oracle.";
                }
            } else if (statusMessage) {
                statusMessage.textContent = data.error || "Could not save thy confession.";
            }
        } catch (err) { //network horror
            if (statusMessage) {
                statusMessage.textContent = "Network error! Check that Flask is running.";
            }
        }
    });
}

if (oracleButton && oracleOutput) {
    oracleButton.addEventListener("click", async () => {
        oracleOutput.textContent = "Listening to thy oracle...";

        try {
            //fetch confession
            const response = await fetch("/oracle");
            const data = await response.json();

            if (response.status === 200) {
                const fortuneBlock = data.fortune
                    ? `<p class="oracle-fortune"><strong>Fortune:</strong> ${data.fortune}</p>`
                    : "";
                //echoed status
                oracleOutput.innerHTML = `
          ${fortuneBlock} 
          <blockquote class="oracle-confession">"${data.text}"</blockquote>
          <small>Echoed ${data.times_given} time(s)</small>
        `;
            } else {
                oracleOutput.textContent = data.error || "Could not reach thy oracle.";
            }
        } catch (err) { //network horror
            oracleOutput.textContent = "Network error! Check that Flask is running.";
        }
    });
}