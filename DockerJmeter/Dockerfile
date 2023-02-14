# Start from the Alpine image
FROM alpine:3.12
# Download and install Apache JMeter
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
# Install Python and pip
RUN apk add python3 && \
    apk add py3-pip	
# Set the working directory
WORKDIR /app
# Copy the files from the host to the container
COPY . /app
# Set the environment variables for Apache JMeter
ENV JMETER_HOME /opt/jmeter
ENV PATH $JMETER_HOME/bin:$PATH
# Set the default command to run in the container
RUN pip3 install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]