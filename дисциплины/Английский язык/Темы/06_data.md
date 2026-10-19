# 🗄️ Данные доехали не полностью

> **Ситуация:** Импорт содержит пропуски и ненужные строки. Перед изменениями нужно обсудить копию данных и проверку результата.

**Твоя цель:** Описать выборку, изменение данных и пропуски в записи.

## 1. Набор для разговора

Учи выражение из средней колонки целиком; затем подставь свои данные.

| Слово / термин | Готовая связка | Смысл здесь |
|---|---|---|
| **query** | run a query | запрос к базе данных |
| **record** | update a record | запись данных |
| **schema** | change the database schema | структура базы или её логическая организация; в PostgreSQL также отдельное пространство имён |
| **transaction** | commit a transaction | группа операций, выполняемая как единое целое |
| **backup** | restore a backup | резервная копия |
| **consistency** | check data consistency | согласованность данных |

### Как это звучит в предложении

<details>
<summary>query — контекст</summary>

> This query returns only active users.

Этот запрос возвращает только активных пользователей.

**Мой пример:** …

</details>

<details>
<summary>record — контекст</summary>

> The record contains a user ID.

Запись содержит ID пользователя.

**Мой пример:** …

</details>

<details>
<summary>schema — контекст</summary>

> We changed the database schema.

Мы изменили схему базы данных.

**Мой пример:** …

</details>

<details>
<summary>transaction — контекст</summary>

> The transaction updates two records.

Транзакция обновляет две записи.

**Мой пример:** …

</details>

<details>
<summary>backup — контекст</summary>

> The backup is stored on a different server.

Резервная копия хранится на другом сервере.

**Мой пример:** …

</details>

<details>
<summary>consistency — контекст</summary>

> We check data consistency after the import.

Мы проверяем согласованность данных после импорта.

**Мой пример:** …

</details>

## 2. Фразовые глаголы в действии

### back up — сделать резервную копию

**Схема:** `back something up`<br>
**Формы:** back — backed — backed<br>
**Порядок слов:** Разделяется; с it: back it up.

> Please back up the database before the import.

Пожалуйста, сделай резервную копию базы перед импортом.

### leave out — пропустить; не включить

**Схема:** `leave something out`<br>
**Формы:** leave — left — left<br>
**Порядок слов:** Разделяется; с them: leave them out.

> The query leaves out inactive accounts.

Запрос не включает неактивные аккаунты.

### fill in — заполнить пропущенные сведения

**Схема:** `fill something in`<br>
**Формы:** fill — filled — filled<br>
**Порядок слов:** Разделяется; с it: fill it in.

> We need to fill in the missing fields.

Нам нужно заполнить пропущенные поля.

## 3. Две готовые реплики

> Some fields are missing from this record.

В этой записи отсутствуют некоторые поля.

> Let's check the data before we change the schema.

Давай проверим данные до изменения схемы.

## 4. Мини-диалог

**A:** Why does this query return fewer records?<br>
**B:** It leaves out inactive accounts.<br>
**A:** Some fields are missing too.<br>
**B:** Let's back up the database, then check which fields we can fill in.<br>

<details>
<summary>Перевод диалога</summary>

A: Почему запрос возвращает меньше записей? B: Он не включает неактивные аккаунты. A: Ещё и некоторых полей не хватает. B: Сделаем резервную копию, затем проверим, какие поля можем заполнить.

</details>

## 5. Тонкость, которая пригодится

Backup — резервная копия; back up — создать её. Field — поле, record — запись. Смысл schema зависит от СУБД и контекста, поэтому уточняй, речь о структуре или пространстве имён.

## 6. Твой ход

Сначала ответь без подсказки. У реплик могут быть другие корректные варианты.

**1. Восстанови слово: This ___ returns only active users.**

<details>
<summary>Показать вариант ответа</summary>

query — Этот запрос возвращает только активных пользователей.

</details>

---

**2. Восстанови связку: Please ___ the database before the import.**

<details>
<summary>Показать вариант ответа</summary>

back up

</details>

---

**3. Данные уже упомянуты. Скажи «Сначала сделай их резервную копию» с them.**

<details>
<summary>Показать вариант ответа</summary>

Back them up first.

</details>

---

**4. Скажи за 30–60 секунд: Объясни, какие записи исключает запрос и каких полей не хватает. Предложи резервную копию и проверку согласованности после импорта.**

<details>
<summary>Посмотреть пример, затем сказать по-своему</summary>

The query leaves out inactive accounts, and some fields are missing. Let's back up the database and check data consistency after the import.

</details>

---

## 7. Заполни под себя

- **Моя реальная ситуация:** …
- **Три связки, которые хочу использовать:** …
- **Моя реплика или короткий диалог:** …
- **Что пришлось подсмотреть:** …

[Шаблон отдельной записи](<../Шаблоны/Словарная запись.md>) · [Тренажёр](../Повторение.html) · [Все темы](../README.md)

**Справка по теме:** [PostgreSQL · транзакции](https://www.postgresql.org/docs/current/tutorial-transactions.html). Примеры и диалоги составлены для этого словаря. [Источники и принципы](../Источники.md).
