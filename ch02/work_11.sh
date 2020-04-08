sed s/$'\t'/$' '/g popular-names.txt

tr '\t' ' ' < popular-names.txt

expand -t 1 popular-names.txt