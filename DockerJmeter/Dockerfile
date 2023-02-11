# Importing alpine image from docker hub
FROM alpine:3.12

WORKDIR /Jmeter
#Defining paths to variables
ARG JMETER_VERSION="5.3"
ENV JMETER_HOME /opt/apache-jmeter-${JMETER_VERSION}
ENV	JMETER_BIN	${JMETER_HOME}/bin
# Downloading Jmeter
ENV	JMETER_DOWNLOAD_URL  https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz

# Adding pre-requisite certificates
ARG TZ="Europe/Amsterdam"
ENV TZ ${TZ}
RUN    apk update \
	&& apk upgrade \
	&& apk add ca-certificates \
	&& update-ca-certificates \
	&& apk add --update openjdk8-jre tzdata curl unzip bash \
	&& apk add --no-cache nss \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /tmp/dependencies  \
	&& curl -L --silent ${JMETER_DOWNLOAD_URL} >  /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz  \
	&& mkdir -p /opt  \
	&& tar -xzf /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz -C /opt  \
	&& rm -rf /tmp/dependencies

#Setting jmeter path and working directories
ENV PATH $PATH:$JMETER_BIN
WORKDIR ${JMETER_HOME}/bin

#Create a /jmx/ folder in current path and keep jmx files inside it
COPY ./jmx/ .

# Command to run jmeter jmx file in CLI mode
# ENTRYPOINT ["jmeter", "-n", "-t", "light_thread.jmx",  "-l",  "./run_results/test_result.jtl"]

#To get results use below command
#docker run --mount type=bind,source="<host absolute path>",target="/opt/apache-jmeter-5.3/bin/run_results" <Image_id>
#Example #docker run --mount type=bind,source="/home/hcm/Aaditya/containerization/DockerJmeter/results/",target="/opt/apache-jmeter-5.3/bin/run_results" 2be1c078ca0d


FROM python:3.8
WORKDIR /FlaskApp
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
 