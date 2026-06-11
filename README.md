E-puck Robot Reactive Behavior Simulation

This repository contains a reactive behavior controller for the e-puck robot, developed as part of my coursework for the **"Introduction to Robotics with Webots"** Specialization on Coursera (University of Colorado Boulder).

Project Overview
  The robot navigates an arena using a Finite State Machine (FSM) driven by infrared distance sensors. It reacts to obstacles in real-time, executing a sequence of precise maneuvers.

Steps:
    Step 0: Drive forward until the first obstacle (O1) is detected (with smooth slowdown).
    Step 1: Turn 180 degrees away from O1 using a hybrid time-step and sensor alignment logic.
    Step 2: Drive forward until the second obstacle (O2) is detected.
    Step 3: Turn right to align with the edge of O2.
    Step 4: Drive along the edge of O2, detecting the corner, and stop completely once the obstacle is cleared.

Technologies Used:
    Webots: Robot simulation environment.
    Python: Controller programming.
    Webots: E-puck model - differential drive robot equipped with IR distance sensors.
