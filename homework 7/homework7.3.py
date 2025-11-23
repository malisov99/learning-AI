"""Используя базу данных фильмов из практической части урока, проверьте следующие гипотезы:

Большинство фильмов выпускаются по пятницам
Известные актеры снимаются в самых кассовых фильмах
Известные актеры снимаются в самыx дорогих фильмах

Построить графики по гипотезам. Сколько актеров из вашего результата вам знакомы?"""

#Импорт библиотек
import pandas as pd
import matplotlib.pyplot as plt
import ast
from requests import get

#Скачивание и распаковка архива
url = "https://storage.yandexcloud.net/academy.ai/the_movies_dataset.zip"
response = get(url)
with open('the_movies_dataset.zip', 'wb') as f:
    f.write(response.content)

!unzip -qo "the_movies_dataset.zip" -d ./the_movies_dataset

FILE_PATH = './the_movies_dataset'

#Загрузка данных
movies = pd.read_csv(f"{FILE_PATH}/movies_metadata.csv", low_memory=False)
credits = pd.read_csv(f"{FILE_PATH}/credits.csv")

import warnings
warnings.filterwarnings('ignore')

#Гипотеза 1
movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')
movies = movies.dropna(subset=['release_date'])
movies['weekday'] = movies['release_date'].dt.day_name()

release_days = movies['weekday'].value_counts()

plt.figure(figsize=(8,5))
release_days.plot(kind='bar', rot=45)
plt.title("Количество фильмов по дням недели")
plt.ylabel("Количество фильмов")
plt.tight_layout()
plt.show()

top_day = release_days.idxmax()
print(f"Больше всего фильмов выпускаются по {top_day}.")

#Подготовка таблицы актеров и объединение с фильмами
credits['cast'] = credits['cast'].apply(ast.literal_eval)

actors_data = []
for i, row in credits.iterrows():
    for actor in row['cast'][:5]:
        actors_data.append({
            'id': row['id'],
            'actor': actor['name'],
            'popularity': actor.get('popularity', 0)
        })

movies['id'] = movies['id'].astype(str)
actors_df['id'] = actors_df['id'].astype(str)

movies['revenue'] = pd.to_numeric(movies['revenue'], errors='coerce')
movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')

merged = actors_df.merge(movies, on='id', how='left')


#Гипотеза 2
actor_revenue = (
    merged.groupby('actor')['revenue']
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(10,6))
actor_revenue.plot(kind='bar')
plt.title("Средние кассовые сборы фильмов по актерам")
plt.ylabel("Средние сборы ($)")
plt.tight_layout()
plt.show()

print("Топ актеров по средним кассовым сборам:")
print(actor_revenue.index.tolist())

#Гипотеза 3
actor_budget = (
    merged.groupby('actor')['budget']
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(10,6))
actor_budget.plot(kind='bar')
plt.title("Средний бюджет фильмов по актерам:")
plt.ylabel("Средний бюджет ($)")
plt.tight_layout()
plt.show()

print("Топ актеров по бюджетам фильмов:")
print(actor_budget.index.tolist())