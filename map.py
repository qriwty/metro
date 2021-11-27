import datetime


# service_language_pack = {
#     "TRANSFER": {
#         "UKR": "Перехід",
#         "RUS": "Переход",
#         "ENG": "Transfer",
#     },
#     "INITIAL": {
#         "UKR": "Початок руху",
#         "RUS": "Начальная остановка",
#         "ENG": "Initial stop"
#     },
#     "TERMINUS": {
#         "UKR": "Кінцева зупинка",
#         "RUS": "Конечная остановка",
#         "ENG": "Terminus"
#     },
#     "TIME": {
#         "UKR": "Час руху",
#         "RUS": "Время в пути",
#         "ENG": "Travel time"
#     },
#     "PATH": {
#         "UKR": "Шлях",
#         "RUS": "Путь",
#         "ENG": "Path"
#     }
# }

language_pack = {
    "STATION": {
        "M1_S1": {
            "UKR": "Академмістечко",
            "RUS": "Академгородок",
            "ENG": "Akademmistechko"
        },
        "M1_S2": {
            "UKR": "Житомирська",
            "RUS": "Житомирская",
            "ENG": "Zhytomyrska"
        },
        "M1_S3": {
            "UKR": "Святошин",
            "RUS": "Святошин",
            "ENG": "Sviatoshyn"
        },
        "M1_S4": {
            "UKR": "Нивки",
            "RUS": "Нивки",
            "ENG": "Nyvky"
        },
        "M1_S5": {
            "UKR": "Берестейська",
            "RUS": "Берестейская",
            "ENG": "Beresteiska"
        },
        "M1_S6": {
            "UKR": "Шулявська",
            "RUS": "Шулявская",
            "ENG": "Shuliavska"
        },
        "M1_S7": {
            "UKR": "Політехнічний інститут",
            "RUS": "Политехнический институт",
            "ENG": "Politekhnichnyi Instytut"
        },
        "M1_S8": {
            "UKR": "Вокзальна",
            "RUS": "Вокзальная",
            "ENG": "Vokzalna"
        },
        "M1_S9": {
            "UKR": "Універсітет",
            "RUS": "Университет",
            "ENG": "Universytet"
        },
        "M1_S10": {
            "UKR": "Театральна",
            "RUS": "Театральная",
            "ENG": "Teatralna"
        },
        "M1_S11": {
            "UKR": "Хрещатик",
            "RUS": "Крещатик",
            "ENG": "Khreschatyk"
        },
        "M1_S12": {
            "UKR": "Арсенальна",
            "RUS": "Арсенальная",
            "ENG": "Arsenalna"
        },
        "M1_S13": {
            "UKR": "Дніпро",
            "RUS": "Днепр",
            "ENG": "Dnipro"
        },
        "M1_S14": {
            "UKR": "Гідропарк",
            "RUS": "Гидропарк",
            "ENG": "Hidropark"
        },
        "M1_S15": {
            "UKR": "Лівобережна",
            "RUS": "Левобережная",
            "ENG": "Livoberezhna"
        },
        "M1_S16": {
            "UKR": "Дарниця",
            "RUS": "Дарница",
            "ENG": "Darbytsia"
        },
        "M1_S17": {
            "UKR": "Чернігівська",
            "RUS": "Черниговская",
            "ENG": "Chernihivska"
        },
        "M1_S18": {
            "UKR": "Лісова",
            "RUS": "Лесная",
            "ENG": "Lisova"
        },

        "M2_S1": {
            "UKR": "Теремки",
            "RUS": "Теремки",
            "ENG": "Teremky"
        },
        "M2_S2": {
            "UKR": "Іподром",
            "RUS": "Ипподром",
            "ENG": "Ipodrom"
        },
        "M2_S3": {
            "UKR": "Виставковий центр",
            "RUS": "Выставочный центр",
            "ENG": "Vystavkovyi Tsentr"
        },
        "M2_S4": {
            "UKR": "Васильківська",
            "RUS": "Васильковская",
            "ENG": "Vasylkivska"
        },
        "M2_S5": {
            "UKR": "Голосіївська",
            "RUS": "Голосеевская",
            "ENG": "Holosiivska"
        },
        "M2_S6": {
            "UKR": "Деміївська",
            "RUS": "Демеевская",
            "ENG": "Demiivska"
        },
        "M2_S7": {
            "UKR": "Либідська",
            "RUS": "Лыбедская",
            "ENG": "Lybidska"
        },
        "M2_S8": {
            "UKR": "Палац Україна",
            "RUS": "Дворец Украина",
            "ENG": "Palats Ukraina"
        },
        "M2_S9": {
            "UKR": "Олімпійська",
            "RUS": "Олипийская",
            "ENG": "Olimpiiska"
        },
        "M2_S10": {
            "UKR": "Площа Льва Толстого",
            "RUS": "Площадь Льва Толского",
            "ENG": "Ploscha Lva Tolstoho"
        },
        "M2_S11": {
            "UKR": "Майдан Незалежності",
            "RUS": "Площадь Независимости",
            "ENG": "Maidan Nezalezhnosti"
        },
        "M2_S12": {
            "UKR": "Поштова площа",
            "RUS": "Почтовая площадь",
            "ENG": "Poshtova Ploscha"
        },
        "M2_S13": {
            "UKR": "Контрактова площа",
            "RUS": "Контрактовая площадь",
            "ENG": "Kontraktova Ploscha"
        },
        "M2_S14": {
            "UKR": "Тараса Шевченка",
            "RUS": "Тараса Шевченка",
            "ENG": "Tarasa Shevchenka"
        },
        "M2_S15": {
            "UKR": "Почайна",
            "RUS": "Почайная",
            "ENG": "Pochaina"
        },
        "M2_S16": {
            "UKR": "Оболонь",
            "RUS": "Оболонь",
            "ENG": "Obolon"
        },
        "M2_S17": {
            "UKR": "Мінська",
            "RUS": "Минская",
            "ENG": "Minska"
        },
        "M2_S18": {
            "UKR": "Героїв Дніпра",
            "RUS": "Героев Днепра",
            "ENG": "Heroiv Dnipra"
        },

        "M3_S1": {
            "UKR": "Сірець",
            "RUS": "Сырец",
            "ENG": "Syrets"
        },
        "M3_S2": {
            "UKR": "Дорогожичі",
            "RUS": "Дорогожичи",
            "ENG": "Dorohozhychi"
        },
        "M3_S3": {
            "UKR": "Лук'янівська",
            "RUS": "Лукьяновская",
            "ENG": "Lukianivska"
        },
        "M3_S4": {
            "UKR": "Золоті ворота",
            "RUS": "Золотые ворота",
            "ENG": "Zoloti Vorota"
        },
        "M3_S5": {
            "UKR": "Палац спорту",
            "RUS": "Дворец спорта",
            "ENG": "Palats Sportu"
        },
        "M3_S6": {
            "UKR": "Кловська",
            "RUS": "Кловская",
            "ENG": "Klovska"
        },
        "M3_S7": {
            "UKR": "Печерська",
            "RUS": "Печерская",
            "ENG": "Pecherska"
        },
        "M3_S8": {
            "UKR": "Дружби народів",
            "RUS": "Дружбы народов",
            "ENG": "Druzhby Narodiv"
        },
        "M3_S9": {
            "UKR": "Видубичі",
            "RUS": "Выдубичи",
            "ENG": "Vydubychi"
        },
        "M3_S10": {
            "UKR": "Славутич",
            "RUS": "Славутич",
            "ENG": "Slavutych"
        },
        "M3_S11": {
            "UKR": "Осокорки",
            "RUS": "Осокорки",
            "ENG": "Osokorky"
        },
        "M3_S12": {
            "UKR": "Позняки",
            "RUS": "Позняки",
            "ENG": "Pozniaky"
        },
        "M3_S13": {
            "UKR": "Харківська",
            "RUS": "Харьковская",
            "ENG": "Kharkivska"
        },
        "M3_S14": {
            "UKR": "Вирлиця",
            "RUS": "Вырлица",
            "ENG": "Vyrlytsia"
        },
        "M3_S15": {
            "UKR": "Бориспільска",
            "RUS": "Бориспольская",
            "ENG": "Boryspilska"
        },
        "M3_S16": {
            "UKR": "Червоний хутір",
            "RUS": "Красный хутор",
            "ENG": "Chervony Khutir"
        }
    },
    "SERVICE": {
        "TRANSFER": {
            "UKR": "Перехід",
            "RUS": "Переход",
            "ENG": "Transfer",
        },
        "INITIAL": {
            "UKR": "Початок руху",
            "RUS": "Начальная остановка",
            "ENG": "Initial stop"
        },
        "TERMINUS": {
            "UKR": "Кінцева зупинка",
            "RUS": "Конечная остановка",
            "ENG": "Terminus"
        },
        "TIME": {
            "UKR": "Час руху",
            "RUS": "Время в пути",
            "ENG": "Travel time"
        },
        "PATH": {
            "UKR": "Шлях",
            "RUS": "Путь",
            "ENG": "Path"
        }
    }
    # "M1_S1": {
    #     "UKR": "Академмістечко",
    #     "RUS": "Академгородок",
    #     "ENG": "Akademmistechko"
    # },
    # "M1_S2": {
    #     "UKR": "Житомирська",
    #     "RUS": "Житомирская",
    #     "ENG": "Zhytomyrska"
    # },
    # "M1_S3": {
    #     "UKR": "Святошин",
    #     "RUS": "Святошин",
    #     "ENG": "Sviatoshyn"
    # },
    # "M1_S4": {
    #     "UKR": "Нивки",
    #     "RUS": "Нивки",
    #     "ENG": "Nyvky"
    # },
    # "M1_S5": {
    #     "UKR": "Берестейська",
    #     "RUS": "Берестейская",
    #     "ENG": "Beresteiska"
    # },
    # "M1_S6": {
    #     "UKR": "Шулявська",
    #     "RUS": "Шулявская",
    #     "ENG": "Shuliavska"
    # },
    # "M1_S7": {
    #     "UKR": "Політехнічний інститут",
    #     "RUS": "Политехнический институт",
    #     "ENG": "Politekhnichnyi Instytut"
    # },
    # "M1_S8": {
    #     "UKR": "Вокзальна",
    #     "RUS": "Вокзальная",
    #     "ENG": "Vokzalna"
    # },
    # "M1_S9": {
    #     "UKR": "Універсітет",
    #     "RUS": "Университет",
    #     "ENG": "Universytet"
    # },
    # "M1_S10": {
    #     "UKR": "Театральна",
    #     "RUS": "Театральная",
    #     "ENG": "Teatralna"
    # },
    # "M1_S11": {
    #     "UKR": "Хрещатик",
    #     "RUS": "Крещатик",
    #     "ENG": "Khreschatyk"
    # },
    # "M1_S12": {
    #     "UKR": "Арсенальна",
    #     "RUS": "Арсенальная",
    #     "ENG": "Arsenalna"
    # },
    # "M1_S13": {
    #     "UKR": "Дніпро",
    #     "RUS": "Днепр",
    #     "ENG": "Dnipro"
    # },
    # "M1_S14": {
    #     "UKR": "Гідропарк",
    #     "RUS": "Гидропарк",
    #     "ENG": "Hidropark"
    # },
    # "M1_S15": {
    #     "UKR": "Лівобережна",
    #     "RUS": "Левобережная",
    #     "ENG": "Livoberezhna"
    # },
    # "M1_S16": {
    #     "UKR": "Дарниця",
    #     "RUS": "Дарница",
    #     "ENG": "Darbytsia"
    # },
    # "M1_S17": {
    #     "UKR": "Чернігівська",
    #     "RUS": "Черниговская",
    #     "ENG": "Chernihivska"
    # },
    # "M1_S18": {
    #     "UKR": "Лісова",
    #     "RUS": "Лесная",
    #     "ENG": "Lisova"
    # },
    #
    #
    #
    # "M2_S1": {
    #     "UKR": "Теремки",
    #     "RUS": "Теремки",
    #     "ENG": "Teremky"
    # },
    # "M2_S2": {
    #     "UKR": "Іподром",
    #     "RUS": "Ипподром",
    #     "ENG": "Ipodrom"
    # },
    # "M2_S3": {
    #     "UKR": "Виставковий центр",
    #     "RUS": "Выставочный центр",
    #     "ENG": "Vystavkovyi Tsentr"
    # },
    # "M2_S4": {
    #     "UKR": "Васильківська",
    #     "RUS": "Васильковская",
    #     "ENG": "Vasylkivska"
    # },
    # "M2_S5": {
    #     "UKR": "Голосіївська",
    #     "RUS": "Голосеевская",
    #     "ENG": "Holosiivska"
    # },
    # "M2_S6": {
    #     "UKR": "Деміївська",
    #     "RUS": "Демеевская",
    #     "ENG": "Demiivska"
    # },
    # "M2_S7": {
    #     "UKR": "Либідська",
    #     "RUS": "Лыбедская",
    #     "ENG": "Lybidska"
    # },
    # "M2_S8": {
    #     "UKR": "Палац Україна",
    #     "RUS": "Дворец Украина",
    #     "ENG": "Palats Ukraina"
    # },
    # "M2_S9": {
    #     "UKR": "Олімпійська",
    #     "RUS": "Олипийская",
    #     "ENG": "Olimpiiska"
    # },
    # "M2_S10": {
    #     "UKR": "Площа Льва Толстого",
    #     "RUS": "Площадь Льва Толского",
    #     "ENG": "Ploscha Lva Tolstoho"
    # },
    # "M2_S11": {
    #     "UKR": "Майдан Незалежності",
    #     "RUS": "Площадь Независимости",
    #     "ENG": "Maidan Nezalezhnosti"
    # },
    # "M2_S12": {
    #     "UKR": "Поштова площа",
    #     "RUS": "Почтовая площадь",
    #     "ENG": "Poshtova Ploscha"
    # },
    # "M2_S13": {
    #     "UKR": "Контрактова площа",
    #     "RUS": "Контрактовая площадь",
    #     "ENG": "Kontraktova Ploscha"
    # },
    # "M2_S14": {
    #     "UKR": "Тараса Шевченка",
    #     "RUS": "Тараса Шевченка",
    #     "ENG": "Tarasa Shevchenka"
    # },
    # "M2_S15": {
    #     "UKR": "Почайна",
    #     "RUS": "Почайная",
    #     "ENG": "Pochaina"
    # },
    # "M2_S16": {
    #     "UKR": "Оболонь",
    #     "RUS": "Оболонь",
    #     "ENG": "Obolon"
    # },
    # "M2_S17": {
    #     "UKR": "Мінська",
    #     "RUS": "Минская",
    #     "ENG": "Minska"
    # },
    # "M2_S18": {
    #     "UKR": "Героїв Дніпра",
    #     "RUS": "Героев Днепра",
    #     "ENG": "Heroiv Dnipra"
    # },
    #
    #
    #
    # "M3_S1": {
    #     "UKR": "Сірець",
    #     "RUS": "Сырец",
    #     "ENG": "Syrets"
    # },
    # "M3_S2": {
    #     "UKR": "Дорогожичі",
    #     "RUS": "Дорогожичи",
    #     "ENG": "Dorohozhychi"
    # },
    # "M3_S3": {
    #     "UKR": "Лук'янівська",
    #     "RUS": "Лукьяновская",
    #     "ENG": "Lukianivska"
    # },
    # "M3_S4": {
    #     "UKR": "Золоті ворота",
    #     "RUS": "Золотые ворота",
    #     "ENG": "Zoloti Vorota"
    # },
    # "M3_S5": {
    #     "UKR": "Палац спорту",
    #     "RUS": "Дворец спорта",
    #     "ENG": "Palats Sportu"
    # },
    # "M3_S6": {
    #     "UKR": "Кловська",
    #     "RUS": "Кловская",
    #     "ENG": "Klovska"
    # },
    # "M3_S7": {
    #     "UKR": "Печерська",
    #     "RUS": "Печерская",
    #     "ENG": "Pecherska"
    # },
    # "M3_S8": {
    #     "UKR": "Дружби народів",
    #     "RUS": "Дружбы народов",
    #     "ENG": "Druzhby Narodiv"
    # },
    # "M3_S9": {
    #     "UKR": "Видубичі",
    #     "RUS": "Выдубичи",
    #     "ENG": "Vydubychi"
    # },
    # "M3_S10": {
    #     "UKR": "Славутич",
    #     "RUS": "Славутич",
    #     "ENG": "Slavutych"
    # },
    # "M3_S11": {
    #     "UKR": "Осокорки",
    #     "RUS": "Осокорки",
    #     "ENG": "Osokorky"
    # },
    # "M3_S12": {
    #     "UKR": "Позняки",
    #     "RUS": "Позняки",
    #     "ENG": "Pozniaky"
    # },
    # "M3_S13": {
    #     "UKR": "Харківська",
    #     "RUS": "Харьковская",
    #     "ENG": "Kharkivska"
    # },
    # "M3_S14": {
    #     "UKR": "Вирлиця",
    #     "RUS": "Вырлица",
    #     "ENG": "Vyrlytsia"
    # },
    # "M3_S15": {
    #     "UKR": "Бориспільска",
    #     "RUS": "Бориспольская",
    #     "ENG": "Boryspilska"
    # },
    # "M3_S16": {
    #     "UKR": "Червоний хутір",
    #     "RUS": "Красный хутор",
    #     "ENG": "Chervony Khutir"
    # }
}

metro = {
    "M1_S1": {
        "TYPE": "START",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S2", datetime.timedelta(minutes=2, seconds=5)]
        ]
    },
    "M1_S2": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S1", datetime.timedelta(minutes=2, seconds=30)],
            ["M1_S3", datetime.timedelta(minutes=2, seconds=30)]
        ]
    },
    "M1_S3": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S2", datetime.timedelta(minutes=2, seconds=45)],
            ["M1_S4", datetime.timedelta(minutes=1, seconds=25)]
        ]
    },
    "M1_S4": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S3", datetime.timedelta(minutes=1, seconds=30)],
            ["M1_S5", datetime.timedelta(minutes=1, seconds=25)]
        ]
    },
    "M1_S5": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S4", datetime.timedelta(minutes=1, seconds=30)],
            ["M1_S6", datetime.timedelta(minutes=2, seconds=50)]
        ]
    },
    "M1_S6": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S5", datetime.timedelta(minutes=2, seconds=35)],
            ["M1_S7", datetime.timedelta(minutes=1, seconds=35)]
        ]
    },
    "M1_S7": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S6", datetime.timedelta(minutes=1, seconds=35)],
            ["M1_S8", datetime.timedelta(minutes=2, seconds=45)]
        ]
    },
    "M1_S8": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S7", datetime.timedelta(minutes=2, seconds=35)],
            ["M1_S9", datetime.timedelta(minutes=1, seconds=35)]
        ]
    },
    "M1_S9": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S8", datetime.timedelta(minutes=1, seconds=35)],
            ["M1_S10", datetime.timedelta(minutes=1, seconds=30)]
        ]
    },
    "M1_S10": {
        "TYPE": "TRANSFER",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S9", datetime.timedelta(minutes=1, seconds=25)],
            ["M1_S11", datetime.timedelta(minutes=1, seconds=30)]
        ],
        "TRANSFER": [
            ["M3_S4", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M1_S11": {
        "TYPE": "TRANSFER",
        "DELAY": datetime.timedelta(minutes=0, seconds=25),
        "CONNECTIONS": [
            ["M1_S10", datetime.timedelta(minutes=1, seconds=25)],
            ["M1_S12", datetime.timedelta(minutes=2, seconds=10)]
        ],
        "TRANSFER": [
            ["M2_S11", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M1_S12": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=25),
        "CONNECTIONS": [
            ["M1_S11", datetime.timedelta(minutes=2, seconds=25)],
            ["M1_S13", datetime.timedelta(minutes=1, seconds=30)]
        ]
    },
    "M1_S13": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S12", datetime.timedelta(minutes=1, seconds=30)],
            ["M1_S14", datetime.timedelta(minutes=2, seconds=10)]
        ]
    },
    "M1_S14": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S13", datetime.timedelta(minutes=1, seconds=55)],
            ["M1_S15", datetime.timedelta(minutes=2, seconds=15)]
        ]
    },
    "M1_S15": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S14", datetime.timedelta(minutes=2, seconds=15)],
            ["M1_S16", datetime.timedelta(minutes=1, seconds=40)]
        ]
    },
    "M1_S16": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S15", datetime.timedelta(minutes=1, seconds=40)],
            ["M1_S17", datetime.timedelta(minutes=2, seconds=5)]
        ]
    },
    "M1_S17": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S16", datetime.timedelta(minutes=2, seconds=5)],
            ["M1_S18", datetime.timedelta(minutes=1, seconds=55)]
        ]
    },
    "M1_S18": {
        "TYPE": "END",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M1_S17", datetime.timedelta(minutes=1, seconds=45)]
        ]
    },



    "M2_S1": {
        "TYPE": "START",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S2", datetime.timedelta(minutes=2, seconds=5)]
        ]
    },
    "M2_S2": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S1", datetime.timedelta(minutes=2, seconds=5)],
            ["M2_S3", datetime.timedelta(minutes=1, seconds=20)]
        ]
    },
    "M2_S3": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S2", datetime.timedelta(minutes=1, seconds=20)],
            ["M2_S4", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M2_S4": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S3", datetime.timedelta(minutes=3, seconds=0)],
            ["M2_S5", datetime.timedelta(minutes=2, seconds=0)]
        ]
    },
    "M2_S5": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S4", datetime.timedelta(minutes=2, seconds=5)],
            ["M2_S6", datetime.timedelta(minutes=1, seconds=25)]
        ]
    },
    "M2_S6": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S5", datetime.timedelta(minutes=1, seconds=20)],
            ["M2_S7", datetime.timedelta(minutes=1, seconds=45)]
        ]
    },
    "M2_S7": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S6", datetime.timedelta(minutes=1, seconds=30)],
            ["M2_S8", datetime.timedelta(minutes=1, seconds=20)]
        ]
    },
    "M2_S8": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S7", datetime.timedelta(minutes=1, seconds=15)],
            ["M2_S9", datetime.timedelta(minutes=1, seconds=35)]
        ]
    },
    "M2_S9": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S8", datetime.timedelta(minutes=1, seconds=30)],
            ["M2_S10", datetime.timedelta(minutes=1, seconds=30)]
        ]
    },
    "M2_S10": {
        "TYPE": "TRANSFER",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S9", datetime.timedelta(minutes=1, seconds=30)],
            ["M2_S11", datetime.timedelta(minutes=3, seconds=25)]
        ],
        "TRANSFER": [
            ["M3_S5", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M2_S11": {
        "TYPE": "TRANSFER",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S10", datetime.timedelta(minutes=1, seconds=25)],
            ["M2_S12", datetime.timedelta(minutes=1, seconds=45)]
        ],
        "TRANSFER": [
            ["M1_S11", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M2_S12": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S11", datetime.timedelta(minutes=1, seconds=55)],
            ["M2_S13", datetime.timedelta(minutes=1, seconds=25)]
        ]
    },
    "M2_S13": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S12", datetime.timedelta(minutes=1, seconds=25)],
            ["M2_S14", datetime.timedelta(minutes=2, seconds=10)]
        ]
    },
    "M2_S14": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S13", datetime.timedelta(minutes=1, seconds=50)],
            ["M2_S15", datetime.timedelta(minutes=2, seconds=35)]
        ]
    },
    "M2_S15": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S14", datetime.timedelta(minutes=2, seconds=10)],
            ["M2_S16", datetime.timedelta(minutes=2, seconds=0)]
        ]
    },
    "M2_S16": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S15", datetime.timedelta(minutes=2, seconds=10)],
            ["M2_S17", datetime.timedelta(minutes=1, seconds=35)]
        ]
    },
    "M2_S17": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S16", datetime.timedelta(minutes=1, seconds=40)],
            ["M2_S18", datetime.timedelta(minutes=1, seconds=55)]
        ]
    },
    "M2_S18": {
        "TYPE": "END",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M2_S17", datetime.timedelta(minutes=1, seconds=55)]
        ]
    },



    "M3_S1": {
        "TYPE": "START",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S2", datetime.timedelta(minutes=2, seconds=5)]
        ]
    },
    "M3_S2": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S1", datetime.timedelta(minutes=2, seconds=5)],
            ["M3_S3", datetime.timedelta(minutes=3, seconds=5)]
        ]
    },
    "M3_S3": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S2", datetime.timedelta(minutes=3, seconds=0)],
            ["M3_S4", datetime.timedelta(minutes=4, seconds=30)]
        ]
    },
    "M3_S4": {
        "TYPE": "TRANSFER",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S3", datetime.timedelta(minutes=4, seconds=0)],
            ["M3_S5", datetime.timedelta(minutes=1, seconds=25)]
        ],
        "TRANSFER": [
            ["M1_S10", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M3_S5": {
        "TYPE": "TRANSFER",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S4", datetime.timedelta(minutes=1, seconds=25)],
            ["M3_S6", datetime.timedelta(minutes=1, seconds=45)]
        ],
        "TRANSFER": [
            ["M2_S10", datetime.timedelta(minutes=3, seconds=0)]
        ]
    },
    "M3_S6": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S5", datetime.timedelta(minutes=1, seconds=50)],
            ["M3_S7", datetime.timedelta(minutes=1, seconds=55)]
        ]
    },
    "M3_S7": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S6", datetime.timedelta(minutes=2, seconds=00)],
            ["M3_S8", datetime.timedelta(minutes=1, seconds=40)]
        ]
    },
    "M3_S8": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S7", datetime.timedelta(minutes=1, seconds=40)],
            ["M3_S9", datetime.timedelta(minutes=2, seconds=25)]
        ]
    },
    "M3_S9": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S8", datetime.timedelta(minutes=2, seconds=30)],
            ["M3_S10", datetime.timedelta(minutes=4, seconds=30)]
        ]
    },
    "M3_S10": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S9", datetime.timedelta(minutes=4, seconds=40)],
            ["M3_S11", datetime.timedelta(minutes=1, seconds=25)]
        ]
    },
    "M3_S11": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S10", datetime.timedelta(minutes=1, seconds=25)],
            ["M3_S12", datetime.timedelta(minutes=2, seconds=40)]
        ]
    },
    "M3_S12": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S11", datetime.timedelta(minutes=2, seconds=30)],
            ["M3_S13", datetime.timedelta(minutes=2, seconds=40)]
        ]
    },
    "M3_S13": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S12", datetime.timedelta(minutes=2, seconds=30)],
            ["M3_S14", datetime.timedelta(minutes=1, seconds=50)]
        ]
    },
    "M3_S14": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S13", datetime.timedelta(minutes=1, seconds=45)],
            ["M3_S15", datetime.timedelta(minutes=1, seconds=50)]
        ]
    },
    "M3_S15": {
        "TYPE": "REGULAR",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S14", datetime.timedelta(minutes=1, seconds=55)],
            ["M3_S16", datetime.timedelta(minutes=2, seconds=0)]
        ]
    },
    "M3_S16": {
        "TYPE": "END",
        "DELAY": datetime.timedelta(minutes=0, seconds=20),
        "CONNECTIONS": [
            ["M3_S15", datetime.timedelta(minutes=2, seconds=10)]
        ]
    }
}
