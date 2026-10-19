# 🧩 Код, который легко менять

> **Ситуация:** Нужно упростить большой модуль, сохранив его поведение. Объясни, что изменится и какой компромисс придётся принять.

**Твоя цель:** Обсудить устройство кода и предложить небольшой рефакторинг.

## 1. Набор для разговора

Учи выражение из средней колонки целиком; затем подставь свои данные.

| Слово / термин | Готовая связка | Смысл здесь |
|---|---|---|
| **dependency** | remove a dependency | зависимость от другого компонента или пакета |
| **refactor** | refactor a function | изменить внутреннюю структуру кода, сохранив его наблюдаемое поведение |
| **maintainable** | keep code maintainable | удобный для сопровождения |
| **coupling** | reduce coupling | связанность компонентов |
| **boilerplate** | generate boilerplate | повторяющийся шаблонный код |
| **trade-off** | a trade-off between speed and memory | компромисс между свойствами |

### Как это звучит в предложении

<details>
<summary>dependency — контекст</summary>

> This dependency is no longer needed.

Эта зависимость больше не нужна.

**Мой пример:** …

</details>

<details>
<summary>refactor — контекст</summary>

> I want to refactor this function.

Я хочу отрефакторить эту функцию.

**Мой пример:** …

</details>

<details>
<summary>maintainable — контекст</summary>

> Smaller modules make the code more maintainable.

Небольшие модули делают код удобнее для сопровождения.

**Мой пример:** …

</details>

<details>
<summary>coupling — контекст</summary>

> We reduced coupling between the modules.

Мы уменьшили связанность модулей.

**Мой пример:** …

</details>

<details>
<summary>boilerplate — контекст</summary>

> The framework generates the boilerplate.

Фреймворк генерирует шаблонный код.

**Мой пример:** …

</details>

<details>
<summary>trade-off — контекст</summary>

> There is a trade-off between speed and memory.

Здесь есть компромисс между скоростью и памятью.

**Мой пример:** …

</details>

## 2. Фразовые глаголы в действии

### set up — настроить; подготовить

**Схема:** `set something up`<br>
**Формы:** set — set — set<br>
**Порядок слов:** Разделяется; с it: set it up.

> Let's set up a small test project.

Давай подготовим небольшой тестовый проект.

### break down — разбить на понятные части

**Схема:** `break something down into parts`<br>
**Формы:** break — broke — broken<br>
**Порядок слов:** Разделяется: break it down into smaller tasks.

> We can break the module down into smaller parts.

Мы можем разбить модуль на меньшие части.

### clean up — привести в порядок

**Схема:** `clean something up`<br>
**Формы:** clean — cleaned — cleaned<br>
**Порядок слов:** Разделяется; с it: clean it up.

> I'll clean up the duplicate code.

Я приведу в порядок дублирующийся код.

## 3. Две готовые реплики

> This change makes the code easier to maintain.

Это изменение делает код удобнее для сопровождения.

> What trade-off are we making here?

На какой компромисс мы здесь идём?

## 4. Мини-диалог

**A:** Why do you want to refactor this module?<br>
**B:** It has too much boilerplate and too many dependencies.<br>
**A:** Can we break it down into smaller parts?<br>
**B:** Yes. I'll set up the tests first, then clean it up.<br>

<details>
<summary>Перевод диалога</summary>

A: Почему хочешь изменить структуру модуля? B: В нём слишком много шаблонного кода и зависимостей. A: Можем разбить на меньшие части? B: Да. Сначала настрою тесты, затем приведу его в порядок.

</details>

## 5. Тонкость, которая пригодится

Глагол set up пишется раздельно. Существительное setup — настройка или конфигурация. Break down здесь означает разбиение, хотя в другой ситуации может означать поломку.

## 6. Твой ход

Сначала ответь без подсказки. У реплик могут быть другие корректные варианты.

**1. Восстанови слово: This ___ is no longer needed.**

<details>
<summary>Показать вариант ответа</summary>

dependency — Эта зависимость больше не нужна.

</details>

---

**2. Восстанови связку: Let's ___ a small test project.**

<details>
<summary>Показать вариант ответа</summary>

set up

</details>

---

**3. Проект уже упомянут. Скажи «Я настрою его» с it.**

<details>
<summary>Показать вариант ответа</summary>

I'll set it up.

</details>

---

**4. Скажи за 30–60 секунд: Предложи разбить модуль на части, убрать зависимость и сначала настроить тесты. Спроси о компромиссе.**

<details>
<summary>Посмотреть пример, затем сказать по-своему</summary>

Let's break the module down into smaller parts and remove this dependency. I'll set up the tests first. What trade-off are we making here?

</details>

---

## 7. Заполни под себя

- **Моя реальная ситуация:** …
- **Три связки, которые хочу использовать:** …
- **Моя реплика или короткий диалог:** …
- **Что пришлось подсмотреть:** …

[Шаблон отдельной записи](<../Шаблоны/Словарная запись.md>) · [Тренажёр](../Повторение.html) · [Все темы](../README.md)

**Справка по теме:** [Martin Fowler · Refactoring](https://refactoring.com/). Примеры и диалоги составлены для этого словаря. [Источники и принципы](../Источники.md).
