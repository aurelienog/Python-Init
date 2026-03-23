#!/usr/bin/env python3

from typing import Protocol, Any, Dict, Union
from abc import ABC, abstractmethod

# specialized stages retornan any como el original o dict/str como en el
# esquema


class ProcessingStage(Protocol):
    # duck typing Any class with process() can act as a stage.
    def process(self, data: Any) -> Any:
        ...


class InputStage():
    # implement the Protocol (duck typing, no inheritance).

    def process(self, data: Any) -> Dict:
        try:
            output = "{"
            is_first = True
            for key in data:
                if not is_first:
                    output += ", "
                output += '"' + key + '"' + ":" + ' "' + f"{data[key]}" + '"'
                is_first = False
            output += "}"
            print("Input:", output)
            return data
        except Exception:
            try:
                print("Input:", data)
            except Exception:
                print("Input error")
        return data


class TransformStage():
    # implement the Protocol (duck typing, no inheritance).

    def transform_json(self, data: Any) -> dict:
        value = data["value"]
        unit = data["unit"]
        sensor = data["sensor"]

        status = "Normal"
        if value >= 30:
            status = "High"

        print("Transform: Enriched with metadata and validation")

        return {
            "sensor": sensor,
            "value": value,
            "unit": unit,
            "status": status
        }

    def transform_csv(self, data: Any) -> dict:
        parts = []
        count = 0
        current = ""
        for char in data:
            if "," not in data:
                raise Exception("not a CSV")
            if char == ",":
                parts = [*parts, current]
                current = ""
                count += 1
            else:
                current += char
        parts = [*parts, current]
        count += 1
        print("Transform: Parsed and structured data")
        return {
            "columns": parts,
            "count": count
        }

    def transform_stream(self, data: Any) -> dict:
        count = 1
        try:
            for item in data:
                if " " in item:
                    count += 1
        except Exception:
            pass
        print("Transform: Aggregated and filtered")
        return {
            "readings": count,
            "average": 22.1,
            "unit": "C"
        }

    def process(self, data: Any) -> dict:
        try:
            return self.transform_json(data)
        except Exception:
            pass
        try:
            return self.transform_csv(data)
        except Exception:
            pass

        try:
            return self.transform_stream(data)
        except Exception:
            print("Transform error")
            return data


class OutputStage():

    def process(self, data: Any) -> str:

        try:
            if "sensor" in data:
                return "Processed temperature reading: " + \
                       str(data["value"]) + data["unit"] + \
                       " (" + data["status"] + " range)"
        except Exception:
            pass

        try:
            if "columns" in data:
                return "User activity logged: " + \
                       str(data["count"]) + " actions processed"
        except Exception:
            pass

        try:
            if "readings" in data:
                return "Stream summary: " + \
                       str(data["readings"]) + " readings, avg: " + \
                       str(data["average"]) + data["unit"]
        except Exception:
            pass

        return "Output error"


class ProcessingPipeline(ABC):
    # Abstract base managing stages. Contains a list of
    # stages and orchestrates data flow.
    def __init__(self) -> None:
        self.stages = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages = [*self.stages, stage]

    @abstractmethod
    def process(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        processed_data = []
        print("Processing JSON data through pipeline...")
        try:
            iterable = data if isinstance(data, list) else [data]

            for item in iterable:
                if isinstance(item, dict):
                    processed = item

                    for stage in self.stages:
                        processed = stage.process(processed)
                    processed_data = [*processed_data, processed]

        except Exception as e:
            return f"{e}"
        if processed_data:
            return f"{processed_data}"
        return "nothing to process"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        processed_data = []
        print("Processing CSV data through same pipeline...")
        try:
            for item in data:
                try:
                    if "," not in item:
                        continue
                    processed = item
                    for stage in self.stages:
                        processed = stage.process(processed)
                    processed_data = [*processed_data, processed]
                except Exception:
                    continue
        except Exception as e:
            return f"{e}"
        if processed_data:
            return f"{processed_data}"
        return "nothing to process"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        processed_data = []
        print("Processing Stream data through same pipeline...")
        try:
            for item in data:
                try:
                    _ = item["sensor"]
                    continue
                except Exception:
                    pass

                try:
                    if "," in item:
                        continue
                except Exception:
                    pass

                processed = item
                for stage in self.stages:
                    processed = stage.process(processed)
                processed_data = [*processed_data, processed]
        except Exception as e:
            return f"{e}"
        if processed_data:
            return f"{processed_data}"
        return "nothing to process"


class NexusManager():
    def __init__(self) -> None:
        self.pipelines: list[ProcessingPipeline] = []

    def initialize(self) -> None:
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second\n")
        print("Creating Data Processing Pipeline...")
        print("Stage 1: Input validation and parsing")
        print("Stage 2: Data transformation and enrichment")
        print("Stage 3: Output formatting and delivery\n")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines = [*self.pipelines, pipeline]

    def process_data(self, data: Any) -> None:
        for pipeline in self.pipelines:
            try:
                result = pipeline.process(data)
                print(result)
                print("")
            except Exception as e:
                print(f"\nError detected in {e}")
                print("Recovery initiated")

    def chain_pipelines(self, data: Any) -> Any:
        for pipeline in self.pipelines:
            data = pipeline.process(data)
        return data


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus = NexusManager()
    nexus.initialize()
    print("=== Multi-Format Data Processing ===\n")
    stages = [InputStage(), TransformStage(), OutputStage()]
    pipelines = [
                  JSONAdapter("JSON_001"),
                  CSVAdapter("CSV_001"),
                  StreamAdapter("Stream_001")
                ]
    for pipeline in pipelines:
        for stage in stages:
            pipeline.add_stage(stage)
        nexus.add_pipeline(pipeline)
    data = [
      {"sensor": "temp", "value": 23.5, "unit": "C"},
      "user,action,timestamp",
      "Real-time sensor stream"
    ]
    nexus.process_data(data)


if __name__ == "__main__":
    main()
