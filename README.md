# Spersonalizowany mailing B2B dla kilku marek

Case study of multi-brand B2B outreach with evidence-based drafts, exclusions, and delivery review.

**Zakres publiczny:** Studium przypadku automatyzacji operacyjnej.

## Problem

Różne marki prowadziły własne kampanie i obsługiwały inne grupy odbiorców. Wspólny proces pomagał zebrać kontekst, przygotować indywidualną treść i odtworzyć decyzje dotyczące kontaktu.

## Jak działa projekt

1. Research zbierał publiczne informacje o firmie, ich źródła i przydatność dla konkretnej kampanii.
2. Osobne reguły kampanii kontrolowały dopasowanie firmy do oferty i ograniczały ryzyko użycia kontaktu przypisanego do innej marki.
3. Kontrole duplikatów, wcześniejszych odpowiedzi i wypisów działały przed skierowaniem rekordu do kolejki. Kolejne audyty porównywały lokalne decyzje z aktualnym stanem kolejek.
4. Klasyfikacja zdarzeń pocztowych umożliwiała powiązanie odpowiedzi z wcześniejszą wiadomością i analizę niepowodzeń dostarczenia.

## Technologie

Python, przetwarzanie HTML/JSON, kolejki, rejestry źródeł, SMTP/IMAP w aplikacjach obsługujących kampanie.

## Co można sprawdzić

Zachowany oddzielny eksport testowy n8n pokazuje integrację Google Sheets → Lemlist. Arkusz dostarcza rekordy, węzeł Set ustawia parametry kampanii, a żądanie HTTP mapuje pola do operacji dodania leada. To dowód przygotowania i integracji rekordów do kampanii. Status faktycznej wysyłki i jej wyniki wymagają danych wykonania z platformy.

[Mapa testowego przepływu n8n](workflows/sheets-to-lemlist.md).

Publikacja opisuje przebieg operacyjny i relację z [SalesPilot](https://github.com/AlexDzien/salespilot-outreach) oraz [Procurement Studio & CRM](https://github.com/AlexDzien/procurement-studio-crm). Skuteczność kampanii pozostaje do udokumentowania na podstawie zagregowanych danych.
