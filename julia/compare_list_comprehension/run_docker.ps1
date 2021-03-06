$versions="0.6", "0.7", "1.0"

$current_path = $(Resolve-Path .).ToString()

foreach($version in $versions){
    docker run -it --rm -v ${current_path}:/data julia:$version bash -c "cd /data; julia compare.jl"
}
