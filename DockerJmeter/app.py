from flask import Flask, request
import requests
import subprocess
import os 

app = Flask(__name__)
    

@app.route("/", methods=["GET", "POST"])
def run_jmeter():
    current_workingdir = os.getcwd()
    print("Working dir = ", current_workingdir)
    if request.method == "GET":
        command = "jmeter -n -t {}/jmx/light_thread.jmx -l {}/run_results/test_result.jtl".format(current_workingdir, current_workingdir)
        status = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if status:
            print(status.stdout)
            return "GET Request recieved"
        else:
            return "Command didnt work"
    elif request.method == "POST":
        command = "jmeter -n -t {}/jmx/light_thread.jmx -l {}/run_results/test_result.jtl".format(current_workingdir, current_workingdir)
        status = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if status:
            return "POST Request received"
        else:
            return "Command didnt work"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
