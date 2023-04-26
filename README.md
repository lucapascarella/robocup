# Introduction to Program Nao Robots for RoboCup Competition

## Overview

- Time and Place: Tuesday 09.00 - 12.00 at ETZ D61.2

## Course Schedule

| Week | Date | Content |
| --- | --- | --- |
| 01 | 27.09.2022 | Introduction, Python Crash Course, Hello World  |
| 02 | 04.10.2022 | Walk It Out, Let’s Dance |
| 03 | 11.10.2022 | Sense and Act, Do the Robot |
| 04 | 18.10.2022 | Python SDK |
| 05 | 25.10.2022 | Project: Physical Soccer (ETL D12) |
| 06 | 01.11.2022 |  |
| 07 | 08.11.2022 |  |
| 08 | 15.11.2022 |  |
| 09 | 22.11.2022 |  |
| 10 | 29.11.2022 | Hello Virtual World, Kick It Out, Object Recognition |
| 11 | 06.12.2022 | Project: Virtual Soccer |
| 12 | 13.12.2022 |  |
| 13 | 20.12.2022 |  |

## Project Description

### Project: Virtual Soccer

- Goal: Design you own algorithm for playing soccer implementing a finite state machine that defines the robot behavior
- Example
  - Behavior: Shoot the ball when the ball is near
  - States: Find Ball, Track Ball, Shoot Ball
  - Code

```python
class YourPlayer(Player):
    FIND_BALL = 0
    TRACK_BALL = 1
    SHOOT_BALL = 2

    def behave(self):
        state = FIND_BALL # initial state

        while True:
            if state == self.FIND_BALL:
                # Ball detection

            elif state == self.TRACK_BALL:
                # Ball tracking

            elif state == self.SHOOT_BALL:
                self.move("Shoot")
                state = TRACK_BALL # state transition

        return
```
