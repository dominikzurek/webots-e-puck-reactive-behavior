# E-puck Robot Reactive Behavior Simulation

This repository contains a reactive behavior controller for the e-puck robot, developed as part of my coursework for the **"Introduction to Robotics with Webots"** Specialization on Coursera (University of Colorado Boulder).

## Project Overview
The robot navigates an arena using a Finite State Machine (FSM) driven by infrared distance sensors. It reacts to obstacles in real-time, executing a sequence of precise maneuvers.

## Project Requirements

To successfully pass this laboratory assignment, the controller had to strictly satisfy the following behavioral constraints in a sequential order:
1. **Obstacle Detection & Smooth Slowdown:** The robot must drive forward and safely detect the first wall obstacle ($O_1$) using its front infrared distance sensors, executing a smooth deceleration before impact.
2. **Precise $180^\circ$ Turn:** Upon approach, the robot must execute a precise $180^\circ$ turn away from $O_1$ without colliding with the wall. The turn must be stabilized using a hybrid combination of a time-step counter and sensor-alignment logic to combat discrete simulator latency.
3. **Wall Alignment & Corner Detection:** The robot must locate a second obstacle/wall ($O_2$), align its body parallel to it, and perform wall-following (skirting the edge of the obstacle).
4. **Autonomous Termination:** The robot must continuously monitor its environment, detect when it has successfully cleared the corner/edge of $O_2$, and immediately bring all motors to a complete stop ($v_L = 0, v_R = 0$), terminating the script loop.

## Execution Steps:
* **Step 0:** Drive forward until the first obstacle (O1) is detected (with smooth slowdown).
* **Step 1:** Turn 180 degrees away from O1 using a hybrid time-step and sensor alignment logic.
* **Step 2:** Drive forward until the second obstacle (O2) is detected.
* **Step 3:** Turn right to align with the edge of O2.
* **Step 4:** Drive along the edge of O2, detecting the corner, and stop completely once the obstacle is cleared.

## Technologies Used:
* **Webots:** Robot simulation environment.
* **Python:** Controller programming.
* **Webots e-puck model:** Differential drive robot equipped with IR distance sensors.
