#!/bin/bash

source env/bin/activate
python audience_of.py @FCBarcelona

telegram-send "FCBarcelona finished"

python audience_of.py @realmadrid

telegram-send "realmadrid finished"

python audience_of.py @Cristiano

telegram-send "Cristiano finished"

python audience_of.py @TeamMessi

telegram-send "TeamMessi finished"

python audience_of.py @adidas

telegram-send "adidas finished"

python audience_of.py @adidasfootball

telegram-send "adidasfootball finished"

python audience_of.py @nike

telegram-send "nike finished"

python audience_of.py @nikefootball

telegram-send "nikefootball finished"

telegram-send "all done"
