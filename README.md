# Drop of Cost Reminder Project
This Python script monitors the price of a specific product on Amazon and sends an email notification when the price drops below a specified threshold.

## Key Features
**Web Scraping with BeautifulSoup:**
  - The project uses the BeautifulSoup library to scrape the product page on Amazon and extract the current price.

**Price Comparison Logic:**
  - The script compares the extracted price with a predefined threshold to determine whether to send a notification.

**Email Notification System:**
  - The script uses the smtplib library to send an email notification when the price drops below the specified threshold.

**User-Agent Header:**
  - The script includes a User-Agent header in the request to mimic a browser request, which helps avoid being blocked by the website.
