# 🐛 Баг, который не получается поймать

> **Ситуация:** После обновления приложение иногда падает. Твоя задача — объяснить проблему и договориться о следующей проверке.

**Твоя цель:** Описать ошибку, попросить данные для проверки и назвать следующий шаг.

## 1. Набор для разговора

Учи выражение из средней колонки целиком; затем подставь свои данные.

| Слово / термин | Готовая связка | Смысл здесь |
|---|---|---|
| **reproduce** | reproduce a bug | воспроизвести |
| **regression** | a regression after an update | ошибка, появившаяся в ранее работавшем поведении |
| **root cause** | find the root cause | коренная причина |
| **workaround** | use a workaround | временный обход проблемы |
| **edge case** | handle an edge case | крайний или необычный случай |
| **stack trace** | attach a stack trace | цепочка вызовов при ошибке |

### Как это звучит в предложении

<details>
<summary>reproduce — контекст</summary>

> I can't reproduce the bug on my laptop.

Я не могу воспроизвести баг на своём ноутбуке.

**Мой пример:** …

</details>

<details>
<summary>regression — контекст</summary>

> This regression appeared after the update.

Эта регрессия появилась после обновления.

**Мой пример:** …

</details>

<details>
<summary>root cause — контекст</summary>

> We found the root cause in the cache.

Мы нашли коренную причину в кэше.

**Мой пример:** …

</details>

<details>
<summary>workaround — контекст</summary>

> This workaround keeps the service running.

Этот обходной способ позволяет сервису работать.

**Мой пример:** …

</details>

<details>
<summary>edge case — контекст</summary>

> An empty file is an edge case.

Пустой файл — крайний случай.

**Мой пример:** …

</details>

<details>
<summary>stack trace — контекст</summary>

> Please attach the stack trace to the issue.

Пожалуйста, приложи стек вызовов к задаче.

**Мой пример:** …

</details>

## 2. Фразовые глаголы в действии

### look into — разобраться; исследовать

**Схема:** `look into something`<br>
**Формы:** look — looked — looked<br>
**Порядок слов:** Объект после into: look into it.

> I'll look into the regression.

Я разберусь с регрессией.

### run into — неожиданно столкнуться с проблемой

**Схема:** `run into something`<br>
**Формы:** run — ran — run<br>
**Порядок слов:** Не разделяется: run into it.

> We ran into an edge case during testing.

Во время тестирования мы столкнулись с крайним случаем.

### narrow down — сузить круг возможных причин

**Схема:** `narrow something down to something`<br>
**Формы:** narrow — narrowed — narrowed<br>
**Порядок слов:** Разделяется; с it: narrow it down.

> We narrowed the cause down to one module.

Мы сузили поиск причины до одного модуля.

## 3. Две готовые реплики

> Could you share the steps to reproduce it?

Можешь прислать шаги для воспроизведения?

> The fix covers this edge case.

Исправление учитывает этот крайний случай.

## 4. Мини-диалог

**A:** Have you looked into the regression?<br>
**B:** Yes. I narrowed it down to the cache module.<br>
**A:** Can you reproduce it?<br>
**B:** Only with an empty file. I'll add a test for that edge case.<br>

<details>
<summary>Перевод диалога</summary>

A: Разобрался с регрессией? B: Да, сузил поиск до модуля кэша. A: Можешь воспроизвести? B: Только с пустым файлом. Добавлю тест на этот крайний случай.

</details>

## 5. Тонкость, которая пригодится

Workaround позволяет обойти проблему; root cause называет её причину. Обход ещё не доказывает, что причина устранена.

## 6. Твой ход

Сначала ответь без подсказки. У реплик могут быть другие корректные варианты.

**1. Восстанови слово: I can't ___ the bug on my laptop.**

<details>
<summary>Показать вариант ответа</summary>

reproduce — Я не могу воспроизвести баг на своём ноутбуке.

</details>

---

**2. Восстанови связку: I'll ___ the regression.**

<details>
<summary>Показать вариант ответа</summary>

look into

</details>

---

**3. Проблема уже упомянута. Скажи: «Я с ней разберусь», используя it.**

<details>
<summary>Показать вариант ответа</summary>

I'll look into it.

</details>

---

**4. Скажи за 30–60 секунд: Скажи коллеге: столкнулся с багом после обновления, сузил поиск до одного модуля, пока используешь обход. Попроси шаги воспроизведения.**

<details>
<summary>Посмотреть пример, затем сказать по-своему</summary>

We ran into a regression after the update. I narrowed it down to one module. We have a workaround for now. Could you share the steps to reproduce it?

</details>

---

## 7. Заполни под себя

- **Моя реальная ситуация:** …
- **Три связки, которые хочу использовать:** …
- **Моя реплика или короткий диалог:** …
- **Что пришлось подсмотреть:** …

[Тренажёр](../Повторение.html) · [Все темы](../README.md)
