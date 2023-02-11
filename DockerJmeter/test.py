import subprocess

command = "jmeter -n -t jmx/light_thread.jmx -l ./run_results/test_result.jtl"
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
if result:
    print("Process Completed")