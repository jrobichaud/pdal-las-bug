#!/usr/bin/env python3

import pdal


def main():
    pipelines = [
        "pipeline_baseline_text_to_text.json",
        "pipeline_ok_step_1_text_to_las.json",
        "pipeline_ok_step_2_las_to_text.json",
        "pipeline_bug_step_1_text_to_las.json",
        "pipeline_bug_step_2_las_to_las.json",
        "pipeline_bug_step_3_las_to_text.json",
    ]
    for pipeline in pipelines:
        with open(pipeline) as pipeline_json:
            json_pipeline = pipeline_json.read()
        pipeline = pdal.Pipeline(json_pipeline)
        pipeline.loglevel = 8  # really noisy
        pipeline.execute()


if __name__ == "__main__":
    main()
