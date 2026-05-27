"""Temperature helpers for the Elke27 integration."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from typing import Any

_IMPLIED_DECIMAL_TEMP_THRESHOLD = 200


def normalize_temperature(value: Any) -> float | None:
    """Normalize thermostat temperatures to display units."""
    if not isinstance(value, int | float):
        return None
    # Some panels report temperature with one implied decimal place.
    if abs(value) >= _IMPLIED_DECIMAL_TEMP_THRESHOLD:
        return float(value) / 10.0
    return float(value)


def encode_temperature_setpoint(value: float) -> int:
    """Encode Fahrenheit degrees to E27 thermostat protocol tenths."""
    return int(
        (Decimal(str(value)) * Decimal(10)).to_integral_value(rounding=ROUND_HALF_UP)
    )
