document.getElementById('open-url').addEventListener('click', function() {
    chrome.tabs.create({ url: 'https://www.aliexpress.com/account/setting/index.html' });
});

document.getElementById('login-google').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: clickGoogleLogin
        });
    });
});

function clickGoogleLogin() {
    const googleLoginButton = document.querySelector('a.fm-sns-new-item.google');
    if (googleLoginButton) {
        googleLoginButton.click();
    } else {
        console.log('Google login button not found.');
    }
}
