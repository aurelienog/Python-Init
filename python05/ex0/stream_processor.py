#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            return "ERROR: not a number"
        length: int = 0
        suma: int = 0
        for num in data:
            suma += num
            length += 1
        if length == 0:
            return "ERROR: empty data"
        return super().format_output(f"Processed {length} numeric values,"
                                     f" sum={suma}, avg={(suma/length):.1f}")

    def validate(self, data: Any) -> bool:
        number: int
        try:
            for num in data:
                number = num
                number += 2
        except TypeError:
            return False
        return True


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            return "ERROR: not a string"
        count: int = 0
        words: int = 0
        in_word: bool = False
        for char in data:
            count += 1
            if char != " " and not in_word:
                in_word = True
                words += 1
            elif char == " ":
                in_word = False

        return super().format_output(f"Processed text: {count} characters,"
                                     f" {words} words")

    def validate(self, data: Any) -> bool:
        text: str = "test concatenate"
        try:
            text = text + data
        except TypeError:
            return False
        return True


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            return "ERROR: not a log"
        result: str
        if data[:5] == "ERROR":
            result = "[ALERT] ERROR level detected: Connection timeout"
        else:
            result = "[INFO] INFO level detected: System ready"
        return f"{super().format_output(result)}"

    def validate(self, data: Any) -> bool:
        try:
            if data[:5] == "ERROR":
                return True
            elif data[:4] == "INFO":
                return True
            else:
                return False
        except TypeError:
            return False


def process_numeric() -> None:
    print("\nInitializing Numeric Processor...")
    processor: NumericProcessor = NumericProcessor()
    data: list = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    if processor.validate(data):
        print("Validation: Numeric data verified")
        print(f"Output: {processor.process(data)}")
    else:
        print("ERROR: invalid data")


def process_text() -> None:
    print("\nInitializing Text Processor...")
    processor: TextProcessor = TextProcessor()
    data: str = "Hello Nexus World"
    print(f"Processing data: {data}")
    if processor.validate(data):
        print("Validation: Text data verified")
        print(f"Output: {processor.process(data)}")
    else:
        print("ERROR: invalid data")


def process_log() -> None:
    print("\nInitializing Log Processor...")
    processor: LogProcessor = LogProcessor()
    data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{data}"')
    if processor.validate(data):
        print("Validation: Log entry verified")
        print(f"Output: {processor.process(data)}")
    else:
        print("ERROR: invalid data")


def process_poly() -> None:
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data = [
        [1, 2, 3],
        "Hello World!",
        "INFO level detected: System ready"
    ]
    i: int = 0
    for processor in processors:
        print(f"Result {i + 1}: {processor.process(data[i])}")
        i += 1


def main() -> None:

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    process_numeric()
    process_text()
    process_log()
    print("\n=== Polymorphic Processing Demo ===")
    process_poly()
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
