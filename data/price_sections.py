# data/price_sections.py

# Основні групи
GROUPS = [
    {
        "id": "consult",
        "emoji": "🩺",
        "title": "Консультація"
    },
    {
        "id": "care",
        "emoji": "✨",
        "title": "Доглядові процедури"
    },
    {
        "id": "inject",
        "emoji": "💉",
        "title": "Інʼєкції"
    },
    {
        "id": "device",
        "emoji": "⚡",
        "title": "Апаратна косметологія"
    },
    {
        "id": "laser",
        "emoji": "💡",
        "title": "Лазерна епіляція"
    },
    {
        "id": "body",
        "emoji": "🏋️",
        "title": "Корекція тіла"
    },
]

# Подрозділи з прив'язкою до групи
SECTION_DEFINITIONS = [
    {
        "id":
        "consult",
        "group":
        "consult",
        "emoji":
        "🩺",
        "title":
        "Консультації та Діагностика",
        "raw_text":
        """Консультація на апараті Observ 520 — 1500 грн
Консультація anti-age — 1000 грн
Консультація акне/проблемна шкіра — 1000 грн
Підбір домашнього догляду/процедур — 800 грн
"""
    },
    {
        "id":
        "cleansing",
        "group":
        "care",
        "emoji":
        "🧼",
        "title":
        "Чистки Обличчя та Спини",
        "raw_text":
        """Комбінована чистка обличчя — 1600 грн
Ультразвукова чистка обличчя — 1200 грн
Механічна чистка обличчя — 1400 грн
Чистка обличчя на косметиці HydroPeptide — 1800 грн
Чистка обличчя з ензимним пілінгом — 1800 грн
Чистка спини — 1800 грн
"""
    },
    {
        "id":
        "peels",
        "group":
        "care",
        "emoji":
        "🧪",
        "title":
        "Пілінги",
        "raw_text":
        """Серединний пілінг TCA — 2000 грн
Серединний пілінг PRX-T33 — 2000 грн
BioRePeelCl3 — 1800 грн
Пілінг Medik8 Even — 1000 грн
Пілінг Medik8 Clarity — 1000 грн
Retibooster — 3300 грн
Peptyglow — 1400 грн
Jalupro Glow PEEL — 1800 грн
"""
    },
    {
        "id":
        "image_care",
        "group":
        "care",
        "emoji":
        "✨",
        "title":
        "Догляд IMAGE Skincare",
        "raw_text":
        """Пілінг Perfect Lift Solution — 1200 грн
Ензимний пілінг Ormedik — 1200 грн
Карбокситерапія — насичення шкіри киснем — 1200 грн
Антиоксидантний догляд з вітаміном C — 1200 грн
Ліфтинговий пілінг Signature — 1200 грн
"""
    },
    {
        "id":
        "casmara_care",
        "group":
        "care",
        "emoji":
        "🌟",
        "title":
        "Догляд CASMARA",
        "raw_text":
        """Goji (антиоксидант, профілактика старіння) — 1600 грн
Q10 Rescue (інтенсивне живлення) — 1600 грн
Ocean Miracle (антивіковий та зміцнюючий) — 1600 грн
Skin Sensation (відновлюючий, зволожуючий, ліфтинговий) — 1600 грн
"""
    },
    {
        "id":
        "hydropeptide_care",
        "group":
        "care",
        "emoji":
        "💧",
        "title":
        "Догляд HydroPeptide",
        "raw_text":
        """Висвітлюючий догляд з вітаміном C — 1400 грн
Чорничний лимонад з вітаміном C — 1400 грн
Чорничний пілінг для чутливої шкіри — 1400 грн
Антивіковий пілінг зі стовбуровими клітинами — 1400 грн
Гарбузовий пілінг для глибокого очищення — 1400 грн
Стоп акне — 1400 грн
Вогонь і лід — 1400 грн
"""
    },
    {
        "id":
        "isclinical_care",
        "group":
        "care",
        "emoji":
        "🌿",
        "title":
        "Догляд IS CLINICAL",
        "raw_text":
        """Вогонь і лід — 2200 грн
Пінний ферментативний догляд — 1800 грн
"""
    },
    {
        "id":
        "medik8_care",
        "group":
        "care",
        "emoji":
        "🔬",
        "title":
        "Догляд MEDIK8",
        "raw_text":
        """Заспокійливий догляд — 1200 грн
Очищаючий догляд — 1200 грн
"""
    },
    {
        "id":
        "ipl_face",
        "group":
        "laser",
        "emoji":
        "💡",
        "title":
        "Фототерапія IPL: Обличчя, Шия",
        "raw_text":
        """Все обличчя — 2800 грн
Щоки + ніс + підборіддя — 2400 грн
Лоб — 1300 грн
Щоки + ніс — 2000 грн
Щоки + підборіддя — 1800 грн
Щоки — 1600 грн
Ніс — 1300 грн
Підборіддя — 1300 грн
Обличчя + шия + декольте — 4000 грн
Обличчя + шия — 3500 грн
Шия — 1500 грн
Декольте — 2800 грн
"""
    },
    {
        "id": "ipl_body",
        "group": "laser",
        "emoji": "🖐️",
        "title": "Фототерапія IPL: Інші Зони",
        "raw_text": """Кисті рук — 2200 грн
Спина — 3500 грн
"""
    },
    {
        "id":
        "ap_cosm",
        "group":
        "device",
        "emoji":
        "⚡",
        "title":
        "Апаратна Косметологія",
        "raw_text":
        """Мікроструми — 1200 грн
УЗ-фонофорез — 1200 грн
Мікродермабразія — 1200 грн
Гідропілінг Aquapure — 2500 грн
"""
    },
    {
        "id":
        "rf_micro",
        "group":
        "device",
        "emoji":
        "🔥",
        "title":
        "RF-Ліфтинг (Мікроголковий)",
        "raw_text":
        """1000 імпульсів — 11000 грн
Обличчя — 9000 грн
Обличчя + шия + декольте — 11000 грн
"""
    },
    {
        "id":
        "rf_noninv",
        "group":
        "device",
        "emoji":
        "♨️",
        "title":
        "RF-Ліфтинг (Неінвазивний)",
        "raw_text":
        """Зона навколо очей — 1500 грн
Зона навколо губ — 1100 грн
Щоки — 1200 грн
Підборіддя — 1200 грн
Ноги (внутрішня частина стегна) — 700 грн
Ноги (зовнішня частина стегна) — 700 грн
Ноги (ділянка під сідницею) — 700 грн
Сідниці — 700 грн
Внутрішня частина стегна + ділянка під сідницею + сідниці — 1800 грн
Живіт — 700 грн
Живіт + боки — 1000 грн
Коліна — 400 грн
*при оплаті 6-ти процедур будь-яких 2-ох зон — знижка 10%
*при оплаті 6-ти процедур будь-яких 3-ох зон — знижка 15%
"""
    },
    {
        "id":
        "laser_face",
        "group":
        "laser",
        "emoji":
        "🎯",
        "title":
        "Лазерна Епіляція: Обличчя",
        "raw_text":
        """Верхня губа — 300 грн
Підборіддя — 300 грн
Міжбрів’я — 200 грн
Лінія чола — 350 грн
Все обличчя — 1100 грн
"""
    },
    {
        "id":
        "laser_body",
        "group":
        "laser",
        "emoji":
        "🦵",
        "title":
        "Лазерна Епіляція: Тіло",
        "raw_text":
        """Пахові області — 500 грн
Руки до ліктя — 700 грн
Руки повністю — 1000 грн
Гомілки — 1300 грн
Стегна — 1200 грн
Коліна — 300 грн
Сідниці — 700 грн
Ноги повністю — 2350 грн
Глибоке бікіні — 1200 грн
Бікіні по лінії трусиків — 800 грн
Груди — 600 грн
Ореоли — 300 грн
Біла лінія живота — 350 грн
Спина — 1800 грн
"""
    },
    {
        "id":
        "laser_complex",
        "group":
        "laser",
        "emoji":
        "🎁",
        "title":
        "Лазерна Епіляція: Комплекси",
        "raw_text":
        """КОМПЛЕКС 1 (ноги + пахи + бікіні глибоке) — 3000 грн
КОМПЛЕКС 2 (ноги до колін + глибоке бікіні + пахи) — 2200 грн
КОМПЛЕКС 3 (глибоке бікіні + пахи) — 1400 грн
"""
    },
    {
        "id":
        "inject_lips",
        "group":
        "inject",
        "emoji":
        "👄",
        "title":
        "Ін'єкції: Губи",
        "raw_text":
        """Teosyal RHA 1 (1.0) — 190€
Teosyal RHA 2 (1.0) — 190€
Teosyal RHA 3 (1.0) — 190€
Teosyal RHA Kiss (0.7) — 160€
Restylane Kiss (1.0) — 190€
Розчинення губ — 2000 грн
"""
    },
    {
        "id":
        "inject_contour",
        "group":
        "inject",
        "emoji":
        "💉",
        "title":
        "Ін'єкції: Контурна Пластика",
        "raw_text":
        """Teosyal Ultra Deep (1.0) — 220€
Teosyal RHA 4 (1.0) — 220€
Restylane Volyme (1.0) — 220€
Restylane Defyne (1.0) — 220€
Restylane Lyft (1.0) — 220€
"""
    },
    {
        "id":
        "inject_collagen",
        "group":
        "inject",
        "emoji":
        "💫",
        "title":
        "Ін'єкції: Колагеностимуляція",
        "raw_text":
        """Gouri — 180€
Karisma — 190€
Гідроксиапатит Ca Radiesse (1.5) — 250€
Feijia для ділянки навколо очей — 6000 грн
"""
    },
    {
        "id":
        "inject_botox",
        "group":
        "inject",
        "emoji":
        "😊",
        "title":
        "Ін'єкції: Ботулінотерапія",
        "raw_text":
        """Full face — 12500 / 14000 грн
Міжбрів’я — 2600 / 3300 грн
Лоб — 2600 / 3300 грн
Очі — 2600 / 3300 грн
Верхня третина — 7500 / 9500 грн
Платизма — 5000 / 6500 грн
Корекція надмірного потовиділення — 11000 / 13500 грн
Ясенна посмішка — 1500 грн
Корекція підборіддя — 1500 грн
Корекція жувальних м’язів — 4500 / 6000 грн
Dao — 1500 грн
"""
    },
    {
        "id":
        "inject_bio",
        "group":
        "inject",
        "emoji":
        "💦",
        "title":
        "Ін'єкції: Біоревіталізація",
        "raw_text":
        """Jalupro — 3800 грн
Jalupro HMW — 5600 грн
Jalupro eye — 4600 грн
Jalupro Super Hydro — 7300 грн
Teosyal Redensity 1 (1 мл) — 3800 грн
Teosyal Redensity 1 (3 мл) — 8500 грн
"""
    },
    {
        "id":
        "inject_meso",
        "group":
        "inject",
        "emoji":
        "🧬",
        "title":
        "Ін'єкції: Мезотерапія",
        "raw_text":
        """Rejuran S — 4300 грн
Rejuran HB — 5200 грн
Rejuran i — 4300 грн
Rejuran Healer (2 мл) — 7500 грн
Полінуклеотиди Plinest Mastelli (3.0) — 4800 грн
Plenhyage strong — 9700 грн
Мезококтейль AKN-ID акне — 1600 грн
Pluryal Mesoline Hair (волосся) — 1250 грн
Plinest Hair Mastelli (волосся) — 4800 грн
Ліполітики (10.0) — 1700 грн
"""
    },
    {
        "id":
        "massage_spm",
        "group":
        "body",
        "emoji":
        "💆‍♀️",
        "title":
        "Масаж: SPM Вакуумний",
        "raw_text":
        """Обличчя — 1200 грн
Ноги + сідниці — 1000 грн
Ноги + сідниці + живіт — 1200 грн
Ноги + сідниці + живіт + спина — 1500 грн
Ноги + сідниці + живіт + спина + руки — 1800 грн
"""
    },
    {
        "id":
        "massage_endo",
        "group":
        "body",
        "emoji":
        "🌀",
        "title":
        "Масаж: Ендосфера",
        "raw_text":
        """45 хв (ноги + живіт + сідниці) — 1500 грн
60 хв (ноги + живіт + сідниці + спина) — 1800 грн
75 хв (ноги + живіт + сідниці + спина + руки) — 2100 грн
Обличчя — 1400 грн
*при оплаті 6-ти процедур (ноги + живіт + сідниці) вартість 8100 грн
*при оплаті 6-ти процедур (ноги + живіт + сідниці + спина) — 9700 грн
*при оплаті 6-ти процедур (ноги + живіт + сідниці + спина + руки) — 11000 грн
*при оплаті 10-ти процедур (ноги + живіт + сідниці) — 12000 грн
*при оплаті 10-ти процедур (ноги + живіт + сідниці + спина) — 15000 грн
*при оплаті 10-ти процедур (ноги + живіт + сідниці + спина + руки) — 18000 грн
"""
    },
]
