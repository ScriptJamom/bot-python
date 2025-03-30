import telebot
import random

bot = telebot.TeleBot('токен бота')

#разложения
table = [
    ["Пластиковая бутылка разлагается до 450 лет! Почему бы не заменить её на стеклянную или металлическую? Планета: не переживает. Мы: переживаем."],
    ["Пакет разлагается до 400 лет! Давайте обойдёмся без пакетов, заменим их тканевыми! Один пакет – тысяча лет на свалке."],
    ["Стекло разлагается более 1000 лет! Пора сдавать стеклянные бутылки на переработку. 1000 лет без стекла — идеальное время для переработки."],
    ["Жевательная резинка разлагается до 30 лет! Лучше выбросить её в урну, а не на землю. Забудь о жевательной резинке на тротуаре — 30 лет её последствия!"],
    ["Алюминиевая банка разлагается до 500 лет! Сдавай её в переработку. Каждая банка – шанс на переработку."],
    ["Бумага разлагается от 2 до 6 месяцев. Лучше сдавать её в макулатуру! Бумага уходит быстро, но переработка — ещё быстрее!"],
    ["Окурок разлагается до 10 лет! Используй специальную урну для окурков. Окурок в урну — не на землю!"],
    ["Пластиковая трубочка разлагается до 200 лет! Лучше использовать многоразовые трубочки. Трубочка: всё это будет долго разлагаться."]
]

#поделки
table1 = [ ['''Цветы из пластиковых бутылок: Пошаговая инструкция:
Отрезаем дно бутылки. Оно станет базой под цветок — её верхними лепестками.
Корректируем форму, вырезая четыре лепестка. Для этого воспользуйтесь ножницами.
Готовые лепестки оплавляем спичками или зажигалкой.
Из корпуса вырезаем от четырёх до шести лепестков, которые с помощью клея соединяем с основой.'''],

['''Божьи коровки из пластика: Божьи коровки из пластиковых бутылок могут стать оригинальным сувениром или проектом вашего ребенка на конкурс в детском саду или школе. Для того чтобы сделать вот такую красоту, вам понадобятся: бутылки красного и черного цвета и степлер. Пошаговый алгоритм изготовления такой:
Вырежите овальные заготовки красного цвета – основу для будущей божьей коровки;
Из черной бутылки вырежите кружки – точки на «божьей коровке»;
На крышке из-под черной бутылки нарисуйте глаза и мордочку насекомого;
Прикрепите крылья – поделка готова.
При желании вы можете использовать в своей «божьей коровке» различные декоративные элементы.'''],

['''Капельный полив: Опытные садоводы знают преимущества капельного полива на огороде. Чтобы организовать его самостоятельно, вам потребуется несколько пластиковых бутылок. Лучший объём — 1,5 литра. Такая форма достаточно удобна, а воду нужно подливать реже.
Отрежьте самое донышко бутылки.
На крышке сделайте несколько отверстий диаметром 0,3-0,5 мм.
Перевернутую бутылку поставьте рядом с растениями, закрепив её в таком положении.''' ], ]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Напиши /info, и я расскажу случайный факт о разложении предметов! Или /podelki что сделать что-то с бытовыми отходами!")


@bot.message_handler(commands=['info'])
def send_random_info(message):
    fact = random.choice(table)
    bot.send_message(message.chat.id, fact)


@bot.message_handler(commands=['podelki'])
def send_random_podelka(message):
    podelka = random.choice(table1)
    bot.send_message(message.chat.id, podelka)
bot.polling()
