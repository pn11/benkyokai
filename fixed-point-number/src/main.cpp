#include <iostream>
#include <chrono>
#include <math.h>


/**
 * @brief 浮動小数点数から固定小数点数への変換
 * 
 * @param float_val 
 * @param lower_bit 小数点以下の数のビット数
 * @return int 
 */
int float_to_fixed(float float_val, int lower_bit)
{
    return (int)round(float_val * (1 << lower_bit));
}

/**
 * @brief 固定小数点数から浮動小数点数への変換
 * 
 * @param fixed_val 
 * @param lower_bit 
 * @return float 
 */
float fixed_to_float(int fixed_val, int lower_bit)
{
    return (float)fixed_val / (float)(1 << lower_bit);
}



int main()
{
	/** 固定小数点の位置 (小数点以下の数に対応するビット数) */
	const int lower_bit = 16;

	// 足し算する回数
	const int n_add = 100;

	// 計算を繰り返す回数
	const int n_repeat = 100000000;


    const float float_val_ini = 123.4567890f;
    const int fixed_val_ini = float_to_fixed(float_val_ini, lower_bit);
    std::cout << "Before calculation:" << std::endl
              << "    float_val = " << std::fixed << float_val_ini << std::endl
              << "    fixed_val = " << fixed_val_ini << std::endl;

    float float_val = 0.0;
    int fixed_val = 0;

    auto t1 = std::chrono::high_resolution_clock::now();
    // 浮動小数点数の計算
	for (int j = 0; j < n_repeat; ++j)
	{
		float_val = 0.0;
		for (int i = 0; i < n_add; ++i)
		{
			float_val += float_val_ini;
		}
	}
	auto t2 = std::chrono::high_resolution_clock::now();

	std::cout << "Floating point calc end." << std::endl;

	auto t3 = std::chrono::high_resolution_clock::now();

    // 固定小数点数の計算
    // すぐ桁落ちしてしまうので、 n_add回足し合わせる計算を n_repeat回繰り返す
	for (int j = 0; j < n_repeat; ++j)
	{
		fixed_val = 0;
		for (int i = 0; i < n_add; ++i)
		{
			fixed_val += fixed_val_ini;
		}
	}

    auto t4 = std::chrono::high_resolution_clock::now();

    std::cout << "Result (float) = " << float_val << std::endl;
    std::cout << "Result (fixed) = " << fixed_to_float(fixed_val, lower_bit) << std::endl;

    std::cout << "Time (float) = " << std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count() << " us" << std::endl;
    std::cout << "Time (fixed) = " << std::chrono::duration_cast<std::chrono::microseconds>(t4 - t2).count() << " us" << std::endl;

    return 0;
}