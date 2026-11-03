# -*- coding: utf-8 -*-
"""
Генератор презентации PowerPoint (.pptx) в ТОЧНОМ ДИЗАЙНЕ САЙТА (1 в 1):
- Темная тема (#040711)
- Неоновые акценты: Cyan (#38bdf8), Rose/Accent (#f43f5e), Emerald (#10b981), Amber (#f59e0b)
- Карточки с полупрозрачной заливкой и светящимися рамками
- Точные диаграммы и схемы 300 DPI из img/
- Типографика, отступы, разметка и карточки показателей в точности как на сайте
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = "/Users/home/Documents/Вычислительные_машины_и_системы/ПР-4_Разработка_и_защита_IT_проекта"
IMG_DIR = os.path.join(BASE_DIR, "img")
OUT_PPTX = os.path.join(BASE_DIR, "Презентация_ПР4_Проект1_Микитенко_Кашин_Сайт_Дизайн.pptx")
OUT_PPTX_MAIN = os.path.join(BASE_DIR, "Презентация_ПР4_Проект1_Микитенко_Ерепов.pptx")
OUT_PPTX_DOCS = os.path.join(BASE_DIR, "docs/Презентация_ПР4_Проект1_Микитенко_Ерепов.pptx")

prs = Presentation()
prs.slide_width = Inches(13.333) # 16:9
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Цветовая палитра сайта
BG_DARK = RGBColor(4, 7, 17)           # #040711
CARD_BG = RGBColor(11, 17, 32)         # #0b1120
CARD_BORDER = RGBColor(30, 41, 59)     # #1e293b
CARD_BORDER_BRIGHT = RGBColor(56, 189, 248) # #38bdf8

COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_TEXT_MUTED = RGBColor(148, 163, 184) # #94a3b8
COLOR_TEXT_SUBTLE = RGBColor(100, 116, 139) # #64748b

COLOR_CYAN = RGBColor(56, 189, 248)    # #38bdf8
COLOR_EMERALD = RGBColor(16, 185, 129) # #10b981
COLOR_ROSE = RGBColor(244, 63, 94)     # #f43f5e
COLOR_AMBER = RGBColor(245, 158, 11)   # #f59e0b

def set_slide_background(slide):
    # Добавляем полноразмерный прямоугольник темного фона
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.color.rgb = BG_DARK
    return bg

def add_site_header(slide, title, category="НИТУ МИСИС • КАФЕДРА ИКТ • ПРОЕКТ № 1"):
    set_slide_background(slide)
    
    # Категория
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = COLOR_CYAN
    
    # Заголовок слайда
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title
    p_title.font.size = Pt(20)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

def add_card(slide, left, top, width, height, fill_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1)
    return shape

# =============================================================================
# СЛАЙД 1: ТИТУЛЬНЫЙ В ДИЗАЙНЕ САЙТА
# =============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1)

# Верхний кикер
kicker = s1.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(0.4))
tf_k = kicker.text_frame
p_k = tf_k.paragraphs[0]
p_k.text = "НИТУ МИСИС • ИНСТИТУТ КОМПЬЮТЕРНЫХ НАУК (ИКН) • КАФЕДРА ИКТ"
p_k.font.size = Pt(11)
p_k.font.bold = True
p_k.font.color.rgb = COLOR_CYAN

# Главный заголовок
h1_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(11.7), Inches(1.3))
tf_h1 = h1_box.text_frame
tf_h1.word_wrap = True
p_h1 = tf_h1.paragraphs[0]
p_h1.text = "Архитектура, аппаратные компоненты и стандарты проводных сетей: исследование сетевых устройств в технологии Ethernet"
p_h1.font.size = Pt(22)
p_h1.font.bold = True
p_h1.font.color.rgb = COLOR_WHITE

# Карточка 1: Описание и команда
add_card(s1, Inches(0.8), Inches(2.4), Inches(7.4), Inches(4.5))
box_desc = s1.shapes.add_textbox(Inches(1.0), Inches(2.55), Inches(7.0), Inches(4.2))
tf_d = box_desc.text_frame
tf_d.word_wrap = True

p_desc = tf_d.paragraphs[0]
p_desc.text = "Практическая работа № 4: Разработка и защита IT-проекта (Проект № 1)\nУчебная дисциплина: «Вычислительные машины, сети и системы»"
p_desc.font.size = Pt(13)
p_desc.font.color.rgb = COLOR_TEXT_MUTED
p_desc.space_after = Pt(14)

p_t_head = tf_d.add_paragraph()
p_t_head.text = "КОМАНДА ПРОЕКТА (ГР. БИВТ-26-6-9):"
p_t_head.font.size = Pt(11)
p_t_head.font.bold = True
p_t_head.font.color.rgb = COLOR_CYAN
p_t_head.space_after = Pt(6)

members = [
    ("Кашин Степан Кириллович", "👑 Старший группы, докладчик"),
    ("Ерепов Кирилл Максимович", "🎨 Дизайнер, работа с виртуальной доской"),
    ("Якушевский Игорь Игоревич", "🧪 Составитель теста (тестер)"),
    ("Утяцкий Владислав Сергеевич", "💻 Программист, моделирование сетей"),
    ("Горбунов Константин Васильевич", "📡 Коммуникатор (связь с командами)")
]
for name, role in members:
    p_m = tf_d.add_paragraph()
    p_m.text = f"• {name} — {role}"
    p_m.font.size = Pt(12)
    p_m.font.color.rgb = COLOR_WHITE
    p_m.space_after = Pt(4)

# Карточка 2: Научный руководитель
add_card(s1, Inches(8.5), Inches(2.4), Inches(4.0), Inches(4.5), border_color=CARD_BORDER_BRIGHT)
box_sci = s1.shapes.add_textbox(Inches(8.7), Inches(2.7), Inches(3.6), Inches(3.9))
tf_sci = box_sci.text_frame
tf_sci.word_wrap = True

p_s0 = tf_sci.paragraphs[0]
p_s0.text = "НАУЧНЫЙ РУКОВОДИТЕЛЬ"
p_s0.alignment = PP_ALIGN.CENTER
p_s0.font.size = Pt(11)
p_s0.font.bold = True
p_s0.font.color.rgb = COLOR_TEXT_SUBTLE
p_s0.space_after = Pt(10)

p_s1 = tf_sci.add_paragraph()
p_s1.text = "Микитенко И. И."
p_s1.alignment = PP_ALIGN.CENTER
p_s1.font.size = Pt(20)
p_s1.font.bold = True
p_s1.font.color.rgb = COLOR_WHITE
p_s1.space_after = Pt(6)

p_s2 = tf_sci.add_paragraph()
p_s2.text = "кандидат технических наук,\nстарший научный сотрудник кафедры ИКТ"
p_s2.alignment = PP_ALIGN.CENTER
p_s2.font.size = Pt(12)
p_s2.font.color.rgb = COLOR_TEXT_MUTED
p_s2.space_after = Pt(24)

p_s3 = tf_sci.add_paragraph()
p_s3.text = "НИТУ МИСИС • МОСКВА, 2026"
p_s3.alignment = PP_ALIGN.CENTER
p_s3.font.size = Pt(11)
p_s3.font.bold = True
p_s3.font.color.rgb = COLOR_EMERALD

# =============================================================================
# СЛАЙД 2: КОМАНДА И РАСПРЕДЕЛЕНИЕ ОБЯЗАННОСТЕЙ (5 КАРТОЧЕК КАК НА САЙТЕ)
# =============================================================================
s2 = prs.slides.add_slide(blank_layout)
add_site_header(s2, "1. Проектная команда и распределение обязанностей", "РАЗДЕЛ 1 • РЕГЛАМЕНТ КАФЕДРЫ ИКТ")

team_data = [
    ("Кашин С. К.", "👑 Старший, докладчик", "Общее руководство проектом, координация работы команды, защита перед комиссией.", COLOR_CYAN),
    ("Ерепов К. М.", "🎨 Дизайнер", "Проектирование интерактивной виртуальной доски Miro / Notion, инфографика L1–L3.", COLOR_ROSE),
    ("Якушевский И. И.", "🧪 Тестер", "Разработка банка из 15 тестовых заданий для кросс-тестирования потока.", COLOR_EMERALD),
    ("Утяцкий В. С.", "💻 Программист", "Моделирование в Cisco Packet Tracer, бенчмаркинг задержек и CSMA/CD.", COLOR_AMBER),
    ("Горбунов К. В.", "📡 Коммуникатор", "Организация кросс-тестирования, взаимное рецензирование, журнал вопросов.", COLOR_CYAN)
]

for idx, (t_name, t_role, t_bio, col) in enumerate(team_data):
    x = Inches(0.8 + idx * 2.38)
    add_card(s2, x, Inches(1.8), Inches(2.25), Inches(5.0), border_color=col)
    t_box = s2.shapes.add_textbox(x + Inches(0.12), Inches(1.95), Inches(2.0), Inches(4.7))
    t_tf = t_box.text_frame
    t_tf.word_wrap = True
    
    p0 = t_tf.paragraphs[0]
    p0.text = t_name
    p0.font.size = Pt(15)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_WHITE
    p0.space_after = Pt(4)
    
    p1 = t_tf.add_paragraph()
    p1.text = t_role
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = col
    p1.space_after = Pt(14)
    
    p2 = t_tf.add_paragraph()
    p2.text = t_bio
    p2.font.size = Pt(11)
    p2.font.color.rgb = COLOR_TEXT_MUTED

# =============================================================================
# ФУНКЦИЯ ДЛЯ СЛАЙДОВ С ИЗОБРАЖЕНИЕМ И 3 КАРТОЧКАМИ ПОД НИМ
# =============================================================================
def make_diagram_slide(slide_num, title, category, img_filename, cards):
    s = prs.slides.add_slide(blank_layout)
    add_site_header(s, title, category)
    
    img_path = os.path.join(IMG_DIR, img_filename)
    if os.path.exists(img_path):
        # Рамка под картинку
        add_card(s, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.7))
        # Картинка центрированная
        s.shapes.add_picture(img_path, Inches(1.2), Inches(1.6), width=Inches(10.933), height=Inches(3.5))
    
    # 3 или 4 карточки внизу
    c_count = len(cards)
    c_w = (11.733 - (c_count - 1) * 0.2) / c_count
    for i, (c_title, c_desc, c_color) in enumerate(cards):
        cx = Inches(0.8 + i * (c_w + 0.2))
        add_card(s, cx, Inches(5.35), Inches(c_w), Inches(1.7), border_color=c_color)
        c_box = s.shapes.add_textbox(cx + Inches(0.12), Inches(5.42), Inches(c_w - 0.24), Inches(1.55))
        c_tf = c_box.text_frame
        c_tf.word_wrap = True
        
        cp0 = c_tf.paragraphs[0]
        cp0.text = c_title
        cp0.font.size = Pt(11.5)
        cp0.font.bold = True
        cp0.font.color.rgb = c_color
        cp0.space_after = Pt(3)
        
        cp1 = c_tf.add_paragraph()
        cp1.text = c_desc
        cp1.font.size = Pt(10)
        cp1.font.color.rgb = COLOR_TEXT_MUTED

# =============================================================================
# СЛАЙД 3: УРОВНИ OSI
# =============================================================================
make_diagram_slide(
    3,
    "2. Архитектура оборудования: уровни модели OSI и границы доменов",
    "РАЗДЕЛ 2 • ТЕОРЕТИЧЕСКИЕ ОСНОВЫ",
    "fig1_architecture.png",
    [
        ("L3 Network (Маршрутизатор)", "N раздельных широковещательных доменов. Полная изоляция broadcast-шторма между интерфейсами.", COLOR_ROSE),
        ("L2 Data Link (Коммутатор)", "N изолированных доменов коллизий по числу портов. Аппаратная микросегментация на ASIC.", COLOR_CYAN),
        ("L1 Physical (Концентратор)", "1 общий домен коллизий (Shared Media). Полудуплекс (Half-Duplex), CSMA/CD, 0 буферизации.", COLOR_EMERALD)
    ]
)

# =============================================================================
# СЛАЙД 4: АНАТОМИЯ КАДРА
# =============================================================================
make_diagram_slide(
    4,
    "3. Анатомия кадра Ethernet II и виртуальные сети IEEE 802.1Q",
    "РАЗДЕЛ 3 • СТАНДАРТЫ IEEE 802.3",
    "fig4_ethernet_frame.png",
    [
        ("1. Преамбула + SFD (8 Б)", "7Б синхронизации (10101010...) + 1Б SFD (10101011) для тактового генератора PHY.", COLOR_ROSE),
        ("2. MAC-адреса (12 Б)", "6Б Destination + 6Б Source (24 бита OUI вендора IEEE + 24 бита ID интерфейса).", COLOR_CYAN),
        ("3. Тег 802.1Q (4 Б)", "TPID 0x8100, приоритет PCP (3 бита QoS), флаг DEI и 12 бит VLAN ID (1..4094).", COLOR_AMBER),
        ("4. MTU и CRC-32 (4 Б)", "Payload (46–1500 байт) и аппаратный полином контроля целостности FCS CRC-32.", COLOR_EMERALD)
    ]
)

# =============================================================================
# СЛАЙД 5: ТОПОЛОГИЯ CISCO PACKET TRACER
# =============================================================================
make_diagram_slide(
    5,
    "4. Корпоративная топология сети в Cisco Packet Tracer",
    "РАЗДЕЛ 4 • СЕТЕВОЕ МОДЕЛИРОВАНИЕ",
    "fig5_topology.png",
    [
        ("Маршрутизатор L3 (ISR 4331)", "Межсетевая маршрутизация IP (RIB/FIB) между подсетями. Полная изоляция broadcast-шторма.", COLOR_ROSE),
        ("Сегмент А (Switch Full-Duplex)", "Cisco Catalyst 2960-X, 1000BASE-T, аппаратная микросегментация на ASIC-матрицах, 0 коллизий.", COLOR_CYAN),
        ("Сегмент Б (Hub Half-Duplex)", "3Com SuperStack, коллизионный арбитраж CSMA/CD, единая разделяемая среда, полудуплекс.", COLOR_EMERALD)
    ]
)

# =============================================================================
# СЛАЙД 6: БЕНЧМАРКИНГ CSMA/CD
# =============================================================================
make_diagram_slide(
    6,
    "5. Эксперимент: Коллапс CSMA/CD хаба против коммутатора",
    "РАЗДЕЛ 5 • ФИЗИЧЕСКИЙ БЕНЧМАРКИНГ",
    "fig2_benchmark_latency.png",
    [
        ("Коллапс разделяемой среды", "При 100% нагрузке частота коллизий на концентраторе лавинообразно достигает 9400 кол/с из-за BEB.", COLOR_ROSE),
        ("Деградация емкости", "Полезная скорость хаба катастрофически падает со 100 Мбит/с до 8.2 Мбит/с (деградация 91.8%).", COLOR_AMBER),
        ("Преимущество Switch", "Коммутатор сохраняет линейную скорость 98.0 Мбит/с при 0 коллизий благодаря выделенным буферам.", COLOR_EMERALD)
    ]
)

# =============================================================================
# СЛАЙД 7: ЗАДЕРЖКИ КОММУТАЦИИ И РАЗГРУЗКА CPU
# =============================================================================
make_diagram_slide(
    7,
    "6. Эксперимент: Задержки коммутации и разгрузка CPU",
    "РАЗДЕЛ 6 • ИНЖЕНЕРНЫЕ ИЗМЕРЕНИЯ",
    "fig3_database_performance.png",
    [
        ("Сквозная (Cut-Through)", "Постоянная ультранизкая задержка 0.85 мкс (ASIC Cisco Nexus 3000) независимо от длины кадра.", COLOR_CYAN),
        ("Буферизация (Store-and-Forward)", "Линейный рост задержки до 12.94 мкс (1518 Б) из-за валидации FCS/CRC-32.", COLOR_AMBER),
        ("Аппаратные разгрузки (TSO/LRO)", "Сегментация TCP и Jumbo-фреймы снижают загрузку CPU хоста с 92.4% до 9.8% (разгрузка 82.6 п.п.).", COLOR_EMERALD)
    ]
)

# =============================================================================
# СЛАЙД 8: ТЕСТИРОВАНИЕ ДРУГИХ КОМАНД
# =============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_site_header(s8, "7. Банк тестовых заданий (Разработчик: Якушевский И. И.)", "РАЗДЕЛ 7 • КРОСС-ТЕСТИРОВАНИЕ ПОТОКА")

# Левая карточка: Структура теста
add_card(s8, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
b8_1 = s8.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.6))
tf8_1 = b8_1.text_frame
tf8_1.word_wrap = True

p8_1 = tf8_1.paragraphs[0]
p8_1.text = "СТРУКТУРА ТЕСТА"
p8_1.font.size = Pt(11)
p8_1.font.bold = True
p8_1.font.color.rgb = COLOR_CYAN
p8_1.space_after = Pt(4)

p8_2 = tf8_1.add_paragraph()
p8_2.text = "15 комплексных вопросов с 4 дистракторами"
p8_2.font.size = Pt(15)
p8_2.font.bold = True
p8_2.font.color.rgb = COLOR_WHITE
p8_2.space_after = Pt(12)

questions_list = [
    "• Разграничение L1/L2/L3 по доменам коллизий и broadcast;",
    "• Алгоритм BEB и правила отката при коллизиях в CSMA/CD;",
    "• Параметры задержек Cut-Through (0.85 мкс) vs Store-and-Forward;",
    "• Тегирование IEEE 802.1Q (VID 1..4094) и протокол STP 802.1D;",
    "• Аппаратные разгрузки NIC: Checksum Offload, TSO, LRO, Jumbo."
]
for q in questions_list:
    p_q = tf8_1.add_paragraph()
    p_q.text = q
    p_q.font.size = Pt(12)
    p_q.font.color.rgb = COLOR_TEXT_MUTED
    p_q.space_after = Pt(6)

# Правая карточка: Автоматизация
add_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), border_color=CARD_BORDER_BRIGHT)
b8_2 = s8.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.6))
tf8_2 = b8_2.text_frame
tf8_2.word_wrap = True

p8_3 = tf8_2.paragraphs[0]
p8_3.text = "АВТОМАТИЗАЦИЯ И РЕЦЕНЗИРОВАНИЕ"
p8_3.font.size = Pt(11)
p8_3.font.bold = True
p8_3.font.color.rgb = COLOR_EMERALD
p8_3.space_after = Pt(4)

p8_4 = tf8_2.add_paragraph()
p8_4.text = "Интерактивный веб-тест и анкета оценки"
p8_4.font.size = Pt(15)
p8_4.font.bold = True
p8_4.font.color.rgb = COLOR_WHITE
p8_4.space_after = Pt(12)

p8_5 = tf8_2.add_paragraph()
p8_5.text = "Разработан Google Apps Script для автоматического развертывания формы тестирования и анкеты экспертного оценивания по 6 официальным показателям методички (с. 33).\n\n" \
           "В веб-интерфейсе реализована защита от повторного прохождения, блокировка радиокнопок после завершения и сохранение истории попыток в localStorage."
p8_5.font.size = Pt(12)
p8_5.font.color.rgb = COLOR_TEXT_MUTED
p8_5.space_after = Pt(16)

p8_6 = tf8_2.add_paragraph()
p8_6.text = "✓ Ключи ответов верифицированы тестером проекта"
p8_6.font.size = Pt(12)
p8_6.font.bold = True
p8_6.font.color.rgb = COLOR_CYAN

# =============================================================================
# СЛАЙД 9: РЕЗЮМЕ И РЕЕСТР ССЫЛОК
# =============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_site_header(s9, "8. Итоги проекта и реестр ссылок (Регламент кафедры)", "РАЗДЕЛ 8 • ЗАКЛЮЧЕНИЕ И РЕЕСТР")

# Левая карточка: Выводы
add_card(s9, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
b9_1 = s9.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.6))
tf9_1 = b9_1.text_frame
tf9_1.word_wrap = True

p9_1 = tf9_1.paragraphs[0]
p9_1.text = "КЛЮЧЕВЫЕ ИНЖЕНЕРНЫЕ ВЫВОДЫ:"
p9_1.font.size = Pt(12)
p9_1.font.bold = True
p9_1.font.color.rgb = COLOR_CYAN
p9_1.space_after = Pt(12)

concls = [
    "1. Коммутаторы полностью вытеснили хабы благодаря ликвидации коллизий и аппаратной изоляции портов (98 Мбит/с vs 8.2 Мбит/с).",
    "2. Сквозная коммутация Cut-Through минимизирует аппаратную задержку до sub-microsecond уровня (0.85 мкс).",
    "3. Аппаратные разгрузки NIC (TSO/LRO/Jumbo) освобождают до 82.6 % ресурсов центрального процессора хоста."
]
for c in concls:
    p_c = tf9_1.add_paragraph()
    p_c.text = c
    p_c.font.size = Pt(12)
    p_c.font.color.rgb = COLOR_WHITE
    p_c.space_after = Pt(10)

# Правая карточка: Реестр ссылок
add_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), border_color=CARD_BORDER_BRIGHT)
b9_2 = s9.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.6))
tf9_2 = b9_2.text_frame
tf9_2.word_wrap = True

p9_2 = tf9_2.paragraphs[0]
p9_2.text = "РЕЕСТР СОСТАВЛЯЮЩИХ ПРОЕКТА:"
p9_2.font.size = Pt(12)
p9_2.font.bold = True
p9_2.font.color.rgb = COLOR_EMERALD
p9_2.space_after = Pt(12)

links = [
    ("Интерактивный веб-портал:", "kukes-misis.github.io/network-ethernet-project1/"),
    ("Онлайн-тест (15 вопр.):", ".../tests/Интерактивный_Тест_Ethernet.html"),
    ("Анкета рецензирования:", ".../tests/Интерактивная_Форма_Оценки_Проекта.html"),
    ("Отчет ГОСТ 7.32-2017:", "18 страниц, Таблица 4.2, формулы, листинги"),
    ("Репозиторий GitHub:", "github.com/kukes-misis/network-ethernet-project1")
]
for l_title, l_val in links:
    p_l = tf9_2.add_paragraph()
    p_l.text = f"• {l_title} {l_val}"
    p_l.font.size = Pt(11.5)
    p_l.font.color.rgb = COLOR_TEXT_MUTED
    p_l.space_after = Pt(8)

# =============================================================================
# СЛАЙД 10: СВЕДЕНИЯ ОБ ИСПОЛЬЗОВАНИИ ИИ
# =============================================================================
s10 = prs.slides.add_slide(blank_layout)
add_site_header(s10, "9. Применение технологий искусственного интеллекта в проекте", "РАЗДЕЛ 9 • СВЕДЕНИЯ ОБ ИСПОЛЬЗОВАНИИ ИИ")

add_card(s10, Inches(0.8), Inches(1.8), Inches(11.733), Inches(5.0), border_color=CARD_BORDER_BRIGHT)
b10 = s10.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(11.133), Inches(4.6))
tf10 = b10.text_frame
tf10.word_wrap = True

p10_1 = tf10.paragraphs[0]
p10_1.text = "Применяемый инструмент: нейросетевая модель Google Gemini (в режиме диалогового ассистента)"
p10_1.font.size = Pt(15)
p10_1.font.bold = True
p10_1.font.color.rgb = COLOR_WHITE
p10_1.space_after = Pt(16)

p10_2 = tf10.add_paragraph()
p10_2.text = "🔹 Самостоятельная работа студентов (гр. БИВТ-26-6-9):\n" \
             "• Теоретический анализ стандартов IEEE 802.3, анатомии кадра и тегирования 802.1Q;\n" \
             "• Расчет параметров CSMA/CD, задержек сериализации Store-and-Forward и Cut-Through;\n" \
             "• Топологическое моделирование в Cisco Packet Tracer, снятие инженерных метрик;\n" \
             "• Составление официального банка из 15 контрольных вопросов с дистракторами и очная защита."
p10_2.font.size = Pt(12.5)
p10_2.font.color.rgb = COLOR_TEXT_MUTED
p10_2.space_after = Pt(14)

p10_3 = tf10.add_paragraph()
p10_3.text = "🔹 Вспомогательная роль ИИ:\n" \
             "• Ускорение написания Python-скриптов отрисовки графиков (matplotlib/seaborn);\n" \
             "• Первичный аудит оформления библиографических записей по ГОСТ 7.0.100-2018;\n" \
             "• Верстка адаптивных веб-форм и интерактивных компонентов сайта.\n" \
             "⚠️ Все результаты работы ИИ прошли обязательную ручную инженерную проверку и корректировку студентами."
p10_3.font.size = Pt(12)
p10_3.font.color.rgb = COLOR_TEXT_MUTED
p10_3.space_after = Pt(14)

p10_4 = tf10.add_paragraph()
p10_4.text = "✓ Соответствует регламенту кафедры ИКТ НИТУ МИСИС"
p10_4.font.size = Pt(12)
p10_4.font.bold = True
p10_4.font.color.rgb = COLOR_EMERALD

# Сохранение презентации
prs.save(OUT_PPTX)
prs.save(OUT_PPTX_MAIN)
prs.save(OUT_PPTX_DOCS)
print(f"Generated PPTX in exact site style: {OUT_PPTX}")
