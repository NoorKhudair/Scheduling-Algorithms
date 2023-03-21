# Scheduling-Algorithms
This is an Implementation of the operating system process scheduling algorithms using numpy .Information about processes is stored in a file named data.txt which contains the cpu burst , arrival time , and priority of each process as shown in the table:
| Process   | CPU burst    | Arrival time  | Priority |
| ----------|:------------:| -------------:|----------|
| P1        | 2            | 0             | 1        |
| P2        | 4      |  0 | 0 |
| P3 | 8  |2    |    1 |
| P4      | 12    |  3 | 2 |
| P3 | 10  |7    |    1 |

The program outputs a Gantt chart for each scheduling algorithm as shown below:
FCFS:
P1:0-2, P2:2-6, P3:6-14, P4:14-26, P5:26-36
SJF:
P1:0-2, P2:2-6, P3:6-14, P5:14-24, P4:24-36
RR:
P1:0-2, P2:2-6, P3:6-10, P4:10-14, P5:14-18, P3:18-22, P4:22-26, P5:26-30, P4:30-34, P5:34-36
Priority:
P2:0-4, P1:4-6, P3:6-14, P5:14-24, P4:24-36
