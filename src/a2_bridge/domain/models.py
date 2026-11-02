from dataclasses import dataclass, field


@dataclass(frozen=True)
class EngineeringObject:
    """Provisional exchange model; refine during business discovery."""

    external_id: str
    object_type: str
    attributes: dict[str, str] = field(default_factory=dict)
