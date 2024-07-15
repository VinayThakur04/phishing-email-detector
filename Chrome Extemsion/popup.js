document.getElementById("checkEmail").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "getEmailData" }, (response) => {
            fetch("https://phisingemaildetector.vercel.app/detect", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(response)
            })
                .then(res => res.json())
                .then(data => {
                    const resultDiv = document.getElementById("result");
                    resultDiv.classList.remove("hidden");
                    resultDiv.innerHTML = formatResults(response, data);
                })
                .catch(error => console.error("Error:", error));
        });
    });
});

function formatResults(email, results) {
    let resultHTML = `<h2>Detection Results</h2>
        <p><strong>From:</strong> ${email.from}</p>
        <p><strong>Subject:</strong> ${email.subject}</p>
        <p><strong>Body:</strong> ${email.body}</p>
        <h3>Phishing Detection:</h3>
        <ul>`;

    for (const [rule, result] of Object.entries(results)) {
        resultHTML += `<li><strong>${rule.replace(/_/g, ' ')}:</strong> ${result ? 'Suspicious' : 'Safe'}</li>`;
    }

    resultHTML += '</ul>';
    return resultHTML;
}
