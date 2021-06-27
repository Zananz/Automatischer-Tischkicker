An table football game that counts goals and how often a player wins against an other player.

It is based on an Raspberry Pi pico runing micropython.

There are 2 terminals with 1 LCD-display and 5 switches. 4 of the 5 switches are used put in the player ID (bin 0000-1111).
The other one is used to log in. Since ther are 4 switches to put in a player ID, there is the opportunity to have 16 differnt players.
There is also a big red button for any of the 3 terminals to subtract 1 goal. 

There are 2 laser barriers to count the goals.

The game is over if a player has 10 goals. If you want to play till 20 for exaple, ther is the possibility to suptract goalpionts by pressing 
the big red buttons. That opens the possibility to start with an negativ goal count. It ist possible to go beyond -99 goals.
 
