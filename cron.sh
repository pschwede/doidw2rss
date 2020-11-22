#!/bin/bash

source env/bin/activate

bin/doidw2rss.py $1

deactivate
