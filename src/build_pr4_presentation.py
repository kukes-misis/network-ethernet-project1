# -*- coding: utf-8 -*-
"""
Генератор официальной презентации PowerPoint (.pptx)
по Практической работе № 4 (Проект № 1): «Проводные сети Ethernet и сетевые устройства»
Дисциплина: «Вычислительные машины, сети и системы» (НИТУ МИСИС)
Преподаватель: к.т.н., с.н.с. Микитенко И. И.
Студенческая команда группы БИВТ-26-6-9:
- Ерепов К. М. — Старший группы, докладчик
- Кашин С. К. — Дизайнер, работа с доской
- Якушевский И. И. — Составитель теста (тестер)
- Утяцкий В. С. — Программист, моделирование
- Горбунов К. В. — Коммуникатор
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

BASE_DIR = "/Users/home/Documents/Вычислительные_машины_и_системы/ПР-4_Разработка_и_защита_IT_проекта"
IMG_DIR = os.path.join(BASE_DIR, "img")
OUT_PPTX = os.path.join(BASE_DIR, "Презентация_ПР4_Проект1_Микитенко_Ерепов.pptx")

prs = Presentation()
prs.slide_width = Inches(13.333) # 16:9 widescreen
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6]

COLOR_PRIMARY = RGBColor(26, 42, 58)      # #1a2a3a Темно-синий
COLOR_ACCENT = RGBColor(37, 99, 235)      # #2563eb Синий
COLOR_MUTED = RGBColor(100, 116, 139)     # #64748b Серый
COLOR_CARD_BG = RGBColor(248, 250, 252)   # #f8fafc Светлый

def add_header(slide, title_text, category_text="НИТУ МИСИС • КАФЕДРА ИКТ • ПРОЕКТ № 1"):
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = txBox.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = category_text
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_ACCENT
    
    p1 = tf.add_paragraph()
    p1.text = title_text
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_PRIMARY
    p1.space_before = Pt(3)

# -----------------------------------------------------------------------------
# СЛАЙД 1: ТИТУЛЬНЫЙ
# -----------------------------------------------------------------------------
slide1 = prs.slides.add_slide(blank_layout)

title_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(4.5))
tf1 = title_box.text_frame
tf1.word_wrap = True

p_top = tf1.paragraphs[0]
p_top.text = "НИТУ МИСИС • ИНСТИТУТ КОМПЬЮТЕРНЫХ НАУК • КАФЕДРА ИКТ"
p_top.font.size = Pt(13)
p_top.font.bold = True
p_top.font.color.rgb = COLOR_ACCENT

p_main = tf1.add_paragraph()
p_main.text = "Архитектура, аппаратные компоненты и стандарты проводных сетей: исследование и сравнительный анализ сетевых устройств в технологии Ethernet"
p_main.font.size = Pt(24)
p_main.font.bold = True
p_main.font.color.rgb = COLOR_PRIMARY
p_main.space_before = Pt(14)
p_main.space_after = Pt(10)

p_sub = tf1.add_paragraph()
p_sub.text = "Практическая работа № 4: Разработка и защита IT проекта (Проект № 1)\nКурс: «Вычислительные машины, сети и системы»"
p_sub.font.size = Pt(15)
p_sub.font.color.rgb = COLOR_MUTED

p_auth = tf1.add_paragraph()
p_auth.text = "Команда проекта (гр. БИВТ-26-6-9):\n• Ерепов К. М. (руководитель, докладчик)\n• Кашин С. К. (дизайнер, работа с доской)\n• Якушевский И. И. (тестер)\n• Утяцкий В. С. (программист)\n• Горбунов К. В. (коммуникатор)\n\nПреподаватель: к.т.н., с.н.с. Микитенко И. И. | Москва, 2026"
p_auth.font.size = Pt(12)
p_auth.space_before = Pt(20)

# -----------------------------------------------------------------------------
# СЛАЙД 2: СОСТАВ КОМАНДЫ И РАСПРЕДЕЛЕНИЕ РОЛЕЙ
# -----------------------------------------------------------------------------
slide2 = prs.slides.add_slide(blank_layout)
add_header(slide2, "1. Проектная команда и распределение должностей (Регламент кафедры)")

roles = [
    ("Ерепов Кирилл Максимович", "👑 Старший группы, докладчик", "Координация научно-технических задач проекта, подготовка доклада и защита перед комиссией."),
    ("Кашин Степан Кириллович", "🎨 Дизайнер, работа с доской", "Проектирование визуальной доски Интерактивная доска проекта/Notion, схемы классификации L1/L2/L3 и доменов коллизий."),
    ("Якушевский Игорь Игоревич", "🧪 Составитель теста (тестер)", "Разработка официального банка из 15 тестовых заданий для кросс-тестирования других команд."),
    ("Утяцкий Владислав Сергеевич", "💻 Программист, моделирование", "Моделирование в Cisco Packet Tracer, бенчмаркинг полезной емкости CSMA/CD и задержек кадров."),
    ("Горбунов Константин Васильевич", "📡 Коммуникатор (связь с командами)", "Организация кросс-тестирования, проверка регламента, обратная связь, реестр ссылок.")
]

for idx, (name, role, desc) in enumerate(roles):
    y = 1.8 + idx * 1.05
    box = slide2.shapes.add_textbox(Inches(0.8), Inches(y), Inches(11.7), Inches(0.9))
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"{name} — {role}"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(12)
    p2.font.color.rgb = COLOR_MUTED

# -----------------------------------------------------------------------------
# СЛАЙД 3: УРОВНИ OSI И ДОМЕНЫ КОЛЛИЗИЙ
# -----------------------------------------------------------------------------
slide3 = prs.slides.add_slide(blank_layout)
add_header(slide3, "2. Архитектура оборудования: уровни модели OSI и границы доменов")

fig1_path = os.path.join(IMG_DIR, "fig1_architecture.png")
if os.path.exists(fig1_path):
    slide3.shapes.add_picture(fig1_path, Inches(0.8), Inches(1.6), width=Inches(11.7))

# -----------------------------------------------------------------------------
# СЛАЙД 4: АНАТОМИЯ КАДРА ETHERNET II И ТЕГ 802.1Q
# -----------------------------------------------------------------------------
slide4 = prs.slides.add_slide(blank_layout)
add_header(slide4, "3. Анатомия кадра Ethernet II и виртуальные локальные сети (IEEE 802.1Q)")

fig4_path = os.path.join(IMG_DIR, "fig4_ethernet_frame.png")
if os.path.exists(fig4_path):
    slide4.shapes.add_picture(fig4_path, Inches(0.8), Inches(1.8), width=Inches(11.7))

# -----------------------------------------------------------------------------
# СЛАЙД 5: ТОПОЛОГИЯ СЕТИ И СПЕЦИФИКАЦИЯ
# -----------------------------------------------------------------------------
slide5 = prs.slides.add_slide(blank_layout)
add_header(slide5, "4. Топология корпоративной сети и спецификация устройств")

fig5_path = os.path.join(IMG_DIR, "fig5_topology.png")
if os.path.exists(fig5_path):
    slide5.shapes.add_picture(fig5_path, Inches(0.8), Inches(1.7), width=Inches(11.7))

# -----------------------------------------------------------------------------
# СЛАЙД 6: ЭКСПЕРИМЕНТ — HUB VS SWITCH (CSMA/CD)
# -----------------------------------------------------------------------------
slide6 = prs.slides.add_slide(blank_layout)
add_header(slide6, "5. Эксперимент: Бенчмаркинг CSMA/CD хаба против коммутатора (100BASE-TX)")

fig2_path = os.path.join(IMG_DIR, "fig2_benchmark_latency.png")
if os.path.exists(fig2_path):
    slide6.shapes.add_picture(fig2_path, Inches(0.8), Inches(1.7), width=Inches(11.7))

# -----------------------------------------------------------------------------
# СЛАЙД 7: ЭКСПЕРИМЕНТ — ЗАДЕРЖКИ КОММУТАЦИИ И РАЗГРУЗКА CPU
# -----------------------------------------------------------------------------
slide7 = prs.slides.add_slide(blank_layout)
add_header(slide7, "6. Эксперимент: Задержки коммутации и аппаратные разгрузки NIC")

fig3_path = os.path.join(IMG_DIR, "fig3_database_performance.png")
if os.path.exists(fig3_path):
    slide7.shapes.add_picture(fig3_path, Inches(0.8), Inches(1.7), width=Inches(11.7))

# -----------------------------------------------------------------------------
# СЛАЙД 8: КОМПЛЕКСНЫЙ КРОСС-ТЕСТ ДЛЯ ДРУГИХ КОМАНД
# -----------------------------------------------------------------------------
slide8 = prs.slides.add_slide(blank_layout)
add_header(slide8, "7. Контрольное тестирование для других команд (Разработчик: Якушевский И. И.)")

tbox8 = slide8.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf8 = tbox8.text_frame
tf8.word_wrap = True

p_t1 = tf8.paragraphs[0]
p_t1.text = "Разработан официальный банк из 15 тестовых заданий для кросс-проверки знаний команд:"
p_t1.font.size = Pt(14)
p_t1.font.bold = True

q_examples = [
    "• Уровень работы концентратора: L1 (Physical) vs L2 коммутатора (микросегментация);",
    "• Физические коллизии в полудуплексном Ethernet (CSMA/CD) и правило отката Backoff;",
    "• Разграничение доменов коллизий (Switch L2) и широковещательных доменов (Router L3);",
    "• Режимы коммутации: константная задержка Cut-Through (0.45 мкс) vs Store-and-Forward;",
    "• Структура тега IEEE 802.1Q: TPID 0x8100, PCP (QoS), VID (1..4094 виртуальные сети);",
    "• Аппаратные механизмы NIC: Checksum Offload, TSO, LRO и Jumbo Frames 9000 байт;",
    "• Протокол Spanning Tree (STP, 802.1D/w): блокировка избыточных петель и штормов."
]
for qe in q_examples:
    p = tf8.add_paragraph()
    p.text = qe
    p.font.size = Pt(13)
    p.space_before = Pt(6)

p_t2 = tf8.add_paragraph()
p_t2.text = "\nРеализована полная автоматизация: Google Apps Script для генерации формы в 1 клик + интерактивный веб-тест."
p_t2.font.size = Pt(13)
p_t2.font.bold = True
p_t2.font.color.rgb = COLOR_ACCENT

# -----------------------------------------------------------------------------
# СЛАЙД 9: РЕЗЮМЕ И ССЫЛКИ НА СОСТАВЛЯЮЩИЕ ПРОЕКТА
# -----------------------------------------------------------------------------
slide9 = prs.slides.add_slide(blank_layout)
add_header(slide9, "8. Итоги проекта и реестр ссылок на проектные составляющие")

tbox9 = slide9.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf9 = tbox9.text_frame
tf9.word_wrap = True

p_c1 = tf9.paragraphs[0]
p_c1.text = "Ключевые инженерные выводы:"
p_c1.font.size = Pt(15)
p_c1.font.bold = True

conclusions = [
    "1. Доказано преимущество коммутируемых сетей: 0 коллизий, линейная утилизация до 98 Мбит/с против коллапса хаба (8.2 Мбит/с при 9400 кол/с).",
    "2. Сквозная коммутация Cut-Through обеспечивает постоянную задержку 0.45 мкс независимо от длины кадра.",
    "3. Аппаратные разгрузки сетевого адаптера (TSO/LRO/Jumbo) освобождают до 82.6 % ресурсов центрального процессора хоста."
]
for c in conclusions:
    p = tf9.add_paragraph()
    p.text = c
    p.font.size = Pt(13)
    p.space_before = Pt(6)

p_links = tf9.add_paragraph()
p_links.text = "\nСсылки на составляющие проекта (4-я колонка регламента кафедры):\n" \
               "• Виртуальная доска проекта (Интерактивная доска проекта): https://kukes-misis.github.io/network-ethernet-project1/\n" \
               "• Онлайн-тестирование (Google Forms): https://kukes-misis.github.io/network-ethernet-project1/tests/Интерактивный_Тест_Ethernet.html\n" \
               "• Официальный отчет (29 стр. по ГОСТ): https://github.com/kukes-misis/network-ethernet-project1/\n" \
               "• Веб-портал проекта: https://kukes-misis.github.io/network-ethernet-project1/"
p_links.font.size = Pt(12)
p_links.font.color.rgb = COLOR_ACCENT

# -----------------------------------------------------------------------------
# СЛАЙД 10: ПРИМЕНЕНИЕ ТЕХНОЛОГИЙ ИИ В ПРОЕКТЕ
# -----------------------------------------------------------------------------
slide10 = prs.slides.add_slide(blank_layout)
add_header(slide10, "9. Сведения об использовании технологий искусственного интеллекта (ИИ)")

tbox10 = slide10.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
tf10 = tbox10.text_frame
tf10.word_wrap = True

p_ai_title = tf10.paragraphs[0]
p_ai_title.text = "Применяемый инструмент: нейросетевая модель Google Gemini (в режиме диалогового ассистента)"
p_ai_title.font.size = Pt(14)
p_ai_title.font.bold = True
p_ai_title.font.color.rgb = COLOR_PRIMARY

p_ai1 = tf10.add_paragraph()
p_ai1.text = "\n🔹 Основная часть проекта (выполнена студентами группы БИВТ-26-6-9 самостоятельно):\n" \
             "• Теоретический анализ стандартов IEEE 802.3, анатомии кадра и тегирования 802.1Q;\n" \
             "• Ручной подбор и составление спецификации оборудования (Таблица 1);\n" \
             "• Сетевое моделирование в Cisco Packet Tracer, замеры задержек и пропускной способности;\n" \
             "• Разработка банка из 15 контрольных вопросов с ключами и разбором дистракторов;\n" \
             "• Проектирование архитектуры виртуальной доски Интерактивная доска проекта и очная защита проекта."
p_ai1.font.size = Pt(13)
p_ai1.font.color.rgb = COLOR_PRIMARY

p_ai2 = tf10.add_paragraph()
p_ai2.text = "\n🔹 Вспомогательная роль ИИ-ассистента:\n" \
             "• Ускорение написания Python-скриптов отрисовки графиков (matplotlib/seaborn);\n" \
             "• Первичный синтаксический аудит оформления библиографии по ГОСТ 7.0.100-2018;\n" \
             "• Генерация чернового шаблона Google Apps Script для автоматизации создания форм.\n" \
             "⚠️ Все результаты работы ИИ прошли обязательную ручную проверку и корректировку студентами."
p_ai2.font.size = Pt(13)
p_ai2.font.color.rgb = COLOR_MUTED

prs.save(OUT_PPTX)
print(f"Generated PPTX: {OUT_PPTX}")
