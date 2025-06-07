# TradingView → Telegram Bot

Бот принимает сигналы от TradingView через webhook и публикует их в Telegram канал.

## Как задеплоить на Render.com

1. Зарегистрируйся на https://render.com
2. Создай новый Web Service
3. Загрузи этот проект из `.zip` или из GitHub
4. Убедись, что в `render.yaml` передан токен через переменные окружения
5. Укажи endpoint вебхука в TradingView: `https://your-app-name.onrender.com/webhook`

## Пример сигнала из TradingView

```json
{
  "message": "🔥 LONG BTCUSD @ 64800\nSL: 64500\nTP: 66000"
}
```

## Важно:

- Бот должен быть админом в канале `@LiquidHunters_x100`