# Google Sheets → Lemlist

Eksport n8n potwierdza cztery połączone węzły. To osobna integracja przygotowania listy do kampanii. Automatyzacja opisana w głównym README obejmuje również niezależne kontrole źródeł, wykluczeń i zdarzeń pocztowych.

| Węzeł | Rola |
| --- | --- |
| Start | Wyzwala testową ścieżkę. |
| Set | Przekazuje parametry kampanii. |
| Google Sheets | Pobiera wiersze z arkusza wskazanego w konfiguracji. |
| HTTP Request | Mapuje dane odbiorcy i firmy do żądania utworzenia leada w Lemlist. |

Publiczna mapa opisuje kontrakt integracji. Nie zawiera treści arkusza, identyfikatorów kampanii, ustawień poświadczeń ani logów dostarczenia.
