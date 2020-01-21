import json

class Json:
    def string_to_json(self, s):
        return json.loads(s)

    def get_days_from_json(self, json):
        return map(lambda datum: datum['name'], json)

    def get_day_number(self, day):
        weeks_day = {
            "Mo": 1,
            "Di": 2,
            "Mi": 3,
            "Do": 4,
            "Fr": 5,
            "Sa": 6,
            "So": 7,
        }
        return weeks_day[day]

    def parse_time(self, day, time):
        if ',' in time[0]:
            period_left = time[0][:13]
            period_right = time[0][-13:]

            period_left_from = period_left[:5]
            period_left_to = period_left[-5:]

            period_right_from = period_right[:5]
            period_right_to = period_right[-5:]

            day_info = [day, period_left_from, period_left_to, period_right_from, period_right_to]

            return day_info

        elif ',' not in time[0]:
            period_left_from = time[0][:5]
            period_right_to = time[0][-5:]

            day_info = [day, period_left_from, period_right_to]

            return day_info

    def get_working_list_from_json(self, display_hours):
        days_list = []
        for period in display_hours:
            day = period['days']
            time = period['times']

            if '-' in day:
                firs_day = day[:2]
                last_day = day[-2:]
                firs_day_numb = self.get_day_number(firs_day)
                last_day_numb = self.get_day_number(last_day)

                days_range = range(firs_day_numb, last_day_numb + 1, 1)

                for day_numb in days_range:
                    day = self.get_key_from_value(day_numb)
                    days_list.append(self.parse_time(day, time))

            elif '-' not in day:
                days_list.append(self.parse_time(day, time))

        return days_list

    def get_key_from_value(self, day_numb):
        weeks_day = {
            "Mo": 1,
            "Di": 2,
            "Mi": 3,
            "Do": 4,
            "Fr": 5,
            "Sa": 6,
            "So": 7,
        }
        return list(weeks_day.keys())[list(weeks_day.values()).index(day_numb)]