"""Pytest setup: expose udi_interface Node/Custom for local test runs."""

import udi_interface
from udi_interface.custom import Custom
from udi_interface.node import Node
from udi_interface.polylogger import LOG_HANDLER, LOGGER

udi_interface.Node = Node
udi_interface.Custom = Custom
udi_interface.LOG_HANDLER = LOG_HANDLER
udi_interface.LOGGER = LOGGER
