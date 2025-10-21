from flask import Blueprint, render_template, abort, request
from datetime import date
from .services.horoscope import SIGNS, generate_daily_horoscope
from .services.sign_profiles import SIGN_PROFILES  # ✅ správný import

bp = Blueprint("core", __name__)

@bp.route("/")
def home():
    """Zobrazení přehledu všech znamení."""
    return render_template("home.html", signs=SIGNS)


@bp.route("/sign/<slug>", methods=["GET", "POST"])
def sign_detail(slug):
    """Detail znamení – denní horoskop + profil."""
    profile = SIGN_PROFILES.get(slug)
    sign = next((s for s in SIGNS if s["slug"] == slug), None)

    if not profile or not sign:
        print(f"❌ Nenalezen profil nebo znamení pro slug: {slug}")
        abort(404)

    today = date.today()
    today_str = today.strftime("%d.%m.%Y")

    # 🔮 Denní horoskop (základní)
    horoscope = generate_daily_horoscope(slug, today)

    # 💫 Personalizovaný výklad (pokud uživatel zadá jméno/fokus)
    personalized = None
    if request.method == "POST":
        name = request.form.get("name")
        focus = request.form.get("focus") or "vše"
        key = f"{name or ''}{focus or ''}"
        personalized = generate_daily_horoscope(slug, today, name=key)

    return render_template(
        "sign_detail.html",
        sign=sign,                 # 💫 základní informace (emoji, název, datumy)
        profile=profile,           # ✨ detailní charakteristika znamení
        horoscope=horoscope,
        personalized=personalized,
        today=today_str,
    )
