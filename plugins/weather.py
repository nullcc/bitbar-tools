#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

KEY = "vs9zuownkkpqoqxw"  # API key
UID = "U88C659E34"  # 用户ID

LOCATION = "xiamen"  # 所在位置,可以根据需要修改
API = "https://api.thinkpage.cn/v3/weather/now.json"  # API URL，可替换为其他 URL
UNIT = "c"  # 单位
LANGUAGE = "zh-Hans"  # 查询结果的返回语言
retry = 5

consts_value = dict()
consts_value["0"] = {"code": "0", "text_en": "Sunny", "text_zh": "晴", "img": "☀️"}
consts_value["1"] = {"code": "1", "text_en": "Clear", "text_zh": "晴", "img": "🌕"}
consts_value["2"] = {"code": "2", "text_en": "Fair", "text_zh": "晴", "img": "☀"}
consts_value["3"] = {"code": "3", "text_en": "Fair", "text_zh": "晴", "img": "🌕"}
consts_value["4"] = {"code": "4", "text_en": "Cloudy", "text_zh": "多云", "img": "☁️"}
consts_value["5"] = {"code": "5", "text_en": "Partly Cloudy", "text_zh": "晴间多云", "img": "🌤"}
consts_value["6"] = {"code": "6", "text_en": "Partly Cloudy", "text_zh": "晴间多云", "img": "🌤️"}
consts_value["7"] = {"code": "7", "text_en": "Mostly Cloudy", "text_zh": "大部多云", "img": "🌥️"}
consts_value["8"] = {"code": "8", "text_en": "Mostly Cloudy", "text_zh": "大部多云", "img": "🌥️"}
consts_value["9"] = {"code": "9", "text_en": "Overcast", "text_zh": "阴", "img": "☁️"}
consts_value["10"] = {"code": "10", "text_en": "Shower", "text_zh": "阵雨", "img": "🌧"}
consts_value["11"] = {"code": "11", "text_en": "Thundershower", "text_zh": "雷阵雨", "img": "⛈"}
consts_value["12"] = {"code": "12", "text_en": "Thundershower with Hail", "text_zh": "雷阵雨伴有冰雹", "img": "⛈"}
consts_value["13"] = {"code": "13", "text_en": "Light Rain", "text_zh": "小雨", "img": "🌧"}
consts_value["14"] = {"code": "14", "text_en": "Moderate Rain", "text_zh": "中雨", "img": "🌧"}
consts_value["15"] = {"code": "15", "text_en": "Heavy Rain", "text_zh": "大雨", "img": "🌧"}
consts_value["16"] = {"code": "16", "text_en": "Storm", "text_zh": "暴雨", "img": "🌧"}
consts_value["17"] = {"code": "17", "text_en": "Heavy Storm", "text_zh": "大暴雨", "img": "🌧"}
consts_value["18"] = {"code": "18", "text_en": "Severe Storm", "text_zh": "特大暴雨", "img": "🌧"}
consts_value["19"] = {"code": "19", "text_en": "Ice Rain", "text_zh": "冻雨", "img": "🌧"}
consts_value["20"] = {"code": "20", "text_en": "Sleet", "text_zh": "雨夹雪", "img": "🌧"}
consts_value["21"] = {"code": "21", "text_en": "Snow Flurry", "text_zh": "阵雪", "img": "🌨"}
consts_value["22"] = {"code": "22", "text_en": "Light Snow", "text_zh": "小雪", "img": "🌨"}
consts_value["23"] = {"code": "23", "text_en": "Moderate Snow", "text_zh": "中雪", "img": "🌨"}
consts_value["24"] = {"code": "24", "text_en": "Heavy Snow", "text_zh": "大雪", "img": "🌨"}
consts_value["25"] = {"code": "25", "text_en": "Snowstorm", "text_zh": "暴雪", "img": "🌨"}
consts_value["26"] = {"code": "26", "text_en": "Dust", "text_zh": "浮尘", "img": ""}
consts_value["27"] = {"code": "27", "text_en": "Sand", "text_zh": "扬沙", "img": ""}
consts_value["28"] = {"code": "28", "text_en": "Duststorm", "text_zh": "沙尘暴", "img": ""}
consts_value["29"] = {"code": "29", "text_en": "Sandstorm", "text_zh": "强沙尘暴", "img": ""}
consts_value["30"] = {"code": "30", "text_en": "Foggy", "text_zh": "雾", "img": "🌫"}
consts_value["31"] = {"code": "31", "text_en": "Haze", "text_zh": "霾", "img": "🌫"}
consts_value["32"] = {"code": "32", "text_en": "Windy", "text_zh": "风", "img": "🌬"}
consts_value["33"] = {"code": "33", "text_en": "Blustery", "text_zh": "大风", "img": "🌬"}
consts_value["34"] = {"code": "34", "text_en": "Hurricane", "text_zh": "飓风", "img": "💨 "}
consts_value["35"] = {"code": "35", "text_en": "Tropical Storm", "text_zh": "热带风暴", "img": "💨 "}
consts_value["36"] = {"code": "36", "text_en": "Tornado", "text_zh": "龙卷风", "img": "🌪"}
consts_value["37"] = {"code": "37", "text_en": "Cold", "text_zh": "冷", "img": "💧"}
consts_value["38"] = {"code": "38", "text_en": "Hot", "text_zh": "热", "img": "🌞"}
consts_value["99"] = {"code": "99", "text_en": "Unknown", "text_zh": "未知", "img": "❓"}


def fetch_weather(location):
    return requests.get(API, params={
        "key": KEY,
        "location": location,
        "language": LANGUAGE,
        "unit": UNIT
    }, timeout=10)


if __name__ == "__main__":
    try:
        response = fetch_weather(LOCATION)
        if response.status_code != 200:
            raise StandardError()
    except:
        if retry > 0:
            response = fetch_weather(LOCATION)
            retry -= 1

    try:
        result_json = json.loads(response.text)
        city = result_json["results"][0].get("location").get("name")
        desc = result_json["results"][0].get("now").get("text")
        temperature = result_json["results"][0].get("now").get("temperature")
        code = result_json["results"][0].get("now").get("code")
        text = "{}:{}℃,{}{}️".format(city, temperature, desc, consts_value[code].get("img"))
        print(text)
    except ValueError:
        print('天气解析失败')

