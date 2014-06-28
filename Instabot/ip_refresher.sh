#!/bin/bash
COUNTER=0
while [ $COUNTER -lt 2 ];do
	./sleep_run.sh & ./tor_setup.sh
	(( COUNTER++ ))
done	
	
