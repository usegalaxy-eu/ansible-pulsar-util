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

def main():
    auth_token = ""
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
            headers={ "auth-token": auth_token }
        )
        for key in request_data[datum]:
            stats[datum][key] = response.json()[key]
    
    return stats

main()
