import requests
from bs4 import BeautifulSoup
import smtplib

cheap_price = 250
sender = "@gmail.com"
url_amazon = "https://www.amazon.com/dp/B09STYVPN4?pd_rd_i=B09STYVPN4&pf_rd_p=7672bfb7-93b0-4322-b745-2104db09c4df&pf_rd_r=9AY3KQQ9XBHRAS1D166V&pd_rd_wg=iu35H&pd_rd_w=puxCO&pd_rd_r=751464e0-81dc-4bcf-bc4e-6c74a07c6ab3&th=1"
header = {
    "Accept-Language": "uk,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}

html_data = requests.get(url=url_amazon, headers=header).text
soup = BeautifulSoup(html_data, "html.parser")
price_soup = soup.find(class_="a-offscreen").text

price = float(price_soup.replace('$', ''))

if price < cheap_price:
    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n'Cheap prise!\n{url_amazon}"
        )