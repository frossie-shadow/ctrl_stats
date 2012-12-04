#!/usr/bin/env python
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
import os
import unittest
from lsst.ctrl.stats.reader import Reader
from lsst.ctrl.stats.classifier import Classifier
from lsst.ctrl.stats.condorEvents import CondorEvents

class test1(unittest.TestCase):
    def setup(self):
        None

    def test1(self):
        filename = os.path.join("tests","testfiles","reader_test.log")
        reader = Reader(filename)
        records = reader.getRecords()

        self.assertTrue("062.000.000" in records)
        self.assertTrue("063.000.000" in records)
        self.assertTrue("064.000.000" in records)

        classifier = Classifier()
        entries, total, updates = classifier.classify(records["063.000.000"])

        rec = entries[0]
        self.assertEqual(rec.condorId, "063.000.000")
        self.assertEqual(rec.dagNode, "A2")
        self.assertEqual(rec.submitTime, "2012-10-17 19:59:57")
        self.assertEqual(rec.executionHost, "141.142.225.136:41156")
        self.assertEqual(rec.executionStartTime, "2012-10-17 20:00:04")
        self.assertEqual(rec.executionStopTime, "2012-10-17 20:00:14")
        self.assertEqual(rec.updateImageSize, 414300)
        self.assertEqual(rec.updateMemoryUsageMb, 81)
        self.assertEqual(rec.updateResidentSetSizeKb, 81996)
        self.assertEqual(rec.userRunRemoteUsage, 1)
        self.assertEqual(rec.sysRunRemoteUsage, 1)
        self.assertEqual(rec.finalDiskUsageKb, 59)
        self.assertEqual(rec.finalDiskRequestKb, 59)
        self.assertEqual(rec.finalMemoryUsageMb, 81)
        self.assertEqual(rec.finalMemoryRequestMb, 81)
        self.assertEqual(rec.bytesSent, 25595)
        self.assertEqual(rec.bytesReceived, 1449)
        self.assertEqual(rec.terminationTime, "2012-10-17 20:00:14")
        self.assertEqual(rec.terminationCode, CondorEvents.TerminatedEvent)


        self.assertEqual(total.firstSubmitTime, "2012-10-17 19:59:57")
        self.assertEqual(total.totalBytesSent, 25595)
        self.assertEqual(total.totalBytesReceived, 1449)
        self.assertEqual(total.submissions, 1)
        self.assertEqual(total.executions, 1)
        self.assertEqual(total.shadowException, 0)
        self.assertEqual(total.socketLost, 0)
        self.assertEqual(total.socketReconnectFailure, 0)
        self.assertEqual(total.socketReestablished, 0)
        self.assertEqual(total.evicted, 0)
        self.assertEqual(total.aborted, 0)
        self.assertEqual(total.slotsUsed, 1)
        self.assertEqual(total.hostsUsed, 1)

        entries, total, updates = classifier.classify(records["062.000.000"])
        self.assertEqual(len(updates), 2)

        rec0 = updates[0]
        rec1 = updates[1]
        self.assertEqual(rec0.imageSize, 272192)
        self.assertEqual(rec0.memoryUsageMb, 40)
        self.assertEqual(rec0.residentSetSizeKb, 40640)
        self.assertEqual(rec1.imageSize, 414292)
        self.assertEqual(rec1.memoryUsageMb, 40)
        self.assertEqual(rec1.residentSetSizeKb, 40640)

if __name__ == "__main__":
    unittest.main()