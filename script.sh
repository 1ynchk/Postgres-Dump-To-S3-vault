#!/bin/bash
cnt=0
result=()
while IFS= read -r var;
do
	if [ "$cnt" -gt 2 ];
	then 
		cmd=$(echo "$var" | grep "rows)")
		if [ ${#cmd} -eq 0 ]; then 
			export DATABASES="${var:1}:$DATABASES"
		fi
	else
		cnt+=1
	fi
done < <(psql -c 'SELECT datname FROM pg_database WHERE datallowconn = true;')
echo "$DATABASES"
exit 0
