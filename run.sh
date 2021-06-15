#!/usr/bin/env bash
rm  output.sh
lynx -listonly -nonumbers -dump https://www1.gogoanime.ai/anime-list.html\?page\={1..80} |  grep  "https://www1.gogoanime.ai/category/*"   |  sed 's/^/python3 anime-link-scaper.py  /;' >> output.sh ; echo done
chmod +x output.sh
./output.sh
