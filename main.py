# Emanuel Biruk Seifegebreal - 2024 --> This project is for learning purposes
# Note: please focus on the program's logic
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept-Language": "en-US,en;q=0.5"
}

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(URL, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, "lxml")
price = float(soup.select_one(".a-price .a-offscreen").getText().split("$")[1]) # .split removes $ to get only the
# price as a float number

MY_EMAIL = "emuout@gmail.com"
PASSWORD = "lncgbzacwhakgxwr" # The password has expired

if price < 100:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="emu_in@yahoo.com",
                            msg=f"Subject:Your Instant Pot costs {price} on Amazon!\nInstant Pot Duo Plus 9-in-1 "
                                f"Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, "
                                f"Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, "
                                f"3 Quart is {price}\n{URL}"
                            )

