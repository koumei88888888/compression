//cantransfer.c
//CAN <->IP implemented.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>
#include <ctype.h>
#include <libgen.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <sys/uio.h>
#include <net/if.h>
#include <netinet/in.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include "terminal.h"
#include "lib.h"
#include "lib.c"

static volatile int running = 1;

int main(int argc, char **argv)
{
	fd_set rdfs;
	int csockrcv;
	int csocksnd;
	int bridge = 0;
	useconds_t bridge_delay = 0;
	unsigned char silentani = 0;
	unsigned char color = 0;
	unsigned char view = 0;
	unsigned char log = 0;
	unsigned char logfrmt = 0;
	int count = 0;
	int rcvbuf_size = 0;
	int opt, ret;
	int currmax=1, numfilter;
	char *ptr, *nptr;
	char ctrlmsg[CMSG_SPACE(sizeof(struct timeval)) + CMSG_SPACE(sizeof(__u32))];
	struct iovec iov;
	struct msghdr msg;
	struct cmsghdr *cmsg;
	struct can_filter *rfilter;
	can_err_mask_t err_mask;
	struct can_frame frame;
	int nbytes, i;
	struct ifreq ifr;
	struct timeval tv, last_tv;
	FILE *logfile = NULL;
	last_tv.tv_sec  = 0;
	last_tv.tv_usec = 0;
	struct sockaddr_can addr;
	int isocksnd,isockrcv;
	struct sockaddr_in dest,source;
	char buf[1024],bufframe[1024];
	int maxfd;
	const int loopback = 0;
	int source_size;

	//isockrcv
	isocksnd = socket(AF_INET, SOCK_DGRAM, 0);
	dest.sin_family = AF_INET;
	dest.sin_addr.s_addr = inet_addr("192.168.11.43");//à∂êÊ
	dest.sin_port = htons(11111);
	bind(isocksnd, (struct sockaddr *)&dest, sizeof(dest));

	//isocksnd
	isockrcv = socket(AF_INET, SOCK_DGRAM, 0);
	source.sin_family = AF_INET;
	source.sin_addr.s_addr = inet_addr("192.168.11.8");//é©ï™
	source.sin_port = htons(11111);
	bind(isockrcv, (struct sockaddr *)&source, sizeof(source));
	
	//csockrcv
	if ( (csockrcv = socket(PF_CAN, SOCK_RAW, CAN_RAW) ) < 0) {
		perror("socket");
		return 1;
	}
	
	memset(&ifr.ifr_name, 0, sizeof(ifr.ifr_name));
	strncpy(ifr.ifr_name, argv[1], strlen(argv[1]));
	addr.can_ifindex = ifr.ifr_ifindex;
	addr.can_family = AF_CAN;
	if (bind(csockrcv, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("bind");
		return 1;
	}
	
	//csocksnd
	if ( (csocksnd = socket(PF_CAN, SOCK_RAW, CAN_RAW) ) < 0) {
		perror("socket");
		return 1;
	}
	setsockopt(csocksnd, SOL_CAN_RAW, CAN_RAW_LOOPBACK,&loopback, sizeof(loopback));
	setsockopt(csocksnd, SOL_CAN_RAW, CAN_RAW_FILTER, NULL, 0);
	if (ioctl(csocksnd, SIOCGIFINDEX, &ifr) < 0) {
		perror("SIOCGIFINDEX");
		return 1;
	}
	addr.can_ifindex = ifr.ifr_ifindex;
	if ( bind(csocksnd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("bind");
		return 1;
	}

	/* these settings are static and can be held out of the hot path */
	iov.iov_base = &frame;
	msg.msg_name = &addr;
	msg.msg_iov = &iov;
	msg.msg_iovlen = 1;
	msg.msg_control = &ctrlmsg;

	while (1) {
		FD_ZERO(&rdfs);
		FD_SET(csockrcv, &rdfs);
		FD_SET(isockrcv,&rdfs);
		maxfd = (csockrcv > isockrcv)? csockrcv : isockrcv;		
		if ((ret = select(maxfd+1, &rdfs, NULL, NULL, NULL)) < 0) {
			running = 0;
			continue;
		}
		//can packet received
		if (FD_ISSET(csockrcv, &rdfs)) {
			int idx;
			/* these settings may be modified by recvmsg() */
			iov.iov_len = sizeof(frame);
			msg.msg_namelen = sizeof(addr);
			msg.msg_controllen = sizeof(ctrlmsg);  
			msg.msg_flags = 0;

			nbytes = recvmsg(csockrcv, &msg, 0);
			fprint_long_canframe(stdout, &frame, NULL, view);

			//ip packet send
			sprint_canframe(bufframe, &frame, view);
			memset(buf, 0, sizeof(buf));
			snprintf(buf, sizeof(buf), bufframe);
			sendto(isocksnd, buf, strlen(buf), 0, (struct sockaddr *)&dest, sizeof(dest));
			printf("\n");
		}
		//ip packet received
		if (FD_ISSET(isockrcv, &rdfs)) {
			memset(buf, 0, sizeof(buf));
			source_size = sizeof(source);
			recvfrom(isockrcv, &buf, sizeof(buf), 0, (struct sockaddr *)&source, &source_size);
			printf("%s\n", buf);

			//can packet send
			parse_canframe(buf, &frame);
			nbytes = write(csocksnd, &frame, sizeof(frame));
		}	
	}
	close(csocksnd);
	close(csockrcv);
	close(isocksnd);
	close(isockrcv);
	return 0;
}
