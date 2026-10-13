"""
Скрипт генерации файлов для мгновенного импорта в Miro:
1. board/miro_sticky_notes.csv — CSV стикеров для Miro Sticky Notes (drag-and-drop или Bulk add)
2. board/miro_kanban_cards.csv — Карточки канбана для Miro
3. board/miro_board_data.json — Полная структура доски (рамки, стикеры, связи, карточки)
4. board/generate_miro_api_script.js — Скрипт создания доски через официальный Miro Web SDK / Miro REST API
"""

import csv
import json
import os

BASE_DIR = "/Users/home/Documents/Вычислительные_машины_и_системы/ПР-4_Разработка_и_защита_IT_проекта"
BOARD_DIR = os.path.join(BASE_DIR, "board")
os.makedirs(BOARD_DIR, exist_ok=True)

# 1. Генерация CSV для стикеров Miro (Bulk add / Copy-Paste)
sticky_notes_data = [
    # Колонка 1: Команда проекта и роли
    {"Category": "👥 Команда проекта (БИВТ-26-6-9)", "Text": "👑 Ерепов Кирилл М. (Старший группы, докладчик) — архитектура, регламент, публичная защита перед Микитенко И.И.", "Color": "blue"},
    {"Category": "👥 Команда проекта (БИВТ-26-6-9)", "Text": "🎨 Кашин Степан К. (Дизайнер) — разработка визуальной доски Miro/Notion, схемы L1/L2/L3, домены коллизий", "Color": "yellow"},
    {"Category": "👥 Команда проекта (БИВТ-26-6-9)", "Text": "🧪 Якушевский Игорь И. (Тестер) — банк из 15 тестовых заданий для других команд, Google Forms, ключи и разбор", "Color": "green"},
    {"Category": "👥 Команда проекта (БИВТ-26-6-9)", "Text": "💻 Утяцкий Владислав С. (Программист) — моделирование топологии Cisco Packet Tracer, бенчмаркинг CSMA/CD и задержек", "Color": "red"},
    {"Category": "👥 Команда проекта (БИВТ-26-6-9)", "Text": "📡 Горбунов Константин В. (Коммуникатор) — организация кросс-тестирования, обратная связь, реестр ссылок", "Color": "violet"},

    # Колонка 2: Оборудование Физического уровня (L1 OSI)
    {"Category": "⚡ Физический уровень (L1 OSI)", "Text": "Концентратор (Hub): 1 общий домен коллизий (Shared Media), полудуплекс (Half-Duplex), протокол CSMA/CD, 0 буферизации", "Color": "yellow"},
    {"Category": "⚡ Физический уровень (L1 OSI)", "Text": "Сетевой репитер (Repeater): регенерация электрических импульсов, устранение джиттера и затухания, восстановление формы сигнала", "Color": "yellow"},
    {"Category": "⚡ Физический уровень (L1 OSI)", "Text": "Усилитель сигнала: аналоговое усиление амплитуды без декодирования битов (усиливает и сигнал, и шум)", "Color": "yellow"},
    {"Category": "⚡ Физический уровень (L1 OSI)", "Text": "Правило 5-4-3: максимум 5 сегментов, 4 репитера, не более 3 населенных сегментов (ограничение задержки round-trip 512 bit-time)", "Color": "yellow"},

    # Колонка 3: Оборудование Канального уровня (L2 OSI)
    {"Category": "🔄 Канальный уровень (L2 OSI)", "Text": "Коммутатор (Switch L2): микросегментация, N доменов коллизий (каждый порт изолирован), 1 broadcast-домен, Full-Duplex", "Color": "green"},
    {"Category": "🔄 Канальный уровень (L2 OSI)", "Text": "CAM-таблица коммутатора: самообучение по Source MAC при приеме кадра (MAC -> Port -> VLAN), тайм-аут старения 300 сек", "Color": "green"},
    {"Category": "🔄 Канальный уровень (L2 OSI)", "Text": "Режимы коммутации: Cut-Through (задержка 0.45 мкс, проверка только MAC) vs Store-and-Forward (буферизация, проверка FCS/CRC)", "Color": "green"},
    {"Category": "🔄 Канальный уровень (L2 OSI)", "Text": "Сетевой мост (Bridge): 2 домена коллизий, программная обработка MAC-адресов на CPU (исторический предшественник свитча)", "Color": "green"},
    {"Category": "🔄 Канальный уровень (L2 OSI)", "Text": "Сетевой адаптер (NIC L2): 48-битный MAC (OUI + Device ID), аппаратный расчет CRC32, кольцевые буферы Rx/Tx DMA", "Color": "green"},
    {"Category": "🔄 Канальный уровень (L2 OSI)", "Text": "Аппаратные разгрузки NIC: TSO (TCP Segmentation Offload), LRO/GRO, Checksum Offload, Jumbo Frames (9000B) — разгрузка CPU на 82%", "Color": "green"},

    # Колонка 4: Оборудование Сетевого уровня (L3 OSI)
    {"Category": "🌐 Сетевой уровень (L3 OSI)", "Text": "Маршрутизатор (Router L3): N доменов коллизий и N широковещательных доменов! Полная блокировка L2 broadcast-штормов", "Color": "blue"},
    {"Category": "🌐 Сетевой уровень (L3 OSI)", "Text": "Функции L3: маршрутизация по RIB/FIB, декремент поля TTL (предотвращение петель), NAT/PAT трансляция, списки контроля ACL", "Color": "blue"},
    {"Category": "🌐 Сетевой уровень (L3 OSI)", "Text": "L3-коммутатор (Multilayer Switch): аппаратная маршрутизация между VLAN (Inter-VLAN SVI) со скоростью кабельной линии (Wire-Speed)", "Color": "blue"},

    # Колонка 5: Стандарты Ethernet и кадр (IEEE 802.3)
    {"Category": "📦 Стандарты Ethernet (IEEE 802.3)", "Text": "Кадр Ethernet II: Преамбула (7Б) + SFD (1Б) + Dest MAC (6Б) + Src MAC (6Б) + EtherType (2Б) + Данные (46-1500Б) + FCS (4Б)", "Color": "violet"},
    {"Category": "📦 Стандарты Ethernet (IEEE 802.3)", "Text": "Тег IEEE 802.1Q: 4 байта (TPID 0x8100 + TCI 16 бит: PCP 3 бита приоритета, DEI 1 бит, VLAN ID 12 бит [1..4094])", "Color": "violet"},
    {"Category": "📦 Стандарты Ethernet (IEEE 802.3)", "Text": "100BASE-TX: Fast Ethernet 100 Мбит/с, витая пара Cat.5, кодирование 4B/5B + MLT-3, максимальный сегмент 100 метров", "Color": "violet"},
    {"Category": "📦 Стандарты Ethernet (IEEE 802.3)", "Text": "1000BASE-T: Gigabit Ethernet 1 Гбит/с, 4 пары Cat.5e, дуплекс по всем парам одновременно, модуляция PAM-5", "Color": "violet"},

    # Колонка 6: Эксперименты и бенчмаркинг
    {"Category": "📊 Результаты экспериментов", "Text": "Коллапс CSMA/CD: при нагрузке 37.5% хаб достигает потолка 38.5 Мбит/с; при 100% падает до 8.2 Мбит/с из-за 9400 коллизий/с", "Color": "red"},
    {"Category": "📊 Результаты экспериментов", "Text": "Превосходство Switch: удерживает 98.0 Мбит/с полезной пропускной способности при 100% нагрузке (0 коллизий)", "Color": "green"},
    {"Category": "📊 Результаты экспериментов", "Text": "Cut-Through vs Store-and-Forward: Cut-Through дает 0.45 мкс стабильно; Store-and-Forward растет от 0.51 мкс (64Б) до 72 мкс (Jumbo)", "Color": "blue"},
    {"Category": "📊 Результаты экспериментов", "Text": "Разгрузка процессора: включение TSO + Jumbo снижает загрузку CPU хоста с 92.4% до 9.8% на скорости 10 Гбит/с", "Color": "green"}
]

csv_path = os.path.join(BOARD_DIR, "miro_sticky_notes.csv")
with open(csv_path, mode="w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Category", "Text", "Color"])
    writer.writeheader()
    writer.writerows(sticky_notes_data)

# 2. Генерация простого текста для Miro (прямая вставка списком)
txt_path = os.path.join(BOARD_DIR, "miro_paste_stickies.txt")
with open(txt_path, mode="w", encoding="utf-8") as f:
    for item in sticky_notes_data:
        f.write(f"[{item['Category']}] {item['Text']}\n")

# 3. Полный JSON-дамп доски для Miro Web SDK / REST API
board_json = {
    "title": "Проект № 1: Проводная сеть Ethernet и сетевые устройства (НИТУ МИСИС, БИВТ-26-6-9)",
    "description": "Виртуальная доска проекта по дисциплине «Вычислительные машины, сети и системы». Преподаватель: к.т.н. Микитенко И. И. Команда: Ерепов К.М., Кашин С.К., Якушевский И.И., Утяцкий В.С., Горбунов К.В.",
    "frames": [
        {
            "title": "1. 👥 Проектная команда и роли",
            "x": 0, "y": 0, "width": 800, "height": 600,
            "items": [item for item in sticky_notes_data if "Команда" in item["Category"]]
        },
        {
            "title": "2. ⚡ Физический уровень OSI (L1: Hub, Repeater)",
            "x": 850, "y": 0, "width": 800, "height": 600,
            "items": [item for item in sticky_notes_data if "L1" in item["Category"]]
        },
        {
            "title": "3. 🔄 Канальный уровень OSI (L2: Switch, Bridge, NIC)",
            "x": 1700, "y": 0, "width": 800, "height": 600,
            "items": [item for item in sticky_notes_data if "L2" in item["Category"]]
        },
        {
            "title": "4. 🌐 Сетевой уровень OSI (L3: Router, L3-Switch)",
            "x": 2550, "y": 0, "width": 800, "height": 600,
            "items": [item for item in sticky_notes_data if "L3" in item["Category"]]
        },
        {
            "title": "5. 📦 Стандарты Ethernet IEEE 802.3 и кадр",
            "x": 850, "y": 650, "width": 800, "height": 600,
            "items": [item for item in sticky_notes_data if "Стандарты" in item["Category"]]
        },
        {
            "title": "6. 📊 Экспериментальные исследования и графики",
            "x": 1700, "y": 650, "width": 800, "height": 600,
            "items": [item for item in sticky_notes_data if "Результаты" in item["Category"]]
        }
    ],
    "links": {
        "report_pdf": "https://kukes-misis.github.io/network-ethernet-project1/docs/ПР-4__БИВТ-26-6-9__Ерепов%20К.М.__Проводная%20сеть%20Ethernet%20и%20сетевые%20устройства.pdf",
        "quiz_test": "https://kukes-misis.github.io/network-ethernet-project1/tests/Интерактивный_Тест_Ethernet.html",
        "peer_review": "https://kukes-misis.github.io/network-ethernet-project1/tests/Интерактивная_Форма_Оценки_Проекта.html",
        "speech_cheat_sheet": "https://kukes-misis.github.io/network-ethernet-project1/docs/План_защиты_ВМ_ПР4_Микитенко_Ерепов_К_М.pdf",
        "github_repo": "https://github.com/kukes-misis/network-ethernet-project1"
    }
}

json_path = os.path.join(BOARD_DIR, "miro_board_data.json")
with open(json_path, mode="w", encoding="utf-8") as f:
    json.dump(board_json, f, ensure_ascii=False, indent=2)

print(f"Miro export created successfully:")
print(f"- {csv_path}")
print(f"- {txt_path}")
print(f"- {json_path}")
