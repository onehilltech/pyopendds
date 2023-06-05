import sys
from datetime import timedelta

from pyopendds import (
    opendds_version_dict,
    init_opendds,
    DomainParticipant,
    StatusKind,
    PyOpenDDS_Error,
)
from pybasic.basic import Reading

if __name__ == "__main__":
    print('OpenDDS Version is:', opendds_version_dict())
    try:
        # Initialize OpenDDS and Create DDS Entities
        init_opendds(opendds_debug_level=1)
        domain = DomainParticipant(34)
        topic = domain.create_topic('Readings', Reading)
        publisher = domain.create_publisher()
        writer = publisher.create_datawriter(topic)

        print('Done!')

    except PyOpenDDS_Error as e:
        sys.exit(e)
