import matplotlib.pyplot as plt
import io

def create_air_quality_graph(districts_data):
    """
    Create a bar chart comparing AQI across districts on a 1–5 scale.
    
    Args:
        districts_data: List of tuples (district_name, parsed_data)
    Returns:
        BytesIO image buffer (PNG)
    """
    # Filter out None results
    districts = [d for d, data in districts_data if data is not None]
    aqi_values = [min(max(int(data['aqi']), 1), 5)  # clamp to 1–5
                  for _, data in districts_data if data is not None]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(
        districts, aqi_values,
        color=[
            "green" if aqi == 1 else 
            "yellow" if aqi == 2 else 
            "orange" if aqi == 3 else 
            "red" if aqi == 4 else 
            "purple" for aqi in aqi_values
        ]
    )

    plt.title("Air Quality Index (AQI) by District", fontsize=16)
    plt.xlabel("District", fontsize=12)
    plt.ylabel("AQI Category (1–5)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 5.5)  # Always show full 1–5 scale

    # Add AQI labels above bars
    for bar, aqi in zip(bars, aqi_values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(aqi),
            ha="center",
            va="bottom"
        )

    # Save plot to memory buffer
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf
