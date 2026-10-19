# 🌐 Медленный API и странный ответ

> **Ситуация:** Клиент долго ждёт ответ сервера. Нужно описать запрос, содержимое ответа и возможное ограничение производительности.

**Твоя цель:** Простыми фразами объяснить обмен между клиентом и сервером.

## 1. Набор для разговора

Учи выражение из средней колонки целиком; затем подставь свои данные.

| Слово / термин | Готовая связка | Смысл здесь |
|---|---|---|
| **endpoint** | call an endpoint | адрес или точка API, через которую доступна операция |
| **payload** | inspect the payload | полезное содержимое передаваемого сообщения |
| **request** | send a request | запрос |
| **response** | receive a response | ответ |
| **latency** | reduce latency | задержка |
| **throughput** | increase throughput | объём обработанной работы за единицу времени |

### Как это звучит в предложении

<details>
<summary>endpoint — контекст</summary>

> This endpoint returns a list of users.

Эта точка API возвращает список пользователей.

**Мой пример:** …

</details>

<details>
<summary>payload — контекст</summary>

> The payload contains a user ID.

Полезная нагрузка содержит ID пользователя.

**Мой пример:** …

</details>

<details>
<summary>request — контекст</summary>

> The client sends a request to the server.

Клиент отправляет запрос серверу.

**Мой пример:** …

</details>

<details>
<summary>response — контекст</summary>

> The response contains an error message.

Ответ содержит сообщение об ошибке.

**Мой пример:** …

</details>

<details>
<summary>latency — контекст</summary>

> High latency makes the app feel slow.

Из-за большой задержки приложение кажется медленным.

**Мой пример:** …

</details>

<details>
<summary>throughput — контекст</summary>

> The new server improves throughput.

Новый сервер повышает пропускную способность.

**Мой пример:** …

</details>

## 2. Фразовые глаголы в действии

### send back — отправить в ответ

**Схема:** `send something back`<br>
**Формы:** send — sent — sent<br>
**Порядок слов:** Разделяется; с it: send it back.

> The server sends back an error message.

Сервер отправляет в ответ сообщение об ошибке.

### slow down — замедлиться; замедлить

**Схема:** `slow down / slow something down`<br>
**Формы:** slow — slowed — slowed<br>
**Порядок слов:** Без объекта: the app slows down; с объектом: slow it down.

> Large requests slow the service down.

Большие запросы замедляют сервис.

### hook up — подключить; связать компоненты

**Схема:** `hook something up to something`<br>
**Формы:** hook — hooked — hooked<br>
**Порядок слов:** Разговорное; с it: hook it up to the test API.

> I'll hook the client up to the test API.

Я подключу клиент к тестовому API.

## 3. Две готовые реплики

> What does this endpoint return?

Что возвращает эта точка API?

> The server is taking too long to respond.

Сервер слишком долго отвечает.

## 4. Мини-диалог

**A:** What does this endpoint return?<br>
**B:** It sends back a list of users.<br>
**A:** Why is the response so slow?<br>
**B:** The payload is large. I'll hook the client up to the test API and check the latency.<br>

<details>
<summary>Перевод диалога</summary>

A: Что возвращает эта точка API? B: Список пользователей. A: Почему ответ такой медленный? B: Передаётся много данных. Подключу клиент к тестовому API и проверю задержку.

</details>

## 5. Тонкость, которая пригодится

Latency описывает задержку, throughput — объём работы за время. Высокая пропускная способность сама по себе не гарантирует быстрый ответ на отдельный запрос. Hook up здесь про подключение компонентов.

## 6. Твой ход

Сначала ответь без подсказки. У реплик могут быть другие корректные варианты.

**1. Восстанови слово: This ___ returns a list of users.**

<details>
<summary>Показать вариант ответа</summary>

endpoint — Эта точка API возвращает список пользователей.

</details>

---

**2. Восстанови связку: The server ___ an error message.**

<details>
<summary>Показать вариант ответа</summary>

sends back

</details>

---

**3. Ответ уже упомянут. Скажи «Сервер отправляет его обратно» с it.**

<details>
<summary>Показать вариант ответа</summary>

The server sends it back.

</details>

---

**4. Скажи за 30–60 секунд: Объясни, что клиент отправляет большой запрос, сервер долго отвечает, а ты проверишь задержку на тестовом API.**

<details>
<summary>Посмотреть пример, затем сказать по-своему</summary>

The client sends a large request, and the server is taking too long to respond. I'll hook the client up to the test API and check the latency.

</details>

---

## 7. Заполни под себя

- **Моя реальная ситуация:** …
- **Три связки, которые хочу использовать:** …
- **Моя реплика или короткий диалог:** …
- **Что пришлось подсмотреть:** …

[Тренажёр](../Повторение.html) · [Все темы](../README.md)
