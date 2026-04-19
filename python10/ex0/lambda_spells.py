#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda x: x.get('power', 0),
                              reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x.get('power', 0) >= min_power,
                          mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda x: "* " + x + " *", spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0}
    maximum = max(mages, key=lambda mage: mage.get('power', 0))
    minimum = min(mages, key=lambda mage: mage.get('power', 0))
    avg = round(sum(m.get('power', 0) for m in mages) / len(mages), 2)
    return {
        'max_power': maximum.get('power', 0),
        'min_power': minimum.get('power', 0),
        'avg_power': avg
    }


def print_sorted_artifacts() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 75, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 80, 'type': 'relic'},
        {'name': 'Storm Crown', 'power': 60, 'type': 'accessory'},
        {'name': 'Fire Staff', 'power': 88, 'type': 'focus'}]
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    is_first = True
    for artifact in sorted_artifacts:
        if not is_first:
            print(" comes before ", end="")
        print(f"{artifact.get('name', 0)} ({artifact.get('power', 0)})",
              end="")
        is_first = False
    print("")


def print_transformed_spells() -> None:
    spells = ['shield', 'tornado', 'fireball', 'darkness']

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(spell, end=" ")
    print()


def main() -> None:

    print_sorted_artifacts()
    print_transformed_spells()

    mages = [
        {'name': 'Storm', 'power': 68, 'element': 'light'},
        {'name': 'Riley', 'power': 71, 'element': 'ice'},
        {'name': 'Casey', 'power': 76, 'element': 'shadow'},
        {'name': 'Riley', 'power': 64, 'element': 'light'},
        {'name': 'Casey', 'power': 99, 'element': 'water'}]

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 75)
    for mage in filtered_mages:
        print(mage)

    print("\nTesting mage stats...")
    print((mage_stats(mages)))


if __name__ == "__main__":
    main()
