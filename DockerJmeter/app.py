from flask import Flask, request
import requests
import subprocess

app = Flask(__name__)
    

@app.route("/run_jmeter", methods=["GET", "POST"])
def run_jmeter():
    if request.method == "GET":
        command = "jmeter -n -t jmx/light_thread.jmx -l ./run_results/test_result.jtl"
        status = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if status:
            return "Request received"
        else:
            return "Command didnt work"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
