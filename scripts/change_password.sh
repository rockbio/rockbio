#!/bin/bash

username=$1
password=$2

echo "$username:$password" | sudo chpasswd