import random
from dataclasses import dataclass
from datetime import date

# === PROFILY ZNAMENÍ ===
from .sign_profiles import SIGN_PROFILES  # může zůstat samostatně

@dataclass
class Horoscope:
    focus: str
    love: str
    career: str
    wellbeing: str
    lucky_numbers: list[str]
    mantra: str
    element: str


# === BLOKY TEXTŮ ===
FOCUS = [
    "vnitřní klid", "novou energii", "prostor pro tvoření", "soustředění na radost",
    "upřímnost v komunikaci", "uzemnění", "otevřenost změně", "trpělivost",
]

LOVE_LINES = [
    "Vztahy si žádají laskavost – i ticho může být projevem lásky.",
    "Dovolte si cítit. Zranitelnost je začátkem důvěry.",
    "Někdy stačí úsměv, aby se srdce znovu otevřelo.",
    "Přestaňte analyzovat city – prostě je žijte.",
]

CAREER_LINES = [
    "Vaše myšlenky dnes mohou inspirovat druhé – sdílejte je.",
    "Zkuste místo tlaku dát prostor spolupráci – výsledky překvapí.",
    "Drobné zlepšení v rutinní činnosti přinese velký dopad.",
    "Mluvte jasně o svých nápadech – svět je chce slyšet.",
]

WELLBEING_LINES = [
    "Pět minut vědomého dechu vrátí jasnost i klid.",
    "Uvolněte ramena a dejte si čaj – i drobnosti mění den.",
    "Vaše tělo si zaslouží pozornost stejně jako vaše sny.",
    "Vydejte se ven. Příroda dnes mluví vaším jazykem.",
]

MANTRA_BITS = [
    "klid", "vnitřní sílu", "vděčnost", "otevřenost", "lehkost", "upřímnost", "radost", "soucit"
]


# === POMOCNÁ FUNKCE ===
def _rng_for(sign_name: str, day: date, name: str | None) -> random.Random:
    """Deterministický generátor pro dané znamení, den a jméno."""
    seed = f"{sign_name}-{day.isoformat()}-{name or ''}"
    return random.Random(seed)


# === HLAVNÍ GENERÁTOR HOROSKOPU ===
def generate_daily_horoscope(slug: str, day: date, name: str | None = None) -> Horoscope:
    sign_data = SIGN_PROFILES.get(slug)
    if not sign_data:
        raise ValueError(f"❌ Neznámé znamení: {slug}")

    r = _rng_for(sign_data["name"], day, name)

    focus = r.choice(FOCUS)
    love = r.choice(LOVE_LINES)
    career = r.choice(CAREER_LINES)
    wellbeing = r.choice(WELLBEING_LINES)
    numbers = sorted({r.randint(1, 49) for _ in range(5)})[:5]
    mantra = f"Dnes volím {r.choice(MANTRA_BITS)}."

    return Horoscope(
        focus=focus,
        love=love,
        career=career,
        wellbeing=wellbeing,
        lucky_numbers=numbers,
        mantra=mantra,
        element=sign_data["element"],
    )


# === PŘEHLED PRO HOMEPAGE ===
SIGNS = [
    {
        "slug": slug,
        "name": data["name"],
        "emoji": data["emoji"],
        "dates": data["dates"],
        "element": data["element"],
        "description": data["description"],
    }
    for slug, data in SIGN_PROFILES.items()
]

SIGNS = sorted(SIGNS, key=lambda s: s["slug"])  # volitelné: pro stabilní pořadí v UI
