import java.util.*;
//import java.Math.*;
class sum{
	public static void main(String args[]){
		int st,en,start=0,end=0;
		Scanner sc=new Scanner(System.in);
		st=sc.nextInt();
		en=sc.nextInt();
		int arr[]={3,2,6,5,1,4,8,9};
		int num=0;
		int num2=0;
		for(int i=0;i<arr.length;i++){
			num+=arr[i];
			if(arr[i]==st){
				start=i;
			}
			if(arr[i]==en){
				end=i;
			}
		}
		int c=0;
		for(int i=start;i<end+1;i++){
			num2+=arr[i]*Math.pow(10,end-start-c);
			c++;
			num-=arr[i];
		}
		System.out.println(num);
		System.out.println(num2+num);
	}
}