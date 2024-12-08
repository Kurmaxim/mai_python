import requests
from bs4 import BeautifulSoup


url = 'https://www.twitch.tv/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  
    html_content = response.text
    print("Данные успешно получены!")
except requests.exceptions.RequestException as e:
    print(f"Ошибка при получении данных: {e}")
    exit()

try:
    soup = BeautifulSoup(html_content, "html.parser")
    print("HTML успешно распарсен!")
except Exception as e:
    print(f"Ошибка при парсинге HTML: {e}")
    exit()

try:
    headers_h1 = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
    print("Найденные заголовки H1:", headers_h1)

    links = [a['href'] for a in soup.find_all("a", href=True)]
    print("Найденные ссылки:", links)
except Exception as e:
    print(f"Ошибка при извлечении данных: {e}")