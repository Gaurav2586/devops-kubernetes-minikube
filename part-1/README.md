#Part-1 consist two microservices.

service-1 called micro-1.py
service-2 called  micro-2.py

#Challange
You have to develop the microservices in two parts.
Microservice 1 should have input string message. It should respond with json of
reverse and random number.
{“message”: “abcdef”} --> {“message”: “fedcba”, “random”: 2.45}
In order to avoid load on microservice 1, we want to delegate the reverse string
task to microservice 2 which will just return reverse of the string
{“message”: “abcdef”} --> {“message”: “fedcba”}
 
#Solution:-
1:- service-1 gives reverse-string 
2:- service-2 gives random number
3:- service-2 is callable using service-1 as per challange demand.

#Result Screenshot :-

![Screenshot](https://github.com/Gaurav2586/devops-challenge/blob/master/zone.png?raw=true "zone")

##Quick look:-
#micro-1.py

![Screenshot](https://github.com/Gaurav2586/devops-challenge/blob/master/zone.png?raw=true "zone")

#micro-1.py

![Screenshot](https://github.com/Gaurav2586/devops-challenge/blob/master/zone.png?raw=true "zone")
