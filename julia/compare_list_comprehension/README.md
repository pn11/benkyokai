# Compare Julia's List and List Comprehension

Running `run_docker.sh` or `run_docker.ps1` will run `compare.jl` in Docker containers. 

## Requirement

- Docker

## 実行結果例

```
$ sudo ./run_docker.sh

Unable to find image 'julia:0.6' locally
0.6: Pulling from library/julia
55cbf04beb70: Pull complete
0293350860a4: Pull complete
bf481968acdd: Pull complete
Digest: sha256:4abe9e7484f15cdc0c79b8e6c94a5afa19739dcbe0f9657b7a3e2389b403e040
Status: Downloaded newer image for julia:0.6
--------------
リスト内包表記
  0.127111 seconds (3 allocations: 76.294 MiB, 60.37% gc time)
--------------
for文 (先に確保)
  0.150150 seconds (2 allocations: 76.294 MiB, 49.19% gc time)
--------------
for文（push）
  0.846705 seconds (10.00 M allocations: 256.141 MiB, 51.63% gc time)
--------------
読み取り
  0.366861 seconds (10.00 M allocations: 152.588 MiB)
Unable to find image 'julia:0.7' locally
0.7: Pulling from library/julia
54f7e8ac135a: Pull complete
046e37470a23: Pull complete
5026358e0524: Pull complete
Digest: sha256:7bcb8158c98b08ffe7e4cf937ab7f45999fcbd96cdd0da0563634ae0813415c2
Status: Downloaded newer image for julia:0.7
--------------
リスト内包表記
  0.050160 seconds (3 allocations: 76.294 MiB, 5.06% gc time)
--------------
for文 (先に確保)
  0.094973 seconds (2 allocations: 76.294 MiB, 14.57% gc time)
--------------
for文（push）
  0.845329 seconds (10.00 M allocations: 256.141 MiB, 49.75% gc time)
--------------
読み取り
  0.352896 seconds (10.00 M allocations: 152.588 MiB)
Unable to find image 'julia:1.0' locally
1.0: Pulling from library/julia
54f7e8ac135a: Already exists
046e37470a23: Already exists
6f4a4205826d: Pull complete
Digest: sha256:01873230ab93e88a1966fc4678e1a5220341526ee0d54640eac1da7afa0ee408
Status: Downloaded newer image for julia:1.0
--------------
リスト内包表記
  0.047165 seconds (3 allocations: 76.294 MiB, 5.72% gc time)
--------------
for文 (先に確保)
  0.090747 seconds (2 allocations: 76.294 MiB, 12.56% gc time)
--------------
for文（push）
  0.833917 seconds (10.00 M allocations: 256.141 MiB, 49.17% gc time)
--------------
読み取り
  0.344674 seconds (10.00 M allocations: 152.588 MiB)

```