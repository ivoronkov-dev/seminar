import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import timedelta

print("bonus (visible edge)")
x = np.random.rand(30)
y = np.random.rand(30)
# edge - это окантовка вокруг графика
plt.scatter(x, y, s=400, c="orange", edgecolor="purple", linewidth=5)
plt.title("bonus (visible edge)")
plt.show()



print('task 2')


plt.figure(figsize=(7, 7))

vals1 = np.random.normal(size=100, scale=5, loc=50)
plt.subplot(311)
plt.hist(vals1, bins = 25)
plt.axis([20, 80, 0, 15])
plt.title("100 значений")

vals2 = np.random.normal(size=1000, scale=5, loc=50)
plt.subplot(312)
plt.hist(vals2, bins = 25)
plt.axis([20, 80, 0, 150])
plt.title("1000 значений")

vals3 = np.random.normal(size=50000, scale=5, loc=50)

plt.subplot(313)
plt.hist(vals3, bins = 25)
plt.axis([20, 80, 0, 7000])
plt.title("5000 значений")

plt.subplots_adjust(hspace=0.7)
plt.show()



print("task 3")
plt.subplot(211)
plt.pie([1/3, 1/3, 1/3], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
plt.title('species')

plt.subplot(212)
plt.pie([2/150, 35/150, 113/150], labels = ['less than 1.2','beetween 1.2 and 1.5','more than 1.5'])
plt.title('PetalLengthCm')
plt.subplots_adjust(hspace=0.7)
plt.show()

print("task 4")

df = pd.read_csv('iris_data.csv')

sl = sorted(list(df['SepalLengthCm']))
sw = sorted(list(df['SepalWidthCm']))
pl = sorted(list(df['PetalLengthCm']))
pw = sorted(list(df['PetalWidthCm']))

slov = {
    'SepalLengthCm': sl,
    'SepalWidthCm': sw,
    'PetalLengthCm': pl,
    'PetalWidthCm': pw}

spis = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'SepalWidthCm', 'PetalWidthCm', 'SepalWidthCm', 'SepalLengthCm', 'PetalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'PetalLengthCm']
for i in range(0, len(spis), 2):
    x1 = spis[i]
    y1 = spis[i+1]

    z = np.polyfit(slov[x1], slov[y1], 1)

    p = np.poly1d(z)

    x_line = np.linspace(min(slov[x1]), max(slov[x1]), 100)
    y_line = p(x_line)


    plt.scatter(slov[x1], slov[y1], marker='x')
    plt.ylabel(y1)
    plt.xlabel(x1)
    plt.plot(x_line, y_line)

    plt.show()

print("task 5")

df = pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])

plt.figure(figsize=(11, 6))
price = list(df['close'])

plt.plot(df['time'], price)

plt.xlabel('Год-Месяц', fontsize=12)
plt.ylabel('Цена закрытия (USD)', fontsize=12)
plt.title('Динамика цены', fontsize=14)
plt.grid(True, alpha=0.3)

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)


plt.show()

print("task 6")

df = pd.read_csv('BTC_data.csv')
df['time'] = pd.to_datetime(df['time'])

dates_numeric = mdates.date2num(df['time'])
degree = 70
coefficients = np.polyfit(dates_numeric, df['close'], degree)
polynomial = np.poly1d(coefficients)

plt.figure(figsize=(11, 6))

plt.plot(df['time'], df['close'], linewidth=2,
         label='Историческая цена BTC', alpha=0.8)

y_fit = polynomial(dates_numeric)
plt.plot(df['time'], y_fit, linewidth=3, color='red')

last_date = df['time'].iloc[-1]
future_dates = [last_date + timedelta(days=30*i) for i in range(1, 6)]
future_dates_numeric = mdates.date2num(future_dates)
future_predictions = polynomial(future_dates_numeric)

plt.plot(future_dates, future_predictions, linewidth=2, color='red',
         linestyle='--', label='Прогноз на 6 месяцев')

plt.xlabel('Год-Месяц', fontsize=12)
plt.ylabel('Цена закрытия (USD)', fontsize=12)
plt.title('Экстраполяция цены полиномом 70-й степени', fontsize=14)
plt.grid(True, alpha=0.3)

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

print("task 8 (bonus)")

a = [1, 1, 2, 3, 3, 4, 5, 6]
b = [4, 5, 5, 6, 7, 7, 8, 9]
print("a:", a)
print("b:", b)
a1, b1 = set(a), set(b)
print("Unique in a:", list(a1))
print("Unique in b:", list(b1))
print("Unique in a+b:", list(a1.union(b1)))
print("Intersection of a and b:", list(a1.intersection(b1)))

