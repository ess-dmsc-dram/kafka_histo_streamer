#  -*- coding: utf-8 -*-

kafka_server = "172.18.0.3:9092"

# Ensure Python will be able to import files in this directory
import sys, os
FILEPATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(FILEPATH)

from time import sleep
from mantid.simpleapi import *


StartLiveData(FromNow=True, FromTime=False, FromStartOfRun=False, UpdateEvery=5.0,
              Instrument="SANS2D", Listener="KafkaEventListener",
              Address=kafka_server, RunTransitionBehavior="Stop",
              PreserveEvents=True, AccumulationMethod="Add",
              OutputWorkspace="test", AccumulationWorkspace="accum",
              ProcessingScriptFilename=FILEPATH + "/preprocess.py",
              PostProcessingScriptFilename=FILEPATH + "/postprocess.py")

while True:
    sleep(1)
