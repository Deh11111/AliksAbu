// Функция ожидания элемента на странице
async function waitForElement(selector, timeout = 10000) {
    const start = Date.now();
    while (Date.now() - start < timeout) {
        const element = document.querySelector(selector);
        if (element) return element;
        await new Promise(resolve => setTimeout(resolve, 100)); // Ждем 100мс перед повторной проверкой
    }
    throw new Error(`Element ${selector} не найден за ${timeout / 1000} секунд`);
}

// Функция для симуляции входа через Google
async function simulateMouseClickAndLogin() {
    try {
        // Находим кнопку для входа через Google на AliExpress
        const googleLoginButton = await waitForElement('a.fm-sns-new-item.google');
        googleLoginButton.click(); // Симулируем клик

    } catch (error) {
        console.error(error.message);
    }
}


async function Fill_email() {
    // Ожидаем появления поля для email
    emailInput = document.getElementById('identifierId');
    emailInput.value = 'conellmarie961@gmail.com'; // Вводим email
    emailInput.dispatchEvent(new Event('input', { bubbles: true }));

    setTimeout(() => {
        // Выбираем кнопку "Tālāk"
        const nextButton = document.getElementById('identifierNext'); // Выбор по атрибуту jsname

        if (nextButton) {
            nextButton.click(); // Кликаем на кнопку "Tālāk"
        } else {
            console.log('Кнопка "Tālāk" не найдена.');
        }
    }, 1000); // Пауза в 1 секунду
    
    // Ждем 3 секунды перед вводом пароля
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Ожидаем появления поля для ввода пароля
    const passwordInput = await waitForElement('input[type="password"]', 10000);
    passwordInput.value = 'paravoz1k'; // Вводим пароль
    passwordInput.dispatchEvent(new Event('input', { bubbles: true }));
   
   
    // Находим кнопку "Далее" для пароля и кликаем
   
    const nextButton = await waitForElement('#passwordNext', 10000);
    nextButton.click();
}

// Слушаем сообщения из popup.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'login-google') {
        simulateMouseClickAndLogin(); // Запускаем функцию симуляции входа через Google
    }
});

// Слушаем сообщения из popup.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'login') {
        Fill_email(); // Запускаем функцию симуляции входа через Google
    }
});