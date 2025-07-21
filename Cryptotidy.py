import requests
import pandas as pd

# Подключение к API CoinGecko для получения данных о криптовалютах
def get_cryptos():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,  # Ограничим выборку до 10 криптовалют
        'page': 1
    }
    response = requests.get(url, params=params)
    return response.json()

# Функция для анализа криптовалют и формирования рейтинга
def analyze_cryptos():
    cryptos = get_cryptos()
    data = []

    for crypto in cryptos:
        # Вытаскиваем нужные параметры
        name = crypto['name']
        market_cap = crypto['market_cap']
        volume = crypto['total_volume']
        current_price = crypto['current_price']

        # Простой расчет "перспективности" криптовалюты
        potential = (market_cap / 1_000_000) + (volume / 1_000_000)  # Примерная метрика

        data.append({
            'Name': name,
            'Market Cap': market_cap,
            'Volume': volume,
            'Price': current_price,
            'Potential': potential
        })

    # Преобразуем данные в DataFrame для удобного отображения
    df = pd.DataFrame(data)
    df = df.sort_values(by='Potential', ascending=False)  # Сортируем по потенциалу

    return df

# Выводим рейтинг криптовалют
def display_rankings():
    rankings = analyze_cryptos()
    print("Top 10 Cryptocurrencies by Potential:")
    print(rankings)

if __name__ == "__main__":
    display_rankings()
