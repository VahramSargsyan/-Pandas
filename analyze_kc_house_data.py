import pandas as pd

# Попробуем разные кодировки
try:
    df = pd.read_csv('kc_house_data.csv', delimiter=',', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('kc_house_data.csv', delimiter=',', encoding='ISO-8859-1')

# Вывод первых 5 строк
print(df.head())

##################################

stroki = df.head()
print(stroki)

# Изучите типы данных
data_types = df.dtypes
print("Типы данных:")
print(data_types)

# Количество пропущенных значений
missing_values = df.isnull().sum()
print("Количество пропущенных значений:")
print(missing_values)

# Основные статистики по числовым признакам
statistics = df.describe()
print("Основные статистики:")
print(statistics)

#################################################

# 3.1 В каком диапазоне изменяются стоимости недвижимости?
price_range = (df['price'].min(), df['price'].max())
print(f"Диапазон стоимости недвижимости: от {price_range[0]} до {price_range[1]}")

# 3.2 Какую долю в среднем занимает жилая площадь от всей площади по всем домам?
avg_living_area_ratio = (df['sqft_living'] / df['sqft_lot']).mean()
print(f"Средняя доля жилой площади от всей площади: {avg_living_area_ratio:.2%}")

# 3.3 Как много домов с разными этажами в данных?
floors_count = df['floors'].value_counts()
print("Количество домов с разными этажами:")
print(floors_count)

# 3.4 Насколько хорошие состояния у домов в данных?
condition_counts = df['condition'].value_counts()
print("Состояния домов:")
print(condition_counts)

# 3.5 Найдите года, когда построили первый дом, когда построили последний дом в данных?
oldest_year = df['yr_built'].min()
newest_year = df['yr_built'].max()
print(f"Первый дом построен в {oldest_year} году")
print(f"Последний дом построен в {newest_year} году")

#####################

# 4.1 Сколько в среднем стоят дома, у которых 2 спальни?
avg_price_2_bedrooms = df[df['bedrooms'] == 2]['price'].mean()
print(f"Средняя стоимость домов с 2 спальнями: {avg_price_2_bedrooms}")

    # 4.2 Какая в среднем общая площадь домов, у которых стоимость больше 600 000?
avg_sqft_lot_over_600k = df[df['price'] > 600000]['sqft_lot'].mean()
print(f"Средняя общая площадь домов, у которых стоимость больше 600 000: {avg_sqft_lot_over_600k}")

    # 4.3 Как много домов коснулся ремонт?
renovated_houses_count = df[df['yr_renovated'] != 0].shape[0]
print(f"Количество домов, которые были отремонтированы: {renovated_houses_count}")

    # 4.4 Насколько в среднем стоимость домов с оценкой grade выше 10 отличается от стоимости домов с оценкой grade меньше 4?
avg_price_grade_above_10 = df[df['grade'] > 10]['price'].mean()
avg_price_grade_below_4 = df[df['grade'] < 4]['price'].mean()
price_difference = avg_price_grade_above_10 - avg_price_grade_below_4
print(f"Разница в средней стоимости домов с оценкой grade выше 10 и с оценкой grade ниже 4: {price_difference}")

##########################################

# 5.1 Сколько вариантов есть у клиента?
# Условия: вид на набережную (waterfront == 1), минимум 3 ванные (bathrooms >= 3), наличие подвала (sqft_basement > 0)
options_1 = df[(df['waterfront'] == 1) & (df['bathrooms'] >= 3) & (df['sqft_basement'] > 0)]
num_options_1 = options_1.shape[0]
print(f"Количество вариантов для клиента: {num_options_1}")

# 5.2 В какой ценовом диапазоне будут дома?
# Условия: красивый вид (view == 4) или вид на набережную (waterfront == 1), хорошее состояние (condition == 5), год постройки >= 1980
options_2 = df[((df['view'] == 4) | (df['waterfront'] == 1)) & (df['condition'] == 5) & (df['yr_built'] >= 1980)]
price_range_2 = (options_2['price'].min(), options_2['price'].max())
print(f"Ценовой диапазон домов: от {price_range_2[0]} до {price_range_2[1]}")

# 5.3 Какая оценка по состоянию у таких домов в среднем?
# Условия: без подвала (sqft_basement == 0), два этажа (floors == 2), стоимость <= 150000
options_3 = df[(df['sqft_basement'] == 0) & (df['floors'] == 2) & (df['price'] <= 150000)]
avg_condition_3 = options_3['condition'].mean()
print(f"Средняя оценка по состоянию для таких домов: {avg_condition_3}")
