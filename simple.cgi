#!/bin/bash
echo "Content-type: text/html"
echo ""

echo "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"myStil.css\"><title>Hello World</title></head>"
echo "<body>"
echo "Hello from Juan Navarrete"
if [ -n "${QUERY_STRING}" ] ; then
        /usr/bin/curl -s ${QUERY_STRING}
fi
echo "</body></html>"