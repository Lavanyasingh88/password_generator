from __future__ import annotations

import argparse
import secrets
import string


def build_charset(include_upper: bool, include_lower: bool, include_digits: bool, include_symbols: bool) -> str:
    charset = ""

    if include_upper:
        charset += string.ascii_uppercase
    if include_lower:
        charset += string.ascii_lowercase
    if include_digits:
        charset += string.digits
    if include_symbols:
        charset += "!@#$%^&*()-_=+[]{};:,.?/|"

    return charset


def generate_password(length: int, include_upper: bool, include_lower: bool, include_digits: bool, include_symbols: bool) -> str:
    charset = build_charset(include_upper, include_lower, include_digits, include_symbols)
    if not charset:
        raise ValueError("Select at least one character type.")
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    return "".join(secrets.choice(charset) for _ in range(length))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("--length", type=int, default=12, help="Password length. Default is 12.")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters.")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters.")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits.")
    parser.add_argument("--symbols", action="store_true", help="Include symbols.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    password = generate_password(
        length=args.length,
        include_upper=not args.no_upper,
        include_lower=not args.no_lower,
        include_digits=not args.no_digits,
        include_symbols=args.symbols,
    )
    print(password)


if __name__ == "__main__":
    main()
