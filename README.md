
# Teacher Break Scheduler

## Description
The Teacher Break Scheduler is a Python script designed to allocate break times for teachers during an exam. The scheduler maintains a specific teacher-to-student ratio, ensuring that there's always the necessary number of teachers present to invigilate the exam.

## Features

1. **Dynamic Ratio Maintenance**: Always keeps the requisite number of teachers on duty based on the total number of students.
2. **Equitable Break Distribution**: Ensures every teacher gets a break, with breaks distributed as evenly as possible.
3. **Customizable Inputs**: Allows user to input the duration of the exam, total number of students, total number of teachers, and the names of the teachers.
4. **Detailed Break Schedule**: Outputs a detailed minute-by-minute break schedule.
5. **Total Break Duration**: At the end of the scheduling, the script also provides a summary of the total break duration each teacher received.

## Usage

1. Run the script:
```bash
python teacherbreak2.py
```

2. Follow the on-screen prompts to input:
   - Length of the exam in minutes.
   - Total number of students.
   - Total number of teachers.
   - Names of each teacher.

3. Review the detailed break schedule output, noting which teachers are on break during specific time intervals.

4. At the end, the script will display the total break duration for each teacher.

## Requirements

- Python 3.x

## Limitations

1. The script assumes that all teachers are present at the beginning and end of the exam (first 15 minutes and last 15 minutes).
2. The script uses a fixed ratio of 1 teacher for every 30 students to calculate the minimum number of teachers required to be on duty.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

