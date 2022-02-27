import geocoder
import requests

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
API_BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid={API_KEY}'

def main():
  """Function which loops through a list of destinations then prints the location and weather"""
  destinations = ['Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge']

  # Loop through each destination and print out the location and current weather
  for destination in destinations:
    # Variables for use in the loop and urls
    location = geocoder.arcgis(destination)
    loc_lat = location.lat
    loc_lng = location.lng
    print(f'{destination} is located at ({loc_lat:.4f}, {loc_lng:.4f})')
    # Set the full api url, using json export data to a dictionary
    full_api_url = API_BASE_URL + '&lat=' + str(loc_lat) + '&lon=' + str(loc_lng)
    result = requests.get(full_api_url).json()
    # Print statement accessing the key/values based off result variable
    print(f"At {destination} right now, it's {result['weather'][0]['description']} with a temperature of {result['main']['temp']:.1f}\u00b0F\n")

main()
