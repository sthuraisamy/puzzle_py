# puzzle_py
# puzzle
This code require python 3.8 and above. The poetry files are included.
## One
### Question
You have 100 doors in a row that are all initially closed. you make 100 passes by the doors
starting with the first door every time. the first time through you visit every door and toggle the
door (if the door is closed, you open it, if its open, you close it). the second time you only visit
every 2nd door (door #2, #4, #6). the third time, every 3rd door (door #3, #6, #9), etc, until you
only visit the 100th door. What state are the doors in after the last pass? Which are open which
are closed?

To start the application,

```python puzzle.py```

Provide parameters for number of doors and initial door state. E.g for the above puzzle the number of doors will be 100 and state will be 1.