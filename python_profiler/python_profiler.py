import argparse
import os
import sys
import cProfile
import io
import pstats
import time
from memory_profiler import profile

def run_script(script_path):
    exec(open(script_path).read())

def main():
    parser = argparse.ArgumentParser(description='Memory profiler for Python scripts.')
    parser.add_argument('script_path', metavar='script', type=str, help='Path to the Python script to be profiled.')
    args = parser.parse_args()

    if not os.path.exists(args.script_path):
        print(f'Error: {args.script_path} does not exist.')
        sys.exit(1)

    # Output memory
    @profile(precision=4)
    def run_script_with_memory_profiling():
        run_script(args.script_path)

    # Run the script with CPU profiling
    pr = cProfile.Profile()
    pr.enable()
    run_script(args.script_path)
    pr.disable()

    # Output memory and CPU profiling results
    print('MEMORY USAGE:')
    run_script_with_memory_profiling()
    print('\nCPU UTILIZATION:')
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumtime')
    ps.print_stats()
    print(s.getvalue())
    print('\nEXECUTION TIME:')
    start_time = time.time()
    run_script(args.script_path)
    end_time = time.time()
    print(f'Time elapsed: {end_time - start_time:.4f} seconds')


if __name__ == '__main__':
    main()

# in the terminal cd into folder containing python_profiler.py then type:
# python .\python_profiler.py test_python.py