// Reference : http://www.turbolinux.com/solution_service/library/features/c_magazine/vol_11.html
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <memory>

/**
 * @brief ポインタが指すもののサイズになっているかチェック
 * 
 * @return int 
 */
int test_size()
{
	std::unique_ptr<sockaddr_in> ptr(new sockaddr_in());
	std::cout << "size of pointed = " << sizeof(*ptr) << std::endl;
	std::cout << "size of unique pointer = " << sizeof(ptr) << std::endl;
	std::cout << "size of raw pointer = " << sizeof(ptr.get()) << std::endl;

	sockaddr_in test;
	std::cout << "size of structure = " << sizeof(test) << std::endl;
}

int main()
{
	// test_size();

	constexpr unsigned short PORT = 60000;

	int socket1, socket2;

	if ((socket1 = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		perror("socket");
		std::exit(1);
	}

	std::unique_ptr<sockaddr_in> server_addr(new sockaddr_in());
	server_addr->sin_family = AF_INET;
	server_addr->sin_addr.s_addr = INADDR_ANY; // From Any Address
	//server_addr->sin_addr.s_addr = inet_addr("127.0.0.1")
	server_addr->sin_port = htons(PORT);

	if (bind(socket1, reinterpret_cast<sockaddr *>(server_addr.get()), sizeof(*server_addr)) < 0)
	{
		perror("bind");
		std::exit(1);
	}

	if (listen(socket1, 1) < 0)
	{
		perror("listern");
		std::exit(1);
	}

	std::unique_ptr<sockaddr_in> client_addr(new sockaddr_in());
	socklen_t len = sizeof(*client_addr);

	if ((socket2 = accept(socket1, reinterpret_cast<sockaddr *>(client_addr.get()), &len)) < 0)
	{
		perror("accept");
		std::exit(1);
	}
	close(socket1);

	char buf[BUFSIZ];
	strcpy(buf, "サーバーが応答しました。\n");
	write(socket2, buf, sizeof(buf));

	close(socket2);

	return 0;
}

