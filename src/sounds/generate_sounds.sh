#!/bin/bash
echo Creating empty sounds...
for i in {0..9}
    do
    for j in {0..9}
        do
        cp template.wav sound_$i$j.wav
        done
    done
echo Done!