
```
.
├── cases: all test cases.
├── data: output metrics data.
├── metrics: code for metrics.
├── schedulers: schedulers implementations.
├── simulator: heterogeneous GPU cluster simulator.
├── config.json: configuration file.
├── main.go: entry point.
└── util: helper codes.

```
## Requirements
Linux OS (e.g., CentOS, RedHat, Ubuntu).

Docker >= 20.10.13.


## Report Analysis
A report is generated to show all the metrics we evaluate. It is a json file with the below format. Explanatory comments have been included in the json to explain the meanings of the fields.
``` json
{
    // "case_name", "case_ranges" and "cluster_configs" are the meta simulation parameters of this report.
	"case_name": "30_ddl", 
	"case_ranges": [
		[
			0,
			400
		]
	],
	"cluster_configs": [
		{
			"GPUs": {
				"GTX2080Ti": 15,
				"A100": 10,
				"V100": 20
			},
			"gpu_count": 45
		}
	],
	// "reports" maps scheduler to their simulated metrics.
	"reports": {
		"AnyScheduler": [
			{
				"scheduler_name": "AnyScheduler",
				"scheduler_info": "AnyInfo",
				"cluster_config": {
					"GPUs": {
						"GTX2080Ti": 15,
						"A100": 10,
						"V100": 20
					},
					"gpu_count": 45
				},
				"case_range": [
					0,
					400
				],
				// "execution records all the detailed metrics."
				"execution": {
					"average_jct_seconds": 37859.0125,
					"average_queue_delay_seconds": 23211.97,
					"average_ddl_violation_duration_seconds": 1827.4782608695627,
					"total_ddl_violation_duration_seconds": 42031.99999999994,
					"ddl_violated_jobs_count": 23,
					"finished_jobs_count": 400,
					"do_schedule_count": 398,
					"average_do_schedule_duration_ms": 0,
					"max_do_schedule_duration_ms": 0,
					"scheduler_execution_record_extra": null
				}
			}
		],
		"HydraBABWithHeuristic": [
			{
			    ...
				"execution": {
				    ...
				    // "scheduler_execution_record_extra" records info for specific scheduler. 
					"scheduler_execution_record_extra": {
						"average_k_means_round_duration_ms": 679,
						"max_k_means_round_duration_ms": 5301,
						"min_k_means_round_duration_ms": 5,
						"distance_solver_record_extra": {
							"memorized_call_count": 3511200,
							"non_memorized_call_count": 97800,
							"call_count": 3609000,
							"distance_algo_record_extra": {
								"call_count": 97800,
								"use_min_cost_algo_count": 31480,
								"use_sjf_greedy_count": 66320,
								"average_min_cost_algo_durations_ms": 136,
								// "min_cost_algo_record_extra" records min-cost algorithm execution details.
								"min_cost_algo_record_extra": {
									"call_count": 31480,
									"exceed_latency_count": 303,
									"use_fall_back_count": 0,
									"average_duration_nano": 130133594,
									"average_expand_nodes_count": 1860.141836086404,
									"average_jobs_count": 0,
									"max_jobs_count": 16,
									"average_total_cut_count": 1825.7169631512072,
									"average_after_expand_cut_count": 744.4926937738246,
									"average_prediction_is_optimus_cut_count": 18.36207115628971,
									"average_prediction_reduce_min_cost_count": 0,
									"average_expand_nothing_cut_count": 0,
									"average_c_hat_cut_count": 243.99666454891994,
									"jobs_count_2_summary_record": [
										{
											"call_count": 3,
											"jobs_count": 16,
											"exceed_latency_count": 3,
											"use_fall_back_count": 0,
											"average_expand_nodes_count": 254616.66666666666,
											"average_duration_nano": 5000072888,
											"average_total_cut_count": 194211.33333333334,
											"average_expand_nothing_cut_count": 0,
											"average_c_hat_cut_count": 0,
											"average_after_expand_cut_count": 60358.666666666664,
											"average_prediction_is_optimus_cut_count": 2606.3333333333335,
											"average_prediction_reduce_min_cost_count": 0
										}
									]
								}
							}
						}
					}
				}
			}
		]
	}
}
```
