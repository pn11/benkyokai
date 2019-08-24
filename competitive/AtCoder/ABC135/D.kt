fun main(argc:Array<String>){
    val MOD = 1000000007L;

    val S = readLine()!!
    var dp = Array(10005, {i->Array(13, {i->0L})})
    dp[0][0] = 1

    for (i in 0..S.length-1){
        var c: Int = 0
        if (S[i] == '?') {
            c = -1
        }
        else {
            c = S[i].toString().toInt()
        }

        for (j in 0..9){
            if (c != -1 && c != j){
                continue
            }
            for (ki in 0..12){
                dp[i+1][(ki*10+j) % 13] += dp[i][ki]
            }
        }
        for (j in 1..12){
            dp[i+1][j] %= MOD
        }
    }
  
    println(dp[S.length][5])
}