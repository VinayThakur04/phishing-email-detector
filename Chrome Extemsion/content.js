function getEmailData() {
    let email = {
        from: document.querySelector('.gD').textContent,
        subject: document.querySelector('.hP').textContent,
        body: document.querySelector('.a3s').innerText
    };
    return email;
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getEmailData") {
        const emailData = getEmailData();
        sendResponse(emailData);
    }
});
