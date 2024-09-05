cd kafka_2.12-3.7.1
# Generate a cluster UUID that will uniquely identify the Kafka cluster.
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
# to configure the log directories passing the cluster id.
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
#  can start the Kafka server
bin/kafka-server-start.sh config/kraft/server.properties
