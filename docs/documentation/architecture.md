# Структура текущей системы

Состояние исходников: `rusbar-main`, `059f0c7`; дата фиксации — 2026-09-10. Этот документ представляет карту текущего репозитория.

## Каталоги

| Путь | Назначение |
| --- | --- |
| [system.json](../../system.json) | Манифест, идентификатор системы, совместимость и регистрация packs |
| [module/TheWitcherTRPG.js](../../module/TheWitcherTRPG.js) | Инициализация системы |
| [module/setup](../../module/setup) | Конфигурация и регистрация моделей, листов и обработчиков |
| [module/data](../../module/data) | Системные модели документов |
| [module/actor](../../module/actor) | Класс Actor, его действия и листы |
| [module/item](../../module/item) | Класс Item, действия и листы предметов |
| [module/activeEffect](../../module/activeEffect) | Класс и редактор ActiveEffect |
| [module/scripts](../../module/scripts) | Вспомогательные обработчики системы |
| [templates](../../templates) | Шаблоны интерфейса |
| [styles](../../styles), [lang](../../lang), [assets](../../assets) | Оформление, локализация и ресурсы |
| [packsJson](../../packsJson), [utils](../../utils) | Исходные документы компедиумов и инструменты |

## Регистрация

[registerDataModels.js](../../module/setup/registerDataModels.js) связывает типы документов с их системными моделями. [registerSheets.js](../../module/setup/registerSheets.js) регистрирует листы и редакторы.

Foundry Actor, Item и ActiveEffect являются разными документами. Подробная схема их обработки и возможные изменения требуют исследования соответствующей версии кода и отдельного согласования.

## Инструменты

В [package.json](../../package.json) определены команды `build:db` и `extract`. Их назначение описано в [документации компедиумов](compendiums.md).

Процесс выпуска задан в [release.yml](../../.github/workflows/release.yml), перечень включаемых файлов — в [build.json](../../build.json). Чтение этих файлов не подтверждает успешную сборку или установку.

Наблюдение о возможном несоответствии регистрации системы в Foundry находится в [аналитике репозитория](../analytics/repository-baseline.md).
