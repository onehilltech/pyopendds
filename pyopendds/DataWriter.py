from __future__ import annotations

from .Topic import Topic

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Publisher import Publisher


class DataWriter:
    def __init__(self, publisher: Publisher, topic: Topic, qos=None, listener=None):
        self.topic = topic
        self.qos = qos
        self.publisher = publisher
        self.listener = listener
        publisher.writers.append(self)

        from _pyopendds import create_datawriter
        create_datawriter(self, publisher, topic)

    def write(self, data):
        pass


