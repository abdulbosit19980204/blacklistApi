# blacklistApi

This API provides endpoints to manage and search data related to users, phones, cards, friends, workers, and Telegram users. Below is an overview of the `SearchApiView` functionality:

## SearchApiView

The `SearchApiView` aggregates data from multiple models and returns a unified response structure. It includes:

- **Users**: Data from the `Users` model.
- **Phones**: Data from the `Phones` model.
- **Cards**: Data from the `Cards` model.
- **Telegram Users**: Data from the `TelegramUser` model in the `lookup` app.

### Endpoint
`GET /api/search/`

### Query Parameters
- `search_text`: A string to search across all models.

### Response Format
```json
{
    "users": [
        {
            "id": 1,
            "name": "John",
            "surname": "Doe",
            "username": "johndoe",
            ...
        }
    ],
    "phones": [
        {
            "id": 1,
            "number": "1234567890",
            "user": 1
        }
    ],
    "cards": [
        {
            "id": 1,
            "bank": "Bank Name",
            "number": "1234-5678-9012-3456",
            ...
        }
    ],
    "telegram_users": [
        {
            "id": 1,
            "telegram_id": 123456789,
            "username": "johndoe",
            ...
        }
    ]
}
```

### Notes
- Ensure that the `lookup` app is installed and properly configured.
- The `TelegramUser` model data is encrypted and decrypted as needed.