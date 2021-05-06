from datetime import date
from dateutil.relativedelta import relativedelta
from typing import Dict
import json
import requests

url = "https://connpass.com/api/v1/event/"


def CallConnpassAPI(eventdate: str, startindex: int = 0) -> Dict:
    """[summary]
    ConnpassAPIを実行し、実行結果をJSONで取得する
    Args:
        eventdate (str): 開催日
        startindex (int): 開始位置　デフォルト0
    Returns:
        (dict): 実行結果
    """
    params = {
        'ymd': eventdate,
        'count': 100,
        'order': 2
    }
    if startindex > 0:
        params['start'] = startindex

    try:
        responce = requests.get(url, params=params)
        result_json = responce.json()
        return result_json
    except Exception as e:
        print('Error code: ', e.code)
        raise e


def GetEventReport() -> None:
    targetMonth = date.today() - relativedelta(months=1)
    for day in range(1, 32):
        try:
            targetDate = date(
                targetMonth.year,
                targetMonth.month,
                day)
            eventdate = targetDate.strftime('%Y%m%d')
            print(f'eventdate:{eventdate}')

            events = CallConnpassAPI(eventdate)
            results_start = events["results_start"]
            results_returned = events["results_returned"]
            results_available = events["results_available"]
            # print(f'results_start:{results_start}')
            # print(f'results_returned:{results_returned}')
            # print(f'results_available:{results_available}')

            while results_returned == 100 and results_available > 100:
                results_start += 100
                events_next = CallConnpassAPI(eventdate, results_start)
                results_start = events_next["results_start"]
                results_returned = events_next["results_returned"]
                results_available = events_next["results_available"]
                # print(f'results_start:{results_start}')
                # print(f'results_returned:{results_returned}')
                # print(f'results_available:{results_available}')
                for event_next in events_next["events"]:
                    events["events"].append(event_next)
            print(len(events["events"]))

            with open(f'./json/ConnpassAPI_{eventdate}.json', 'w', encoding="utf-8") as f:
                json.dump(events, f, indent=4)
        except Exception as e:
            if type(e) == ValueError:
                continue
            else:
                raise e


if __name__ == "__main__":
    GetEventReport()
