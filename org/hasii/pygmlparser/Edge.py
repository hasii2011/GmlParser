
from typing import cast

from org.hasii.pygmlparser.exceptions.GMLParseException import GMLParseException
from org.hasii.pygmlparser.graphics.EdgeGraphics import EdgeGraphics


class Edge:
    def __init__(self):

        self.id:     int = cast(int, None)
        self.source: int = cast(int, None)
        self.target: int = cast(int, None)

        self.label: int = cast(int, None)
        self.source_node = None
        self.target_node = None

        self.graphics: EdgeGraphics = cast(EdgeGraphics, None)

    def validate(self, rawIdx: int):
        """
        Tests for the mandatory attributes id, source, and target from GML

        Args:
            rawIdx: Index into the source input
        Raises
            `GMLParseException` if mandatory properties are not valid
        """

        if self.source is None:
            raise GMLParseException(f'[pos {rawIdx}] edge has no source')
        if self.target is None:
            raise GMLParseException(f'[pos {rawIdx}] edge has no target')

        if not isinstance(self.source, int):
            raise GMLParseException(f'[pos {rawIdx}] edge has non-int source: {self.source}')
        if not isinstance(self.target, int):
            raise GMLParseException(f'[pos {rawIdx}] edge has non-int target: {self.target}')

    def __str__(self):
        meStr: str = f'Edge[id: {self.id} label: {self.label} source: {self.source} target: {self.target}] {self.graphics.__str__()}'

        return meStr

    def __repr__(self):
        return self.__str__()
