# Install Java 8
sudo add-apt-repository ppa:webupd8team/java
apt-get update
apt-get install oracle-java8-installer
apt-get update

# Install Neo4j server
wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
echo 'deb http://debian.neo4j.org/repo stable/' >/tmp/neo4j.list
mv /tmp/neo4j.list /etc/apt/sources.list.d
apt-get update
apt-get install neo4j=1:3.5.3
echo "open /etc/neo4j/neo4j.conf and uncomment '\
        'dbms.connectors.default_listen_address', '\
        'dbms.connector.bolt.listen_address', '\
        'dbms.connector.http.listen_address'"
echo "run 'service neo4j restart' to start the database running"
