#
# LSST Data Management System
# Copyright 2008-2012 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#
from __future__ import absolute_import
import re

from .record import Record


class JobAdInformation(Record):
    """Job ad information event triggered

    Extra job ClassAd attributed are noted.  This event is written
    as a supplement to other events when the configuration paramter
    EVENT_LOG_JOB_AD_INFORMATION_ATTRS is set.

    Parameters
    ----------
    year: `str`
        the year to tag the job with
    lines: list
        the strings making up this record
    """

    def __init__(self, year, lines):
        Record.__init__(self, year, lines)

        # slot name in which this job is running
        self.slotName = None
        pat = r"MachineSlotName = \"(?P<slotname>\S+)\""
        for line in lines:
            if line.startswith("MachineSlotName"):
                values = re.search(pat, line).groupdict()
                self.slotName = values["slotname"]
                if self.slotName == "$$(Name)":
                    self.slotName = None
                else:
                    self.slotName = self.slotName.split("@")[0]
                return


eventClass = JobAdInformation
eventCode = "028"
