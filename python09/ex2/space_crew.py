#!/usr/bin/env python3

from enum import Enum
from pydantic import (BaseModel, Field, model_validator,    # type: ignore
                      ConfigDict, ValidationError)
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    model_config = ConfigDict(extra='forbid')
    member_id: str = Field(
        min_length=3,
        max_length=10
    )
    name: str = Field(
        min_length=2,
        max_length=50
    )
    rank: Rank
    age: int = Field(
        ge=18,
        le=80
    )
    specialization: str = Field(
        min_length=3,
        max_length=30
    )
    years_experience: int = Field(
        ge=0,
        le=50
    )
    is_active: bool = True


class SpaceMission(BaseModel):
    model_config = ConfigDict(extra='forbid')
    mission_id: str = Field(
        min_length=5,
        max_length=15
    )
    mission_name: str = Field(
        min_length=3,
        max_length=100
    )
    destination: str = Field(
        min_length=3,
        max_length=50
    )
    launch_date: datetime
    duration_days: int = Field(
        ge=1,
        le=3650,
        description="Duration in days, ranging from 1 to 3650"
        "(maximum of 10 years)."
    )
    crew: list[CrewMember] = Field(
        min_length=1,
        max_length=12
    )
    mission_status: str = "planned"
    budget_millions: float = Field(
        ge=1.0,
        le=10000.0,
        description="budget in millions of dollars"
    )

    @model_validator(mode="after")
    def validate_business_rules(self) -> "SpaceMission":
        errors: list[str] = []
        has_leader = False
        has_inactive_member = False
        experimented_members = 0

        if not self.mission_id.startswith('M'):
            errors.append('Mission ID must start with "M"')

        for member in self.crew:
            if not member.is_active:
                has_inactive_member = True
            if (member.rank == Rank.CAPTAIN
                    or member.rank == Rank.COMMANDER):
                has_leader = True
            if member.years_experience >= 5:
                experimented_members += 1

        if self.duration_days > 365:
            if experimented_members < (len(self.crew) / 2):
                errors.append('Long missions (> 365 days) need '
                              '50% experienced crew (5+ years)')

        if not has_leader:
            errors.append("Mission must have at least one Commander"
                          " or Captain")

        if has_inactive_member:
            errors.append("All crew members must be active")

        if errors:
            raise ValueError(f"{'; '.join(errors)}")
        return self


def print_crew(crew: list[dict]) -> None:
    print(f"Crew size: {len(crew)}")
    print("Crew members: ")
    for member in crew:
        rank = member["rank"]
        print(f'- {member["name"]} ({rank})'
              f' - {member["specialization"]}')


def print_mission(m: SpaceMission) -> None:
    mission = m.model_dump(mode="json")
    print(f"Mission: {mission['mission_name']}")
    print(f"ID: {mission['mission_id']}")
    print(f"Destination: {mission['destination']}")
    print(f"Duration: {mission['duration_days']} days")
    print(f"Budget: ${mission['budget_millions']}")
    print_crew(mission['crew'])


def main() -> None:
    SPACE_MISSIONS = [{
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }, {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Jupiter Orbit Colony Mission',
        'destination': 'Jupiter Orbit',
        'launch_date': '2024-10-01T00:00:00',
        'duration_days': 1065,
        'crew': [
            {
                'member_id': 'CM011',
                'name': 'Emma Brown',
                'rank': 'commander',
                'age': 49,
                'specialization': 'Mission Command',
                'years_experience': 27,
                'is_active': True
            },
            {
                'member_id': 'CM012',
                'name': 'John Hernandez',
                'rank': 'lieutenant',
                'age': 36,
                'specialization': 'Science Officer',
                'years_experience': 22,
                'is_active': True
            },
            {
                'member_id': 'CM013',
                'name': 'Sofia Rodriguez',
                'rank': 'commander',
                'age': 29,
                'specialization': 'Life Support',
                'years_experience': 20,
                'is_active': True
            },
            {
                'member_id': 'CM014',
                'name': 'Sofia Lopez',
                'rank': 'lieutenant',
                'age': 44,
                'specialization': 'Systems Analysis',
                'years_experience': 25,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4626.0
    }, {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Europa Colony Mission',
        'destination': 'Europa',
        'launch_date': '2024-02-07T00:00:00',
        'duration_days': 666,
        'crew': [
            {
                'member_id': 'CM021',
                'name': 'Lisa Garcia',
                'rank': 'captain',
                'age': 36,
                'specialization': 'Medical Officer',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM022',
                'name': 'John Garcia',
                'rank': 'cadet',
                'age': 46,
                'specialization': 'Security',
                'years_experience': 25,
                'is_active': True
            },
            {
                'member_id': 'CM023',
                'name': 'Michael Johnson',
                'rank': 'officer',
                'age': 54,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM024',
                'name': 'Sarah Rodriguez',
                'rank': 'lieutenant',
                'age': 54,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM025',
                'name': 'Maria Smith',
                'rank': 'cadet',
                'age': 38,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4976.0
    }, {
        'mission_id': 'M2024_LUNA',
        'mission_name': 'Mars Colony Mission',
        'destination': 'Mars',
        'launch_date': '2024-06-13T00:00:00',
        'duration_days': 222,
        'crew': [
            {
                'member_id': 'CM031',
                'name': 'Anna Davis',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Communications',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM032',
                'name': 'Elena Garcia',
                'rank': 'lieutenant',
                'age': 42,
                'specialization': 'Science Officer',
                'years_experience': 23,
                'is_active': True
            },
            {
                'member_id': 'CM033',
                'name': 'Anna Brown',
                'rank': 'officer',
                'age': 55,
                'specialization': 'Engineering',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM034',
                'name': 'Emma Smith',
                'rank': 'captain',
                'age': 37,
                'specialization': 'Research',
                'years_experience': 23,
                'is_active': True
            },
            {
                'member_id': 'CM035',
                'name': 'Sofia Smith',
                'rank': 'lieutenant',
                'age': 53,
                'specialization': 'Security',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM036',
                'name': 'Maria Hernandez',
                'rank': 'commander',
                'age': 41,
                'specialization': 'Medical Officer',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM037',
                'name': 'John Hernandez',
                'rank': 'officer',
                'age': 42,
                'specialization': 'Science Officer',
                'years_experience': 20,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4984.6
    }, {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Saturn Rings Research Mission',
        'destination': 'Saturn Rings',
        'launch_date': '2024-09-18T00:00:00',
        'duration_days': 602,
        'crew': [
            {
                'member_id': 'CM041',
                'name': 'William Davis',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Medical Officer',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM042',
                'name': 'Sarah Smith',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM043',
                'name': 'Elena Garcia',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM044',
                'name': 'Sofia Williams',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Systems Analysis',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'CM045',
                'name': 'Sarah Jones',
                'rank': 'lieutenant',
                'age': 25,
                'specialization': 'Maintenance',
                'years_experience': 11,
                'is_active': True
            },
            {
                'member_id': 'CM046',
                'name': 'Lisa Rodriguez',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Life Support',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM047',
                'name': 'Sarah Smith',
                'rank': 'cadet',
                'age': 28,
                'specialization': 'Pilot',
                'years_experience': 8,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 1092.6
    }]

    print("Space Mission Crew Validation")
    for mission in SPACE_MISSIONS:
        print("=========================================")
        try:
            m = SpaceMission(**mission)
            print("Valid mission created:")
            print_mission(m)
        except ValidationError as e:
            print("Expected validation error:")
            for error in e.errors():
                message = error["msg"]
                print(message)
        print("\n=========================================\n")


if __name__ == "__main__":
    main()
