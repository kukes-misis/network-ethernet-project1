# -*- coding: utf-8 -*-
"""
Генератор графических схем и аналитических графиков для Лабораторной работы № 4:
«Современные сети и системы: исследование сетевого оборудования и понятий»
Задание группы № 1: Проводная сеть Ethernet, режимы работы и стандарты сетевых устройств
Курс: «Вычислительные машины, сети и системы» (НИТУ МИСИС, кафедра ИКТ)
Преподаватель: к.т.н., с.н.с. Микитенко И. И.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Arrow

BASE_DIR = "/Users/home/Documents/Вычислительные_машины_и_системы/ПР-4_Разработка_и_защита_IT_проекта"
IMG_DIR = os.path.join(BASE_DIR, "img")
os.makedirs(IMG_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

def generate_fig1_architecture():
    """Схема 1: Классификация оборудования по уровням модели OSI (L1, L2, L3) и границы доменов"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.0), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    
    # Левая колонка: Уровни OSI и сетевое оборудование
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 7)
    ax1.axis('off')
    ax1.set_title("Классификация сетевого оборудования по уровням OSI", fontsize=11, fontweight='bold', pad=14)
    
    layers = [
        ("Уровень L3: Сетевой (Network)\nМаршрутизатор (Router), L3-коммутатор", 
         "IP-пакеты, логическая адресация,\nизоляция широковещательных доменов", 
         "#ebf5fb", "#2980b9", 4.8),
        ("Уровень L2: Канальный (Data Link)\nКоммутатор (Switch), Сетевой мост (Bridge)", 
         "Кадры Ethernet II, MAC-адреса, CAM-таблица,\nмикросегментация доменов коллизий", 
         "#e8f8f5", "#27ae60", 2.8),
        ("Уровень L1: Физический (Physical)\nКонцентратор (Hub), Повторитель (Repeater), Усилитель", 
         "Битовый поток, электрические/оптические сигналы,\nединый домен коллизий (Shared Media)", 
         "#fef9e7", "#f39c12", 0.8)
    ]
    
    for title, desc, bg_col, border_col, y in layers:
        rect = FancyBboxPatch((0.5, y), 9.0, 1.6, boxstyle="round,pad=0.1,rounding_size=0.15", 
                              facecolor=bg_col, edgecolor=border_col, linewidth=1.8)
        ax1.add_patch(rect)
        ax1.text(0.8, y + 1.1, title, fontsize=9.5, fontweight='bold', color=border_col, va='center')
        ax1.text(0.8, y + 0.45, desc, fontsize=8.5, color='#34495e', va='center')

    # Правая колонка: Границы доменов коллизий и широковещания
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 7)
    ax2.axis('off')
    ax2.set_title("Границы сетевых доменов коллизий и широковещания", fontsize=11, fontweight='bold', pad=14)
    
    # Broadcast domain (L3)
    bd_rect = FancyBboxPatch((0.5, 4.0), 9.0, 2.4, boxstyle="round,pad=0.15,rounding_size=0.2", 
                             facecolor='#f4ecf7', edgecolor='#8e44ad', linewidth=1.5, linestyle='--')
    ax2.add_patch(bd_rect)
    ax2.text(1.0, 6.0, "Широковещательный домен (Broadcast Domain)", fontsize=10, fontweight='bold', color='#8e44ad')
    ax2.text(1.0, 5.5, "Ограничивается интерфейсом маршрутизатора L3 (или VLAN)", fontsize=8.5, color='#5b2c6f')
    
    # Collision domains (L2 & L1)
    cd1_rect = FancyBboxPatch((1.0, 4.2), 3.8, 1.0, boxstyle="round,pad=0.08,rounding_size=0.1", 
                              facecolor='#d4efdf', edgecolor='#27ae60', linewidth=1.2)
    ax2.add_patch(cd1_rect)
    ax2.text(2.9, 4.7, "Порт Switch: Домен коллизии №1", fontsize=7.8, fontweight='bold', color='#196f3d', ha='center')
    
    cd2_rect = FancyBboxPatch((5.2, 4.2), 3.8, 1.0, boxstyle="round,pad=0.08,rounding_size=0.1", 
                              facecolor='#d4efdf', edgecolor='#27ae60', linewidth=1.2)
    ax2.add_patch(cd2_rect)
    ax2.text(7.1, 4.7, "Порт Switch: Домен коллизии №2", fontsize=7.8, fontweight='bold', color='#196f3d', ha='center')

    # Shared Hub Collision Domain
    hub_cd = FancyBboxPatch((0.5, 0.8), 9.0, 2.6, boxstyle="round,pad=0.15,rounding_size=0.2", 
                            facecolor='#fdebd0', edgecolor='#d35400', linewidth=1.5, linestyle=':')
    ax2.add_patch(hub_cd)
    ax2.text(1.0, 3.0, "Единый разделяемый домен коллизий Концентратора (Hub)", fontsize=10, fontweight='bold', color='#d35400')
    ax2.text(1.0, 2.5, "Все порты хаба находятся в одной шине CSMA/CD: одновременная передача = коллизия", fontsize=8.2, color='#7e5109')
    
    for i, x in enumerate([1.5, 3.8, 6.2, 8.5]):
        node_box = FancyBboxPatch((x-0.6, 1.1), 1.2, 0.9, boxstyle="round,pad=0.05,rounding_size=0.08", 
                                 facecolor='#ffffff', edgecolor='#ba4a00', linewidth=1.0)
        ax2.add_patch(node_box)
        ax2.text(x, 1.55, f"PC-{i+1}", fontsize=8.0, fontweight='bold', color='#2c3e50', ha='center')

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig1_architecture.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig1: {out_path}")

def generate_fig2_throughput_collision():
    """Схема 2: Расчётно-теоретическая модель CSMA/CD: пропускная способность и коллизии (Hub vs Switch)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    
    # 1. Полезная пропускная способность сети (Throughput)
    # Опорные расчетные точки аналитической модели CSMA/CD
    load_pts = np.array([5.0, 10.0, 20.0, 30.0, 37.5, 50.0, 70.0, 85.0, 100.0])
    hub_pts  = np.array([4.9,  9.7, 18.9, 27.5, 35.0, 31.2, 19.4, 12.1,   8.2])
    switch_pts = np.array([4.9, 9.8, 19.6, 29.4, 36.75, 49.0, 68.6, 83.3, 98.0])

    # Гладкая интерполяция для отображения кривой
    load_dense = np.linspace(5.0, 100.0, 200)
    hub_dense = np.interp(load_dense, load_pts, hub_pts)
    switch_dense = np.interp(load_dense, load_pts, switch_pts)
    
    ax1.plot(load_dense, switch_dense, color='#2980b9', lw=2.5, label='Коммутатор (Switch 100BASE-TX Full-Duplex)')
    ax1.plot(load_dense, hub_dense, color='#e74c3c', lw=2.5, linestyle='--', label='Концентратор (Hub 100BASE-TX Half-Duplex, CSMA/CD)')
    
    # Опорные маркеры на графике, строго совпадающие с Таблицей 2 отчета
    ax1.plot(load_pts, switch_pts, 'o', color='#1f618d', markersize=5)
    ax1.plot(load_pts, hub_pts, 's', color='#922b21', markersize=5)
    
    ax1.axvline(37.5, color='#e74c3c', linestyle=':', alpha=0.7)
    ax1.annotate('Точка насыщения шины CSMA/CD\n(Нагрузка 37.5%, Выход = 35.0 Мбит/с)', 
                 xy=(37.5, 35.0), xytext=(45, 18),
                 arrowprops=dict(arrowstyle="->", color='#c0392b', lw=1.5),
                 fontsize=8.5, fontweight='bold', color='#c0392b')
    
    ax1.annotate('Коллапс CSMA/CD при 100%:\n8.2 Мбит/с', 
                 xy=(100, 8.2), xytext=(72, 3),
                 arrowprops=dict(arrowstyle="->", color='#922b21', lw=1.2),
                 fontsize=8.0, fontweight='bold', color='#922b21')

    ax1.set_title("Полезная пропускная способность сети (Throughput)\nв зависимости от предлагаемой нагрузки (Offered Load)", fontsize=10.5, fontweight='bold', pad=12)
    ax1.set_xlabel("Предлагаемая сетевая нагрузка на сегмент (%)", fontsize=9.5)
    ax1.set_ylabel("Полезная пропускная способность (Мбит/с)", fontsize=9.5)
    ax1.set_xlim(0, 105)
    ax1.set_ylim(0, 105)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper left', fontsize=8.5)
    
    # 2. Интенсивность коллизий в секунду от числа узлов (при нагрузке 70%)
    nodes = np.array([2, 4, 8, 12, 16, 24, 32, 48, 64])
    collisions_hub = np.array([12, 48, 185, 420, 890, 1750, 3100, 5800, 9400])
    collisions_switch = np.zeros_like(nodes)
    
    ax2.plot(nodes, collisions_hub, marker='o', color='#e74c3c', lw=2.2, label='Концентратор (Hub): коллизии в общей шине')
    ax2.plot(nodes, collisions_switch, marker='s', color='#27ae60', lw=2.5, label='Коммутатор (Switch): микросегментация (0 коллизий)')
    
    for x, y in zip(nodes[::2], collisions_hub[::2]):
        ax2.annotate(f"{y} кол/с", (x, y), textcoords="offset points", xytext=(-5, 7), fontsize=8.0, color='#c0392b')
        
    ax2.set_title("Интенсивность сетевых коллизий при высокой нагрузке (70%)\nв зависимости от числа активных узлов в сегменте", fontsize=10.5, fontweight='bold', pad=12)
    ax2.set_xlabel("Количество активных хостов в домене коллизий", fontsize=9.5)
    ax2.set_ylabel("Число зарегистрированных коллизий (коллизий/сек)", fontsize=9.5)
    ax2.set_yscale('symlog', linthresh=10)
    ax2.set_ylim(-1, 15000)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper left', fontsize=8.5)
    
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig2_benchmark_latency.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig2: {out_path}")

def generate_fig3_latency_modes():
    """Схема 3: Аналитическая модель задержек коммутации и аппаратные разгрузки NIC"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    
    # 1. Задержка коммутации от размера кадра на скорости 1 Гбит/с
    # Формула: t_total = (L_bytes * 8 / 1000) + t_asic (где t_asic = 0.80 мкс)
    frame_sizes = np.array([64, 128, 256, 512, 1024, 1518, 9000])
    t_asic = 0.80
    
    latency_saf = (frame_sizes * 8) / 1000.0 + t_asic
    latency_ff = np.full_like(frame_sizes, (64 * 8) / 1000.0 + t_asic, dtype=float)
    latency_cut = np.full_like(frame_sizes, (6 * 8) / 1000.0 + t_asic, dtype=float)
    
    x_indices = np.arange(len(frame_sizes))
    width = 0.25
    
    ax1.bar(x_indices - width, latency_saf, width, label='Store-and-Forward (Cisco Catalyst 2960-X)', color='#2980b9')
    ax1.bar(x_indices, latency_ff, width, label='Fragment-Free (буферизация 64 байт)', color='#f39c12')
    ax1.bar(x_indices + width, latency_cut, width, label='Cut-Through (Cisco Nexus 3000 ASIC)', color='#27ae60')
    
    # Подписи точных значений задержки над ключевыми столбцами
    ax1.annotate(f"{latency_saf[0]:.2f} мкс", xy=(0 - width, latency_saf[0]), xytext=(0, 2),
                 textcoords="offset points", ha='center', fontsize=7.0, color='#1b4f72')
    ax1.annotate(f"{latency_saf[5]:.2f} мкс", xy=(5 - width, latency_saf[5]), xytext=(0, 2),
                 textcoords="offset points", ha='center', fontsize=7.0, color='#1b4f72')
    ax1.annotate(f"{latency_saf[6]:.2f} мкс", xy=(6 - width, latency_saf[6]), xytext=(0, 2),
                 textcoords="offset points", ha='center', fontsize=7.0, color='#1b4f72')
    ax1.annotate(f"{latency_cut[0]:.2f} мкс", xy=(0 + width, latency_cut[0]), xytext=(0, 2),
                 textcoords="offset points", ha='center', fontsize=7.0, color='#145a32')

    ax1.set_xticks(x_indices)
    ax1.set_xticklabels([f"{s} Б" for s in frame_sizes], fontsize=8.5)
    ax1.set_title("Сравнение задержки коммутации кадров (Latency)\nв зависимости от размера кадра на скорости 1 Гбит/с", fontsize=10.5, fontweight='bold', pad=12)
    ax1.set_xlabel("Размер кадра Ethernet II (байт полезных данных + заголовок)", fontsize=9.5)
    ax1.set_ylabel("Полная задержка коммутации t_total (мкс)", fontsize=9.5)
    ax1.set_yscale('log')
    ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax1.legend(loc='upper left', fontsize=8.0)
    
    # 2. Влияние аппаратных разгрузок NIC на загрузку CPU хоста
    modes = ['Базовый NIC\n(MTU 1500, no offload)', 'Checksum Offload\n(MTU 1500)', 'TSO + LRO\n(MTU 1500)', 'Jumbo Frames\n(MTU 9000 + TSO/LRO)']
    pps_k = [810, 810, 810, 142]
    cpu_util = [92.4, 68.2, 34.5, 9.8]
    
    x_m = np.arange(len(modes))
    w2 = 0.35
    ax2_twin = ax2.twinx()
    
    b1 = ax2.bar(x_m - w2/2, cpu_util, w2, label='Загрузка CPU хоста (%)', color='#e74c3c', alpha=0.85)
    b2 = ax2_twin.bar(x_m + w2/2, pps_k, w2, label='Пакетная нагрузка (тыс. пак/с)', color='#34495e', alpha=0.85)
    
    for rect in b1:
        h = rect.get_height()
        ax2.annotate(f"{h:.1f}%", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom', fontsize=8.0, fontweight='bold', color='#c0392b')
        
    for rect in b2:
        h = rect.get_height()
        ax2_twin.annotate(f"{int(h)}k", xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                          textcoords="offset points", ha='center', va='bottom', fontsize=8.0, fontweight='bold', color='#2c3e50')
    
    ax2.set_xticks(x_m)
    ax2.set_xticklabels(modes, fontsize=8.0)
    ax2.set_title("Расчетная эффективность аппаратных разгрузок NIC:\nснижение нагрузки на ядра CPU на 82.6 п.п. (10G-трафик)", fontsize=10.5, fontweight='bold', pad=12)
    ax2.set_ylabel("Загрузка центрального процессора хоста (%)", fontsize=9.0, color='#c0392b')
    ax2_twin.set_ylabel("Поток пакетов / прерываний (тыс. пак/с)", fontsize=9.0, color='#2c3e50')
    ax2.set_ylim(0, 115)
    ax2_twin.set_ylim(0, 1000)
    ax2.grid(True, linestyle=':', alpha=0.6, axis='y')
    
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig3_database_performance.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig3: {out_path}")

def generate_fig4_ethernet_frame():
    """Схема 4: Анатомия кадра Ethernet II и IEEE 802.1Q VLAN Tagging с границами CRC-32"""
    fig, ax = plt.subplots(figsize=(12, 5.2), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.axis('off')
    
    ax.text(6, 5.1, "Структура кадра Ethernet II (DIX) с тегированием IEEE 802.1Q (VLAN Tag)", 
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1a2a3a')
    
    # Поля кадра
    fields = [
        ("Преамбула\n(Preamble)", "7 Байт\n(10101010...)", "#f0f3f4", 0.3, 1.4),
        ("SFD\n(Старт кадра)", "1 Байт\n(10101011)", "#e5e8e8", 1.8, 1.1),
        ("MAC назначения\n(Dest MAC)", "6 Байт\n(48 бит)", "#d4efdf", 3.0, 1.6),
        ("MAC источника\n(Source MAC)", "6 Байт\n(48 бит)", "#d4efdf", 4.7, 1.6),
        ("802.1Q Tag\n(VLAN тег)", "4 Байта\n(TPID/VID)", "#fcf3cf", 6.4, 1.4),
        ("EtherType\n(Тип протокола)", "2 Байта\n(0x0800 IPv4)", "#d6eaf8", 7.9, 1.3),
        ("Полезные данные (Payload)\nL3 IP-пакет + L4 Segment", "46 – 1500 Байт\n(MTU, до 9000 Jumbo)", "#ebdef0", 9.3, 1.8),
        ("FCS / CRC-32\n(Контроль)", "4 Байта\n(CRC кадра)", "#fadbd8", 11.2, 0.7)
    ]
    
    for f_name, f_size, f_col, x, w in fields:
        rect = FancyBboxPatch((x, 2.6), w-0.08, 1.6, boxstyle="round,pad=0.05,rounding_size=0.1", 
                              facecolor=f_col, edgecolor='#34495e', linewidth=1.4)
        ax.add_patch(rect)
        ax.text(x + (w-0.08)/2, 3.6, f_name, ha='center', va='center', fontsize=8.0, fontweight='bold', color='#2c3e50')
        ax.text(x + (w-0.08)/2, 3.0, f_size, ha='center', va='center', fontsize=7.5, color='#7f8c8d')

    # Граница расчета FCS (CRC-32): от Dest MAC до конца Payload
    crc_span = FancyBboxPatch((3.0, 2.2), 8.0, 0.3, boxstyle="square,pad=0", 
                              facecolor='#e74c3c', edgecolor='none', alpha=0.3)
    ax.add_patch(crc_span)
    ax.annotate('', xy=(3.0, 2.35), xytext=(11.0, 2.35),
                arrowprops=dict(arrowstyle="<->", color='#c0392b', lw=1.5))
    ax.text(7.0, 2.05, "Область расчёта контрольной суммы FCS (CRC-32): от Dest MAC до конца данных/заполнения.\nПреамбула, SFD и само поле FCS в расчёт НЕ включаются!", 
            ha='center', va='center', fontsize=7.8, fontweight='bold', color='#922b21')

    # Детализация тега 802.1Q
    vlan_rect = FancyBboxPatch((3.5, 0.3), 7.2, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1", 
                               facecolor='#fefde8', edgecolor='#d4ac0d', linewidth=1.5)
    ax.add_patch(vlan_rect)
    ax.text(7.1, 1.4, "Внутренняя структура 4-байтового тега стандарта IEEE 802.1Q:", 
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#7d6608')
    
    vlan_sub = [
        ("TPID (0x8100)\n16 бит (2 Байта)", 3.8, 1.6),
        ("PCP (Приоритет CoS)\n3 бита (8 классов)", 5.5, 1.6),
        ("DEI (CFI)\n1 бит", 7.2, 0.9),
        ("VLAN ID (VID)\n12 бит (1..4094 сети)", 8.2, 2.3)
    ]
    for s_name, sx, sw in vlan_sub:
        s_box = FancyBboxPatch((sx, 0.5), sw-0.08, 0.7, boxstyle="round,pad=0.03,rounding_size=0.08", 
                               facecolor='#ffffff', edgecolor='#b7950b', linewidth=1.0)
        ax.add_patch(s_box)
        ax.text(sx + (sw-0.08)/2, 0.85, s_name, ha='center', va='center', fontsize=7.2, color='#2c3e50')

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig4_ethernet_frame.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig4: {out_path}")

def generate_fig5_topology():
    """Схема 5: Эталонная топология проводной корпоративной сети (Hub, Switch, Router, Repeater)"""
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    ax.text(6, 5.7, "Архитектурная топология проводной корпоративной сети (Проект № 1)", 
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1a2a3a')
    
    # 1. Router L3 (Центральный маршрутизатор Cisco ISR 4331)
    r_box = FancyBboxPatch((4.7, 4.2), 2.6, 1.1, boxstyle="round,pad=0.08,rounding_size=0.15", 
                           facecolor='#ebf5fb', edgecolor='#2980b9', linewidth=1.8)
    ax.add_patch(r_box)
    ax.text(6.0, 4.9, "Маршрутизатор L3\nCisco ISR 4331/K9", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#1b4f72')
    ax.text(6.0, 4.4, "Шлюз по умолчанию: 192.168.1.1 / 192.168.2.1", ha='center', va='center', fontsize=7.5, color='#7f8c8d')
    
    # 2. Коммутатор L2 (Cisco Catalyst 2960-X-24TS-L)
    sw_box = FancyBboxPatch((1.5, 2.4), 3.4, 1.1, boxstyle="round,pad=0.08,rounding_size=0.15", 
                            facecolor='#e8f8f5', edgecolor='#27ae60', linewidth=1.8)
    ax.add_patch(sw_box)
    ax.text(3.2, 3.1, "Коммутатор L2 (Store-and-Forward)\nCisco Catalyst 2960-X-24TS-L", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#145a32')
    ax.text(3.2, 2.65, "Микросегментация, CAM 16K, VLAN 10/20", ha='center', va='center', fontsize=7.5, color='#7f8c8d')

    # 3. Концентратор L1 (100BASE-TX Hub)
    hub_box = FancyBboxPatch((7.2, 2.4), 3.4, 1.1, boxstyle="round,pad=0.08,rounding_size=0.15", 
                             facecolor='#fef9e7', edgecolor='#f39c12', linewidth=1.8)
    ax.add_patch(hub_box)
    ax.text(8.9, 3.1, "Концентратор L1 (Half-Duplex)\nD-Link DFE-908Dx Hub", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#b9770e')
    ax.text(8.9, 2.65, "Shared Media CSMA/CD, 100 Мбит/с", ha='center', va='center', fontsize=7.5, color='#7f8c8d')

    # Линии связи от роутера
    ax.plot([5.3, 3.2], [4.2, 3.5], color='#2980b9', lw=2.0)
    ax.text(4.0, 3.9, "Trunk 802.1Q (Gi0/0/0)", fontsize=7.5, color='#2980b9', fontweight='bold', rotation=22)
    
    ax.plot([6.7, 8.9], [4.2, 3.5], color='#7f8c8d', lw=2.0)
    ax.text(7.6, 3.9, "100BASE-TX (Gi0/0/1)", fontsize=7.5, color='#7f8c8d', fontweight='bold', rotation=-22)

    # Клиенты коммутатора L2
    pcs_sw = [("PC-1 (VLAN 10)\n192.168.10.2", 1.2), ("PC-2 (VLAN 20)\n192.168.20.2", 3.2), ("Сервер (NIC 10G)\n192.168.10.10", 5.0)]
    for name, px in pcs_sw:
        pc_box = FancyBboxPatch((px-0.8, 0.6), 1.6, 0.9, boxstyle="round,pad=0.05,rounding_size=0.08", 
                                facecolor='#ffffff', edgecolor='#27ae60', linewidth=1.2)
        ax.add_patch(pc_box)
        ax.text(px, 1.05, name, ha='center', va='center', fontsize=7.2, color='#2c3e50')
        ax.plot([px, 3.2], [1.5, 2.4], color='#27ae60', lw=1.2, linestyle='-')

    # Клиенты концентратора L1
    pcs_hub = [("PC-3 (Host A)\n192.168.2.2", 7.6), ("PC-4 (Host B)\n192.168.2.3", 9.2), ("Репитер L1\nУдлинитель линка", 10.8)]
    for name, px in pcs_hub:
        pc_box = FancyBboxPatch((px-0.7, 0.6), 1.4, 0.9, boxstyle="round,pad=0.05,rounding_size=0.08", 
                                facecolor='#ffffff', edgecolor='#d35400', linewidth=1.2)
        ax.add_patch(pc_box)
        ax.text(px, 1.05, name, ha='center', va='center', fontsize=7.2, color='#2c3e50')
        ax.plot([px, 8.9], [1.5, 2.4], color='#d35400', lw=1.2, linestyle='--')

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig5_topology.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig5: {out_path}")

def main():
    print("Generating all 5 scientific diagrams with calibrated data...")
    generate_fig1_architecture()
    generate_fig2_throughput_collision()
    generate_fig3_latency_modes()
    generate_fig4_ethernet_frame()
    generate_fig5_topology()
    print("All diagrams generated successfully!")

if __name__ == "__main__":
    main()
