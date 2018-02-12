 #include <mpi.h>
 #include <stdio.h>
 #include <string.h>
 #include <time.h>

 #define BUFSIZE 128
 #define TAG 0
 #define data 1000000

 int main(int argc, char *argv[])
 {
   char idstr[32];
   char buff[BUFSIZE];
   int numprocs;
   int myid;
   int i,j, start, end;
   long total, sum;
   float temp;
   MPI_Status stat;
   clock_t start_t,end_t;
   start_t=clock();
   /* MPI programs start with MPI_Init; all 'N' processes exist thereafter */
   MPI_Init(&argc,&argv);
   /* find out how big the SPMD world is */
   MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
   /* and this processes' rank is */
   MPI_Comm_rank(MPI_COMM_WORLD,&myid);

   /* At this point, all programs are running equivalently, the rank
 *       distinguishes the roles of the programs, with
 *             rank 0 often used specially... */
   if(myid == 0)
   {
     printf("%d: We have %d processors\n", myid, numprocs);
	/*receive results*/
	for (i=1; i<numprocs;i++)
	{	MPI_Recv(&sum, 1, MPI_LONG, i, TAG, MPI_COMM_WORLD, &stat);
		printf("sum %ld\n", sum);
		total = total + sum;
	}
	printf("total %ld\n", total);
    end_t=clock();
    printf("time used: %ld\n", end_t-start_t);
   }
   else
   {
	/*work load*/
	start = (myid-1)*data/(numprocs-1);
	if (myid == numprocs) 
		end = data;
	else
		end = myid*data/(numprocs-1);
	for (i = start; i< end; i++){
		sum = sum + i;
		for(j=0;j<1000;j++)
		temp = 3.14*3.14;
	}
	MPI_Send(&sum, 1, MPI_LONG, 0, TAG, MPI_COMM_WORLD);
	
   }

   /* MPI programs end with MPI Finalize; this is a weak synchronization point */
   MPI_Finalize();
   return 0;
 }


