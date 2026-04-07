#!/usr/bin/env python3

from typing import Tuple
from importlib.metadata import version, PackageNotFoundError


def analyze_data() -> None:
    # import requests
    import numpy
    import pandas
    import matplotlib.pyplot
    matrix = numpy.random.randint(0, 100, size=1000)
    frame = pandas.DataFrame({"value": matrix})
    summary = frame["value"].describe()
    print(summary)


def check_installation(libraries: list[Tuple[str, str]]) -> bool:
    print("Checking dependencies:")
    missing_library = False
    for item in libraries:
        library: str = item[0]
        description: str = item[1]
        try:
            print(f"[OK] {library} ({version(library)}) - {description}")
        except PackageNotFoundError:
            print(f"[KO] {library} is not installed")
            missing_library = True
    if missing_library:
        print("\nPlease run one of this installation instructions:")
        print("- pip install -r requirements.txt")
        print("- poetry install")
        return False
    return True


def main() -> None:
    libraries = [("pandas", "Data manipulation ready"),
                 ("numpy", "Numerical computation ready"),
                 ("requests", "Network access ready"),
                 ("matplotlib", "Visualization ready")]

    print("\nLOADING STATUS: Loading programs...\n")
    ready = check_installation(libraries)
    if not ready:
        return
    analyze_data()

    print("\nAnalyzing Matrix data..."
          "\nProcessing 1000 data points..."
          "\nGenerating visualization...")

    print("\nAnalysis complete")


if __name__ == "__main__":
    main()
