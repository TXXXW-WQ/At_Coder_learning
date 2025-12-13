# 地下鉄システムの設計
class UndergroundSystem:

    def __init__(self):
        self.cus_dict = {}
        self.history = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cus_dict[id] = (stationName,t)

    def checkOut(self, id: int, endStation: str, end_time: int) -> None:
        start_station, start_time = self.cus_dict.pop(id)
        key = (start_station, endStation)
        all_time, all_count = self.history.get(key, (0,0))
        self.history[key] = (all_time + (end_time - start_time), all_count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        all_time, all_count = self.history.get(key,(0,0))
        return all_time / all_count
