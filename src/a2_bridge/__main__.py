import argparse

from a2_bridge.config import Settings


def main() -> int:
    parser = argparse.ArgumentParser(description="a2-bridge integration foundation")
    parser.add_argument("--check-config", action="store_true")
    args = parser.parse_args()
    if args.check_config:
        try:
            Settings.from_env()
        except ValueError as exc:
            parser.exit(2, f"Configuration error: {exc}\n")
        print("Configuration valid. No remote connections were made.")
    else:
        parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
