# Durable Agent Runtime

A C++ CLI demo being developed into a durable agent runtime.

## Current capability

Count entries matching `INFO`, `WARN`, or `ERROR` in a fixed,
in-memory log fixture.

The CLI validates the command, argument count, and requested level.
`CountTask` represents the request, and `CountResult` stores the count.

## Requirements

- C++20-compatible compiler
- CMake 3.22 or newer
- Python 3 for the CLI contract test

## Build

```bash
cmake -S . -B build
cmake --build build
```

## Run

```bash
./build/dar count ERROR
```

Expected output:

```text
count=3
```

The fixture contains one `INFO`, one `WARN`, and three `ERROR` entries.

Successful requests return exit status `0`. Invalid requests print
an error to stderr and return exit status `1`.

Example invalid request:

```bash
./build/dar count DEBUG
echo $?
```

Expected exit status: `1`.

## Test

```bash
ctest --test-dir build --output-on-failure
```

The `dar_cli_contract` test runs a Python script covering eight CLI
cases. It checks exit statuses, exact stdout, and error messages.

## Current limitations

- Log entries are hardcoded; there is no file input yet.
- No persistence or restart recovery.
- No external tool execution or model integration.
