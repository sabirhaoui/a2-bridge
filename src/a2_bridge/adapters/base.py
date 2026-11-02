from typing import Iterable, Protocol

from a2_bridge.domain.models import EngineeringObject


class EngineeringSource(Protocol):
    def read_objects(self) -> Iterable[EngineeringObject]: ...


class EngineeringTarget(Protocol):
    def upsert_object(self, item: EngineeringObject) -> None: ...
