#include <stdio.h>
#include <string.h>
#include <unistd.h>     /* read(),write(),fork(),close(),...       */
#include <sys/socket.h> /* socket(), bind(), listen(), accept()... */
#include <netinet/in.h> /* struct sockaddr_in,...                  */
#include <netdb.h>      /* gethostbyname(),....                    */

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <memory>

int main(int argc, char *argv[])
{
  constexpr unsigned short PORT = 60000;

  int socket_;
  //struct sockaddr_in  addr;
  std::unique_ptr<sockaddr_in> addr(new sockaddr_in());
  struct hostent *hp;
  char buf[BUFSIZ];
  if (argc < 2)
  {
    printf("%s SERVER\n", argv[0]);
    std::exit(1);
  }

  if ((socket_ = socket(AF_INET, SOCK_STREAM, 0)) < 0)
  {
    perror("socket");
    std::exit(1);
  }
  //memset((char*)&addr, 0, sizeof(addr));
  if ((hp = gethostbyname(argv[1])) == NULL)
  {
    perror("gethostbyname");
    std::exit(1);
  }
  //bcopy(hp->h_addr, &(addr->sin_addr), hp->h_length);
  addr->sin_family = AF_INET;
  addr->sin_port = htons(PORT);
  if (connect(socket_, reinterpret_cast<sockaddr *>(addr.get()), sizeof(*addr)) < 0)
  {
    perror("connect");
    std::exit(1);
  }

  read(socket_, buf, sizeof(buf));
  printf("%s", buf);
  close(socket_);
  return 0;
}