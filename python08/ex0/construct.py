
import sys
import os
import site


def print_inside_report() -> None:
    print("\nMATRIX STATUS: Welcome to the construct")

    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")

    print("\nSUCCESS: You're in an isolated environment!"
          "Safe to install packages without affecting"
          "the global system.")

    print("\nPackage installation path:")
    address = site.getsitepackages()[0]
    if address:
        print(address)


def print_outside_report() -> None:
    print("\nMATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!"
          "\nThe machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")

    print("\nThen run this program again.")


def main() -> None:
    if sys.prefix != sys.base_prefix:
        print_inside_report()
    else:
        print_outside_report()


if __name__ == "__main__":
    main()
