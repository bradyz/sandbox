#!/bin/bash
sleep 3 &
wait; torify ruby testclient.rb &
wait; kill $(ps a | grep "tor")
