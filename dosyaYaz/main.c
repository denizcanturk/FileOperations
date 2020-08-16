//#include <stdio.h>
//#include <stdlib.h>

/* a) Dosyaya 15 Sayı yazdıran Program */

//int main()
//{
//   int num;
//   FILE *fptr;

//   // use appropriate location if you are using MacOS or Linux
//   fptr = fopen("sayilar.txt","w");

//   if(fptr == NULL)
//   {
//      printf("Error!");
//      exit(1);
//   }
//    for (int i = 0; i < 15; i++){
//   printf("Enter Num %d: ", i+1);
//   scanf("%d",&num);

//   fprintf(fptr,"%d\n",num);

//    }
//   fclose(fptr);

//   return 0;
//}



///* b) Dosyaya 25 Sayı ilave eden yazdıran Program */

//int main()
//{
//    srand(time(0));
//   int num;
//   FILE *fptr;

//   // use appropriate location if you are using MacOS or Linux
//   fptr = fopen("sayilar.txt","a");

//   if(fptr == NULL)
//   {
//      printf("Error!");
//      exit(1);
//   }
//    for (int i = 0; i < 25; i++){
//        num = rand() % 100;
//   printf("Random Number %d: \n", num);

//   fprintf(fptr,"%d\n",num);

//    }
//   fclose(fptr);

//   return 0;
//}

#include <stdio.h>
#include <stdlib.h>
/* c) Dosyayı Okuyan ve Asal Sayı Bulan Program*/
int main()
{
   int num = 0,id=0;
   FILE *fptr;

   // use appropriate location if you are using MacOS or Linux
   fptr = fopen("sayilar.txt","r");

   if(fptr == NULL)
   {
      printf("Error!");
      exit(1);
   }
   while (!feof(fptr)) {
       fscanf(fptr, "%d", &num);
      if ((num % 2 != 0) && (num % 3 != 0) && (num % 5 != 0) && (num % 7 != 0)) {
          printf("%d is a Prime Number\n", num);
          id++;
          num=0;
      }
   }

   fclose(fptr);

   return 0;
}
