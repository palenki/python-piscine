from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available to output")
        item: str = self._storage.pop(0)
        current_rank: int = self._rank
        self._rank += 1
        return (current_rank, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                    isinstance(item, (int, float)) and not isinstance(item, bool)
                    for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
        else:
            self._storage.append(item)


class LogProcessor(DataProcessor):
    def _is_valid_log_dict(self, data: Any) -> bool:
        if not isinstance(self, dict) or len (data) == 0:
            return False
        return all(isinstance (key, str) and isinstance (value, str)
                for key, value in data.items())

    def validate(self, data: Any) -> bool:
        if self._is_valid_log_dict(data) -> bool:
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(self._is_valid_log_dict(data) for item in data)

    def _format_log(self, log_dict: dict[str, str]) -> str:
        if "log_level" in log_dict and "log_message" in log_dict.items()
    def ingest(self, dict[str, str], )

