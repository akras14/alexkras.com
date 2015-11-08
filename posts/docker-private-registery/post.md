I kept running into the following error, when trying to `docker pull` a docker image from our private repo.

<pre highlight="false">
docker pull some.ip/db:20151004073001
Error response from daemon: unable to ping registry endpoint https://some.ip/v0/
v2 ping attempt failed with error: Get https://some.ip/v2/: tls: failed to parse certificate from server: x509: negative serial number
v1 ping attempt failed with error: Get https://some.ip/v1/_ping: tls: failed to parse certificate from server: x509: negative serial number
</pre>

Googling the error was not very helpful, and it took me a while to find a solution, even though it is very simple. You just have to let docker know that it's ok to trust that repo:

1. `sudo vim /etc/default/docker`
2. Add the following line: `DOCKER_OPTS="$DOCKER_OPTS --insecure-registry your.registery.ip.or.url"`
3. Restart docker via: `sudo service docker restart`
