set -euo pipefail

DAY=$1
if [[ -z "$1" ]]; then
  echo "missing argument for day"
  echo "usage: ./fetchInput DAY"
  exit 1;
fi

INPUT_FILE="src/input/day$DAY.txt"
if [[ ! -f $INPUT_FILE ]]; then
  YEAR=$(date +%Y)
  curl -sS --cookie "session=$(cat cookie.txt)" "https://adventofcode.com/$YEAR/day/$DAY/input" -o $INPUT_FILE
  echo "Fetched $INPUT_FILE"
  git add $INPUT_FILE
else
  echo "$INPUT_FILE already exists"
fi

SOURCE_FILE="src/day$DAY.py"
if [[ ! -f $SOURCE_FILE ]]; then
  cp src/skeleton.py src/day$DAY.py
  sed -i "s/'REPLACE_ME'/$DAY/g" src/day$DAY.py
  echo "Created $SOURCE_FILE"
  git add $SOURCE_FILE
else
  echo "$SOURCE_FILE already exists"
fi
