# templates/chat/effect-delivery.hbs

## Текущее состояние — 14.3.1.00108 / TASK-0011.008

2026-09-19. Ссылка на исходный ChatMessage отображается только при action.messageUuid. Без исходного сообщения отдельная карточка эффекта не создаёт пустую/невалидную ссылку; цели/состояния/кнопка прежние. visibility выбирает effectDelivery.js, не шаблон.

[Локальные проверки и границы B08](../../../../task-0011-static-checks.md#task-0011008). Ниже — прежние датированные срезы; утверждения о прямых query/неожидаемой доставке заменены этим разделом.

**14.3.1.00107, 2026-09-19, TASK-0011.007.** [Исходник](../../../../../../templates/chat/effect-delivery.hbs).

## Назначение и основные способы использования

Содержимое отдельного сообщения о доставке эффектов. Получает подготовленный view context от renderDelivery в [effectDelivery.js](../../../../../../module/scripts/effectDelivery.js); напрямую игровые документы не изменяет. Кнопка появляется только в waiting, полный список сохраняется при завершении.

## Сущности и действия

action.name/messageUuid — название и native `a.content-link[data-link][data-uuid]` исходного ChatMessage. stateLabel — состояние группы; targets.name/resultLabel/entries — адресат и результаты, имя эффекта/статуса, duration при hasDuration (включая0). needsReview показывает предупреждение, waiting — пояснение и `button.send-effect-delivery`. Значения экранируются обычными двойными скобками HBS.

## Зависимости и потребители

effectDelivery.js/renderDelivery подготавливает данные, createEffectDelivery/saveDelivery сохраняют content; bindEffectDelivery обрабатывает кнопку через существующий scripts/chat.js и Foundry hook. Шаблон использует native localize/each/if и ru/en WITCHER.EffectDelivery. Повтор не вызывает бросок, расход ресурсов или подбор текущих токенов. Видимость задаётся самим ChatMessage whisper/blind, не шаблоном; нейтральные controls для blind автора добавляются сервисом.

[Локальная проверка настоящим Handlebars ru/en и пределы](../../../../task-0011-static-checks.md#task-0011007). Браузер/реальное сохранение ожидаются в B07.
