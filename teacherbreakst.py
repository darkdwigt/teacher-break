import streamlit as st
import math
from collections import deque

def schedule_breaks(learners, exam_duration, teacher_names):
    # Constants
    TEACHER_RATIO = 30
    INITIAL_DURATION = 15
    END_DURATION = 15

    total_teachers = len(teacher_names)
    
    # Number of teachers that must remain on duty to maintain the ratio
    min_on_duty = math.ceil(learners / TEACHER_RATIO)
    
    # Middle period available for breaks
    middle_duration = exam_duration - (INITIAL_DURATION + END_DURATION)

    # Calculate maximum break time each teacher can take
    each_teacher_break = middle_duration / total_teachers

    # Initialize break end-times for each teacher to 0
    break_end_times = {name: 0 for name in teacher_names}

    # Maintain a queue of teachers for break scheduling
    teachers_queue = deque(teacher_names)

    schedule = [(0, INITIAL_DURATION, total_teachers, [])]
    current_time = INITIAL_DURATION
    
    while current_time < exam_duration - END_DURATION:
        on_duty = []
        on_break = []

        for i in range(total_teachers):
            teacher = teachers_queue[i]
            if break_end_times[teacher] <= current_time and len(on_break) < total_teachers - min_on_duty:
                on_break.append(teacher)
                break_end_times[teacher] = current_time + each_teacher_break
            else:
                on_duty.append(teacher)

        # Rotate queue to change break order for next iteration
        teachers_queue.rotate(-1)

        next_event_time = min(break_end_times[t] for t in on_break)
        next_event_time = min(next_event_time, exam_duration - END_DURATION)

        # Only add to the schedule if there's a meaningful duration
        if next_event_time > current_time:
            schedule.append((current_time, next_event_time, len(on_duty), on_break))
        
        current_time = next_event_time

    schedule.append((current_time, exam_duration, total_teachers, []))
    return schedule

def main():
    st.title("Teacher Break Scheduler")

    exam_duration = st.slider("Length of exam in minutes:", 0, 300, 120) 
    learners = st.slider("Number of learners:", 0, 500, 100) 
    num_teachers = st.slider("Number of teachers:", 0, 20, 5)

    teacher_names = []
    for i in range(num_teachers):
        name = st.text_input(f"Enter the name of teacher {i+1}:")
        teacher_names.append(name)

    if st.button("Generate Schedule"):
        required_teachers = math.ceil(learners / 30.0)
        if num_teachers <= required_teachers:
            st.write(f"All {num_teachers} teachers are needed on duty for the entire duration due to {learners} learners.")
            return

        schedule = schedule_breaks(learners, exam_duration, teacher_names)

        for start_time, end_time, on_duty, break_set in schedule:
            st.write(f"From minute {start_time:.2f} to {end_time:.2f}, {on_duty} teachers are on duty. Teachers on break: {', '.join(break_set) or 'None'}.")

        # Calculate and display total break duration for each teacher
        total_breaks = {teacher: 0 for teacher in teacher_names}
        for start_time, end_time, _, break_set in schedule:
            break_duration = end_time - start_time
            for teacher in break_set:
                total_breaks[teacher] += break_duration

        st.write("\nTotal break durations:")
        for teacher, duration in total_breaks.items():
            st.write(f"{teacher}: {duration:.2f} minutes")

if __name__ == "__main__":
    main()
