mkdir -p build
cd build

CC=clang cmake ..
make

echo "Running fuzzer"
./tests/utility_fuzzer_test -max_total_time=60

echo "Running tests"
./tests/utility_test


echo "Program output: "

./main


