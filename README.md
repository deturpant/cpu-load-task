# ***CPU Load microservice***

Backend microservice "CPU Load", which allows you to obtain data on processor load for the last hour. Every 5 seconds, data is saved to the database.
The microservice is written in the aiohttp framework. Gino is used to interact with the database.
Provides 3 answers:
1) CPU load for the last hour (every 5 seconds) (**"/last_hours_loads"**)
2) CPU load for the last hour (averaged over minutes) (**"/avg_loads"**)
3) Intervals for stopping the service. (**"/shutdowns"**)

To raise the service, you need to create a "conf.yaml" file in the "config" directory. An example of filling out the config is in the "config" folder. After filling out the config, you need to install the dependencies contained in requirements.txt
Or build a docker image and run the container. The dockerfile is located at the root of the repository.
