 #include <stdio.h>
 #include <string.h>
 #include <time.h>
 #include <pthread.h>

 #define data 1000000
 #define num_thread 4

 long sub_sum[num_thread];
clock_t start_t,end_t;

 void *thr_fuc(void *parm){
  int *thread_id;
  int i,j;
  int start, end;
  long sum, temp;
  thread_id = (int*) parm;
  printf("thread ID: %d\n", *thread_id);

  start = (*thread_id)*data/(num_thread);
        if (*thread_id == num_thread)
                end = data;
        else
                end = (*thread_id+1)*data/(num_thread);
 printf("start: %d, end: %d\n", start, end);
end_t = clock();
   printf("Thread start time: %ld\n", end_t-start_t);
  for (i = start; i< end; i++){
        sub_sum[*thread_id] = sub_sum[*thread_id] + i;
        for(j=0;j<10000;j++)
        temp = 3.14*3.14;
   }
end_t = clock();
   printf("Thread finish time: %ld\n", end_t-start_t);
  return NULL;
 }


 int main(int argc, char *argv[])
 {
   int i,j;
   long sum;
   float temp;
   pthread_t thread_id[num_thread];
   int parm[num_thread];
   start_t=clock();
   for (i = 0; i < num_thread; i++){
     parm[i] = i;
     pthread_create(&thread_id[i], NULL,thr_fuc, &parm[i]);
   }
   sum = 0;
   for (i = 0; i < num_thread; i++){
     pthread_join(thread_id[i], NULL);
     printf("sub total %ld\n", sub_sum[i]);
     end_t = clock();
   printf("time used: %ld\n", end_t-start_t);
     sum = sum + sub_sum[i];
   }
   printf("total %ld\n", sum);
   end_t = clock();
   printf("time used: %ld\n", end_t-start_t);
   return 0;
 }

