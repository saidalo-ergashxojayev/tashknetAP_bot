from typing import Dict, Optional, Tuple

def parse_air_pollution_data(result: Dict) -> Optional[Dict]:
    """
    Parse air pollution API response and return formatted data
    
    Args:
        result (Dict): Raw API response from OpenWeather air pollution endpoint
        
    Returns:
        Dict: Parsed air pollution data with AQI and components, or None if parsing fails
    """
    try:
        if not result or 'list' not in result or len(result['list']) == 0:
            return None
        
        data = result['list'][0]
        aqi = data['main']['aqi']
        components = data['components']
        
        # Map AQI index to qualitative description
        aqi_descriptions = {
            1: "Good",
            2: "Satisfactory", 
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }
        
        return {
            'aqi': aqi,
            'aqi_description': aqi_descriptions.get(aqi, "Unknown"),
            'timestamp': data.get('dt'),
            'components': {
                'co': components.get('co', 0),  # Carbon monoxide
                'no': components.get('no', 0),  # Nitrogen monoxide
                'no2': components.get('no2', 0),  # Nitrogen dioxide
                'o3': components.get('o3', 0),  # Ozone
                'so2': components.get('so2', 0),  # Sulphur dioxide
                'pm2_5': components.get('pm2_5', 0),  # Fine particles
                'pm10': components.get('pm10', 0),  # Coarse particles
                'nh3': components.get('nh3', 0)  # Ammonia
            }
        }
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing air pollution data: {e}")
        return None



def format_air_quality_message(parsed_data: Dict) -> str:
    """
    Format parsed air pollution data into a user-friendly message
    
    Args:
        parsed_data (Dict): Parsed air pollution data
        
    Returns:
        str: Formatted message for the user
    """
    aqi = parsed_data['aqi']
    desc = parsed_data['aqi_description']
    comp = parsed_data['components']
    
    # Emoji based on air quality
    emoji_map = {
        1: "🟢",
        2: "🟡",
        3: "🟠",
        4: "🔴",
        5: "🟣"
    }
    emoji = emoji_map.get(aqi, "⚪")
    
    message = f"{emoji} <b>Air Quality: {desc}</b> (AQI: {aqi})\n\n"
    
    message += "<blockquote>"
    message += "<b>Pollutant Levels (μg/m³):</b>\n"
    message += f"• CO (Carbon monoxide): {comp['co']:.2f}\n"
    message += f"• NO₂ (Nitrogen dioxide): {comp['no2']:.2f}\n"
    message += f"• O₃ (Ozone): {comp['o3']:.2f}\n"
    message += f"• SO₂ (Sulphur dioxide): {comp['so2']:.2f}\n"
    message += f"• PM2.5 (Fine particles): {comp['pm2_5']:.2f}\n"
    message += f"• PM10 (Coarse particles): {comp['pm10']:.2f}\n"
    message += f"• NH₃ (Ammonia): {comp['nh3']:.2f}\n"
    message += "</blockquote>"
    return message