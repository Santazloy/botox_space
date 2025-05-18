import re
from config import NEW_PRICE_LINE_TOTAL_WIDTH, MAX_SERVICE_NAME_LEN, PRICE_KEYWORDS

def parse_service_line(line: str):
    line = line.strip()
    if not line:
        return None
    if line.startswith("*"):
        return {"name": line, "price": None, "currency": None, "is_note": True}

    match = re.match(
        r"^(.*?)\s*—\s*([\d\.]+)(/\d*[\d\.]*)?\s*([€грн]+)\s*(.*)?$", line
    )
    if match:
        name, price1, price_slash, currency, extra = match.groups()
        name = name.strip()
        price_str = price1 + (price_slash or "")
        if extra:
            name += f" {extra.strip()}"
        return {
            "name": name,
            "price": price_str,
            "currency": currency.strip(),
            "is_note": False
        }

    return {"name": line, "price": None, "currency": None, "is_note": True}

def format_price_item(name, price_str, currency,
                      total_width=NEW_PRICE_LINE_TOTAL_WIDTH,
                      max_name_display_len=MAX_SERVICE_NAME_LEN):
    if price_str is None:
        return name
    price_display = f"{price_str} {currency}"
    if len(name) > max_name_display_len:
        name = name[:max_name_display_len - 3] + "..."
    spaces = total_width - len(name) - len(price_display)
    if spaces < 1:
        spaces = 1
    return f"{name}{' ' * spaces}{price_display}"