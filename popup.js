document.getElementById('open-url').addEventListener('click', function() {
    chrome.tabs.create({ url: 'https://login.aliexpress.com/?returnUrl=https%3A%2F%2Fwww.aliexpress.com%2Faccount%2Fsetting%2Findex.html%3Fspm%3Da2g0o.home.headerAcount.7.67db76dba1hp53' });
});

document.getElementById('login-google').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        // Отправляем сообщение на выполнение симуляции логина через Google
        chrome.tabs.sendMessage(tabs[0].id, { action: 'login-google' });
    });
});

document.getElementById('login').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        // Отправляем сообщение на выполнение симуляции логина через Google
        chrome.tabs.sendMessage(tabs[0].id, { action: 'login' });
    });
});