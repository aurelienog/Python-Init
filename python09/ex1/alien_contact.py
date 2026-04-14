#!/usr/bin/env python3

from pydantic import (BaseModel, ConfigDict, Field,     # type: ignore
                      ValidationError, model_validator)  # type: ignore
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    model_config = ConfigDict(extra='forbid')
    contact_id: str = Field(
        min_length=5,
        max_length=15
    )
    timestamp: datetime
    location: str = Field(
        min_length=3,
        max_length=100
    )
    contact_type: ContactType
    signal_strength: float = Field(
        ge=0.0,
        le=10.0,
        description="Signal strength on a scale from 0.0 to 10.0."
    )
    duration_minutes: int = Field(
        ge=1,
        le=1440,
        description="Duration in minutes, ranging from 1 to 1440"
        "(maximum of 24 hours)."
    )
    witness_count: int = Field(
        ge=1,
        le=100,
        description="Number of witnesses, from 1 to 100 people."
    )
    message_received: str | None = Field(
        max_length=500,
        default=None
    )
    is_verified: bool = Field(
        default=False
    )

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        errors: list[str] = []
        if not self.contact_id.startswith("AC"):
            errors.append('Contact ID must start with "AC" (Alien Contact)')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            errors.append("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            errors.append("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            errors.append("Strong signals (> 7.0)"
                          " should include received messages")

        if errors:
            raise ValueError("; ".join(errors))
        return self


def print_contact(contact: AlienContact) -> None:
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")
    print("")


def main() -> None:
    ALIEN_CONTACTS = [{
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'visual',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_002',
        'timestamp': '2024-08-20T00:00:00',
        'location': 'Mauna Kea Observatory, Hawaii',
        'contact_type': 'radio',
        'signal_strength': 5.6,
        'duration_minutes': 152,
        'witness_count': 6,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_003',
        'timestamp': '2024-11-15T00:00:00',
        'location': 'Very Large Array, New Mexico',
        'contact_type': 'telepathic',
        'signal_strength': 4.5,
        'duration_minutes': 19,
        'witness_count': 14,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_004',
        'timestamp': '2024-02-24T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'telepathic',
        'signal_strength': 2.4,
        'duration_minutes': 46,
        'witness_count': 9,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_005',
        'timestamp': '2024-09-10T00:00:00',
        'location': 'SETI Institute, California',
        'contact_type': 'telepathic',
        'signal_strength': 6.4,
        'duration_minutes': 134,
        'witness_count': 5,
        'message_received': 'Warning about solar flare activity',
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_006',
        'timestamp': '2024-02-02T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 2.7,
        'duration_minutes': 20,
        'witness_count': 14,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_007',
        'timestamp': '2024-03-25T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.0,
        'duration_minutes': 138,
        'witness_count': 10,
        'message_received': 'Request for peaceful contact',
        'is_verified': True
    }, {
        'contact_id': 'AC_2024_008',
        'timestamp': '2024-11-30T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 8.6,
        'duration_minutes': 122,
        'witness_count': 13,
        'message_received': 'Unknown language pattern identified',
        'is_verified': True
    }, {
        'contact_id': 'AC_2024_009',
        'timestamp': '2024-09-27T00:00:00',
        'location': 'Mauna Kea Observatory, Hawaii',
        'contact_type': 'visual',
        'signal_strength': 2.1,
        'duration_minutes': 25,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_010',
        'timestamp': '2024-06-12T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'physical',
        'signal_strength': 4.3,
        'duration_minutes': 52,
        'witness_count': 11,
        'message_received': None,
        'is_verified': True
    }, {
        'contact_id': 'AC_2024_011',
        'timestamp': '2024-11-05T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'radio',
        'signal_strength': 3.7,
        'duration_minutes': 235,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_012',
        'timestamp': '2024-07-04T00:00:00',
        'location': 'International Space Station',
        'contact_type': 'radio',
        'signal_strength': 5.3,
        'duration_minutes': 111,
        'witness_count': 10,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_013',
        'timestamp': '2024-02-12T00:00:00',
        'location': 'Antarctic Research Station',
        'contact_type': 'visual',
        'signal_strength': 6.8,
        'duration_minutes': 228,
        'witness_count': 11,
        'message_received': None,
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_014',
        'timestamp': '2024-10-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'radio',
        'signal_strength': 7.2,
        'duration_minutes': 113,
        'witness_count': 8,
        'message_received': 'Mathematical sequence detected: prime numbers',
        'is_verified': False
    }, {
        'contact_id': 'AC_2024_015',
        'timestamp': '2024-01-02T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'radio',
        'signal_strength': 2.1,
        'duration_minutes': 9,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    }, {
        "contact_id": "WRONG_FORMAT",
        "timestamp": "2024-01-15T14:30:00",
        "location": "Area 51",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": None,
        "is_verified": False
    }, {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-01-16T09:15:00",
        "location": "Roswell",
        "contact_type": "telepathic",
        "signal_strength": 6.2,
        "duration_minutes": 30,
        "witness_count": 1,
        "message_received": None,
        "is_verified": False
    }
    ]

    print("Alien Contact Log Validation")
    for contact in ALIEN_CONTACTS:
        print("======================================")
        try:
            c = AlienContact(**contact)
            print_contact(c)
        except ValidationError as error:
            print("Expected validation error:")
            for err in error.errors():
                err = err['msg'].split(", ")[1]
                for message in err.split("; "):
                    print(message)
        print("======================================")


if __name__ == "__main__":
    main()
