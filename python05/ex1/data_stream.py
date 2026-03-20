#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [data for data in data_batch if criteria in data]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
             "processed_count": self.processed_count
             }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.temperatures = []

    def process_batch(self, data_batch: List[Any]) -> str:
        formatted_str = "["
        first = True
        self.temperatures = []
        self.processed_count = 0

        for data in data_batch:
            if not isinstance(data, dict):
                continue

            for key in data:
                if key not in ("temp", "humidity", "pressure"):
                    continue
                if not first:
                    formatted_str += ", "
                formatted_str += f"{key}:{data[key]}"
                first = False
                self.processed_count += 1
                if key == "temp":
                    self.temperatures = [*self.temperatures, data]
        formatted_str += "]"

        return ("Initializing Sensor Stream...\n"
                f"Stream ID: {self.id}, Type: Environmental Data\n"
                f"Processing sensor batch: {formatted_str}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch
                for key in item
                if isinstance(item, dict)
                and key in ("temp", "humidity", "pressure")
                and item[key] > 20]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        count = 0
        suma = 0
        for temp in self.temperatures:
            suma += temp["temp"]
            count += 1
        try:
            average = suma / count
        except ZeroDivisionError:
            return {
                "processed_count": self.processed_count,
            }
        return {
            "processed_count": self.processed_count,
            "average_temp": average
            }

    def report(self) -> str:
        data = self.get_stats()
        return (f"Sensor analysis: {data['processed_count']} "
                f"readings processed, avg temp: {data['average_temp']}°C")

    def report_summary(self, data_batch: List[Any]) -> str:
        self.process_batch(data_batch)
        return f"- Sensor data: {self.processed_count} readings processed"

    def report_critical(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch, "critical")
        critics = 0
        for _ in filtered:
            critics += 1
        if critics > 0:
            return f"{critics} critical sensor alerts"
        return ""


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.buy = []
        self.sell = []

    def process_batch(self, data_batch: List[Any]) -> str:
        formatted_str = "["
        first = True
        self.buy = []
        self.sell = []
        self.processed_count = 0

        for data in data_batch:
            if not isinstance(data, dict):
                continue

            for key in data:
                if key not in ("buy", "sell"):
                    continue
                if not first:
                    formatted_str += ", "
                formatted_str += f"{key}:{data[key]}"
                first = False
                self.processed_count += 1
                if key == "buy":
                    self.buy = [*self.buy, data]
                elif key == "sell":
                    self.sell = [*self.sell, data]
        formatted_str += "]"

        return ("Initializing Transaction Stream...\n"
                f"Stream ID: {self.id}, Type: Financial Data\n"
                f"Processing transaction batch: {formatted_str}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        if criteria == "critical":
            return [item for item in data_batch
                    for key in item
                    if isinstance(item, dict) and key in ("sell", "buy")
                    and item[key] > 100]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        buy_total = 0
        sell_total = 0
        for item in self.buy:
            buy_total += item["buy"]
        for item in self.sell:
            sell_total += item["sell"]
        return {
             "processed_count": self.processed_count,
             "net_flow": buy_total - sell_total
             }

    def report(self) -> str:
        data = self.get_stats()
        if data["net_flow"] > 0:
            return (f"Transaction analysis: {data['processed_count']} "
                    f"operations, net flow: +{data['net_flow']} units")
        else:
            return (f"Transaction analysis: {data['processed_count']} "
                    f"operations, net flow: {data['net_flow']} units")

    def report_summary(self, data_batch: List[Any]) -> str:
        self.process_batch(data_batch)
        return (f"- Transaction data: {self.processed_count} operations "
                "processed")

    def report_critical(self, data_batch: List[Any]) -> str:
        filtered = self.filter_data(data_batch, "critical")
        critics = 0
        for _ in filtered:
            critics += 1
        if critics == 1:
            return f"{critics} large transactions"
        elif critics > 1:
            return f"{critics} large transaction"
        return ""


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.errors = []

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count = 0
        for data in data_batch:
            if not isinstance(data, str) or data not in ("login",
                                                         "logout", "error"):
                continue
            self.processed_count += 1
        self.errors = self.filter_data(data_batch, "error")
        return ("Initializing Event Stream...\n"
                f"Stream ID: {self.id}, Type: System Events\n"
                f"Processing event batch {data_batch}")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [log for log in data_batch
                if isinstance(log, str) and log == criteria]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        count = 0
        for _ in self.errors:
            count += 1
        return {
             "processed_count": self.processed_count,
             "error": count
             }

    def report(self) -> str:
        data = self.get_stats()
        if data["error"] > 1:
            return (f"Event analysis: {data['processed_count']} events"
                    f", {data['error']} errors detected")
        else:
            return (f"Event analysis: {data['processed_count']} events"
                    f", {data['error']} error detected")

    def report_summary(self, data_batch: List[Any]) -> str:
        self.process_batch(data_batch)
        return (f"- Event data: {self.processed_count} events processed")

    def report_critical(self, data_batch: List[Any]) -> str:
        return None


class StreamProcessor():
    def __init__(self):
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams = [*self.streams, stream]

    def report_all(self, data_batches: List[List[Any]]) -> None:
        i = 0
        for stream in self.streams:
            try:
                print(stream.process_batch(data_batches[i]))
                print(stream.report())
                print("")
            except Exception as e:
                print(f"Error processing stream {stream.id}: {e}\n")
            finally:
                i += 1

    def process_all(self, data_batches: List[Any]) -> None:
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for stream in self.streams:
            try:
                print(f"{stream.report_summary(data_batches)}")
            except Exception as e:
                print(f"Error processing stream {stream.id}: {e}\n")

        print("\nStream filtering active: High-priority data only")
        print("Filtered results:", end=" ")
        is_first = True
        for stream in self.streams:
            try:
                content = stream.report_critical(data_batches)
                if content is not None:
                    if is_first:
                        print(f"{content}", end="")
                    else:
                        print(f", {content}", end="")
                    is_first = False
            except Exception as e:
                print(f"\nError processing stream {stream.id}: {e}\n")
        print("\n\nAll streams processed successfully."
              "Nexus throughput optimal.")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    data = [
        [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}],
        [{"buy": 100}, {"sell": 150}, {"buy": 75}],
        ["login", "error", "logout"]
    ]
    processor = StreamProcessor()
    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_01"),
        EventStream("EVENT_001")]

    for stream in streams:
        processor.add_stream(stream)
    processor.report_all(data)

    print("=== Polymorphic Stream Processing ===")
    data = [{"temp": 28}, {"humidity": 56}, {"buy": 100}, {"sell": 150},
            {"buy": 75}, {"sell": 50}, "login", "error", "logout"]
    processor.process_all(data)


if __name__ == "__main__":
    main()
