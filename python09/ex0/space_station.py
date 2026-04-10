#!/usr/bin/env python3

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError  # type: ignore


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3,
        max_length=10,
    )
    name: str = Field(
        min_length=1,
        max_length=50,
    )
    crew_size: int = Field(
        ge=1,
        le=20,
    )
    power_level: float = Field(
        ge=0.0,
        le=100.0,
    )
    oxygen_level: float = Field(
        ge=0.0,
        le=100.0,
    )
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(
        default=None,
        max_length=200
    )


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = SpaceStation(
            station_id="SFSF",
            name="Alpha",
            crew_size=5,
            power_level=80.5,
            oxygen_level=95.0,
            last_maintenance=datetime.now()
        )
        for key, value in station.model_dump().items():
            if value is not None:
                if key == "last_maintenance":
                    value = value.strftime("%d/%m/%Y %H:%M")
                print(f"{key}: {value}")

    except ValidationError as error:
        for err in error.errors():
            field = ".".join(str(x) for x in err["loc"])
            message = err["msg"]
            print(f"{field}: {message.lower()}")
    print("========================================")


if __name__ == "__main__":
    main()
