set -euo pipefail

day=$1
if [[ -z "$1" ]]; then
  echo "missing argument for day"
  echo "usage: ./fetchInput DAY"
  exit 1;
fi

inputFile="src/input/day$day.txt"
if [[ ! -f $inputFile ]]; then
  year=$(date +%Y)
  curl -sS --cookie "session=$(cat cookie.txt)" "https://adventofcode.com/$year/day/$day/input" -o $inputFile
  echo "Fetched $inputFile"
  git add $inputFile
else
  echo "$inputFile already exists"
fi

sourceFile="src/day$day.py"
if [[ ! -f $sourceFile ]]; then
  cp src/skeleton.py src/day$day.py
  sed -i "s/'REPLACE_ME'/$day/g" src/day$day.py
  echo "Created $sourceFile"
  git add $sourceFile
else
  echo "$sourceFile already exists"
fi
