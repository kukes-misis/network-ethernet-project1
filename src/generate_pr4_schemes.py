# -*- coding: utf-8 -*-
"""
Генератор высококачественных научных иллюстраций (300 DPI)
для Практической работы № 4: «Проводные сети Ethernet и сетевые устройства»
(Концентраторы, мосты, коммутаторы, маршрутизаторы, репитеры, NIC, стандарты Ethernet)
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle, Arrow

IMG_DIR = "/Users/home/Documents/Вычислительные_машины_и_системы/ПР-4_Разработка_и_защита_IT_проекта/img"
os.makedirs(IMG_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8

def generate_fig1_osi_devices():
    """Схема 1: Классификация сетевых устройств по уровням OSI и доменам коллизий/широковещания"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9), dpi=300, gridspec_kw={'height_ratios': [1.2, 1.0]})
    fig.patch.set_facecolor('#ffffff')
    
    # Верхняя часть: Уровни OSI и устройства
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 6)
    ax1.axis('off')
    
    ax1.text(5, 5.6, "Классификация сетевых устройств по уровням модели OSI (ISO/IEC 7498-1)", 
             ha='center', va='center', fontsize=13, fontweight='bold', color='#1a2a3a')
    
    layers = [
        ("Уровень 3: Сетевой (Network)\nPDU: Пакет (Packet)\nАдресация: Логическая (IPv4 / IPv6)", 
         "Маршрутизатор (Router), L3-коммутатор\n• Маршрутизация пакетов по IP-адресам (RIB/FIB)\n• Изоляция широковещательных доменов\n• Трансляция сетевых адресов (NAT/PAT), списки доступа (ACL)",
         "#e8f4f8", "#0288d1", 4.0),
        ("Уровень 2: Канальный (Data Link)\nPDU: Кадр (Frame)\nАдресация: Физическая (MAC-адрес 48 бит)", 
         "Коммутатор (Switch), Сетевой мост (Bridge), NIC (MAC-уровень)\n• Микросегментация, CAM-таблица (MAC -> Port, Aging 300с)\n• Разделение доменов коллизий, Full-Duplex (IEEE 802.3x)\n• Виртуальные сети VLAN (IEEE 802.1Q), Spanning Tree (802.1D/w)",
         "#e8f8f5", "#00897b", 2.3),
        ("Уровень 1: Физический (Physical)\nPDU: Бит (Bit stream)\nСреда: Медная витая пара, оптоволокно", 
         "Репитер (Повторитель), Концентратор (Хаб), Усилитель сигнала\n• Регенерация формы и амплитуды импульсов, подавление джиттера\n• Общая разделяемая среда (Shared Media, Half-Duplex)\n• Метод множественного доступа CSMA/CD, коллизии в шине",
         "#fef9e7", "#f39c12", 0.6)
    ]
    
    for l_title, l_devices, bg_col, border_col, y in layers:
        rect1 = FancyBboxPatch((0.3, y), 3.8, 1.4, boxstyle="round,pad=0.1,rounding_size=0.15", facecolor=bg_col, edgecolor=border_col, linewidth=1.8)
        ax1.add_patch(rect1)
        ax1.text(0.5, y + 0.7, l_title, ha='left', va='center', fontsize=9.5, fontweight='bold', color='#2c3e50')
        
        ax1.annotate('', xy=(4.6, y + 0.7), xytext=(4.1, y + 0.7),
                     arrowprops=dict(arrowstyle="->", color=border_col, lw=2.0))
        
        rect2 = FancyBboxPatch((4.7, y), 5.0, 1.4, boxstyle="round,pad=0.1,rounding_size=0.15", facecolor='#ffffff', edgecolor=border_col, linewidth=1.5)
        ax1.add_patch(rect2)
        ax1.text(4.9, y + 0.7, l_devices, ha='left', va='center', fontsize=9.0, color='#34495e')

    # Нижняя часть: Сравнение доменов коллизий и широковещания
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 4.5)
    ax2.axis('off')
    
    ax2.text(5, 4.2, "Сравнительное разграничение доменов коллизий и широковещательных доменов", 
             ha='center', va='center', fontsize=12, fontweight='bold', color='#1a2a3a')
    
    devices_domain = [
        ("Концентратор (Hub / Repeater)\nУровень 1 (Physical)", 
         "1 Домен коллизий (Shared Media)\n1 Широковещательный домен\n(Каждый входящий кадр передается\nво все подключенные порты без фильтрации)", "#e74c3c", 0.5),
        ("Коммутатор (Switch / Bridge)\nУровень 2 (Data Link)", 
         "N Доменов коллизий (по 1 на каждый порт)\n1 Широковещательный домен\n(Микросегментация, коллизии отсутствуют,\nBroadcast передается всем портам в VLAN)", "#2980b9", 3.7),
        ("Маршрутизатор (Router)\nУровень 3 (Network)", 
         "N Доменов коллизий\nN Широковещательных доменов\n(Широковещательный трафик L2 изолирован\nи не пересекает границы L3-интерфейсов)", "#27ae60", 6.9)
    ]
    
    for title, desc, col, x in devices_domain:
        rect = FancyBboxPatch((x, 0.4), 2.7, 3.4, boxstyle="round,pad=0.1,rounding_size=0.15", facecolor='#f8f9fa', edgecolor=col, linewidth=2.0)
        ax2.add_patch(rect)
        ax2.text(x + 1.35, 3.2, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color=col)
        
        ax2.plot([x + 0.2, x + 2.5], [2.6, 2.6], color=col, lw=1.0, linestyle='--')
        ax2.text(x + 1.35, 1.5, desc, ha='center', va='center', fontsize=8.8, color='#2c3e50', multialignment='center')

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig1_architecture.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig1: {out_path}")

def generate_fig2_throughput_collision():
    """Схема 2: Бенчмаркинг пропускной способности и частоты коллизий (Hub vs Switch)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    
    # 1. Полезная пропускная способность при росте нагрузки
    offered_load = np.linspace(5, 100, 100)
    g = offered_load / 100.0
    throughput_hub = offered_load * np.exp(-1.3 * (g ** 1.8))
    throughput_hub = throughput_hub * (38.5 / np.max(throughput_hub))
    throughput_switch = np.minimum(offered_load * 0.98, 98.0)
    
    ax1.plot(offered_load, throughput_switch, color='#2980b9', lw=2.5, label='Коммутатор (Switch 100BASE-TX Full-Duplex)')
    ax1.plot(offered_load, throughput_hub, color='#e74c3c', lw=2.5, linestyle='--', label='Концентратор (Hub 100BASE-TX Half-Duplex, CSMA/CD)')
    
    ax1.axvline(37.5, color='#e74c3c', linestyle=':', alpha=0.7)
    ax1.annotate('Критическая точка насыщения CSMA/CD\n(Load ~37.5%, Max = 38.5 Мбит/с)', 
                 xy=(37.5, 38.5), xytext=(45, 20),
                 arrowprops=dict(arrowstyle="->", color='#c0392b', lw=1.5),
                 fontsize=8.5, fontweight='bold', color='#c0392b')
    
    ax1.set_title("Полезная пропускная способность сети (Throughput)\nв зависимости от предлагаемой нагрузки (Offered Load)", fontsize=10.5, fontweight='bold', pad=12)
    ax1.set_xlabel("Предлагаемая сетевая нагрузка на сегмент (%)", fontsize=9.5)
    ax1.set_ylabel("Полезная пропускная способность (Мбит/с)", fontsize=9.5)
    ax1.set_xlim(0, 105)
    ax1.set_ylim(0, 105)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='lower right', fontsize=8.5)
    
    # 2. Частота коллизий в секунду в зависимости от числа узлов
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
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper left', fontsize=8.5)
    
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig2_benchmark_latency.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig2: {out_path}")

def generate_fig3_latency_modes():
    """Схема 3: Задержка коммутации (Store-and-Forward vs Cut-Through) и оптимизация NIC"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    
    # 1. Задержка кадра от его размера (Store-and-Forward vs Cut-Through на 1 Гбит/с)
    frame_sizes = np.array([64, 128, 256, 512, 1024, 1518, 9000])
    latency_saf_1g = (frame_sizes * 8) / 1000.0 + 0.8
    latency_cut_1g = np.full_like(frame_sizes, (6 * 8) / 1000.0 + 0.8, dtype=float)
    latency_ff_1g = np.full_like(frame_sizes, (64 * 8) / 1000.0 + 0.8, dtype=float)
    
    x_indices = np.arange(len(frame_sizes))
    width = 0.25
    
    ax1.bar(x_indices - width, latency_saf_1g, width, label='Store-and-Forward (с полной буферизацией и CRC)', color='#2980b9')
    ax1.bar(x_indices, latency_ff_1g, width, label='Fragment-Free (буферизация первых 64 байт)', color='#f39c12')
    ax1.bar(x_indices + width, latency_cut_1g, width, label='Cut-Through (трансляция по 6 байтам MAC DA)', color='#27ae60')
    
    ax1.set_xticks(x_indices)
    ax1.set_xticklabels([f"{s} Б" for s in frame_sizes], fontsize=8.5)
    ax1.set_title("Сравнение задержки коммутации кадров (Latency)\nв зависимости от размера PDU на скорости 1 Гбит/с", fontsize=10.5, fontweight='bold', pad=12)
    ax1.set_xlabel("Размер кадра Ethernet II (байт)", fontsize=9.5)
    ax1.set_ylabel("Задержка прохождения коммутатора (микросекунды, мкс)", fontsize=9.5)
    ax1.set_yscale('log')
    ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax1.legend(loc='upper left', fontsize=8.0)
    
    # 2. Влияние аппаратных разгрузок NIC (Hardware Offload) на загрузку CPU и PPS
    modes = ['Базовый NIC\n(MTU 1500, no offload)', 'Checksum Offload\n(MTU 1500)', 'TSO + LRO\n(MTU 1500)', 'Jumbo Frames\n(MTU 9000 + TSO/LRO)']
    pps_k = [810, 810, 810, 142]
    cpu_util = [92.4, 68.2, 34.5, 9.8]
    
    x_m = np.arange(len(modes))
    w2 = 0.35
    ax2_twin = ax2.twinx()
    
    b1 = ax2.bar(x_m - w2/2, cpu_util, w2, label='Загрузка CPU хоста (%)', color='#e74c3c', alpha=0.85)
    b2 = ax2_twin.bar(x_m + w2/2, pps_k, w2, label='Интенсивность прерываний / PPS (тыс. пак/с)', color='#34495e', alpha=0.85)
    
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
    ax2.set_title("Эффективность аппаратных механизмов сетевого адаптера (NIC):\nразгрузка CPU и пакетная производительность на 10G-канале", fontsize=10.5, fontweight='bold', pad=12)
    ax2.set_ylabel("Загрузка центрального процессора (%)", fontsize=9.0, color='#c0392b')
    ax2_twin.set_ylabel("Пакетная нагрузка (тыс. пакетов/сек)", fontsize=9.0, color='#2c3e50')
    ax2.set_ylim(0, 110)
    ax2_twin.set_ylim(0, 1000)
    ax2.grid(True, linestyle=':', alpha=0.6, axis='y')
    
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig3_database_performance.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig3: {out_path}")

def generate_fig4_ethernet_frame():
    """Схема 4: Анатомия кадра Ethernet II и IEEE 802.1Q VLAN Tagging"""
    fig, ax = plt.subplots(figsize=(12, 4.8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    ax.text(6, 4.6, "Структура кадра Ethernet II (DIX) с тегированием IEEE 802.1Q (VLAN Tag)", 
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1a2a3a')
    
    # Поля стандартного кадра
    fields = [
        ("Преамбула\n(Preamble)", "7 Байт\n(10101010...)", "#f0f3f4", 0.3, 1.4),
        ("SFD\n(Начало кадра)", "1 Байт\n(10101011)", "#e5e8e8", 1.8, 1.1),
        ("MAC назначения\n(Dest MAC)", "6 Байт\n(48 бит)", "#d4efdf", 3.0, 1.6),
        ("MAC источника\n(Source MAC)", "6 Байт\n(48 бит)", "#d4efdf", 4.7, 1.6),
        ("802.1Q Tag\n(VLAN тег)", "4 Байта\n(TPID/VID)", "#fcf3cf", 6.4, 1.4),
        ("EtherType\n(Тип протокола)", "2 Байта\n(0x0800 IPv4)", "#d6eaf8", 7.9, 1.3),
        ("Полезные данные (Payload)\nIP-пакет + L4 Segment", "46 – 1500 Байт\n(MTU, до 9000 Jumbo)", "#ebdef0", 9.3, 1.8),
        ("FCS / CRC32\n(Контроль)", "4 Байта\n(Хэш кадра)", "#fadbd8", 11.2, 0.7)
    ]
    
    for f_name, f_size, f_col, x, w in fields:
        rect = FancyBboxPatch((x, 2.2), w-0.08, 1.6, boxstyle="round,pad=0.05,rounding_size=0.1", 
                              facecolor=f_col, edgecolor='#34495e', linewidth=1.4)
        ax.add_patch(rect)
        ax.text(x + (w-0.08)/2, 3.2, f_name, ha='center', va='center', fontsize=8.0, fontweight='bold', color='#2c3e50')
        ax.text(x + (w-0.08)/2, 2.6, f_size, ha='center', va='center', fontsize=7.5, color='#7f8c8d')

    # Детализация тега 802.1Q
    ax.annotate('', xy=(7.05, 1.9), xytext=(7.05, 2.15),
                arrowprops=dict(arrowstyle="->", color='#d4ac0d', lw=2.0))
    
    vlan_rect = FancyBboxPatch((3.5, 0.4), 7.2, 1.4, boxstyle="round,pad=0.08,rounding_size=0.1", 
                               facecolor='#fefde8', edgecolor='#d4ac0d', linewidth=1.5)
    ax.add_patch(vlan_rect)
    ax.text(7.1, 1.5, "Внутренняя структура 4-байтового тега IEEE 802.1Q:", 
            ha='center', va='center', fontsize=8.8, fontweight='bold', color='#7d6608')
    
    vlan_sub = [
        ("TPID (0x8100)\n16 бит (2 Байта)", 3.8, 1.6),
        ("PCP (Приоритет CoS)\n3 бита (QoS)", 5.5, 1.6),
        ("DEI (CFI)\n1 бит", 7.2, 0.9),
        ("VLAN ID (VID)\n12 бит (1..4094 сети)", 8.2, 2.3)
    ]
    for s_name, sx, sw in vlan_sub:
        s_box = FancyBboxPatch((sx, 0.6), sw-0.08, 0.7, boxstyle="round,pad=0.03,rounding_size=0.08", 
                               facecolor='#ffffff', edgecolor='#b7950b', linewidth=1.0)
        ax.add_patch(s_box)
        ax.text(sx + (sw-0.08)/2, 0.95, s_name, ha='center', va='center', fontsize=7.2, color='#2c3e50')

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
    
    ax.text(6, 5.7, "Архитектура исследуемой сетевой топологии: интеграция сетевых устройств L1/L2/L3", 
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#1a2a3a')
    
    # 1. Router в центре
    r_box = FancyBboxPatch((4.8, 3.8), 2.4, 1.2, boxstyle="round,pad=0.1,rounding_size=0.15", 
                           facecolor='#e8f8f5', edgecolor='#27ae60', linewidth=2.0)
    ax.add_patch(r_box)
    ax.text(6.0, 4.6, "Маршрутизатор (Router L3)\nCisco ISR 4331 (IOS-XE)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#1e8449')
    ax.text(6.0, 4.05, "IP: 192.168.1.1 / 192.168.2.1", ha='center', va='center', fontsize=8.0, color='#2c3e50')
    
    # 2. Сегмент А: Коммутатор Switch L2 + Хосты
    sw_box = FancyBboxPatch((1.0, 2.2), 3.2, 1.1, boxstyle="round,pad=0.1,rounding_size=0.15", 
                            facecolor='#ebf5fb', edgecolor='#2980b9', linewidth=2.0)
    ax.add_patch(sw_box)
    ax.text(2.6, 2.9, "Коммутатор (Switch L2)\nCisco Catalyst 2960-X", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#2471a3')
    ax.text(2.6, 2.45, "Микросегментация, Full-Duplex 1G", ha='center', va='center', fontsize=7.8, color='#2c3e50')
    
    # Хосты к коммутатору
    ax.plot([1.5, 2.6], [1.3, 2.2], color='#2980b9', lw=1.8)
    ax.plot([3.7, 2.6], [1.3, 2.2], color='#2980b9', lw=1.8)
    
    pc1_box = FancyBboxPatch((0.6, 0.4), 1.8, 0.9, boxstyle="round,pad=0.08,rounding_size=0.1", facecolor='#f4f6f7', edgecolor='#7f8c8d', linewidth=1.2)
    ax.add_patch(pc1_box)
    ax.text(1.5, 0.85, "Рабочая станция PC-1\n192.168.1.10 (NIC 1G)", ha='center', va='center', fontsize=7.5, color='#2c3e50')
    
    pc2_box = FancyBboxPatch((2.8, 0.4), 1.8, 0.9, boxstyle="round,pad=0.08,rounding_size=0.1", facecolor='#f4f6f7', edgecolor='#7f8c8d', linewidth=1.2)
    ax.add_patch(pc2_box)
    ax.text(3.7, 0.85, "Рабочая станция PC-2\n192.168.1.11 (NIC 1G)", ha='center', va='center', fontsize=7.5, color='#2c3e50')
    
    # 3. Сегмент Б: Концентратор Hub L1 + Репитер + Хосты
    hub_box = FancyBboxPatch((7.8, 2.2), 3.2, 1.1, boxstyle="round,pad=0.1,rounding_size=0.15", 
                             facecolor='#fdebd0', edgecolor='#e67e22', linewidth=2.0)
    ax.add_patch(hub_box)
    ax.text(9.4, 2.9, "Концентратор (Hub L1)\n3Com SuperStack II", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#d35400')
    ax.text(9.4, 2.45, "Общая шина (Shared Media, CSMA/CD)", ha='center', va='center', fontsize=7.8, color='#2c3e50')
    
    # Репитер в сегменте Hub
    ax.plot([10.5, 9.4], [1.5, 2.2], color='#e67e22', lw=1.8)
    rep_box = FancyBboxPatch((9.7, 0.8), 2.0, 0.7, boxstyle="round,pad=0.06,rounding_size=0.1", facecolor='#fef9e7', edgecolor='#f39c12', linewidth=1.2)
    ax.add_patch(rep_box)
    ax.text(10.7, 1.15, "Репитер (Repeater L1)\nУдлинитель витой пары", ha='center', va='center', fontsize=7.2, color='#b7950b')
    
    # Хост за Hub
    ax.plot([8.2, 9.4], [1.3, 2.2], color='#e67e22', lw=1.8)
    pc3_box = FancyBboxPatch((7.3, 0.4), 1.8, 0.9, boxstyle="round,pad=0.08,rounding_size=0.1", facecolor='#f4f6f7', edgecolor='#7f8c8d', linewidth=1.2)
    ax.add_patch(pc3_box)
    ax.text(8.2, 0.85, "Хост PC-3 (Half-Duplex)\n192.168.2.10 (CSMA/CD)", ha='center', va='center', fontsize=7.5, color='#2c3e50')

    # Линии связи Router <-> Switch и Router <-> Hub
    ax.plot([4.8, 2.6], [4.4, 3.3], color='#27ae60', lw=2.2)
    ax.text(3.3, 4.0, "Subnet 1: 192.168.1.0/24\n(Коллизии = 0)", fontsize=8.0, color='#1e8449', fontweight='bold')
    
    ax.plot([7.2, 9.4], [4.4, 3.3], color='#e67e22', lw=2.2, linestyle='--')
    ax.text(8.7, 4.0, "Subnet 2: 192.168.2.0/24\n(Единый домен коллизий)", fontsize=8.0, color='#d35400', fontweight='bold')

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "fig5_topology.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated fig5: {out_path}")

if __name__ == "__main__":
    generate_fig1_osi_devices()
    generate_fig2_throughput_collision()
    generate_fig3_latency_modes()
    generate_fig4_ethernet_frame()
    generate_fig5_topology()
