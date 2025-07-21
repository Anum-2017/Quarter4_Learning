# Step 1: Extract Info from Prompts 

We'll extract the intent and parameters for each prompt.

## 1. "What's the weather going to be like in Dubai tomorrow afternoon?"
- Intent: get_weather_forecast
- Location: "Dubai"
- Datetime: "tomorrow afternoon"

## 2. "Find me some good Chinese restaurants near downtown that are open right now"
- Intent: search_restaurants
- Cuisine: "Chinese"
- Location: "downtown"
- Open now: True

## 3. "Send an email to Sarah about the project deadline being moved to next Wednesday"
- Intent: send_email
- Recipient: "Sarah"
- Subject/Body: "project deadline moved to next Wednesday"

## 4. "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign"
- Intent: schedule_meeting
= Team: "marketing"
- Datetime: "this Friday at 2 PM"
- Topic: "new campaign"

## 5. "I want to buy a wireless Bluetooth headphones under $100 with good reviews"
- Intent: product_search
- Category: "wireless Bluetooth headphones"
- Budget: < $100
- Sort by: "good reviews"

