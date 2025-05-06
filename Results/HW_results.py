import json
import pandas as pd

# Load JSON file
with open('heavy_workload.json', 'r') as f:
    data = json.load(f)

# Initialize a list to collect rows
rows = []

# Iterate over each algorithm section in 'reports'
for algorithm_name, reports in data['reports'].items():
    for report in reports:
        exec = report['execution']
        case_range = report['case_range']
        rows.append({
            "Algorithm": algorithm_name,
            # "Case_Range_Start": case_range[0],
            # "Case_Range_End": case_range[1],
            "Case_Range": f"{case_range[0]}-{case_range[1]}",
            "Average_JCT_Seconds": exec["average_jct_seconds"],
            "Average_Queue_Delay_Seconds": exec["average_queue_delay_seconds"],
            "Average_DDL_Violation_Duration_Seconds": exec["average_ddl_violation_duration_seconds"],
            "Total_DDL_Violation_Duration_Seconds": exec["total_ddl_violation_duration_seconds"],
            "DDL_Violated_Jobs_Count": exec["ddl_violated_jobs_count"],
            "Finished_Jobs_Count": exec["finished_jobs_count"],
            "Do_Schedule_Count": exec["do_schedule_count"],
            "Average_Do_Schedule_Duration_ms": exec["average_do_schedule_duration_ms"],
            "Max_Do_Schedule_Duration_ms": exec["max_do_schedule_duration_ms"]
        })

# Convert list of dicts to DataFrame
df = pd.DataFrame(rows)

# Save as CSV
df.to_csv('HW_results.csv', index=False)

# Optional: save as Excel
# df.to_excel('HW_results.xlsx', index=False)
