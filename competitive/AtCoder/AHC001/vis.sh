docker run --rm -v $(pwd)/tools:/tools --rm -w /tools rust bash -c "cargo run --release --bin vis example.in res2.out"

