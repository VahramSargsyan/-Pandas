# Анализ данных из kc_house_data.csv

## Типы данных

```python
id                 int64
date              object
price            float64
bedrooms           int64
bathrooms        float64
sqft_living        int64
sqft_lot           int64
floors           float64
waterfront         int64
view               int64
condition          int64
grade              int64
sqft_above         int64
sqft_basement      int64
yr_built           int64
yr_renovated       int64
zipcode            int64
lat              float64
long             float64
sqft_living15      int64
sqft_lot15         int64
```

## Количество пропущенных значений

```python
id               0
date             0
price            0
bedrooms         0
bathrooms        0
sqft_living      0
sqft_lot         0
floors           0
waterfront       0
view             0
condition        0
grade            0
sqft_above       0
sqft_basement    0
yr_built         0
yr_renovated     0
zipcode          0
lat              0
long             0
sqft_living15    0
sqft_lot15       0
```

## Основные статистики

```python
                 id         price      bedrooms     bathrooms   sqft_living      sqft_lot        floors    waterfront          view     condition         grade    sqft_above  sqft_basement      yr_built  yr_renovated       zipcode           lat          long  sqft_living15     sqft_lot15
count  2.161300e+04  2.161300e+04  21613.000000  21613.000000  21613.000000  2.161300e+04  21613.000000  21613.000000  21613.000000  21613.000000  21613.000000  21613.000000   21613.000000  21613.000000  21613.000000  21613.000000  21613.000000  21613.000000   21613.000000   21613.000000
mean   4.580302e+09  5.400881e+05      3.370842      2.114757   2079.899736  1.510697e+04      1.494309      0.007542      0.234303      3.409430      7.656873   1788.390691     291.509045   1971.005136     84.402258  98077.939805     47.560053   -122.213896    1986.552492   12768.455652
std    2.876566e+09  3.671272e+05      0.930062      0.770163    918.440897  4.142051e+04      0.539989      0.086517      0.766318      0.650743      1.175459    828.090978     442.575043     29.373411    401.679240     53.505026      0.138564      0.140828     685.391304   27304.179631
min    1.000102e+06  7.500000e+04      0.000000      0.000000    290.000000  5.200000e+02      1.000000      0.000000      0.000000      1.000000      1.000000    290.000000       0.000000   1900.000000      0.000000  98001.000000     47.155900   -122.519000     399.000000     651.000000
25%    2.123049e+09  3.219500e+05      3.000000      1.750000   1427.000000  5.040000e+03      1.000000      0.000000      0.000000      3.000000      7.000000   1190.000000       0.000000   1951.000000      0.000000  98033.000000     47.471000   -122.328000    1490.000000    5100.000000
50%    3.904930e+09  4.500000e+05      3.000000      2.250000   1910.000000  7.618000e+03      1.500000      0.000000      0.000000      3.000000      7.000000   1560.000000       0.000000   1975.000000      0.000000  98065.000000     47.571800   -122.230000    1840.000000    7620.000000
75%    7.308900e+09  6.450000e+05      4.000000      2.500000   2550.000000  1.068800e+04      2.000000      0.000000      0.000000      4.000000      8.000000   2210.000000     560.000000   1997.000000      0.000000  98118.000000     47.678000   -122.125000    2360.000000   10083.000000
max    9.900000e+09  7.700000e+06     33.000000      8.000000  13540.000000  1.651359e+06      3.500000      1.000000      4.000000      5.000000     13.000000   9410.000000    4820.000000   2015.000000   2015.000000  98199.000000     47.777600   -121.315000    6210.000000  871200.000000
```

# Ответы на вопросы

## В каком диапазоне изменяются стоимости недвижимости?

Диапазон стоимости недвижимости: от 75000.0 до 7700000.0

## Какую долю в среднем занимает жилая площадь от всей площади по всем домам?

Средняя доля жилой площади от всей площади: 32.37%

## Как много домов с разными этажами в данных?

Количество домов с разными этажами:
floors
1.0    10680
2.0     8241
1.5     1910
3.0      613
2.5      161
3.5        8

## Насколько хорошие состояния у домов в данных?

Состояния домов:
condition
3    14031
4     5679
5     1701
2      172
1       30

## Найдите года, когда построили первый дом, когда построили последний дом в данных?

Первый дом построен в 1900 году
Последний дом построен в 2015 году

## Дополнительные вопросы

### 4.1 Сколько в среднем стоят дома, у которых 2 спальни?
Средняя стоимость домов с 2 спальнями: 401372.681884058

### 4.2 Какая в среднем общая площадь домов, у которых стоимость больше 600 000?
Средняя общая площадь домов, у которых стоимость больше 600 000: 20442.524776214832

### 4.3 Как много домов коснулся ремонт?
Количество домов, которые были отремонтированы: 914

### 4.4 Насколько в среднем стоимость домов с оценкой grade выше 10 отличается от стоимости домов с оценкой grade меньше 4?
Разница в средней стоимости домов с оценкой grade выше 10 и с оценкой grade ниже 4: 1488885.1175298805

## Выбор дома клиенту

### 5.1 Сколько вариантов есть у клиента?
Количество вариантов для клиента: 41

### 5.2 В какой ценовом диапазоне будут дома?
Ценовой диапазон домов: от 1295000.0 до 3000000.0

### 5.3 Какая оценка по состоянию у таких домов в среднем?
Средняя оценка по состоянию для таких домов: 3.0