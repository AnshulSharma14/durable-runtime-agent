Project name : Durable Agent Runtime
Current capability : counts ERROR entries in a fixed,in-memory fixture
Requirements : C++20 compiler and CMAKE 3.22 or newer
commands : 
	cmake -S . -B build
	cmake --build build
	./build/dar
	ctest --test-dir build --output-on-failure
expected output : error_count=3
Current limitations : no persistence,recovery,or model integration;the smoke test checks successful exit only 
