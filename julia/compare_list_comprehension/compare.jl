const N = 10000000

function list_comprehension(test_list)
    new_list = [t*t for t in test_list]
    return new_list
end

function for_loop(test_list)
    new_list = similar(test_list)
    length = size(test_list)[1]
    for i in 1:length
        new_list[i] = (test_list[i]*test_list[i])
    end
    return new_list
end

function for_loop_append(test_list)
    new_list = []
    for t in test_list
        push!(new_list, t*t)
    end
    return new_list
end

function test()
    test_list = randn(N)

    println("--------------")
    println("リスト内包表記")
    @time array1 = list_comprehension(test_list)
    println("--------------")
    println("for文 (先に確保)")
    @time array2 = for_loop(test_list)
    println("--------------")
    println("for文（push）")
    @time array3 = for_loop_append(test_list)
    println("--------------")
    println("読み取り")
    @time for i in 1:N
        @assert array1[i] == array2[i]
        @assert array1[i] == array3[i]
    end

end

test()

