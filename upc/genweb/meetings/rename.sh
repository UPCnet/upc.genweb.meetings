#!/bin/sh
sed -e "s/Products.meetings/upc.genweb.meetings/g" config.py > config.py.out
mv config.py.out config.py
sed -e "s/\"meetings\"/\"upc.genweb\"/g" config.py > config.py.out
mv config.py.out config.py
sed -e "s/\"meetings\"/\"upc.genweb.meetings\"/g" profiles.zcml > profiles.zcml.out
mv profiles.zcml.out profiles.zcml
sed -e "s/Products.meetings/upc.genweb.meetings/g" Meeting.py > Meeting.py.out
mv Meeting.py.out Meeting.py
sed -e "s/Products.meetings/upc.genweb.meetings/g" profiles/default/import_steps.xml > profiles/default/import_steps.xml.out
mv profiles/default/import_steps.xml.out profiles/default/import_steps.xml
sed -e "s/Products.meetings/upc.genweb.meetings/g" setuphandlers.py > setuphandlers.py.out
mv setuphandlers.py.out setuphandlers.py