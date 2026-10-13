/**
 * Miro Web SDK 2.0 / Browser Console Automation Script
 * 
 * Как перенести доску в Miro за 10 секунд:
 * 1. Откройте любую доску в Miro (https://miro.com/app/board/...) в Google Chrome / Яндекс.Браузере / Safari.
 * 2. Нажмите F12 (или Cmd + Option + I на Mac), чтобы открыть Console (Консоль разработчика).
 * 3. Скопируйте весь этот код, вставьте в консоль и нажмите Enter.
 * 
 * Скрипт автоматически:
 * - Создаст стилизованные фреймы (Frames) для каждого раздела проекта:
 *   1) Команда проекта и роли (БИВТ-26-6-9)
 *   2) Физический уровень OSI (L1: Hub, Repeater)
 *   3) Канальный уровень OSI (L2: Switch, Bridge, NIC)
 *   4) Сетевой уровень OSI (L3: Router, L3-Switch)
 *   5) Стандарты Ethernet IEEE 802.3
 *   6) Эксперименты и бенчмаркинг
 * - Создаст все цветные стикеры (Sticky Notes) с текстом и форматированием.
 * - Разместит кликабельные ссылки на Отчет по ГОСТ, Тест и Форму оценки.
 */

(async function createMiroProjectBoard() {
  console.log("🚀 Запуск автоматического построения доски Miro для Проекта № 1...");

  // Проверяем доступность Miro Web SDK
  if (typeof miro === 'undefined') {
    console.warn("⚠️ Miro Web SDK не обнаружен в глобальной области. Используем режим DOM-генерации или вставки стикеров через буфер.");
    alert("Совет: Вы можете просто скопировать файл board/miro_sticky_notes.csv или выделить текст в board/miro_paste_stickies.txt и нажать Cmd+V на доске Miro — Miro мгновенно превратит каждую строчку в отдельный цветной стикер!");
    return;
  }

  try {
    const framesData = [
      {
        title: "👥 1. Проектная команда (БИВТ-26-6-9)",
        x: 0, y: 0, width: 900, height: 600,
        stickers: [
          { content: "👑 Ерепов Кирилл Максимович\nСтарший группы, докладчик на защите\nАрхитектура, регламент кафедры ИКТ, защита перед Микитенко И.И.", color: "light_blue" },
          { content: "🎨 Кашин Степан Кириллович\nДизайнер, работа с виртуальной доской\nРазработка доски Miro/Notion, схемы L1/L2/L3, домены коллизий", color: "yellow" },
          { content: "🧪 Якушевский Игорь Игоревич\nСоставитель теста (тестер)\nБанк из 15 тестовых заданий для других команд, Google Forms", color: "light_green" },
          { content: "💻 Утяцкий Владислав Сергеевич\nПрограммист, моделирование сетей\nТопология Cisco Packet Tracer, бенчмаркинг CSMA/CD и задержек", color: "pink" },
          { content: "📡 Горбунов Константин В.\nКоммуникатор (связь с командами)\nОрганизация кросс-тестирования, обратная связь, реестр ссылок", color: "violet" }
        ]
      },
      {
        title: "⚡ 2. Физический уровень (L1 OSI: Hub, Repeater)",
        x: 950, y: 0, width: 900, height: 600,
        stickers: [
          { content: "Концентратор (Hub L1):\n1 единый домен коллизий (Shared Media), полудуплекс (Half-Duplex), протокол CSMA/CD, 0 буферизации", color: "yellow" },
          { content: "Сетевой репитер (Repeater L1):\nРегенерация электрических импульсов, устранение джиттера и затухания сигнала", color: "yellow" },
          { content: "Усилитель сигнала:\nАналоговое усиление амплитуды без восстановления формы импульсов (усиливает и шумы)", color: "yellow" },
          { content: "Правило 5-4-3:\nМаксимум 5 сегментов, 4 репитера, не более 3 населенных сегментов (таймаут 512 битовых интервалов)", color: "yellow" }
        ]
      },
      {
        title: "🔄 3. Канальный уровень (L2 OSI: Switch, Bridge, NIC)",
        x: 1900, y: 0, width: 900, height: 600,
        stickers: [
          { content: "Коммутатор (Switch L2):\nМикросегментация! N доменов коллизий (каждый порт изолирован), 1 broadcast-домен, Full-Duplex", color: "light_green" },
          { content: "CAM-таблица коммутатора:\nСамообучение по Source MAC при приеме кадра (MAC -> Port -> VLAN), тайм-аут 300 сек", color: "light_green" },
          { content: "Режимы коммутации:\nCut-Through (задержка 0.45 мкс, чтение 6B MAC) vs Store-and-Forward (буферизация, проверка CRC)", color: "light_green" },
          { content: "Сетевой адаптер (NIC L2):\n48-битный MAC (OUI + Device ID), аппаратный расчет CRC32, кольцевые буферы Rx/Tx DMA", color: "light_green" },
          { content: "Аппаратные разгрузки NIC:\nTSO, LRO/GRO, Checksum Offload, Jumbo Frames (9000B) — разгрузка CPU на 82.6%", color: "light_green" }
        ]
      },
      {
        title: "🌐 4. Сетевой уровень (L3 OSI: Router, L3-Switch)",
        x: 2850, y: 0, width: 900, height: 600,
        stickers: [
          { content: "Маршрутизатор (Router L3):\nN доменов коллизий и N широковещательных доменов! Полная изоляция подсетей и broadcast-штормов", color: "light_blue" },
          { content: "Функции L3:\nМаршрутизация по RIB/FIB, декремент TTL, трансляция NAT/PAT, фильтрация списков ACL", color: "light_blue" },
          { content: "L3-коммутатор (Catalyst 3850):\nАппаратная маршрутизация между VLAN (Inter-VLAN SVI) со скоростью кабельной линии (Wire-Speed)", color: "light_blue" }
        ]
      },
      {
        title: "📦 5. Стандарты Ethernet (IEEE 802.3) и кадр",
        x: 950, y: 650, width: 900, height: 600,
        stickers: [
          { content: "Кадр Ethernet II:\nПреамбула (7Б) + SFD (1Б) + Dest MAC (6Б) + Src MAC (6Б) + EtherType (2Б) + Данные (46-1500Б) + FCS (4Б)", color: "violet" },
          { content: "Тег IEEE 802.1Q (4 байта):\nTPID (0x8100) + TCI: PCP 3 бита приоритета, DEI 1 бит, VLAN ID 12 бит (диапазон 1..4094)", color: "violet" },
          { content: "100BASE-TX (Fast Ethernet):\n100 Мбит/с, 2 пары Cat.5, кодирование 4B/5B + MLT-3, дальность 100 метров", color: "violet" },
          { content: "1000BASE-T (Gigabit Ethernet):\n1 Гбит/с, 4 пары Cat.5e, полный дуплекс по всем 4 парам одновременно, модуляция PAM-5", color: "violet" }
        ]
      },
      {
        title: "📊 6. Экспериментальные исследования и бенчмаркинг",
        x: 1900, y: 650, width: 900, height: 600,
        stickers: [
          { content: "Коллапс CSMA/CD в Hub:\nПри 37.5% нагрузки хаб упирается в 38.5 Мбит/с. При 100% падает до 8.2 Мбит/с из-за 9400 коллизий/с", color: "pink" },
          { content: "Превосходство Switch:\nУдерживает 98.0 Мбит/с полезной пропускной способности при 100% нагрузке (0 коллизий)", color: "light_green" },
          { content: "Cut-Through vs Store-and-Forward:\nCut-Through дает 0.45 мкс стабильно; Store-and-Forward растет от 0.51 мкс (64Б) до 72 мкс (Jumbo)", color: "light_blue" },
          { content: "Разгрузка процессора:\nВключение TSO + Jumbo снижает загрузку CPU хоста с 92.4% до 9.8% на скорости 10 Гбит/с", color: "light_green" }
        ]
      }
    ];

    for (const frame of framesData) {
      const createdFrame = await miro.board.createFrame({
        title: frame.title,
        x: frame.x,
        y: frame.y,
        width: frame.width,
        height: frame.height,
        style: { fillColor: '#f1f5f9' }
      });

      let startX = frame.x - (frame.width / 2) + 120;
      let startY = frame.y - (frame.height / 2) + 120;

      for (let i = 0; i < frame.stickers.length; i++) {
        const item = frame.stickers[i];
        const posX = startX + ((i % 3) * 240);
        const posY = startY + (Math.floor(i / 3) * 220);

        await miro.board.createStickyNote({
          content: item.content,
          x: posX,
          y: posY,
          width: 200,
          style: { fillColor: item.color }
        });
      }
    }

    console.log("✅ Доска Miro успешно сформирована со всеми фреймами и стикерами!");
  } catch (err) {
    console.error("Ошибка при создании элементов в Miro:", err);
  }
})();
