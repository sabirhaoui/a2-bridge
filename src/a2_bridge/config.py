import os
from dataclasses import dataclass
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Settings:
    aveva_base_url: str
    aras_base_url: str

    @classmethod
    def from_env(cls) -> "Settings":
        values = []
        for name in ("A2_AVEVA_BASE_URL", "A2_ARAS_BASE_URL"):
            value = os.environ.get(name, "").strip()
            try:
                parsed = urlsplit(value)
                valid = (
                    parsed.scheme == "https" and bool(parsed.hostname)
                    and parsed.username is None and parsed.password is None
                    and not parsed.query and not parsed.fragment
                    and not any(char.isspace() for char in value)
                )
                parsed.port
            except ValueError:
                valid = False
            if not valid:
                raise ValueError(f"{name} must be an HTTPS URL without credentials, query, or fragment")
            values.append(value.rstrip("/"))
        return cls(*values)
