//usage: picup_ID.exe yuki_1230s_field.csv
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
	FILE *fi,*fo,*can;
	int i = 0;
	int m;
	char fname[256][256];
	char buf[256];
	char str[256];
	char canid[256][8];
	char *tok;
	
	can = fopen("canid.txt", "r");
	while(fgets(canid[i],sizeof(canid[i]),can)!=NULL) {
		canid[i][strlen(canid[i])-1] = '\0';
		sprintf(fname[i], "%s_log.csv", canid[i]);
		i++;
	}
	fclose(can);
	
	for(m = 0; m < i; m++) {
		fi = fopen(argv[1], "r");
		fo = fopen(fname[m], "w");
		while(fgets(buf,sizeof(buf),fi)!=NULL) {
			strcpy(str, buf);
			tok = strtok(buf, ",");
			if(strstr(tok, canid[m])) {
				//tok = strtok(NULL, "\n");
				//printf("%s", buf);
				fputs(str, fo);
			}
		}
		fclose(fo);
		fclose(fi);
	}
	return 0;
}