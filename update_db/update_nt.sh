#! /bin/bash
for in $(seq -w 0 99); do
     wget -q --continue --wait 10 --random-wait ftp://ftp.ncbi.nlm.nih.gov/blast/db/nt.${i}.tar.gz &&
     wget -q --continue --wait 10 --random-wait ftp://ftp.ncbi.nlm.nih.gov/blast/db/nt.${i}.tar.gz.md5 &&
     echo "Successfully retrieved nt.${i}.tar.gz" ||
     echo "nt.${i}.tar.gz failed or does not exist.";
done
