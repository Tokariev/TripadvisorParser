from Server import *
from CityParser import *
from Json import *


if __name__ == '__main__':
    server = Server()
    city_parser = Cities_parser()

    #city_urls = city_parser.get_city_urls(server)

    ### Json ###
    json_string = '{ "tags": null, "display_hours": [{"days": "So", "times": ["17:00 - 00:00"] },{"days": "Di - Do", "times"' \
                  ': ["17:00 - 00:00"] },{ "days": "Fr - Sa", "times": ["12:00 - 15:30", "19:00 - 00:30"] }]}'

    json_string = '{ "display_hours":[ { "days": "So - Mi", "times": ["12:00 - 14:30", "18:00 - 22:00"] }] }'

    parser = Json()

    json = parser.string_to_json(json_string)
    display_hours = json['display_hours']

    days_list = parser.get_working_list_from_json(display_hours)

    pass






