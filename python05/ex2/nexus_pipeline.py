#!/usr/bin/env python3

from typing import Protocol, Any, Dict, Union
from abc import ABC, abstractmethod

# specialized stages retornan any como el original o dict/str como en el
# esquema


class ProcessingStage(Protocol):
    # duck typing Any class with process() can act as a stage.
    def process(self, data: Any) -> Any:
        return data


class InputStage():
    # implement the Protocol (duck typing, no inheritance).
    def process(self, data: Any) -> Dict:
        try:
            print()
        except Exception:
            print()


class TransformStage():
    # implement the Protocol (duck typing, no inheritance).
    def process(self, data: Any) -> Dict:
        return {}


class OutputStage():
    # implement the Protocol (duck typing, no inheritance).
    def process(self, data: Any) -> str:
        return ""


class ProcessingPipeline(ABC):
    # Abstract base managing stages. Contains a list of
    # stages and orchestrates data flow.
    def __init__(self) -> None:
        self.stages = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages = [*self.stages, stage]

    @abstractmethod
    def process(self, data: Any) -> Any:
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            keys = [item[key] for item in data for key in item]
            output = f"Output: Processed {data[keys[0]]} reading: {data[keys[1]]}{data[keys[2]]}  (Normal range)"
            return output
        except Exception as e:
            return f"{e}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        return data


class NexusManager():
    def __init__(self) -> None:
        self.pipelines: list[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines = [*self.pipelines, pipeline]

    def process_data(self, data: Any) -> None:
        for pipeline in self.pipelines:
            try:
                pipeline.add_stage(data)
                pipeline.process()
            except Exception as e:
                print(f"\nError detected in {e}")


def main() -> None:
    print("Initializing Nexus Manager...")
    nexus = NexusManager()
    # stages = [InputStage(), TransformStage(), OutputStage()]
    pipelines = [
                 JSONAdapter("JSON_001"),
                 CSVAdapter("CSV_001"),
                 StreamAdapter("Stream_001")]
    for pipeline in pipelines:
        nexus.add_pipeline(pipeline)
    data = [
      {"sensor": "temp", "value": 23.5, "unit": "C"},
      "user,action,timestamp", "Real-time", "sensor" "stream"
    ]
    nexus.process_data(data)


if __name__ == "__main__":
    main()
