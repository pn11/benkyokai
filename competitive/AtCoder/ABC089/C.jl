function solve()
    N = parse(Int64, readline())
    S = [chomp(readline()) for s in 1:N]
  
	numMARCH = [0, 0, 0, 0, 0]
    MARCH = ["M", "A", "R", "C", "H"]
  
  	for name in S
        for (i, m) in enumerate(MARCH)
            if name[1] == m[1]
                numMARCH[i] += 1
            end
        end
    end

    nonzero = numMARCH[numMARCH .!= 0]
    if length(nonzero) < 3
        println(0)
        return
    end

  	combinations::Int64 = 0
    for i in 1:length(nonzero)
    	for j in i+1:length(nonzero)
            for k in j+1:length(nonzero)
                combinations += nonzero[i]*nonzero[j]*nonzero[k]
            end
        end
    end
    println(combinations)
    
end

solve()
