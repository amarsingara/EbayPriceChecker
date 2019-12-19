import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.ebay.ca/itm/Dell-Chromebook-11-6-Inches-16GB-Intel-N2840-2-58GHz-4GB-16GB-Laptop-Grade-B-C/133237071377?epid=17034762280&hash=item1f058c5e11&_trkparms=ispr%3D1&enc=AQAEAAADIKvsXIZtBqdkfsZsMtzFbFsbX3WcW5fmB%2Fx7ZbaZTyexlCjI7LDlLA9prZ9Y6U7OABTNaVWhajUJ0WX64o%2FkxDM6upBu05QgfhIaPRYtff3lA9VLBZqSukgISdA%2BtmvfyOO%2Bp2yszGAA0CorfTdT8jUb51Qizp9jBmTOUaqgr0rXzAz%2BiewyAqqtBI6YzNFp0MA%2B0wOJonq462tc%2F7y5jMfcvtKdp2L1H%2FHF7XcV1pGI9B25uhD09g%2BZOXTiGXCKGK6wXYu661BPUdpLPSBlScjNKCKCM8ze%2FYI7pJ%2Bz5roNsoFT22G9BFVqGKCaLRLfYHUjYfpEuqD7XNHWD2aZMHrwv353dRHxu5qjOOZZPyFCxODM8rUu6KKsXMCILi8%2BDLmhs4xha4uE9Qy5i%2F0JmWtHf9WB36PL%2FUXPYV1m0e5MQC2Ry%2Fw%2F5wqZixr%2B7y9dZ7LuFFoJOweNNshk7kyv0cGYbYExuTn2cVC3V9E7vg73saximnPih%2FckjX%2FJ8I6MT0JS2JqJXnn40grlg40Lm6VuOJhGUST8clZlGdEYZyBJy0icuujJuQg44dQeqHVdO3IGyHuf2MbCMpBF5zs3gnLllByttM%2B8ytzlBL49FA4iWAYKbGDJwUolVWX34bA%2BCrAPWL2YQyOheRkNlf8U%2BsCZIjJzAJvay%2BQrpQnxJ%2FpNAtkk3mWMBg%2FdJ36res8rx%2BU25ntpGSa7ifP1v7OcVF4VVmdUJbBf3ZReTZlAe1BRnTOUfsMctjbwZKM34Utf6w8vNTAh4HNErqU%2BPqUSCs8aXUBhqhSC2t%2FtlIQWVxRLDQffpkiGJVbcLaO4uETOauuATIYKHJtbeoHqzufRHpubBblJDryKvaNlubx8H0w9UmHRGR0tbYAkFl6p2th7O8NcNY1HwBFRK9F2CmqjeOprktiTiSpnx7z4%2FgDJ2rn6Q8BncsbC6gwlSiYQc7ZeOM3GQdVOIfAwr5rSNW7xx3RfUbDAf7y85KhR6GiHW26pAr4tZUqD1sqZ8ra4%2BhhrufIrTzZSZRCXfkTOg3UF5xQO15x4xIXigsplbTe4VoSA&checksum=1332370713774f682d432938477d8ff64d3031dee70f'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()
    converted_price = float(price[3:9])
    
    print(converted_price)
    print(title.strip())

    if(converted_price > 100.00):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('amarsingara@gmail.com', 'gjuqhynfskjytymp')

    subject = 'Price Fell Down!'
    body = 'Check Ebay Link https://www.ebay.ca/itm/Dell-Chromebook-11-6-Inches-16GB-Intel-N2840-2-58GHz-4GB-16GB-Laptop-Grade-B-C/133237071377?epid=17034762280&hash=item1f058c5e11&_trkparms=ispr%3D1&enc=AQAEAAADIKvsXIZtBqdkfsZsMtzFbFsbX3WcW5fmB%2Fx7ZbaZTyexlCjI7LDlLA9prZ9Y6U7OABTNaVWhajUJ0WX64o%2FkxDM6upBu05QgfhIaPRYtff3lA9VLBZqSukgISdA%2BtmvfyOO%2Bp2yszGAA0CorfTdT8jUb51Qizp9jBmTOUaqgr0rXzAz%2BiewyAqqtBI6YzNFp0MA%2B0wOJonq462tc%2F7y5jMfcvtKdp2L1H%2FHF7XcV1pGI9B25uhD09g%2BZOXTiGXCKGK6wXYu661BPUdpLPSBlScjNKCKCM8ze%2FYI7pJ%2Bz5roNsoFT22G9BFVqGKCaLRLfYHUjYfpEuqD7XNHWD2aZMHrwv353dRHxu5qjOOZZPyFCxODM8rUu6KKsXMCILi8%2BDLmhs4xha4uE9Qy5i%2F0JmWtHf9WB36PL%2FUXPYV1m0e5MQC2Ry%2Fw%2F5wqZixr%2B7y9dZ7LuFFoJOweNNshk7kyv0cGYbYExuTn2cVC3V9E7vg73saximnPih%2FckjX%2FJ8I6MT0JS2JqJXnn40grlg40Lm6VuOJhGUST8clZlGdEYZyBJy0icuujJuQg44dQeqHVdO3IGyHuf2MbCMpBF5zs3gnLllByttM%2B8ytzlBL49FA4iWAYKbGDJwUolVWX34bA%2BCrAPWL2YQyOheRkNlf8U%2BsCZIjJzAJvay%2BQrpQnxJ%2FpNAtkk3mWMBg%2FdJ36res8rx%2BU25ntpGSa7ifP1v7OcVF4VVmdUJbBf3ZReTZlAe1BRnTOUfsMctjbwZKM34Utf6w8vNTAh4HNErqU%2BPqUSCs8aXUBhqhSC2t%2FtlIQWVxRLDQffpkiGJVbcLaO4uETOauuATIYKHJtbeoHqzufRHpubBblJDryKvaNlubx8H0w9UmHRGR0tbYAkFl6p2th7O8NcNY1HwBFRK9F2CmqjeOprktiTiSpnx7z4%2FgDJ2rn6Q8BncsbC6gwlSiYQc7ZeOM3GQdVOIfAwr5rSNW7xx3RfUbDAf7y85KhR6GiHW26pAr4tZUqD1sqZ8ra4%2BhhrufIrTzZSZRCXfkTOg3UF5xQO15x4xIXigsplbTe4VoSA&checksum=1332370713774f682d432938477d8ff64d3031dee70f'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'amarsingara@gmail.com',
        'amarsingara@hotmail.com',
        msg
    )
    print('Email has been sent!')
    
    server.quit()


check_price()



