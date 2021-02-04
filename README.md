# KafkaForLoop

This repo contains files to check the kafka values in another class and compare if the recording is already in process
or stopped. 

## How to Run

- Run consumer.py which will listen for any added value in the topic.
- Run producer.py and press 1 or 2 to start or stop recording.
- This will also check if the recording is already happening or not. 
- When stop recording is pressed the sequence number will be updated, and it will allow us to start recording again.

## How it Works

- Consumer.py file is just used to listed to the new values resent in message queue.
- Producer.py gets the preset sequence number for the data to be sent and also gives options to start or stop recording.
- Once the start recording is pressed then the listUpdates.py class is called to check for the present recording status.
- The queue data is stored in myList which is declared as global variable. 
- Kafka Consumer is run for 6 seconds to get all the data form queue and store it in myList variable.
- The searching or filtering can be initiated using myList variable to get the current status of framework.

## Milestones

- Intergrate this working framework with the ImageProcessFramework for complete setup.
- Create proper topic names depending on the hours minutes seconds time format for filtering purposes.
- Creating and updating timestamp in queue data and filtering form timestamp values.
- ~~Incrementing Sequence numbers if EndRec is received.~~



### This contains important data, try to keep multiple backups of this moduel.
