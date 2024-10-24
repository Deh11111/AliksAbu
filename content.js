// Функция ожидания элемента на странице
async function waitForElement(selector, timeout = 100000) {
    const start = Date.now();
    while (Date.now() - start < timeout) {
        const element = document.querySelector(selector);
        if (element) return element;
        await new Promise(resolve => setTimeout(resolve, 1000)); // Ждем 100мс перед повторной проверкой
    }
    throw new Error(`Element ${selector} не найден за ${timeout / 1000} секунд`);
}

// Функция для симуляции входа через Google
async function simulateMouseClickAndLogin() {
    try {
        // Находим кнопку для входа через Google на AliExpress
        // const googleLoginButton = await waitForElement('a.fm-sns-new-item.google');
        const googleLoginButton =  await waitForElement('a._1unVQ._2vtTC');
        console.log(googleLoginButton);
        googleLoginButton.click(); // Симулируем клик

    } catch (error) {
        console.error(error.message);
    }
}


async function enterEmail() {
    try {
        // Ожидаем появления поля для email
        console.log("Ожидаем поле для email...");
        const emailInput = await waitForElement('#identifierId'); // Ожидаем, пока элемент будет доступен
        console.log("Поле для email найдено.");

        emailInput.value = 'lauxzhenqian@gmail.com'; // Вводим email
        console.log("Email введен: lauxzhenqian@gmail.com");
        emailInput.dispatchEvent(new Event('input', { bubbles: true }));

        // Ждем 2 секунды, чтобы убедиться, что данные ввели
        console.log("Ожидаем 2 секунды перед нажатием кнопки 'Далее'...");
        await new Promise(resolve => setTimeout(resolve, 2000)); 

        // Выбираем кнопку "Tālāk" и кликаем
        console.log("Ищем кнопку 'Далее'...");
        const nextButton = await waitForElement('#identifierNext'); // Ждем, пока кнопка станет доступной
        console.log("Кнопка 'Далее' найдена.");
        nextButton.click(); // Симулируем клик
        console.log("Кнопка 'Далее' нажата.");
    } catch (error) {
        console.error('Ошибка при вводе email:', error.message);
    }
}

async function enterPassword() {
    try {
        // Ждем 8 секунд перед вводом пароля
        console.log("Ожидаем 8 секунд перед вводом пароля...");
        await new Promise(resolve => setTimeout(resolve, 8000)); 

        // Ожидаем появления поля для ввода пароля
        console.log("Ожидаем поле для ввода пароля...");
        const passwordInput = await waitForElement('input[type="password"]', 10000);
        console.log("Поле для ввода пароля найдено.");
        
        passwordInput.value = 'paravoz1k'; // Вводим пароль
        console.log("Пароль введен.");
        passwordInput.dispatchEvent(new Event('input', { bubbles: true }));

        // Ждем 2 секунды перед нажатием кнопки "Далее"
        console.log("Ожидаем 2 секунды перед нажатием кнопки 'Далее' для пароля...");
        await new Promise(resolve => setTimeout(resolve, 2000)); 

        // Находим кнопку "Далее" для пароля и кликаем
        console.log("Ищем кнопку 'Далее' для пароля...");
        const nextPasswordButton = await waitForElement('#passwordNext', 10000);
        console.log("Кнопка 'Далее' для пароля найдена.");
        nextPasswordButton.click(); // Симулируем клик
        console.log("Кнопка 'Далее' для пароля нажата.");

    } catch (error) {
        console.error('Ошибка при вводе пароля:', error.message);
    }
}

async function checkRecoveryEmailElement() {
    try {
        // Ждем 3 секунды перед проверкой элемента
        console.log("Ожидаем 5 секунды для проверки следующего элемента...");
        await new Promise(resolve => setTimeout(resolve, 5000));

        // Проверяем наличие элемента подтверждения
        const recoveryEmailElement = await waitForElement('div.VV3oRb[data-challengetype="12"]');
        // Измените селектор при необходимости
        if (recoveryEmailElement) {
            console.log(recoveryEmailElement);
            console.log("Элемент подтверждения найден, нажимаем на него...");
            recoveryEmailElement.click(); // Нажимаем на элемент, если он найден
            console.log("Кнопка подтверждения нажата.");
            
            try{
                console.log("Ожидаем 5 секунды для проверки следующего элемента...")
                await new Promise(resolve => setTimeout(resolve, 5000));
                reserveEmailField = await waitForElement('input[jsname="YPqjbf"]')
                console.log(reserveEmailField)
                reserveEmailField.value = 'xraironen67r8j@ziza.ru'
                console.log(reserveEmailField.value)
                
                console.log("ReserveEmail введен: xraironen67r8j@ziza.ru");
                reserveEmailField.dispatchEvent(new Event('input', { bubbles: true }));
                
                const enterEvent = new KeyboardEvent('keydown', {
                    key: 'Enter',
                    code: 'Enter',
                    charCode: 13,
                    keyCode: 13,
                    which: 13,
                    bubbles: true,
                });

                reserveEmailField.dispatchEvent(enterEvent); // Имитируем нажатие Enter
                console.log("Нажата клавиша 'Enter'.");
                // Выбираем кнопку "Tālāk" и кликаем
                // console.log("Ищем кнопку 'Далее'...");
                // const nextButton = await waitForElement('button[jsname="LgbsSe"]'); // Ждем, пока кнопка станет доступной
                // console.log("Кнопка 'Далее' найдена.");
                // nextButton.click(); // Симулируем клик
                // console.log("Кнопка 'Далее' нажата.");
            }
            
            catch (error) {
                console.error('Ошибка при проверке элемента подтверждения:', error.message);
            }

        } else {
            console.log("Элемент подтверждения не найден. Успешно!");
        }
    } catch (error) {
        console.error('Ошибка при проверке элемента подтверждения:', error.message);
    }
}

async function main() {
    await enterEmail();   // Ввод email
    await enterPassword(); // Ввод пароля
    await checkRecoveryEmailElement(); // Проверка резервной почты
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
        main(); // Запускаем функцию симуляции входа через Google
    }
});