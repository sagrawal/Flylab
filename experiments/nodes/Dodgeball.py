#!/usr/bin/env python
from __future__ import division
import roslib; roslib.load_manifest('experiments')
import rospy
import numpy as N
import ExperimentLib
from experiments.srv import *



#######################################################################################################
class ExperimentDodgeball():
    def __init__(self):
        rospy.init_node('Experiment')
        
        # Fill out the data structure that defines the experiment.
        self.experimentparams = ExperimentParamsRequest()
        
        self.experimentparams.experiment.description = "Dodgeball"
        self.experimentparams.experiment.maxTrials = -1
        self.experimentparams.experiment.trial = 1
        
        self.experimentparams.save.filenamebase = "dodgeball"
        self.experimentparams.save.arenastate = True
        self.experimentparams.save.video = True
        self.experimentparams.save.bag = False
        self.experimentparams.save.onlyWhileTriggered = True
        
        self.experimentparams.home.enabled = True
        self.experimentparams.home.x = 0.0
        self.experimentparams.home.y = 0.0
        self.experimentparams.home.speed = 20
        self.experimentparams.home.timeout = -1
        self.experimentparams.home.tolerance = 2
        
        self.experimentparams.waitEntry = 0.0
        
        self.experimentparams.triggerEntry.enabled = True
        self.experimentparams.triggerEntry.distanceMin = 20.0
        self.experimentparams.triggerEntry.distanceMax = 50.0
        self.experimentparams.triggerEntry.speedMin =  3.0
        self.experimentparams.triggerEntry.speedMax = 40.0
        self.experimentparams.triggerEntry.angleMin = 00.0 * N.pi / 180.0
        self.experimentparams.triggerEntry.angleMax =180.0 * N.pi / 180.0
        self.experimentparams.triggerEntry.angleTest = 'inclusive'
        self.experimentparams.triggerEntry.angleTestBilateral = True
        self.experimentparams.triggerEntry.timeHold = 0.5
        self.experimentparams.triggerEntry.timeout = -1
        
        self.experimentparams.move.enabled = True
        self.experimentparams.move.mode = 'relative'        
        self.experimentparams.move.relative.tracking = False
        self.experimentparams.move.relative.frameidOriginPosition = "Fly1"
        self.experimentparams.move.relative.frameidOriginAngle = "Fly1"
        self.experimentparams.move.relative.distance = 3
        self.experimentparams.move.relative.angle = 0
        self.experimentparams.move.relative.angleType = 'constant'
        self.experimentparams.move.relative.speed = 20
        self.experimentparams.move.relative.speedType = 'constant'
        self.experimentparams.move.relative.tolerance = 2
        self.experimentparams.move.timeout = 4
        
        self.experimentparams.triggerExit.enabled = False
        self.experimentparams.triggerExit.distanceMin = 0.0
        self.experimentparams.triggerExit.distanceMax = 999.0
        self.experimentparams.triggerExit.speedMin =  0.0
        self.experimentparams.triggerExit.speedMax = 999.0
        self.experimentparams.triggerExit.angleMin =  0.0 * N.pi / 180.0
        self.experimentparams.triggerExit.angleMax =180.0 * N.pi / 180.0
        self.experimentparams.triggerExit.angleTest = 'inclusive'
        self.experimentparams.triggerExit.angleTestBilateral = True
        self.experimentparams.triggerExit.timeHold = 1.0
        self.experimentparams.triggerExit.timeout = -1

        self.experiment = ExperimentLib.Experiment(self.experimentparams)


    def Run(self):
        self.experiment.Run()



if __name__ == '__main__':
    try:
        experiment = ExperimentDodgeball()
        experiment.Run()
        
    except KeyboardInterrupt:
        rospy.loginfo("Shutting down")

        
