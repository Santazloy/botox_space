# data/cosmetics_sections.py

BRANDS = [
    {"id": "hydropeptide", "emoji": "🧴", "title": "HydroPeptide"},
    {"id": "medik8",       "emoji": "💊", "title": "Medik8"},
    {"id": "image",        "emoji": "🎨", "title": "Image"},
    {"id": "isclinical",   "emoji": "🧪", "title": "Is Clinical"},
    {"id": "colorescience","emoji": "☀️", "title": "Colorescience"},
    {"id": "revitalash",   "emoji": "💄", "title": "Revitalash"},
    {"id": "academie",     "emoji": "🎓", "title": "Academie"},
    {"id": "histolab",     "emoji": "🔬", "title": "Histolab"},
]

SUBGROUP_DEFINITIONS = [
    # HydroPeptide
    {
        "id": "hydropeptide_cleansers",
        "brand": "hydropeptide",
        "emoji": "🧼",
        "title": "Засоби для очищення та тонізації",
        "raw_text": """Cleansing gel
Exfoliant Cleanser
Pre-Treatment Toner
Cashmere Cleanse молочко
Міцелярні серветки"""
    },
    {
        "id": "hydropeptide_serums",
        "brand": "hydropeptide",
        "emoji": "💧",
        "title": "Сироватки та концентрати",
        "raw_text": """Retinol Routine Booster
Firma-Bright
LumaPro-C
Power Serum
HydroStem
Spot Correction
Redefining Serum
Soothing Serum"""
    },
    {
        "id": "hydropeptide_masks",
        "brand": "hydropeptide",
        "emoji": "🎭",
        "title": "Маски",
        "raw_text": """Radiance Mask
Balancing Mask
Rejuvenating Mask
Miracle Mask"""
    },
    {
        "id": "hydropeptide_creams",
        "brand": "hydropeptide",
        "emoji": "🧴",
        "title": "Крем основний догляд",
        "raw_text": """Power Luxe
Power Lift
NiMnі Day Cream
Face Lift
AquaBoost"""
    },
    {
        "id": "hydropeptide_spf",
        "brand": "hydropeptide",
        "emoji": "☀️",
        "title": "Крем SPF",
        "raw_text": """Solar Defense Tinted SPF30 з тоном
Solar Defense SPF50 без тону
Solar Defense Body SPF30"""
    },
    {
        "id": "hydropeptide_eye",
        "brand": "hydropeptide",
        "emoji": "👁️",
        "title": "Догляд за шкірою навколо очей",
        "raw_text": """Vital Eyes
Eye Authority"""
    },

    # Medik8
    {
        "id": "medik8_serums",
        "brand": "medik8",
        "emoji": "💉",
        "title": "Сироватки",
        "raw_text": """C-Tetra
Clarity Peptides
Hydr8 B5 Intense
Bakuchiol Peptides
Liquid Peptides
Sleep Glycolic"""
    },
    {
        "id": "medik8_eye",
        "brand": "medik8",
        "emoji": "👁️",
        "title": "Догляд за шкірою навколо очей",
        "raw_text": """Illuminating Eye Balm
Eyelift Peptides
Advanced Night Eye
Crystal Retinal Ceramide 3
Crystal Retinal Ceramide 6
Crystal Retinal Ceramide 10"""
    },
    {
        "id": "medik8_cleansers",
        "brand": "medik8",
        "emoji": "🧼",
        "title": "Засоби для очищення та тоніки",
        "raw_text": """LIPID-BALANCE Cleansing Oil
Press & Glow
Press & Clear
Micellar Mousse
Clarifying Foam
Gentle Cleanse
Calmwise Soothing Cleanser
Pore Cleanse Gel Intense
Surface Radiance Cleanse
Daily Refresh Balancing Toner
Blemish Control Pads"""
    },
    {
        "id": "medik8_creams",
        "brand": "medik8",
        "emoji": "🧴",
        "title": "Креми та SPF",
        "raw_text": """Crystal Retinal 3
Crystal Retinal 6
Crystal Retinal 10
Advanced Day Total Protect SPF30
Calmwise Colour Correct
C-Tetra Cream
Intelligent Retinol Smoothing Night Cream
Advanced Night Restore
Daily Radiance Vitamin C SPF30
Total Moisture Daily Facial Cream
Balance Moisturiser"""
    },
    {
        "id": "medik8_masks",
        "brand": "medik8",
        "emoji": "🎭",
        "title": "Маски",
        "raw_text": """H.E.O. Mask"""
    },

    # Image
    {
        "id": "image_daily",
        "brand": "image",
        "emoji": "☀️",
        "title": "DAILY PREVENTION",
        "raw_text": """Daily Prevention Pure Mineral Hydrating Moisturizer SPF30
Daily Prevention Matte Moisturizer SPF30
Daily Prevention Pure Mineral Tinted Moisturizer SPF30
Daily Prevention Advanced Smartblend Mineral Monitoring SPF50
Daily Prevention Protect and Refresh Mist SPF30
Clear Solar Gel SPF30"""
    },
    {
        "id": "image_iluma",
        "brand": "image",
        "emoji": "🌟",
        "title": "ILUMA",
        "raw_text": """Intense Brightening Exfoliating Cleanser
Intense Brightening Exfoliating Powder
Intense Brightening Serum
Intense Brightening Crème
Intense Brightening Eye Crème"""
    },
    {
        "id": "image_md",
        "brand": "image",
        "emoji": "🔬",
        "title": "MD",
        "raw_text": """Restoring Power-C Serum
Restoring Youth Serum
Restoring Youth Repair Crème
Restoring Daily Defense Moisturizer SPF50
Restoring Retinol Crème
Restoring Brightening Crème
Restoring Collagen Recovery Eye Gel
Restoring Overnight Retinol Masque
Restoring Eye Mask Патчі
Restoring Facial Cleanser"""
    },
    {
        "id": "image_ageless",
        "brand": "image",
        "emoji": "🕰️",
        "title": "AGELESS",
        "raw_text": """Total Facial Cleanser
Total Pure Hyaluronic Filler
Total Retinol-A Crème
Total Repair Crème
Total Eye Lift Crème with SCT
Total Anti-Age Serum
Total Overnight Retinol Masque"""
    },
    {
        "id": "image_clearcell",
        "brand": "image",
        "emoji": "💧",
        "title": "CLEAR CELL",
        "raw_text": """Medicated Acne Lotion
Clarifying Salicylic Blemish Gel
Clarifying Repair Crème
Mattifying Moisturizer
Salicylic Gel Cleanser
Salicylic Clarifying Pads"""
    },
    {
        "id": "image_max",
        "brand": "image",
        "emoji": "🚀",
        "title": "The MAX",
        "raw_text": """Stem Cell Facial Cleanser
Stem Cell Crème
Stem Cell Serum
Eye Crème
Neck Lift"""
    },
    {
        "id": "image_ormedic",
        "brand": "image",
        "emoji": "🌿",
        "title": "ORMEDIC",
        "raw_text": """Balancing Facial Cleanser
Balancing Antioxidant Serum
Balancing Bio Peptide Crème
Balancing Eye Lift Gel"""
    },
    {
        "id": "image_vitalc",
        "brand": "image",
        "emoji": "🍊",
        "title": "VITAL C",
        "raw_text": """Hydrating Facial Cleanser
Hydrating Anti-Aging Serum
Hydrating A,C,E Serum
Hydrating Repair Crème
Hydrating Enzyme Masque
Hydrating Eye Recovery Gel
Hydrating Intense Moisturizer
Hydrating Water Buster
Hydrating Overnight Masque"""
    },
    {
        "id": "image_imask",
        "brand": "image",
        "emoji": "🎭",
        "title": "I MASK",
        "raw_text": """Purifying Probiotic Mask
Hydrating Hydrogel Sheet Mask"""
    },
    {
        "id": "image_biome",
        "brand": "image",
        "emoji": "🦠",
        "title": "BIOME+",
        "raw_text": """Cleansing Comfort Balm
Dew Bright Serum
Smoothing Crème"""
    },

    # Is Clinical
    {
        "id": "isclinical_cleansing",
        "brand": "isclinical",
        "emoji": "🧼",
        "title": "Очищення",
        "raw_text": """Cleansing Complex 180 мл
Cleansing Complex 60 мл
Cleansing Complex Polish"""
    },
    {
        "id": "isclinical_spf",
        "brand": "isclinical",
        "emoji": "☀️",
        "title": "SPF",
        "raw_text": """Extreme Protect SPF30
Extreme Protect SPF40
Eclipse SPF50+
Eclipse SPF50+ Beige
Perfectint Powder SPF40 Beige
Perfectint Powder SPF40 Cream
Perfectint Powder SPF40 Ivory"""
    },
    {
        "id": "isclinical_creams",
        "brand": "isclinical",
        "emoji": "🧴",
        "title": "Крем, емульсія",
        "raw_text": """Moisturizing Complex
Reparative Moisture Emulsion
Firming Complex
Recovery Balm 60 г"""
    },
    {
        "id": "isclinical_eye",
        "brand": "isclinical",
        "emoji": "👁️",
        "title": "Догляд за шкірою навколо очей",
        "raw_text": """Eye Complex
Youth Complex"""
    },
    {
        "id": "isclinical_serums",
        "brand": "isclinical",
        "emoji": "💉",
        "title": "Сироватки",
        "raw_text": """Hydra-Cool Serum
Active Serum
Pro-Heal Serum Advance
Super Serum Advance
Brightening Serum
GeneXC Serum"""
    },
    {
        "id": "isclinical_lips",
        "brand": "isclinical",
        "emoji": "💋",
        "title": "Губи",
        "raw_text": """Скраб для губ
Еліксир для губ
Набір Lip Duo"""
    },
    {
        "id": "isclinical_masks",
        "brand": "isclinical",
        "emoji": "🎭",
        "title": "Маски",
        "raw_text": """Hydra-Intensive Cooling Mask"""
    },
    {
        "id": "isclinical_sets",
        "brand": "isclinical",
        "emoji": "🎁",
        "title": "Набори",
        "raw_text": """Pure Calm
Pure Clarity
Warm Up Down
Smooth & Smoothe
Pure Radiance"""
    },

    # Colorescience (no subgroups)
    {
        "id": "colorescience_all",
        "brand": "colorescience",
        "emoji": "☀️",
        "title": "Colorescience",
        "raw_text": """Сонцезахисна пудра SPF50, напівначинений MEDIUM
Сонцезахисна пудра SPF50, світлий FAIR
Сонцезахисна пудра SPF50 GLOW
Сонцезахисний крем для обличчя SPF50 GLOBAL CLASSIC
Сонцезахисний крем для обличчя MATTE SPF50
Сонцезахисний крем для обличчя SPF50 світлий FAIR
Сонцезахисний крем для обличчя SPF50 напівначинений MEDIUM
Сонцезахисний крем для обличчя SPF50 GLOW"""
    },

    # Revitalash (no subgroups)
    {
        "id": "revitalash_all",
        "brand": "revitalash",
        "emoji": "💄",
        "title": "Revitalash",
        "raw_text": """Thickening Shampoo
Thickening Conditioner
Сироватка для вій для чутливих очей 2 мл
Сироватка-кондиціонер для вій 2 мл
Кольоровий гель для брів
Прозорий гель для моделювання брів"""
    },

    # Academie (no subgroups)
    {
        "id": "academie_all",
        "brand": "academie",
        "emoji": "🎓",
        "title": "Academie",
        "raw_text": """Phyto-Gommage Marin
Регенеруюча тональна основа тон 1
Регенеруюча тональна основа тон 2
Регенеруюча тональна основа тон 3"""
    },

    # Histolab (two levels)
    {
        "id": "histolab_basicscience",
        "brand": "histolab",
        "emoji": "🔬",
        "title": "Basic Science",
        "raw_text": """Двофазний засіб для зняття макіяжу
Ензимний пілінг порошок багатофункціональний
Glyzin Azulene Ampoule Complex Sheet Mask 72
Aqua Hyaluron Ampoule Complex Sheet Mask
Gluthin Vita C Complex Sheet Mask
Salmon Wrinkle Ampoule Complex Sheet Mask 50
Маска на нетканій основі «Заспокійлива для лікування акне»
Маска на нетканій основі «Мультивітамінна з освітлюючим комплексом»
Маска післяпроцедурна на нетканій основі «Регенеруюча з охолоджувальним ефектом»"""
    },
    {
        "id": "histolab_dermascience",
        "brand": "histolab",
        "emoji": "🧪",
        "title": "Derma Science",
        "raw_text": """Azulene DNA Cream
BB Cream «Сяйво шкіри» з SPF35
Гідрогель відновлюючий з центеллою
Захисний регенеруючий крем-гель «Друга шкіра»
Концентрат з гіалуроновою кислотою 62%
Концентрат з епідермальним чинником зростання EGF63%
Концентрат з комплексом азулена72%
Концентрат освітлювальний з вітаміном C47%
Крем післяпроцедурний з EGF
Крем післяпроцедурний з вітаміном K
Крем сонцезахисний після процедур для обличчя SPF50+
Сонцезахисна есенція для чутливої шкіри SPF50+
Тональний бальзам відновлюючий «Постпроцедурний» SPF35+
Тонуючий крем з азуленом"""
    },
    {
        "id": "histolab_aquascience",
        "brand": "histolab",
        "emoji": "💦",
        "title": "Aqua Science",
        "raw_text": """Water-Max Hydrating Moisturizer
Water-Max Infusion Mist Toner
Water-Max Hydrating Cream
Ceracles Water Cream
Water-Max Foam Cleanser"""
    },
    {
        "id": "histolab_acnexscience",
        "brand": "histolab",
        "emoji": "⚗️",
        "title": "Acnex Science",
        "raw_text": """Delta Active Cream
Gamma Crystal Serum
Omega Spot Solution"""
    },
    {
        "id": "histolab_agescience",
        "brand": "histolab",
        "emoji": "⏳",
        "title": "Age Science",
        "raw_text": """Premium Renewal Essence
Premium Eye Cream
Premium Timeless Cream
Premium Energizing Solution"""
    },
    {
        "id": "histolab_whitescience",
        "brand": "histolab",
        "emoji": "🌟",
        "title": "White Science",
        "raw_text": """Whiteness Lightening Mist
Whiteness Lightening Serum
Whiteness Corrector
Whiteness Mela-X Cream"""
    },
]