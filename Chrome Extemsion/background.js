chrome.runtime.onInstalled.addListener(() => {
    console.log("Phishing Email Detector Extension Installed");
  });
  
  chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.create({ url: "popup.html" });
  });
  