#!/bin/bash
cd data
if [ -d "COVID-19" ]; then
  git pull 
else
  git clone https://github.com/CSSEGISandData/COVID-19.git
fi
