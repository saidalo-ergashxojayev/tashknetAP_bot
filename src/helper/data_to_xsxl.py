import io
import pandas as pd
from datetime import datetime

def save_air_pollution_history_to_buffer(data: dict) -> io.BytesIO:
    """
    Save historical air pollution data into an in-memory Excel buffer 
    with human-readable timestamps.

    Args:
        data (dict): JSON response from OpenWeather Air Pollution API

    Returns:
        io.BytesIO: Excel file in memory
    """
    if "list" not in data:
        raise ValueError("Invalid data format: 'list' key not found")

    rows = []
    for entry in data["list"]:
        dt = datetime.fromtimestamp(entry["dt"])  # convert unix -> human readable
        aqi = entry.get("main", {}).get("aqi")
        components = entry.get("components", {})

        row = {
            "timestamp": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "aqi": aqi,
            "co": components.get("co"),
            "no": components.get("no"),
            "no2": components.get("no2"),
            "o3": components.get("o3"),
            "so2": components.get("so2"),
            "pm2_5": components.get("pm2_5"),
            "pm10": components.get("pm10"),
            "nh3": components.get("nh3"),
        }
        rows.append(row)

    df = pd.DataFrame(rows)

    # Write to buffer
    buf = io.BytesIO()
    df.to_excel(buf, index=False)
    buf.seek(0)  # reset pointer so Telegram can read it from start

    return buf
