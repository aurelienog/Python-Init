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


def print_station(station: SpaceStation) -> None:
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}")
    print(f"Oxygen: {station.oxygen_level}")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not Operational")


def main() -> None:
    print("Space Station Data Validation")

    stations: list[dict] = [
        {
            "station_id": "LGW125",
            "name": "Titan Mining Outpost",
            "crew_size": 6,
            "power_level": 76.4,
            "oxygen_level": 95.5,
            "last_maintenance": "2023-07-11T00:00:00",
            "is_operational": True,
            "notes": None
        }, {
            "station_id": "TOOLONG123456",
            "name": "Test Station",
            "crew_size": 25,
            "power_level": 85.0,
            "oxygen_level": 92.0,
            "last_maintenance": "2024-01-15T10:30:00",
            "is_operational": True
        },
    ]
    for s in stations:
        print("========================================")
        try:
            station = SpaceStation(**s)
            print_station(station)

        except ValidationError as error:
            print("Expected validation error:")
            for err in error.errors():
                field = ".".join(str(x) for x in err["loc"])
                message = err["msg"]
                print(f"{field}: {message.lower()}")
        print("========================================")


if __name__ == "__main__":
    main()
