from a2_bridge.adapters.base import EngineeringSource
from a2_bridge.domain.models import EngineeringObject


def preview_exchange(source: EngineeringSource) -> list[EngineeringObject]:
    """Read a source for inspection. Does not write to a target."""
    return list(source.read_objects())
