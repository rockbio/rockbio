#!/bin/bash
export domain=$1
export name=$2
export address=$3
whmapi1 addzonerecord domain=$domain name=$name class=IN ttl=86400 type=A address=$address
