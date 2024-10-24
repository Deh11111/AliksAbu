document.getElementById('start').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        // Выполняем скрипт на активной вкладке
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: openAndNavigateToAliExpress
        });
    });
});

function openAndNavigateToAliExpress() {
    const url = 'https://www.aliexpress.com/p/address-manage/index.html';
    window.location.href = url;
}
