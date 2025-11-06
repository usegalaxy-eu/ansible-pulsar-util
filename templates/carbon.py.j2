import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-lat", "--latitude",
        help="Latitude of pulsar node",
        type=float
    )
    parser.add_argument(
        "-lon", "--longitude",
        help="Longitude of pulsar node",
        type=float
    )
    args = parser.parse_args()
    return args.latitude, args.longitude


def get_carbon_intensity(lat, lon) -> float:
    request = f"""
        https://api.electricitymaps.com/v3/carbon-intensity/
        latest?lat={lat}&lon={lon}&temporalGranularity=hourly
    """
    response = requests.get(
        request,
        headers={ "auth-token": "{{ energy_auth_token }}" }
    ).json()
    return { "carbon_intensity": response["carbonIntensity"] }


def get_price_day_ahead(lat, lon) -> dict:
    request = f"""
        https://api.electricitymaps.com/v3/price-day-ahead/
        latest?lat={lat}&lon={lon}&temporalGranularity=hourly
    """
    response = requests.get(
        request,
        headers={ "auth-token": "{{ energy_auth_token }}" }
    ).json()
    return {"value": response["value"], "unit": response["unit"]}


def get_electricity_mix(lat, lon) -> dict:
    request = f"""
        https://api.electricitymaps.com/v3/electricity-mix/
        latest?lat={lat}&lon={lon}&temporalGranularity=hourly
    """
    response = requests.get(
        request,
        headers={ "auth-token": "{{ energy_auth_token }}" }
    ).json()
    mix = response["data"]["mix"]
    mix["unit"] = response["unit"]
    return mix


def get_energy_metrics() -> dict:
    """
    Retrieve carbon intensity data for each pulsar node.
    """
    destinations = {{ destinations }}
    influx_entries = {}

    for node, (lat, lon) in destinations.items():
        carbon_intensity = get_carbon_intensity(lat, lon)
        price_day_ahead = get_price_day_ahead(lat, lon)
        influx_entries[node] = f"{{ consumer_energy_measurement }}, carbon_intensity={carbon_intensity}, price_day_ahead={price_day_ahead}"

    return influx_entries


def get_energy_metrics() -> dict:
    lat, lon = parse_args()
    request_data = {
        "carbon-intensity" : ["carbonIntensity"],
        "price-day-ahead" : ["value", "unit"]
    }
    stats = {}

    for datum in request_data:
        stats[datum] = {}
        request = f"""
            https://api.electricitymaps.com/v3/{datum}/
            latest?lat={lat}&lon={lon}&temporalGranularity=hourly
        """
        response = requests.get(
            request,
            headers={ "auth-token": "{{ energy_auth_token }}" }
        ).json()
        for key in request_data[datum]:
            stats[datum][key] = response[key]
    
    return stats
