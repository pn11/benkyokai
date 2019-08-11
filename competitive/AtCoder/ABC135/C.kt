fun main(argc:Array<String>){
    val N = readLine()!!.toInt()
    val A = readLine()!!.split(" ").map{it.toLong()}.toMutableList()
    val B = readLine()!!.split(" ").map{it.toLong()}.toMutableList()
    var beaten = 0L
    for (i in 0..N-1){
        if (A[i] >= B[i]){
            beaten += B[i]
            A[i] = A[i] - B[i]
            B[i] = 0
        }
        else {
            beaten += A[i]
            B[i] -= A[i]
            A[i] = 0
        }
        if (A[i+1] >= B[i]){
            beaten += B[i]
            A[i+1] = A[i+1] - B[i]
            B[i] = 0
        }
        else {
            beaten += A[i+1]
            B[i] -= A[i+1]
            A[i+1] = 0
        }
    }
    println(beaten)
}
