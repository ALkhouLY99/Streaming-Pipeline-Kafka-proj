
# using bash script 
cd kafka_2.12-3.7.1
bin/kafka-topics.sh --create --topic toll --bootstrap-server localhost:9092
-----------------------------
# or 
------------------------------ admin.py -------------------------
#  using python API 
from kafka.admin import KafkaAdminClient, NewTopic

# Step 1: Connect to Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='kafka-client'
)

# Step 2: Define the new topic
topic_list = []
new_topic = NewTopic(name="toll", num_partitions=1, replication_factor=1)
topic_list.append(new_topic)

# Step 3: Create the topic
admin_client.create_topics(new_topics=topic_list)

print("Topic 'toll' created successfully.")

# Step 4: Close the admin client
admin_client.close()
