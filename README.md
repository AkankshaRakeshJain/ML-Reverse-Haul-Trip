# ML-Reverse-Haul-Trip

One of the key optimization that are run in transportation is the reverse-haul logistics optimization. Reverse-haul logistics in simple terms is a trip (vehicle journey) from Point A to Point B and then back to Point A from Point B. (A to B and back to A). Optimization in reverse-haul means converting all single trip/journeys (A to B) into a reverse-haul (A to B to A).

Excel file consists of all ‘single trip journeys’ in our Automobile business. (A to B movement only). The columns are as follows: Trip ID (Unique id for each trip), Dispatch Date/Delivery Date (Date of start/end of the trip), Dispatch/Delivery Cluster (Location cluster for start/end cities), Lat/long of Dispatch/Delivery cluster (Geo-location of start/end clusters).
 
Task : Create maximum unique connections of reverse-haul logistics with ‘minimum time’ between the two connections among the single trip data provided using Python programming.
 
Eg output: Connection 1 : Trip id :12345 – Trip id 67890; Time difference : 2 days,  (Now this should be the best connection for Trip id 12345 with least possible time)
 
(Note: Once a connection is established between two trips, they should not be used for further connection)
 
